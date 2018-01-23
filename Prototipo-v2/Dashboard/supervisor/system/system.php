<?php

	include 'dbManager.php';

	$functionName = $_POST['functionName'];
	$name = $_POST['name'];
	$password = $_POST['password'];

	if ($functionName == "lsSupervisor") {
	    lsSupervisor();
	} /*else if ($functionName == "cluster") {
	    cluster($area);
	} else if ($functionName == "robot") {
	    robot($area, $cluster);
	}*/


	function lsSupervisor() {

		$dbManager = new dbManager;
		$dbManager->connectDB();
		$method = $dbManager->listSupervisor();
		$dbManager->closeConnection();
	    echo $method;
	}

?>