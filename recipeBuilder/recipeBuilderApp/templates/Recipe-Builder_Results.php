<!DOCTYPE html>
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>Recipe-Builder | Your Results</title>
<link rel="stylesheet" href="rbResultsCSS.css" type="text/css" >
</head>

<body>

<ul>
   <li><a href="/">Home</a></li>
   <li><a href="Recipe-Builder_About.htm">About Us</a></li>
   <li><a href="Recipe-Builder_Login.htm">Log In</a></li>
   <li><a href="Recipe-Builder_SignUp.htm">Sign Up</a></li>
</ul>

<div>
   <h1>Your Results</h1>
   <p>Based on your entries, here's what we were able to
 locate for you:</p>
</div>

<?php

   $ingredientAmount = count($_POST["ingredient"]);
   $total = 0.00;
   $placeholder = 0.00;

   $i = 0;

   while ($i < $ingredientAmount)
   {
      if ($_POST["ingredient"][$i] != "")
      {
         echo <p>The $_POST["ingredient"][$i] . is/are $ . $placeholder . </p>;
         $total += $placeholder;
      }
      $i++;
   }

   echo <p><h1>Your Total is: $total.<h1></p>;

?>

<p>If you would like to build another recipe, click the button below.</p><br>

<div class="buttonHolder">
<a href="Recipe-Builder_Form.htm" class="button button1">Build Again</a>
   <!-- Add destination file later with database -->
   <a href="Saved_Recipes.htm" class="button button1">Save Recipe</a>
</div>


<img src="Recipe-Builder.png" class="center">

</body>
</html>
