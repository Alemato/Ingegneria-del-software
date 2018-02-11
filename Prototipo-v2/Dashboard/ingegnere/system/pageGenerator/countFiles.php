<?php

	class countFiles {	


		function areaFiles() {

			$dir = 'data/';
			$areaHTML = "";

			$json = file_get_contents($dir.'Aree.json');
			$jsonData = json_decode($json, true);

			uasort($jsonData, function($a, $b) {
				return $a < $b;
			});

			foreach ($jsonData as $key => $value) {
				
				$areaHTML .= '<div class="col-md-3" id='.$key.'>
							<div class="card">
							<div class="header">
							<h4 class="title">'.$key.'</h4>
							<h4 class="title">Inefficiency Rate: '.$value.'%</h4>
							</div>
							<div class="ct-chart" style="height: 0% !important;">
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
							<button type="Apri" class="btn btn-success btn-block center-block" style="margin-bottom: 10px; width: 50% !important;" onclick="window.open(\'Cluster.php?area='.$key.'\', \'_self\');">Apri</button>
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


		function clusterFiles($nArea, $dbManager) {

			$dir = 'data/';
			$files = scandir($dir);
			$clusterHTML = "";
			$HTMLred = "";
			$HTMLgreen = "";
			$dbManager->connectDB();

			foreach ($files as $f => $value) {
				
				foreach ($files as $f2 => $value2) {

					if(strcmp($value2, ('A' . ($nArea) . 'C' . ($f+1) . '.json')) == false) {

						$json = file_get_contents($dir . ('A' . ($nArea) . 'C' . ($f+1) . '.json'));
						$jsonData = json_decode($json, true);

						$val = $dbManager->getInefCluster($nArea, $f+1);
						$alert = "";
						
						if($val <= $jsonData["ClusterInef"]) {

							$alert = 'style="border: solid 5px #D50000;"';
						} else {

							$alert = 'style="border: solid 5px #00C853;"';
						}

						$clusterHTML = '<div class="col-md-3" id='.$jsonData["ClusterName"].'>
								<div class="card" '.$alert.'>
								<div class="header">
								<h4 class="title">'.$jsonData["ClusterName"].'</h4>
								<h4 class="title">Inefficiency Rate: '.$jsonData["ClusterInef"].'%</h4>
								</div>
								<div style="height: 0% !important; padding:10px;">
								<div style="width:100%;">
								  <div class="progress">
									  <div class="progress-bar progress-bar-success" role="progressbar" style="width:'.(100-$jsonData["ClusterInef"]).'%">
										'.(100-$jsonData["ClusterInef"]).'%
									  </div>
									  <div class="progress-bar progress-bar-danger" role="progressbar" style="width:'.$jsonData["ClusterInef"].'%">
										'.$jsonData["ClusterInef"].'%
									  </div>
								  </div>
								</div>
								</div>
								<button type="Apri" class="btn btn-success btn-block center-block" style="margin-bottom: 10px; width: 50% !important;" onclick="window.open(\'Robot.php?area=A'.$nArea."&cluster=".$jsonData["ClusterName"].'\', \'_self\');">Apri</button>
								<div class="form-group col-md-8">
                                        <label  class="sr-only"></label>
                                        <input class="form-control" id="sub'.$jsonData["ClusterName"].'" value="'.$val.'">
                                </div>
                                <button type="submit" class="btn btn-primary mb-1" onclick="submitClick(\''.$jsonData["ClusterName"].'\',\'A'.($nArea).'\');">Submit</button>
								<div class="footer">
											<div class="legend">
													<i class="fa fa-circle text-success"></i> Efficiency
													<i class="fa fa-circle text-danger"></i> Inefficiency
											</div>
												</div>
											</div>
										</div>
								</div>';

						if($val <= $jsonData["ClusterInef"]) {

							$HTMLred .= $clusterHTML;
						} else {

							$HTMLgreen .= $clusterHTML;
						}
					}
				}
			}

			$dbManager->closeConnection();
			echo $HTMLred.$HTMLgreen;
		}


		function robotsCount($nArea, $nCluster) {

			$json = file_get_contents('data/A' . ($nArea) . 'C' . ($nCluster) . '.json');
			$data = json_decode($json, true);
			$robotHTML = "";

			uasort($data["Robots"], function($a, $b) {
				return $a < $b;
			});

			foreach ($data["Robots"] as $key => $value) {
				
				$robotHTML .= '<div class="col-md-3" id='.$key.'>
								<div class="card">
								<div class="header">
								<h4 class="title">'.$key.'</h4>
								<h4 class="title">Inefficiency Rate: '.$value.'%</h4>
								</div>
								<div style="height: 0% !important; padding:10px;">
								<div style="width:100%;">
								  <div class="progress">
									  <div class="progress-bar progress-bar-success" role="progressbar" style="width:'.(100-$value).'%">
										'.(100-$value).'%
									  </div>
									  <div class="progress-bar progress-bar-danger" role="progressbar" style="width:'.$value.'%">
										'.$value.'%
									  </div>
								  </div>
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