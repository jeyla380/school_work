<!DOCTYPE html>
<!-- HTML Form -->
<html>
    <head>
        <meta charset="UTF-8">
        <title>MySQL Form</title>
        <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Montserrat:400,700" rel="stylesheet" type="text/css">
        <link href="https://fonts.googleapis.com/css?family=Lato:400,700,400italic,700italic" rel="stylesheet" type="text/css">
        <script src="javascript.js"></script>
        <!-- Theme CSS -->
        <link href="../../../css/freelancer.min.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <div class="container-fluid">
            <div class="row">
                <div class="col-sm-8">
                    <form method="post" action="Results.php" class="form-horizontal" name="myForm">
                        <div class="form-group">
                            <br>
                            <div class="col-md-4">
                                <h2>MySQL Form</h2>
                            </div>
                            
                            <hr>
                            <br>
                            <div class="form-group">
                                <label class="col-md-4 control-label" for="idPlayers">ID <strong>(For Searching and Updating Purposes Only)</strong></label>
                                <div class="col-md-4">
                                    <input id="idPlayers" name="idPlayers" type="text" placeholder="Please enter the ID Number" class="form-control input-md">
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="col-md-4 control-label" for="FirstName">First Name</label>
                                <div class="col-md-4">
                                    <input id="FirstName" name="FirstName" type="text" placeholder="Enter your first name" class="form-control input-md">
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="col-md-4 control-label" for="LastName">Last Name</label>
                                <div class="col-md-4">
                                    <input id="LastName" name="LastName" type="text" placeholder="Enter your last name" class="form-control input-md">
                                    <span></span>
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
                                <label class="col-md-4 control-label" for="Birthdate">Birthdate</label>
                                <div class="col-md-4">
                                    <input id="Birthdate" name="Birthdate" type="date" class="form-control input-md" min="1900-01-01">
                                    <span></span>
                                </div>
                            </div>
                            
                            <div class="form-group">
                                <label class="col-md-4 control-label" for="Password">Password</label>
                                <div class="col-md-4">
                                    <input id="Password" name="Password" type="password" placeholder="Enter your password" class="form-control input-md">
                                    <span></span>
                                </div>
                            </div>
                            <br>
                            
                            <!-- Buttons for Search, Add, Update -->
                            <div class="col-md-4">
                                <label>Choose what you would like to do:</label>
                                <div id="Choice" value="Choice" name="Choice">
                                    <button type="submit" name="Choice" value="Search" class="btn btn-primary">Search</button>
                                    <button type="submit" name="Choice" value="Insert" class="btn btn-primary">Add</button>
                                    <button type="submit" name="Choice" value="Update" class="btn btn-primary">Update</button>
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
