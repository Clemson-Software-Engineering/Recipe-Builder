<!DOCTYPE html>
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>Recipe-Builder | Sign Up Success!</title>
</head>

<body>

  <ul>

     <li><a href="/">Home</a></li>

     <li><a href="/recipeBuilder/aboutpage">About Us</a></li>

     <li><a href="/accounts/login">Log In</a></li>

     <li><a href="/authentication/create">Sign Up</a></li>

  </ul>

<?php

echo "<h1>Welcome " . $_POST["username"] . "!</h1>";
echo "<p>Your account is now active.</p>";

?>

</body>
</html>
