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
user = form.getvalue("username", "(no username)")
passw = form.getvalue("password", "(no password)")

print("""
 <form action="SQL_injection.cgi" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="username"  name="username" aria-describedby="basic-addon1">
    <input type="text" class="form-control" placeholder="password"  name="password" aria-describedby="basic-addon1">
		<div class="btn-group">
			<button type="submit" class="btn btn-default">LogIn</button>
		</div>
	</div>
</form>""")

if form.has_key("username") & form.has_key("password"):
  # The injection can be made by making username and password true
  query = """SELECT * FROM User WHERE username = "%s" AND password = "%s" """ % (user, passw)

  c.execute(query)
  result =  c.fetchall()

  print ("""
    <p>Your Information:</p>
    """)
  print """<table class="table table-condensed">"""
  print """<tr><th>Name</th><th>Username</th><th>Email</th><th>Direction</th><th>Password</th><th>Age</th><th>Student Number</th></tr>"""
  for e in result:
    print """<tr>"""
    for i in range(1,len(e)):
      print """<td>%s</td>""" % e[i]
    print """</tr>"""
  print """</table>"""


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
