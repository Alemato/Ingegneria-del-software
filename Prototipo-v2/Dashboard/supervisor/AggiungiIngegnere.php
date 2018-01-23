<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8"/>
    <link rel="icon" type="image/png" href="assets/img/favicon.ico">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>

    <title>AggiungiIngegneri</title>

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

        .search_margin {
            margin-bottom: 30px;
        }
        .margine_bottone{
            margin: 9px 3px !important;

        }
        .margine_bottone_salva{
            margin-left: 15px !important;
            margin-top: 15px !important;
        }


    </style>

</head>
<body>

<div class="wrapper">
    <div class="sidebar" data-color="blue">
        <div class="sidebar-wrapper">
            <div class="logo">
                <a href="Dashboard.html" class="simple-text">
                    Micron Technology
                </a>
            </div>

            <ul class="nav">
                <li>
                    <a href="Dashboard.html">
                        <p>Lista Ingegneri</p>
                    </a>
                </li>
                <li class="active">
                    <a>
                        <p>Aggiungi Ingegnere</p>
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
                    <a class="navbar-brand" href="#">Aggiungi Ingegnere</a>
                    <a href="Dashboard.html">
                        <button type="button" class="btn btn-default margine_bottone">Back</button>
                    </a>
                </div>
                <div class="collapse navbar-collapse">


                    <ul class="nav navbar-nav navbar-right">
                        <li>
                            <a href="">
                                <p>Profile</p>
                            </a>
                        </li>

                        <li>
                            <a href="#">
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
            <div class="container-fluid">
                <div class="row">
                    <div class="col-md-8">

                        <div>
                            <form role="form">
                                <div class="form-group">
                                    <label class="control-label">Nome</label>
                                    <input type="text" class="form-control underlined" placeholder="Nome">
                                </div>
                                <div class="form-group">
                                    <label class="control-label">Cognome</label>
                                    <input type="text" class="form-control underlined" placeholder="Cognome">
                                </div>
                                <div class="form-group">
                                    <label class="control-label">Mansione</label>
                                    <input type="text" class="form-control underlined" placeholder="Mansione">
                                </div>
                                <div class="form-group">
                                    <label class="control-label">Codice ID</label>
                                    <input type="text" class="form-control underlined" placeholder="CodiceID">
                                </div>

                            </form>
                        </div>
                    </div>
                </div>
            </div>

            <div>
                <a href="Dashboard.html">
                    <input class="btn btn-default margine_bottone_salva" type="submit" value="Salva">
                </a>
            </div>

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

<!-- autoGenerate areas -->
<script src="system/pageGenerator/area.js"></script>

</html>
