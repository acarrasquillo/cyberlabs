#!/usr/bin/python
import cgi,cgitb, template, bleach, os
cgitb.enable()
print ("Content-Type: text/html; charset=utf-8\r\n")
print

print template.header()
print template.navbar()

print ("""
	<div class="page-header">
	  <h1>Instructions <small>LITE 2015</small></h1>
	</div>
	<p>
		A professor of literature was hacked and can not access the server that he manages.<br> 
		He does not know much about cybersecurity and hired a student to help him.<br>
		The system administrator lets the student has a public web application in python of a course on the server which used popen.
	</p>

	<div class="panel panel-info">
  <div class="panel-heading">
    <h3 class="panel-title">Goals</h3>
  </div>
  <div class="panel-body">
    <ol>
    	<li>
    	The professor said that he has a file hidden in the server that contains a username <br>
    	and password, find that file.

    	</li>
    <ol>
  </div>
</div>
	""")

print ("""
	<script>
		document.getElementById("instructions").className = "active";
	</script>

	""")
print template.footer()