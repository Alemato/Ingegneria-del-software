<?php

	include 'countFiles.php';
	include "../dbManager.php";

	$functionName = $_POST['functionName'];
	$area = $_POST['nArea'];
	$cluster = $_POST['nCluster'];
	$value = $_POST['value'];


	if ($functionName == "area") {
	    area();
	} else if ($functionName == "cluster") {
	    cluster($area);
	} else if ($functionName == "robot") {
	    robot($area, $cluster);
	} else if ($functionName == "setInef") {
		$idA= str_replace('A', '', $area);
		$idC= str_replace('C', '', $cluster);
	    setInef($idA, $area, $idC, $cluster, $value);
	}


	function area() {

	    $countFiles = new countFiles();
	    $method = $countFiles->areaFiles();
	    echo $method;
	}


	function cluster($nArea) {

		$dbManager = new dbManager;
	    $countFiles = new countFiles();
	    $method = $countFiles->clusterFiles($nArea, $dbManager);
	    echo $method;
	}


	function robot($nArea, $nCluster) {

	    $countFiles = new countFiles();
	    $method = $countFiles->robotsCount($nArea, $nCluster);
	    echo $method;
	}


	function setInef($idA, $area, $idC, $cluster, $value) {
		
		$dbManager = new dbManager;
		$dbManager->connectDB();
		$dbManager->setInefCluster($idA, $area, $idC, $cluster, $value);
		$dbManager->closeConnection();
	}

?>