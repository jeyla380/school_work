<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<?php
//get post variable
$captainName = htmlentities($_POST['CapName']);
$captainName = strtolower($captainName);
$captainName = ucwords($captainName);

$captainAge = $_POST['CapAge'];
$shipName = $_POST['ShipName'];
?>
<html>
    <head>
        <meta charset="UTF-8">
        <title></title>
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">
                <div class="row">
                    <div class="col-2"></div>
                    <div class="col-8">
                        <?php
                        // put your code here
                        $num = 0;
                        print("<p>Captain $captainName at the age of $captainAge, took over the $shipName ship."
                                . "Here are some of their past accomplishments and not-so-great ones.</p>");
                        
                        $earlyYears = fopen("EarlyYears.txt", "r") or die("Unable to open this file");
                        while(!feof($earlyYears))
                        {
                            $earlyRandom[$num] = fgets($earlyYears);
                            $num++;
                        }
                        fclose($earlyYears);
                        
                        shuffle($earlyRandom);
                        print("<p>Their earliest career began with: <ul><li>$earlyRandom[0]</li> <li>$earlyRandom[1]</li></ul></p>");
                        
                        if($captainAge > 25)
                        {
                            $tour = 4 + ($captainAge - 26);
                        }
                        else
                        {
                            $tour = floor(($captainAge - 17) / 2);
                        }
                        $tourRandom = explode("\n", file_get_contents("Tours.txt"));
                        shuffle($tourRandom);
                        
                        print("<p>Here are their career accomplishments: <ul>");
                        for($x = 0; $x < $tour; $x++)
                        {
                            print("<li>" . $tourRandom[$x]. "</li>");
                        }
                        ?>
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
