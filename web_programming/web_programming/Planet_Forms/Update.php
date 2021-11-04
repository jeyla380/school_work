<?php

$update = "UPDATE `CSIS2440`.`Planets` SET `Active` = 'Y'";
if ($desc != "A short description of the planet") {
    $update .= ", `Desc` = '$desc' ";
}
$update .= "WHERE (`PlanetName` = '".$name."')";
$success = $connect->query($update);
if ($success == FALSE) {
    //error if query did not run
    $failure = "Whole Query " .$update. "<br>";
    echo $failure;
    die('Invalid query: ' .mysqli_error($connect));
} else {
    //let user know it worked
    echo $name . " was given a space station. <br>";
}
