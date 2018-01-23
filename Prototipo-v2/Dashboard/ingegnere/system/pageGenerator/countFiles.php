<?php

	class countFiles {	


		function areaFiles() {

			$dir = 'data/';
			$areaHTML = "";

			$json = file_get_contents($dir.'Aree.json');
			$jsonData = json_decode($json, true);

			foreach ($jsonData as $key => $value) {
				
				$areaHTML .= '<div class="col-md-3">
							<div class="card" onclick="window.open(\'Cluster.php?area='.$key.'\', \'_self\');">
							<div class="header">
							<h4 class="title">'.$key.'</h4>
							<h4 class="title">Inefficiency Rate: '.$value.'%</h4>
							</div>
							<div class="ct-chart">
							<div id="canvas-holder" style="width:100%;">
								<canvas id="chart_'.$key.'"/>
								<script language="JavaScript">
									var ctx'.$key.' = document.getElementById("chart_'.$key.'").getContext("2d");
									var chart_'.$key.' = new Chart(ctx'.$key.', {
										type: "pie",
										data: {
											labels: ["Inefficiency ", "Efficiency "],
											datasets: [{
												backgroundColor: [
													"#ff4a55",
													"#87cb16"
												],
												data: ['.$value.', '.(100-$value).']
											}]
										},
										options: {
											legend: {
												display: false
											},
											responsive: true
										}
									});
								</script>
							</div>
							</div>
							<div class="footer">
										<div class="legend">
												<i class="fa fa-circle text-success"></i> Efficiency
												<i class="fa fa-circle text-danger"></i> Inefficiency
										</div>
											</div>
										</div>
									</div>
							</div>';
			}

			echo $areaHTML;
		}


		function clusterFiles($nArea) {

			$dir = 'data/';
			$files = scandir($dir);
			$clusterHTML = "";

			foreach ($files as $f => $value) {
				
				foreach ($files as $f2 => $value2) {

					if(strcmp($value2, ('A' . ($nArea) . 'C' . ($f+1) . '.json')) == false) {

						$json = file_get_contents($dir . ('A' . ($nArea) . 'C' . ($f+1) . '.json'));
						$jsonData = json_decode($json, true);

						$clusterHTML .= '<div class="col-md-3">
								<div class="card" onclick="window.open(\'Robot.php?area=A'.$nArea."&cluster=".$jsonData["ClusterName"].'\', \'_self\');">
								<div class="header">
								<h4 class="title">'.$jsonData["ClusterName"].'</h4>
								<h4 class="title">Inefficiency Rate: '.$jsonData["ClusterInef"].'%</h4>
								</div>
								<div class="ct-chart">
								<div id="canvas-holder" style="width:100%;">
									<canvas id="chart_'.$jsonData["ClusterName"].'"/>
									<script language="JavaScript">
										var ctx'.$jsonData["ClusterName"].' = document.getElementById("chart_'.$jsonData["ClusterName"].'").getContext("2d");
										var chart_'.$jsonData["ClusterName"].' = new Chart(ctx'.$jsonData["ClusterName"].', {
											type: "pie",
											data: {
												labels: ["Inefficiency ", "Efficiency "],
												datasets: [{
													backgroundColor: [
														"#ff4a55",
														"#87cb16"
													],
													data: ['.$jsonData["ClusterInef"].', '.(100-$jsonData["ClusterInef"]).']
												}]
											},
											options: {
												legend: {
													display: false
												},
												responsive: true
											}
										});
									</script>
								</div>
								</div>
								<div class="footer">
											<div class="legend">
													<i class="fa fa-circle text-success"></i> Efficiency
													<i class="fa fa-circle text-danger"></i> Inefficiency
											</div>
												</div>
											</div>
										</div>
								</div>';
					}
				}
			}

			echo $clusterHTML;
		}


		function robotsCount($nArea, $nCluster) {

			$json = file_get_contents('data/A' . ($nArea) . 'C' . ($nCluster) . '.json');
			$data = json_decode($json, true);
			$robotHTML = "";

			foreach ($data["Robots"] as $key => $value) {
				
				$robotHTML .= '<div class="col-md-3">
								<div class="card">
								<div class="header">
								<h4 class="title">'.$key.'</h4>
								<h4 class="title">Inefficiency Rate: '.$value.'%</h4>
								</div>
								<div class="ct-chart">
								<div id="canvas-holder" style="width:100%;">
									<canvas id="chart_'.$key.'"/>
									<script language="JavaScript">
										var ctx'.$key.' = document.getElementById("chart_'.$key.'").getContext("2d");
										var chart_'.$key.' = new Chart(ctx'.$key.', {
											type: "pie",
											data: {
												labels: ["Inefficiency ", "Efficiency "],
												datasets: [{
													backgroundColor: [
														"#ff4a55",
														"#87cb16"
													],
													data: ['.$value.', '.(100-$value).']
												}]
											},
											options: {
												legend: {
													display: false
												},
												responsive: true
											}
										});
									</script>
								</div>
								</div>
								<div class="footer">
											<div class="legend">
													<i class="fa fa-circle text-success"></i> Efficiency
													<i class="fa fa-circle text-danger"></i> Inefficiency
											</div>
												</div>
											</div>
										</div>
								</div>';
			}

			echo $robotHTML;
		}
	}
?>