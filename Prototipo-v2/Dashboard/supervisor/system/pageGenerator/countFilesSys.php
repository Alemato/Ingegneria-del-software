<?php

	include 'countFiles.php';

	$functionName = $_POST['functionName'];
	$area = $_POST['nArea'];
	$cluster = $_POST['nCluster'];

	if ($functionName == "area") {
	    area();
	} else if ($functionName == "cluster") {
	    cluster($area);
	} else if ($functionName == "robot") {
	    robot($area, $cluster);
	}


	function area() {

	    $countFiles = new countFiles();
	    $method = $countFiles->areaFiles();
	    echo $method;
	}


	function cluster($nArea) {

	    $countFiles = new countFiles();
	    $method = $countFiles->clusterFiles($nArea);
	    echo $method;
	}


	function robot($nArea, $nCluster) {

	    $countFiles = new countFiles();
	    $method = $countFiles->robotsCount($nArea, $nCluster);
	    echo $method;
	}

?>