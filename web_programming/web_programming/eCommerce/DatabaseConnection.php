<?php
$host = "localhost";
$user = "root";
$pass = "DBAdmin";
$databasename = "CSIS2440";
$connection = new mysqli($host, $user, $pass, $databasename)
        or die('Could not connect to the database server.  ' . mysqli_connect_error($connection));

function mysql_fix_string($conn, $string) {
    if (get_magic_quotes_gpc()) {
        $string = stripslashes($string);
    }
    $string = htmlentities($string);
    return $conn->real_escape_string($string);
}

if($connection->connect_error == false)
{
    //echo "<h2>Connection!</h2>";
}
else
{
    echo $connection->connect_error;
}
//print_r($connection);
