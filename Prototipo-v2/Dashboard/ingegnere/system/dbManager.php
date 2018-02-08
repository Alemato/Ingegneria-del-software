<?php

class dbManager {

	private $servername = "localhost";
	private $username = "root";
	private $password = "";
	private $dbname = "spaghettioverflow";
	private $conn, $sql, $result;


	function connectDB() {

		$this->conn = new mysqli($this->servername, $this->username, $this->password, $this->dbname);
		$this->checkConnection();
	}


	private function checkConnection() {

		if ($this->conn->connect_error) {
			die("Connessione fallita: " . $this->conn->connect_error);
		} 
	}


	private function executeQuery() {

		$this->result = $this->conn->query($this->sql);

		if ($this->result === FALSE) {

			echo "Errore: " . $this->sql . "<br>" . $this->conn->error;
		}
	}


	function closeConnection() {

		$this->conn->close();
	}


	/* SET INEF CLUSTER */
	function setInefCluster($idA, $nameA, $idC, $nameC, $inef) {

		$this->sql = "INSERT IGNORE INTO areas (id, name)
					  VALUES ('$idA', '$nameA')";

		$this->executeQuery();


		$this->sql = "INSERT INTO clusters (id, idA, name, inef)
					  VALUES ($idC, '$idA', '$nameC', '$inef')
					  ON DUPLICATE KEY UPDATE
					  id = $idC,
					  idA = $idA,
					  name = '$nameC',
					  inef = $inef";
						
		$this->executeQuery();
	}


	/* GET INEF CLUSTER */
	function getInefCluster($nArea, $id) {
					  
		$this->sql = "SELECT clusters.inef
					  FROM clusters INNER JOIN areas
					  ON areas.id = clusters.idA
					  WHERE clusters.idA = '$nArea'
					  AND 	clusters.id = '$id'";
		$this->executeQuery();

		if ($this->result->num_rows > 0) {
			
			while($row = $this->result->fetch_assoc()) {
				return $row["inef"];
			}
		} else {
			return "40";
		}
	}
}
?>