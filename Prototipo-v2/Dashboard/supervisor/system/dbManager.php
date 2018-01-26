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


	function insertEngineer($name, $username, $password) {

		$this->sql = "INSERT INTO engineers (name, username, password)
					  VALUES ('$name', '$username', '$password')";
		$this->executeQuery();
	}


	function insertSupervisor($name, $username, $password) {

		$this->sql = "INSERT INTO supervisors (name, username, password)
					  VALUES ('$name', '$username', '$password')";
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


	function listUsers() {

		$HTML = "";

		$this->sql = "SELECT name, username FROM engineers";
		$this->executeQuery();

		if ($this->result->num_rows > 0) {

			while($row = $this->result->fetch_assoc()) {

				$HTML .= '<div class="list-group-item">
						<div class="row">
							<div class="col-md-9">
								<div class="col-md-3">
									<p class="list-group-item-heading text-dark">Nome Ingegnere: <b>'.$row["name"].'</b></p>
								</div>
								<div class="col-md-3">
									<p class="list-group-item-text text-dark")">ID Ingegnere: <b>'.$row["username"].'</b></p>
								</div>
								<div class="col-md-3">
									<p class="list-group-item-text text-dark">Mansione: <b>Ingegnere</b></p>
								</div>
							</div>
							<div class="col-md-2">
								<a href="../Dashboard.php">
									<a class="btn btn-default margine_bottone_salva" id='.$row["username"].' onClick="del_click(this.id, \'Ingegnere\')">Elimina</a>
								</a>
							</div>
						</div>
					</div>';
			}
		}

		$this->sql = "SELECT name, username FROM supervisors";
		$this->executeQuery();

		if ($this->result->num_rows > 0) {

			while($row = $this->result->fetch_assoc()) {

				$HTML .= '<div class="list-group-item">
						<div class="row">
							<div class="col-md-9">
								<div class="col-md-3">
									<p class="list-group-item-heading text-dark">Nome Ingegnere: <b>'.$row["name"].'</b></p>
								</div>
								<div class="col-md-3">
									<p class="list-group-item-text text-dark">ID Ingegnere: <b>'.$row["username"].'</b></p>
								</div>
								<div class="col-md-3">
									<p class="list-group-item-text text-dark">Mansione: <b>Supervisor</b></p>
								</div>
							</div>
							<div class="col-md-2">
								<a href="../Dashboard.php">
									<a class="btn btn-default margine_bottone_salva" id='.$row["username"].' onClick="del_click(this.id, \'Supervisor\')">Elimina</a>
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