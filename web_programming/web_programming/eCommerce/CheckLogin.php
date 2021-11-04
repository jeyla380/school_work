<?php
session_start();
unset($_SESSION['NotMatch']);

//connect to database
require_once 'DatabaseConnection.php';

$myUsername = $_POST['myUsername'];
$myPassword = $_POST['myPassword'];

//Protect MySQL Injection
$myUsername = mysql_fix_string($connection, $myUsername);
$myPassword = mysql_fix_string($connection, $myPassword);

//hashes the password
$hash = hash("ripemd128", $myPassword);

$sql = "Select * FROM CSIS2440.Account WHERE Username = '$myUsername' AND Password = '$myPassword'";
$result = $connection->query($sql);
if(!$result)
{
    $message = "Whole query: " .$sql. "<br>";
    echo $message;
    die('Invalid query: ' .mysqli_error($connection));
}

//num_row is counting table row
$count = $result->num_rows;

//if $result matches with $myUsername and $myPassword, table row = 1 row
if($count == 1)
{
    $row = $result->fetch_assoc();
    $_SESSION['myUsername'] = $myUsername;
    $_SESSION['myPassword'] = $myPassword;
    $_SESSION['Birthday'] = $row['Birthday'];
    $_SESSION['Email'] = $row['Email'];
    
    header("Location:Catalogue.php");
}
else
{
    header("Location:Login.php");
    $_SESSION['NotMatch']++;
    echo "Incorrect username or password";
}

