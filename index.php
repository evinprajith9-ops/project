<?php
session_start();
if(isset($_POST['login'])){
    $_SESSION['teacher'] = "Class 6 Teacher";
    header("Location: dashboard.php");
}
?>
<!DOCTYPE html>
<html>
<head>
<title>Teacher Login</title>
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<div class="container">
<h2>Teacher Login</h2>
<form method="post">
<input type="text" placeholder="Username" required>
<input type="password" placeholder="Password" required>
<button name="login">Login</button>
</form>
</div>
</body>
</html>
