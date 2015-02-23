#!/usr/bin/python
import cgi, template
import cgitb
import bleach
import string
cgitb.enable()


print ("X-XSS-Protection: 0;")
print ("Content-Type: text/html; charset=utf-8\r\n")
print
print template.header()

print template.navbar()

print ("""
    <div class="page-header">
      <h1>XSS: <small>In JavaScript</small></h1>
    </div>
	""")

form = cgi.FieldStorage()
message = form.getvalue("message", "Prueba")
inputform = "<input type=\"text\" value=\""

print("""
	<div class="input-group">
		<input type="text" class="form-control" placeholder="Input text"  name="message" aria-describedby="basic-addon1">
		<span class="input-group-btn">
			<button class="btn btn-default" onclick="myFrame()">Search</button>
		</span>
	</div>

""")

if message != "":

  print ("""

    <div id="demo" class="embed-responsive embed-responsive-16by9">
    </div>

    """)


  print (
    """
    <p>
      <div class="panel panel-danger">
       <div class="panel-heading">
        Incerted input incorrectly escaped.
       </div>
        <div class="panel-body">
         <pre> <i> </i> </pre>
        </div>
      </div>

    """) 

  print(
    """
      <div class="panel panel-success">
       <div class="panel-heading">
        Incerted input correctly escaped.
       </div>
        <div class="panel-body">
         <pre> <i></i> </pre>
       </div>
      </div>
    </p>
    """)

  print ("""

    <script>
    function myFrame(query) {
        var x = document.createElement("IFRAME");
        x.setAttribute("src", "http://www.bing.com/search?q=");
        x.setAttribute("class","embed-responsive-item");
        document.getElementById("demo").appendChild(x);
    }
    </script>

    """)

print template.footer()