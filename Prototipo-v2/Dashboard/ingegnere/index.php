<?php

include("config.php");
session_start();

if(isset($_SESSION['login_user_en'])){
    header("location:area.php");
 }

if($_SERVER["REQUEST_METHOD"] == "POST") {
   
   $myusername = mysqli_real_escape_string($db,$_POST['username']);
   $mypassword = mysqli_real_escape_string($db,$_POST['password']); 
   
   $sql = "SELECT name FROM engineers WHERE username = '$myusername' and password = '$mypassword'";
   $result = mysqli_query($db,$sql);
   $row = mysqli_fetch_array($result,MYSQLI_ASSOC);
   $active = $row['name'];
   
   $count = mysqli_num_rows($result);
     
   if($count == 1) {
      $_SESSION['login_user_en'] = $myusername;
      
      header("Location:area.php");
   }
}

?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8" />
    <link rel="icon" type="image/png" href="assets/img/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />

    <title>Login</title>

    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport' />
    <meta name="viewport" content="width=device-width" />


    <!-- Bootstrap core CSS     -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet" />

    <!-- Animation library for notifications   -->
    <link href="assets/css/animate.min.css" rel="stylesheet"/>

    <!--  Light Bootstrap Table core CSS    -->
    <link href="assets/css/light-bootstrap-dashboard.css?v=1.4.0" rel="stylesheet"/>


    <!--  CSS for Demo Purpose, don't include it in your project     -->
    <link href="assets/css/demo.css" rel="stylesheet" />


    <!--     Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>
    <link href="assets/css/pe-icon-7-stroke.css" rel="stylesheet" />

    <style type="text/css">

        .login_margin{
            margin-top: 180px;
        }

    </style>

</head>
<body>

<div class="wrapper">
    <div class="sidebar" data-color="blue">
        <div class="sidebar-wrapper">
            <div class="logo">
                <a>
                    Micron Technology
                </a>
            </div>

        </div>
    </div>




    <div class="main-panel">

            <div class="container">
                <div class=" col-sm-4 col-sm-offset-4 login_margin">

                    <form class="form-signin" action = "" method = "post">
                        <h2 class="form-signin-heading">Please sign in</h2>
                        <label for="inputEmail" class="sr-only">ID</label>
                        <input type = "text" name = "username" class="form-control" placeholder="ID" required="" autofocus="">
                        <label for="inputPassword" class="sr-only">Password</label>
                        <input  type = "password" name = "password" class="form-control" placeholder="Password" required="">
                        <a>
                            <button class="btn btn-lg btn-primary btn-block margin-top" type="submit" value="Submit">Sign in</button>
                        </a>
                    </form>
                </div>

            </div>



    </div>


</body>

<!--   Core JS Files   -->
<script src="assets/js/jquery.3.2.1.min.js" type="text/javascript"></script>
<script src="assets/js/bootstrap.min.js" type="text/javascript"></script>

<!--  Charts Plugin -->
<script src="assets/js/chartist.min.js"></script>

<!--  Notifications Plugin    -->
<script src="assets/js/bootstrap-notify.js"></script>

<!-- Light Bootstrap Table Core javascript and methods for Demo purpose -->
<script src="assets/js/light-bootstrap-dashboard.js?v=1.4.0"></script>

<!-- Light Bootstrap Table DEMO methods, don't include it in your project! -->
<script src="assets/js/demo.js"></script>

</html>
