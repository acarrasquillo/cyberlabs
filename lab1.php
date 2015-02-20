<?php include('header.php'); ?>
<?php include('navbar.php'); ?>

	<form name="XSS" action="lab1.php" method="post">
	<div class="input-group">
		<input type="text" class="form-control" placeholder="Escribete algo compañer@"  name="input" aria-describedby="basic-addon1">
		<span class="input-group-btn">
			<button class="btn btn-default" type="submit">Search</button>
		</span>
	</div>
	</form>
	<br>
	<p>  

		<?php 
			if ($_POST["input"]== ""){
				
			}
			else{
				$texto = $_POST["input"];
				print $texto;
			}	
					

		?>

		<div class="panel panel-danger">
		<div class="panel-heading">
		HTML incertado escapado incorrectamente.
		</div>
		<div class="panel-body">
		<?php
			print "<pre>".htmlspecialchars($texto)."</pre>"
		?>
		</div>
				
			   </div>

			<div class="panel panel-success">
				<div class="panel-heading">	
					HTML incertado escapado correctamente.
			    </div>
			    <div class="panel-body">
			    	<?php
						print "<pre>".htmlspecialchars(htmlspecialchars($texto))."</pre>"
					?>
		        </div>
			
		</div>
	</p>

<?php include('footer.php'); ?>