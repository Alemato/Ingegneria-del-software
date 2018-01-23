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


	/* INSERT */
	function insertCluster($name, $inef) {

		$this->sql = "INSERT INTO clusters (name, inef)
					  VALUES ('$name', '$inef')";
		$this->executeQuery();
	}


	function insertEngineer($username, $password) {

		$this->sql = "INSERT INTO engineers (username, password)
					  VALUES ('$username', '$password')";
		$this->executeQuery();
	}


	function insertSupervisor($username, $password) {

		$this->sql = "INSERT INTO supervisors (username, password)
					  VALUES ('$username', '$password')";
		$this->executeQuery();
	}


	/* UPDATE */
	function updateClusterInef($name, $inef) {

		$this->sql = "UPDATE clusters SET inef=$inef WHERE name='$name'";
		$this->executeQuery();
	}


	function updateEngineerPassword($username, $password) {

		$this->sql = "UPDATE engineers SET password='$password' WHERE username='$username'";
		$this->executeQuery();
	}


	function updateSupervisorPassword($username, $password) {

		$this->sql = "UPDATE supervisors SET password='$password' WHERE username='$username'";
		$this->executeQuery();
	}


	/* DELETE */
	function deleteEngineer($username) {

		$this->sql = "DELETE FROM engineers WHERE username='$username'";
		$this->executeQuery();
	}


	function deleteSupervisor($username) {

		$this->sql = "DELETE FROM supervisors WHERE username='$username'";
		$this->executeQuery();
	}


	/* SELECT*/
	function existEnginner($username) {
		
		$this->sql = "SELECT username FROM engineers WHERE username='$username'";
		$this->executeQuery();

		if($this->result->num_rows >=1 ) {

			return true;
		}

		return false;
	}


	function existSupervisor($username) {
		
		$this->sql = "SELECT username FROM supervisors WHERE username='$username'";
		$this->executeQuery();

		if($this->result->num_rows >= 1 ) {

			return true;
		}

		return false;
	}


	function listSupervisor() {

		$HTML = "";

		$this->sql = "SELECT name, username FROM supervisors";
		$this->executeQuery();

		if ($this->result->num_rows > 0) {

			while($row = $this->result->fetch_assoc()) {

				$HTML .= '<div class="list-group-item">
						<div class="row">
							<div class="col-md-9">
								<div class="col-md-3">
									<p class="list-group-item-heading text-dark">Nome Ingegnere: '.$row["name"].'</p>
								</div>
								<div class="col-md-3">
									<p class="list-group-item-text text-dark">ID Ingegnere: '.$row["username"].'</p>
								</div>
							</div>
							<div class="col-md-2">
								<a href="Dashboard.html">
									<button class="btn btn-default" type="submit">Rimuovi</button>
								</a>
							</div>
						</div>
					</div>';
			}
		}

		echo $HTML;
	}
}
?>