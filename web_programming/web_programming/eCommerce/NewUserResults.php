<?php
//COMPLETE
require_once 'DatabaseConnection.php';
include 'NewUser.php';

$selectSubmit = $_POST['selectSubmit'];
$number = $_POST['number'];
$username = $_POST['Username'];
$email = $_POST['Email'];
$birthday = $_POST['Birthday'];
$password = $_POST['Password'];

//Protect MySQL Injection
$username = mysql_fix_string($connection, $username);
$password = mysql_fix_string($connection, $password);

//hashes password
$hash = hash("ripemd128", $password);

//Doesn't show password when displayed
$output_password = str_repeat('*', strlen($password));

if($selectSubmit)
{
    $insert = "INSERT INTO `CSIS2440`.`Account` (`Username`, `Email`, `Birthday`, `Password`) VALUES ('".$username."', '".$email."', '".$birthday."', '".$password."')";
    $success = $connection->query($insert);
    
    if($success == false)
    {
        $failure = "Whole query:" .$insert. "<br>";
        echo $failure;
        print("Invalid query: " .mysqli_error($connection). "<br>");
    }
    else
    {
        ?>
        <br>
        <div class="col-md-8">
            <h4>Information Has Been Added</h4>
            <table border="2" cellpadding="3" cellspacing="1">
                <tr align="center">
                    <th>Username</th>
                    <th>Email</th>
                    <th>Birthday (yyyy-mm-dd)</th>
                    <th>Password</th>
                </tr>
                <tr>
                    <?php
                    print<<<HTML
                    <td>$username</td>
                    <td>$email</td>
                    <td>$birthday</td>
                    <td>$output_password</td>
HTML;
                    ?>
                </tr>
            </table>
        </div>
        <br>
        <?php
    }
}
?>

<div class="col-md-8">
    <form method="post" action="NewUser.php" class="form-horizontal">
        <div class="form-group">
            <div class="col-md-6">
                <input id="Submit" name="UnSubmit" class="btn btn-primary" type="submit" value="Enter">
            </div>
        </div>
        <input type='hidden' value=0 name='number'>
    </form>
</div>
