<!DOCTYPE hmtl>
<cfheader name="X-XSS-Protection" value="0">
<html>
<head>
<title> Simple XSS Exercice</title>
</head>
<body>
	<?php
		header("X-XSS-Protection: 0");
	?>

	<form name="XSS" action="index.php" method="post">
		Search :<input type="text" name="input" value="<?php print $input;?>">
		<input type="submit" value="submit">
	</form>

	<p>  

		<?php 
			if ($_POST["input"]== ""){
				
			}
			else{
				$texto = $_POST["input"];
				print $texto;
			}	
					

		?>
	</p>

</body>
</hmtl>
