#!/usr/bin/python
import cgi,cgitb, template, bleach, os
cgitb.enable()

print ("Content-Type: text/html; charset=utf-8\r\n")
print

print template.header()
print template.navbar()


print (""" 
	<div class="page-header"> 
	<h1> LITE 2015: Homeworks</h1>
	</div>
	""")

form = cgi.FieldStorage()
stuid = form.getvalue("stuid", "")

print ("""

	<div class="panel panel-primary">
	<div class="panel-heading">
		<h5 class="panel-tittle">Student #</h5>
	</div>
	<div class="panel-body">
		<p> Access your first submitted assigment incerting your student number.</p>
		<form method="get">
			<div class="input-group">
				<span class="input-group-addon" id="basic-addon1"><span class = "glyphicon glyphicon-user"></span></span>
				<input type="text" value="%s" class="form-control" name="stuid" aria-describedby="basic-addon1" placeholder="Student number"></input>
				<span class="input-group-btn">
					<button class="btn btn-default" type="submit">Search</button>
				</span>
			</div>
		</form>
	</div>
	</div> <!-- panel-primary -->

	""" % bleach.clean(stuid))

if stuid != '':

	try:
		homeworks = os.popen("ls %s/" % stuid)
		print "<ol>"
		for line in enumerate(homeworks.readlines(), start=1):
			print "<li>"
			print ("""

			<div>
				<!-- Large modal -->
				<button type="button" class="btn btn-default btn-xs" data-toggle="modal" data-target="#modal%(linenum)s">
				<span class = "glyphicon glyphicon-modal-window"></span> %(filename)s
				</button>
					<div id="modal%(linenum)s" class="modal fade bs-example-modal-lg" tabindex="-%(linenum)s" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
					  <div class="modal-dialog modal-lg">
					    <div class="modal-content">
					    	<div class="modal-header">
			        		<button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
			        		<h4 class="modal-title" id="myModalLabel">%(filename)s</h4>
			      			</div>
			      			<div class="modal-body">
			      				<iframe width="99.6%%" height="300" src="%(stunumber)s/%(filename)s"></iframe>
					      	</div>
					      	<div class="modal-footer">
					        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
						    </div>
					    </div>
					  </div>
					</div>
			</div>
			""" % {"linenum": line[0],"filename": line[1], "stunumber": stuid})
			print "</li>"

		print "</ol>"
	except IOError:
		print "Could not find files with that student number"




print template.footer()
