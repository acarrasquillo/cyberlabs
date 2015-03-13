#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()
import os
import template

print """Content-Type: text/html"""
print

print template.header()
print template.navbar()

print """
	<div class="row row-offcanvas row-offcanvas-right">
        <div class="col-xs-12 col-sm-9">
          <p class="pull-right visible-xs">
            <button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">Toggle Labs</button>
          </p>
          <div class="jumbotron">
            <h1>Professor Acevedo</h1>
            <p>Puertorican Literature Course. In this webpage students can search for homeworks assigned in class.</p>
            <br>
          </div>
          
        </div><!--/.col-xs-12.col-sm-9-->

        <div class="col-xs-6 col-sm-3 sidebar-offcanvas" id="sidebar">
          <div class="list-group">
            <a href="homeworks.cgi" class="list-group-item">Homeworks Insecure</a>
            <a href="homeworks2.cgi" class="list-group-item">Homeworks Secure</a>
            <!-- <a href="#" class="list-group-item">Lab 6</a>
            <a href="#" class="list-group-item">Lab 7</a>
            <a href="#" class="list-group-item">Lab 8</a>
            <a href="#" class="list-group-item">Lab 9</a>
            <a href="#" class="list-group-item">Lab 10</a> -->
          </div>
        </div><!--/.sidebar-offcanvas-->
     </div><!--/row-->"""

print ("""
  <script>
    document.getElementById("home").className = "active";
  </script>
  """)
print template.footer()