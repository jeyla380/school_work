<?php

$host = "localhost";
$user = "root";
$password = "DBAdmin";
$db = "CSIS2440";
$connect = new mysqli($host, $user, $password, $db) or die('Could not connect to database server.' . mysqli_connect_error($connect));

if($connect->connect_error == false)
{
    echo "<h2>Connection!</h2>";
}
else
{
    echo $connect->connect_error;
}
print_r($connect);








