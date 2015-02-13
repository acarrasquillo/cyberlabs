  <?php include('header.php'); ?>
  <?php include('navbar.php'); ?>

      <div class="row row-offcanvas row-offcanvas-right">
        <div class="col-xs-12 col-sm-9">
          <p class="pull-right visible-xs">
            <button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">Toggle Labs</button>
          </p>
          <div class="jumbotron">
            <h1>Cybersecurity</h1>
            <p>Securing a computer system has traditionally been a battle of wits: the penetrator tries to find the holes, and the designer tries to close them.</p>
            <br>
            <p style="text-align:right">— Gosser</p>
          </div>
          
        </div><!--/.col-xs-12.col-sm-9-->

        <div class="col-xs-6 col-sm-3 sidebar-offcanvas" id="sidebar">
          <div class="list-group">
            <a href="lab1.php" class="list-group-item">Lab 1</a>
            <a href="test.cgi" class="list-group-item">Lab 2</a>
            <!-- <a href="#" class="list-group-item">Lab 3</a>
            <a href="#" class="list-group-item">Lab 4</a>
            <a href="#" class="list-group-item">Lab 5</a>
            <a href="#" class="list-group-item">Lab 6</a>
            <a href="#" class="list-group-item">Lab 7</a>
            <a href="#" class="list-group-item">Lab 8</a>
            <a href="#" class="list-group-item">Lab 9</a>
            <a href="#" class="list-group-item">Lab 10</a> -->
          </div>
        </div><!--/.sidebar-offcanvas-->
      </div><!--/row-->

      <hr>

  <?php include('footer.php'); ?>