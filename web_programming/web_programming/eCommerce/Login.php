<!DOCTYPE html>
<?php
  session_start();
?>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Login</title>
                <!-- Custom fonts for this theme -->
        <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">

        <!-- Theme CSS -->

        <link href="../../../css/freelancer.min.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <?php
        print<<<LOGIN
        <div>
            <form name="Login" method="post" action="CheckLogin.php">
            <br>
            <table align="center" border="0" cellpadding="3" cellspacing="1">
                <tr>
                    <td colspan="3"><h2>Account Sign-In</h2><hr><br></td>
                </tr>
                <tr>
                    <td width="80">Username: </td>
                    <td width="300"><input name="myUsername" id="myUsername" type="text" class="error"></td>
                </tr>
                <tr>
                    <td width="80">Password: </td>
                    <td width="300"><input name="myPassword" id="myPassword" type="password"></td>
                </tr>
                <tr>
                    <td colspan="3" align="center">
LOGIN;
        if(isset($_SESSION['NotMatch'])) //NEED ATTENTION
        {
            echo "<br>The username and password do not match";
        }
        
        print<<<LOGIN
                    </td>
                <tr>
                    <td colspan="3"><br></td>
                </tr>
                <tr>
                    <td colspan="2"><a href="NewUser.php">Create an Account</a></td>
                    <td><input type="submit" name="Login" value="Login" onclick= "return loginfilled();"></a></td>
                </tr>
            </table>
            </form>
        </div>
LOGIN;
        ?>
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
