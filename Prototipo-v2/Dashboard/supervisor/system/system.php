<?php

	include 'dbManager.php';

	$functionName = $_POST['functionName'];
	$name = $_POST['name'];
	$user = $_POST['user'];
	$password = $_POST['password'];

	if ($functionName == "lsSupervisor") {
	    lsSupervisor();
	} else if ($functionName == "addUser") {
	    addUser($name, $user, $password);
	} /*else if ($functionName == "robot") {
	    robot($area, $cluster);
	}*/


	function lsSupervisor() {

		$dbManager = new dbManager;
		$dbManager->connectDB();
		$method = $dbManager->listSupervisor();
		$dbManager->closeConnection();
	    echo $method;
	}


	function addUser($name, $user, $password) {

		$dbManager = new dbManager;
		$dbManager->connectDB();

		if(!$dbManager->existEnginner($user)) {
			
			$dbManager->insertEngineer($name, $user, $password);
			echo "Aggiunto";
		} else {

			echo "User esistente";
		}

		$dbManager->closeConnection();
	}

?>