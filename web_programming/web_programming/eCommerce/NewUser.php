<!DOCTYPE html>
<!--COMPLETE-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>New Account Form</title>
                <!-- Custom fonts for this theme -->
        <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">
        <script src="FormValidation.js"></script>

        <!-- Theme CSS -->

        <link href="../../../css/freelancer.min.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-8">
                    <form method="post" action="NewUserResults.php" class="form-horizontal" name="UserForm">
                        <div class="form-group">
                            <br>
                            <div class="col-md-4">
                                <h2>New User Form</h2>
                            </div>
                            
                            <hr>
                            <br>
                            
                            <div class="form-group">
                                <label class="col-md-4 control-label" for="Username">Username</label>
                                <div class="col-md-4">
                                    <input id="Username" name="Username" type="text" placeholder="Enter a username" class="form-control input-md" maxlength="15">
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="col-md-4 control-label" for="Email">Email</label>
                                <div class="col-md-4">
                                    <input id="Email" name="Email" type="text" placeholder="Enter your email as _____@example.com" class="form-control input-md">
                                    <span></span>
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="col-md-4 control-label" for="Birthday">Birthdate</label>
                                <div class="col-md-4">
                                    <input id="Birthday" name="Birthday" type="date" class="form-control input-md" min="1900-01-01">
                                    <span></span>
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="col-md-4 control-label" for="Password">Password</label>
                                <div class="col-md-4">
                                    <input id="Password" name="Password" type="password" placeholder="Enter a password" class="form-control input-md">
                                    <span></span>
                                </div>
                            </div>
                            <br>
                            
                            <!-- Submit button -->
                            <div class="col-md-4">
                                <div id="selectSubmit">
                                    <button type="submit" name="selectSubmit" value="Submit" class="btn btn-primary" onclick="return(validateSubmit());">Submit</button>
                                    <button type="button" name="returnLogin" class="btn btn-primary" onclick="location.href='Login.php';">Return to Login</button>
                                </div>
                            </div>
                            <input type="hidden" value=1 name="number">
                            <br>
                            <hr>
                        </div>
                    </form>
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
