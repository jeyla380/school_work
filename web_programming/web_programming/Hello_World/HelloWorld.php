<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Hello World</title>
        <?php
        /*
         * CSIS 2440
         * Day 1, Assignment 1
         */
        $name = "Jessemy";
        $age = 23;
        $female = true;
        $iceCream = "Oreo";
        $imagefile = "img/plant.jpg";
        ?>
    </head>
    <body>
        <div>
            <?php
            //Will be printed onto webpage
            echo "<h3 style='font-family:Courier; color:pink;'>Hello World, this is my first PHP page!</h3>";
            print "<p style='font-family:Courier;'>My name is $name and I'm $age years old. I really like to eat $iceCream ice cream!</p>";
            print '<p style="font-family:Courier;">The variables being used are: $name, $age, and $iceCream.</p>';
            print ("<img src='$imagefile' height='150'>");
            ?>
        </div>
    </body>
</html>
