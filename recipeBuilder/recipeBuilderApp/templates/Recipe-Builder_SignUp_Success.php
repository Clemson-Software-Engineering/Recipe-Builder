<!DOCTYPE html>
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>Recipe-Builder | Sign Up Success!</title>
</head>

<body>
  
<ul>

   <li><a href="Recipe-Builder_Home.htm">Home</a></li>

   <li><a href="Recipe-Builder_About.htm">About Us</a></li>

   <li><a href="Recipe-Builder_Login.htm">Log In</a></li>

   <li><a href="Recipe-Builder_SignUp.htm">Sign Up</a></li>

</ul>

<?php

echo "<h1>Welcome " . $_POST["username"] . "!</h1>";
echo "<p>Your account is now active.</p>";

?>

</body>
</html>
