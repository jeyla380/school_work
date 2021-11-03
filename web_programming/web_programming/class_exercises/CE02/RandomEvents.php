<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Random Page</title>
    </head>
    <body>
        <?php
            //random number game
            $point = 0;
            print("<table> <tr> <th>Player</th> <th>Computer</th> <th>Rounds</th> </tr><br>");
            
            for($round = 0; $round < 10; $round++)
            //this will go through 10 times before stopping
            {
                $playerScore = rand(1,100);
                $computerScore = rand(1,100);
                print("<tr> <td>$playerScore</td> <td>$computerScore</td>");
                
                if($playerScore < $computerScore)
                {
                    print("<td>Player lost this round</td> </tr><br>");
                    $point--;
                }
                else if($playerScore > $computerScore)
                {
                    print("<td>The player won this round!</td> </tr><br>");
                    $point++;
                }
                else
                {
                    print("<td>The player tied with the computer</td> </tr><br>");
                }
            }
            
            print("<tr> <td colspan=2>Player Score: </td> <td>$point</td> </tr> </table>");
            ($point > 0)? print("Good Job, you won! <br>") : print("You lost. <br>");
            
            
            //Chinese Zodiac
            $year = date("Y");
            print("<p> It's the year of the: ");
            
            switch($year % 12)
            {
                case 0:
                    echo "Monkey </p>";
                    break;
                case 1:
                    echo "Rooster </p>";
                    break;
                case 2:
                    echo "Dog </p>";
                    break;
                case 3:
                    echo "Boar </p>";
                    break;
                case 4:
                    echo "Rat </p>";
                    break;
                case 5: 
                    echo "Ox </p>";
                    break;
                case 6:
                    echo "Tiger </p>";
                    break;
                case 7:
                    echo "Rabbit </p>";
                    break;
                case 8:
                    echo "Dragon </p>";
                    break;
                case 9:
                    echo "Snake </p>";
                    break;
                case 10:
                    echo "Horse </p>";
                    break;
                case 11:
                    echo "Lamb </p>";
                    break;
                default:
                    echo " <br> There is something wrong </p>";
                    break;
            }
        ?>
    </body>
</html>
