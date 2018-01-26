<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <link rel="icon" type="image/png" href="assets/img/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>

    <title>Robots</title>

    <meta content='width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0' name='viewport'/>
    <meta name="viewport" content="width=device-width"/>


    <!-- Bootstrap core CSS     -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet"/>

    <!-- Animation library for notifications   -->
    <link href="assets/css/animate.min.css" rel="stylesheet"/>

    <!--  Light Bootstrap Table core CSS    -->
    <link href="assets/css/light-bootstrap-dashboard.css?v=1.4.0" rel="stylesheet"/>


    <!--  CSS for Demo Purpose, don't include it in your project     -->
    <link href="assets/css/demo.css" rel="stylesheet"/>


    <!--     Fonts and icons     -->
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet">
    <link href='http://fonts.googleapis.com/css?family=Roboto:400,700,300' rel='stylesheet' type='text/css'>
    <link href="assets/css/pe-icon-7-stroke.css" rel="stylesheet"/>

    <style type="text/css">

        .search_margin{
            margin-bottom: 30px;
        }
        .margine_bottone{
            margin: 9px 3px !important;

        }


    </style>

</head>
<body>

<div class="wrapper">
    <div class="sidebar" data-color="blue">
        <div class="sidebar-wrapper">
            <div class="logo">
                <a href="Dashboard.php" class="simple-text">
                    Micron Technology
                </a>
            </div>

            <ul class="nav">
                <li>
                    <a href="Dashboard.php">
                        <p>Home</p>
                    </a>
                </li>
                <li>
                    <a href="Area.php">
                        <p>Area</p>
                    </a>
                </li>
                <li class="active">
                    <a>
                        <p>Robot</p>
                    </a>
                </li>

            </ul>
        </div>
    </div>

    <!-- Main Pannel -->

    <div class="main-panel">

        <!-- Navbar Menu Top -->

        <nav class="navbar navbar-default navbar-fixed">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse"
                            data-target="#navigation-example-2">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <a class="navbar-brand" href="#">Robot View</a>
                    <a href="Cluster.php">
                        <button type="button" class="btn btn-default margine_bottone">Back</button>
                    </a>
                </div>
                <div class="collapse navbar-collapse">


                    <ul class="nav navbar-nav navbar-right">
                        <li>
                            <a href="Login.php">
                                <p>Log out</p>
                            </a>
                        </li>
                        <li class="separator hidden-lg"></li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- Corpo -->

        <div class="content">

            <!-- Search -->

            <div class="col-sm-12">

                <div class="row search_margin">
                    <div class="col-lg-6">
                        <div class="input-group">
                            <input type="text" class="form-control" placeholder="Example R1" id="searchTXT">
                            <span class="input-group-btn">
                                <button class="btn btn-default" type="button" id="search">Search</button>
                            </span>
                        </div>
                    </div>
                </div>

            </div>

            <div class="container-fluid">
                <div class="row" id="autoRobot">
                    <!-- autoGenerate areas -->
                </div>
            </div>
        </div>


</body>

<!--   Core JS Files   -->
<script src="assets/js/jquery.3.2.1.min.js" type="text/javascript"></script>
<script src="assets/js/bootstrap.min.js" type="text/javascript"></script>

<!--  Notifications Plugin    -->
<script src="assets/js/bootstrap-notify.js"></script>

<!--  Charts Plugin -->
<script src="assets/js/Chart.bundle.js"></script>

<!-- autoGenerate areas -->
<script src="system/pageGenerator/robot.js"></script>

</html>