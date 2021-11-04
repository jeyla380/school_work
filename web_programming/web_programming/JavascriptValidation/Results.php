<?php
require_once 'DatabaseConnect.php';
include 'Form.php';

$choiceSelect = $_POST['Choice'];
$number = $_POST['number'];
$firstName = $_POST['FirstName'];
$lastName = $_POST['LastName'];
$email = $_POST['Email'];
$birthDate = $_POST['Birthdate'];
$password = $_POST['Password'];
$id = $_POST['idPlayers'];

//Protect MySQL Injection
$email = mysql_fix_string($connect, $email);
$password = mysql_fix_string($connect, $password);

//so you can't see the password when displaying input
$output_password = str_repeat('*', strlen($password));
//hash option:
//$hash = hash("ripemd128", $password);

    //based on what was chosen
    switch ($choiceSelect) 
    {
        case "Insert": //COMPLETE
            $insert = "INSERT INTO `CSIS2440`.`Players` (`FirstName`, `LastName`, `Email`, `Birthdate`, `Password`) "
            . "VALUES ('".$firstName."', '".$lastName."', '".$email."', '".$birthDate."', '".$password."')";
            $success = $connect->query($insert);

            if($success == false)
            {
                //query is unable to run
                $fail = "Whole query " .$insert. "<br>";
                echo $fail;
                print('Invalid query: ' .mysqli_error($connect). "<br>");
            }
            else
            {
                //successful!
                print<<<HTML
                <br>
                <div class="col-md-8">
                <h4>Information Has Been Added </h4>
                    <table border="2" cellpadding="3" cellspacing="1">
                        <tr align="center">
                            <th>First Name</th>
                            <th>Last Name</th>
                            <th>Email</th>
                            <th>Birthdate (yyyy-mm-dd)</th>
                            <th>Password</th>
                        </tr>
                        <tr align="center">
                            <td>$firstName</td>
                            <td>$lastName</td>
                            <td>$email</td>
                            <td>$birthDate</td>
                            <td>$output_password</td>
                        </tr>
                    </table>
                </div>
                <br>
HTML;
            }
            break;
            
        case "Search": //COMPLETE
            $search = "SELECT idPlayers, FirstName, LastName, Email, Birthdate, Password FROM CSIS2440.Players WHERE idPlayers = '$id'";
            $return = $connect->query($search);
                                    
            if(!$return)
            {
                //error
                $message = "Whole query " .$search;
                echo $message;
                ie('Invalid query: ' .mysqli_error($connect));
            }
            else
            {
                //successful!
                if (mysqli_num_rows($return) > 0) 
                {
                    // output data of each row
                    while($row = mysqli_fetch_assoc($return)) 
                    {
                        $printId = $row["idPlayers"];
                        $printFirst = $row["FirstName"];
                        $printLast = $row["LastName"];
                        $printEmail = $row["Email"];
                        $printBirth = $row["Birthdate"];
                        $printPass = $row["Password"];
                        $output_printPass = str_repeat('*', strlen($printPass));
                        
                        print<<<HTML
                        <br>
                        <div class="col-md-8">
                        <h4>Search Results </h4>
                            <table border="2" cellpadding="3" cellspacing="1">
                                <tr align="center">
                                    <th>ID</th>
                                    <th>First Name</th>
                                    <th>Last Name</th>
                                    <th>Email</th>
                                    <th>Birthdate (yyyy-mm-dd)</th>
                                    <th>Password</th>
                                </tr>
                                <tr align="center">
                                    <td>$id</td>
                                    <td>$printFirst</td>
                                    <td>$printLast</td>
                                    <td>$printEmail</td>
                                    <td>$printBirth</td>
                                    <td>$output_printPass</td>
                                </tr>
                            </table>
                        </div>
                        <br>
HTML;
                    }
                }
            }
            break;
        
        case "Update":
            $update = "UPDATE CSIS2440.Players SET FirstName = '$firstName', LastName = '$lastName', Email='$email', Birthdate = '$birthDate', Password = '$password' WHERE idPlayers = '$id'";
            $success = $connect->query($update);
            if($success == false)
            {
                //didn't update
                $fail = "Whole query " .$update. "<br>";
                echo $fail;
                die ('Invalid query: ' .mysqli_error($connect));
            }
            else
            {
                print<<<HTML
                        <br>
                        <div class="col-md-8">
                            <h4>Your Information Has Been Updated </h4>
                        </div>
                        <br>
HTML;
            }
            break;
    }

//Submit button appears with "Add", "Search", or "Update" is clicked on & resets the form
print<<<FORM
<div class="col-md-8">
   <form method="post" action="Form.php" class="form-horizontal">
FORM;

print<<<FORM
        <div class="form-group">
            <div class="col-md-6">
                <input id="submit" name="UnSubmit" class="btn btn-primary" type="submit">
            </div>
        </div>
        <input type='hidden' value=0 name='number'>
    </form>
</div>
FORM;


