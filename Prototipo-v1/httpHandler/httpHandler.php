<?php

	// Set variabili ricevuti dall'ESB
	$idArea = $_POST['ID_Area'];
	$cluster = $_POST['ID_Cluster'];
	$nameRobot = $_POST['Name_Of_Robot'];
	$s1 = $_POST['S1'];
	$s2 = $_POST['S2'];
	$s3 = $_POST['S3'];
	$s4 = $_POST['S4'];
	$s5 = $_POST['S5'];
	$s6 = $_POST['S6'];
	$s7 = $_POST['S7'];

	// Parametri di connessione
	$host    = "localhost";
	$port    = 2222;

	// Messaggio da inviare tramite socket
	$separatore = ",";
	$message = $idArea . $separatore . $cluster . $separatore . $nameRobot . $separatore . 
			   $s1 . $separatore . $s2 . $separatore . $s3 . $separatore . 
			   $s4 . $separatore . $s5 . $separatore . $s6 . $separatore . $s7;

	//echo $message;
	
	// Creazione Socket
	$socket = socket_create(AF_INET, SOCK_STREAM, 0) or die("Impossibile creare il socket\n");

	// Connessione al server su porta '2222' in localhost
	$result = socket_connect($socket, $host, $port) or die("Impossibile connettersi al server\n");  

	// Invio stringa al server
	socket_write($socket, $message, strlen($message)) or die("Impossibile inviare i dati al server\n");

	socket_close($socket);

?>