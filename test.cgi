#!/usr/bin/python
import cgi
import cgitb
cgitb.enable()

print ("Content-Type: text/html; charset=utf-8\r\n")
print

# form = cgi.FieldStorage()

# hola = form.getvalue("cheo")

# print ("hola")
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
    <link href="bootstrap-3.3.2-dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="bootstrap-3.3.2-dist/css/offcanvas.css" rel="stylesheet">

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
          <a class="navbar-brand" href="index.php">Cybersecurity Labs</a>
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

form = cgi.FieldStorage()
message = form.getvalue("message", "(no message)")

print("""
 <form action="test.cgi" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="Escribete algo"  name="message" aria-describedby="basic-addon1">
		<span class="input-group-btn">
			<button class="btn btn-default" type="submit">Search</button>
		</span>
	</div>
</form>

<p>Searched for: %s</p>

""" % message)


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
    <script src="bootstrap-3.3.2-dist/js/bootstrap.min.js"></script>

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="bootstrap-3.3.2-dist/assets/js/ie10-viewport-bug-workaround.js"></script>

    <script src="bootstrap-3.3.2-dist/assets/js/offcanvas.js"></script>
  </body>

</html>
	""")