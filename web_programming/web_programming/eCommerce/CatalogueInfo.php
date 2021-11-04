<?php
require_once 'DatabaseConnection.php';
$infonumber = $_GET['info'];
if($infonumber > 0)
{
    $sql = "SELECT Name, Price, Description, Image FROM CSIS2440.Products WHERE ProductID= " . $infonumber;
    $productName = "SELECT Name FROM CSIS2440.Products WHERE ProductID= " .$infonumber;
    $nameresult = $connection->query($productName);
    if(mysqli_num_rows($nameresult))
    {
        list($productInfoName) = mysqli_fetch_row($nameresult);
        echo "<h4>$productInfoName Information</h4>";
    }
    echo "<hr>";
    echo "<table align='left' width='100%'><tr> <th class='namestyle'>Name</th> <th class='namestyle'>Price</th> <th>Description</th> <th>Image</th> </tr>";
    $result = $connection->query($sql);
    if(mysqli_num_rows($result) > 0)
    {
        list($infoName, $infoPrice, $infoDesc, $infoImage) = mysqli_fetch_row($result);
        echo "<tr>";
        echo "<td align=\"left\" width=\"250px\">$infoName</td>";
        echo "<td align=\"left\" width=\"125px\">" .money_format('%(#8n', $infoPrice). "</td>";
        echo "<td padding='3' align=\"center\">$infoDesc</td>";
        echo "<td align=\"center\"><img src='productImg\\$infoImage' height=\"160px\"></td>";
        echo "</tr>";
    }
    echo "</table>";
}

