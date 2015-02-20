#!/usr/bin/python
# This program is for lab purposes only. This isnt a secure way to implement
# querys in a application because it is open to atacks by SQL Injection

import cgi
import cgitb
cgitb.enable()
import MySQLdb

print """Content-Type: text/html"""
print

print("""
	<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="images/favicon.ico">
    <title>Cybersecurity Labs</title>
    <!-- Bootstrap core CSS -->
    <link href="../bootstrap-3.3.2-dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Custom styles for this template -->
    <link href="../bootstrap-3.3.2-dist/css/offcanvas.css" rel="stylesheet">
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  """)


print("""<body>
    <div class="container">
    <nav class="navbar navbar-fixed-top navbar-inverse">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="../index.php">Cybersecurity Labs</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div><!-- /.nav-collapse -->
      </div><!-- /.container -->
    </nav><!-- /.navbar -->
	""")

# First we create a connection object (db) that represents the database
db = MySQLdb.connect("localhost", "jdelavega", "6TsseuXp", "atackpr_sqlin")

# Once we have a connection with the database, we can create a cursor object (c)
# this cursor will let us use the execute() method to perform SQL commands
c = db.cursor()

form = cgi.FieldStorage()
stuNum = form.getvalue("num_estudiante", "(no student number)")

print """<H3><u>Instructions</u>:</H3>"""
print """<p><font size="3">The following box asks the user for an input. The developer, again, forgot to sanitize the inputs.
          We need to show him that input validation is important, so I have a task for you. You need to get the information of
          all the students and professors."""

print """<p><font size="2">Hint: The Professor and the User table have the same amount of columns and the same types maybe you can
          make a compund query.<font></p>"""

print("""
 <form action="sqli2.cgi" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="sudent number"  name="num_estudiante" aria-describedby="basic-addon1">
		<span class="input-group-btn">
			<button class="btn btn-default" type="submit">LogIn</button>
		</span>
	</div>
</form>""")

if form.has_key("num_estudiante"):
  # Try to do an injection here with Union to show the data of all students and professors
  query = """SELECT * FROM User WHERE num_estudiante = "%s" """ % stuNum

  c.execute(query)
  result = c.fetchall()

  print ("""
    <p>Your Information: </p>
    """)
  print """<table class="table table-condensed">"""
  print """<tr><th>Name</th><th>Username</th><th>Email</th><th>Direction</th><th>Password</th><th>Age</th><th>Student Number</th></tr>"""
  for e in result:
    print """<tr>"""
    for i in range(1,len(e)-1):
      print """<td>%s</td>""" % e[i]
    print """</tr>"""
  print """</table>"""

  print """<p>The query: SELECT * FROM User WHERE num_estudiante = "<font color="red">%s</font>" """ % stuNum


print("""
      <hr>
      <footer>
        <p>&copy; Computer Security Lab 2015</p>
      </footer>
    </div><!--/.container-->
    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="../bootstrap-3.3.2-dist/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../bootstrap-3.3.2-dist/assets/js/ie10-viewport-bug-workaround.js"></script>
    <script src="../bootstrap-3.3.2-dist/assets/js/offcanvas.js"></script>
  </body>
</html>
	""")

c.close()
