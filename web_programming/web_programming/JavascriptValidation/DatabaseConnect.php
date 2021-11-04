<?php

$host = "localhost";
$user = "root";
$password = "DBAdmin";
$db = "CSIS2440";
$connect = new mysqli($host, $user, $password, $db) or die('Could not connect to database server.' . mysqli_connect_error($connect));

function mysql_fix_string($conn, $string) {
    if (get_magic_quotes_gpc()) {
        $string = stripslashes($string);
    }
    $string = htmlentities($string);
    return $conn->real_escape_string($string);
}

if($connect->connect_error == false)
{
    //echo "<h2>Connection!</h2>";
}
else
{
    echo $connect->connect_error;
}
//print_r($connect);








