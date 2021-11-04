<!DOCTYPE html>
<?php
    /*error_reporting(-1); // reports all errors
    ini_set("display_errors", "1"); // shows all errors
    ini_set("log_errors", 1);
    ini_set("error_log", "/tmp/php-error.log");*/

    session_start();    
    setlocale(LC_MONETARY, "en_US");
    $product = $_POST['SelectProduct'];
    $action = $_POST['action'];
    
    switch($action)
    {
        case "Add": //adding products
            $_SESSION['cart'][$product]++; //add one
            break;
        case "Remove": //removing products
            $_SESSION['cart'][$product]--; //subtract one
            if($_SESSION['cart'][$product] <= 0)
            {
                unset($_SESSION['cart'][$product]); //removes the products entirely when less than or equal to 0. Don't want to get into negative range.
            }
            break;
        case "Empty":
            unset($_SESSION['cart']); //empties the entire cart
            break;
    } 
    require_once 'DatabaseConnection.php'; 
?>

<html>
    <head>
        <meta charset="UTF-8">
        <title>Catalogue</title>
        <script>
            function produceInfo(key) 
            {
                //creates the datafile with query string
                var data_file = "CatalogueInfo.php?info=" + key;
                //this is making the http request
                var http_request = new XMLHttpRequest();
                try 
                {
                    // Opera 8.0+, Firefox, Chrome, Safari
                    http_request = new XMLHttpRequest();
                } 
                catch (e) 
                {
                    try 
                    {
                        http_request = new ActiveXObject("Msxml2.XMLHTTP");
                    } 
                    catch (e) 
                    {
                        try 
                        {
                            http_request = new ActiveXObject("Microsoft.XMLHTTP");
                        } 
                        catch (e) 
                        {
                            alert("Your browser broke!");
                            return false;
                        }
                    }
                }
                http_request.onreadystatechange = function () 
                {
                    if (http_request.readyState == 4)
                    {
                        var text = http_request.responseText;
                        document.getElementById("productInfo").innerHTML = text;
                    }
                }
                http_request.open("GET", data_file, true);
                http_request.send();
            }
        </script>
                <!-- Custom fonts for this theme -->
        <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

        <!-- Theme CSS -->

        <link href="../../../css/freelancer.min.css" rel="stylesheet" type="text/css"/>
        <style>
            table th
            {
                text-align: center;
            }
            th.namestyle
            {
                text-align: left;
            }
        </style>
    </head>
    
    <body>
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-2">
                    <div></div>
                </div>
                
                <div class="col-sm-8">
                    <form action="Catalogue.php" method="Post">
                        <div class="form-group">
                            <div class="col-md-8">
                                    <br>
                                    <h1><?php 
                                        if(isset($_SESSION['myUsername']))
                                        {
                                            echo "Welcome ", $_SESSION['myUsername'];
                                        }
                                    ?></h1>
                                    <hr>
                                    <br>
                            <h6>Please Select a Product: </h6>
                            <select id="SelectProduct" name="SelectProduct" class="select">
                                <?php
                                    $search = "SELECT Name, ProductID FROM CSIS2440.Products ORDER BY Name";
                                    $return = $connection->query($search);
                                    
                                    if(!$return)
                                    {
                                        $message = "Whole query: " .$search;
                                        echo $message;
                                        die("Invalid query: " .mysqli_error());
                                    }
                                    
                                    while($row = mysqli_fetch_array($return))
                                    {
                                        if($row['ProductID'] == $product)
                                        {
                                            echo "<option value='" .$row['ProductID']. "'selected = 'selected'>" .$row['Name']. "</option>\n";
                                        }
                                        else
                                        {
                                            echo "<option value='" .$row['ProductID']. "'>" .$row['Name']. "</option>\n";
                                        }
                                    }
                                ?>
                            </select>
                            <table>
                                <tr>
                                    <td><input id="Add" type="submit" value="Add" name="action" class="button"></td>
                                    <td><input id="Remove" type="submit" value="Remove" name="action" class="button"></td>
                                    <td><input id="Empty" type="submit" value="Empty" name="action" class="button"></td>
                                    <td><input id="Info" type="button" value="Info" name="action" class="button" onclick="produceInfo(document.getElementById('SelectProduct').value);"></td>
                                </tr>
                            </table>
                        </div>
                    </div>
                    </form>
                </div>
            </div>
            
            <div class="row">
                <div class="col-sm-2"></div>
                <div class="col-sm-8">
                    <div>
                        <?php
                            if($_SESSION['cart']) //if cart isn't empty, show cart
                        {
                            echo "<table border=\"1\" padding=\"1\" width=\"660px\"><tr> <th class='namestyle'>Name</th> <th>Quantity</th> <th>Price</th> <th width=\"80px\">Cost</th> </tr>";
                            foreach($_SESSION['cart'] as $product => $quantity)
                            {
                                $sql = "SELECT Name, Price FROM CSIS2440.Products WHERE ProductID = " .$product;
                                $result = $connection->query($sql);
                                if(mysqli_num_rows($result) > 0)
                                {
                                    list($name, $price) = mysqli_fetch_row($result);
                                    $cost = $price * $quantity;
                                    $total = $total + $cost;
                                    
                                    echo "<tr>";
                                    echo "<td align=\"left\" width=\"400px\">$name</td>";
                                    echo "<td align=\"center\" width=\"75px\">$quantity</td>";
                                    echo "<td align=\"center\" width=\"100px\">" .money_format('%(#8n', $price). "</td>";
                                    echo "<td align=\"center\" width=\"120px\">" .money_format('%(#8n', $cost). "</td>";
                                    echo "</tr>";
                                }
                            }
                            
                            //show total
                            echo "<tr>";
                            echo "<td align=\"right\">Total Products</td> <td align=\"right\">$totalProducts</td> <td align=\"right\">Total</td>";
                            echo "<td align=\"right\">" .money_format('%(#8n', $total). "</td>";
                            echo "</tr>";
                        }
                        else
                        {
                            echo "<tr>";
                            echo "<td>&nbsp;&nbsp;&nbsp;&nbsp;There are no items in the cart</td>";
                            echo "</tr>";
                        }
                        echo "</table>";
                        mysqli_close($connection);
                        ?>
                    </div>
                </div>
            </div>
            
            <div class="row">
                <div class="col-sm-1">
                </div>
                <div class="col-sm-10">
                    <div class="form-group">
                        <br>
                        <br>
                        <br>
                        <div id="productInfo"></div>
                    </div>
                </div>
            </div>
        </div>
            <!-- Bootstrap core JavaScript -->
            <script src="../../../vendor/jquery/jquery.min.js" type="text/javascript"></script>
            <script src="../../../vendor/bootstrap/js/bootstrap.bundle.min.js" type="text/javascript"></script>

            <!-- Plugin JavaScript -->
            <script src="../../../vendor/jquery-easing/jquery.easing.min.js" type="text/javascript"></script>

            <!-- Contact Form JavaScript -->
            <script src="../../../js/jqBootstrapValidation.min.js" type="text/javascript"></script>
            <script src="../../../js/contact_me.min.js" type="text/javascript"></script>

            <!-- Custom scripts for this template -->
            <script src="../../../js/freelancer.min.js" type="text/javascript"></script>
    </body>
</html>
