<?php

	class countFiles {	


		function areaFiles() {

			$dir = 'data/';
			$files = scandir($dir);
			$filesCount = 0;

			foreach ($files as $f => $value) {
				
				foreach ($files as $f2 => $value2) {

					if(strcmp($value2, ('A' . ($f+1) . 'C1.json')) == false) {

						$filesCount = $filesCount+1;
					}
				}
			}
			echo $filesCount;
		}


		function clusterFiles($nArea) {

			$dir = 'data/';
			$files = scandir($dir);
			$filesCount = 0;

			foreach ($files as $f => $value) {
				
				foreach ($files as $f2 => $value2) {

					if(strcmp($value2, ('A' . ($nArea) . 'C' . ($f+1) . '.json')) == false) {

						$filesCount = $filesCount+1;
					}
				}
			}
			echo $filesCount;
		}


		function robotsCount($nArea, $nCluster) {

			$json = file_get_contents('data/A' . ($nArea) . 'C' . ($nCluster) . '.json');
			$data = json_decode($json, true);
			$card = "";

			foreach ($data["Robot"] as $key) {
				
				$card .= '<div class="col-md-3"><div class="card"><div class="header">'.
					        	   '<h4 class="title">Robot '.$key["Name_Of_Robot"].'</h4>'.
					         	   '<p class="category">Info blu blu blu</p>'.
					         	   '<h4 class="title">Inefficiency Rate</h4>'.
					         	   '<p class="category">The Last Hour</p>'.
					      	  '</div>'.
					      	  '<div class="content">'.
					          	  '<div id="chartHours" class="ct-chart">'.
					             	   '<p class="category"></p>'.
					           	 '</div>'.
					          	  '<div class="footer">'.
					              	  '<div class="legend">'.
					             	       '<i class="fa fa-circle text-success"></i> Efficiency'.
					               	     '<i class="fa fa-circle text-danger"></i> Inefficiency'.
					              	  '</div>'.
					              	  '<hr>'.
					              	  '<div class="stats">'.
					              	      '<i class="fa fa-history"></i> Updated ___ minutes ago'.
					             	   '</div>'.
					            	'</div>'.
					        	'</div>'.
					    	'</div>'.
						'</div>';
			}

			echo $card;
		}
	}
?>