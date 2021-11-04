<?php
//write your insert statment
$insert = "INSERT INTO `CSIS2440`.`Planets` (`PlanetName`, `PosX`, `PosY`, `PosZ`, `Desc`, `Faction`) "
        . "VALUES ('$name', '$posx', '$posy', '$posz', '$desc', '$faction')";
//echo $insert;
$success = $connect->query($insert);

if ($success == FALSE) {
    //error if query did not run
    $failure = "Whole query " . $insert . "<br>";
    echo $failure;
    print('Invalid query: ' . mysqli_error($connect) . "<br>");
} else {
    //let them know it was added
    echo $name . " was added.<br>";
}
