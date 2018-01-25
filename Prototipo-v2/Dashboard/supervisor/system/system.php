<?php
	
	include 'dbManager.php';

	$functionName = $_POST['functionName'];
	$name = $_POST['name'];
	$user = $_POST['user'];
	$password = $_POST['password'];
	$type = $_POST['type'];

	if ($functionName == "lsUsers") {
	    lsUsers();
	} else if ($functionName == "addUser" && $type == "Ingegnere") {
	    addIng($name, $user, $password);
	} else if ($functionName == "addUser" && $type == "Supervisor") {
	    addSupv($name, $user, $password);
	} else if ($functionName == "removeUser") {
	    removeUser($user, $type);
	}


	function lsUsers() {

		$dbManager = new dbManager;
		$dbManager->connectDB();
		$method = $dbManager->listUsers();
		$dbManager->closeConnection();
	    echo $method;
	}


	function addIng($name, $user, $password) {

		$dbManager = new dbManager;
		$dbManager->connectDB();

		if(!$dbManager->existEnginner($user)) {
			
			$dbManager->insertEngineer($name, $user, $password);
			echo "Ingegnere aggiunto";
		} else {

			echo "Ingegnere esistente";
		}

		$dbManager->closeConnection();
	}


	function addSupv($name, $user, $password) {

		$dbManager = new dbManager;
		$dbManager->connectDB();

		if(!$dbManager->existSupervisor($user)) {
			
			$dbManager->insertSupervisor($name, $user, $password);
			echo "Supervisor aggiunto";
		} else {

			echo "Supervisor esistente";
		}

		$dbManager->closeConnection();
	}


	function removeUser($user, $type) {

		if($type == "Ingegnere") {

			$dbManager = new dbManager;
			$dbManager->connectDB();
			$dbManager->deleteEngineer($user);
			$dbManager->closeConnection();
			
		}  else if ($type == "Supervisor") {

			$dbManager = new dbManager;
			$dbManager->connectDB();
			$dbManager->deleteSupervisor($user);
			$dbManager->closeConnection();
		}
	}

?>