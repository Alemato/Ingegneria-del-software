var number;

$.ajax({
    type: "POST",
    url: 'system/pageGenerator/countFilesSys.php',
    data: {
    		"functionName": "area",
    		"nArea":0,
    		"nCluster":0
    	  },
    success: function(response) {
        number = response;
    }
});


$(document).ready(function () {

	var card = "";
	for (var i = 0; i < number; i++) {
		
		card += '<div class="col-md-3"><div class="card"><div class="header">' +
						        	   '<h4 class="title">Area ' + (i+1) + '</h4>' +
						         	   '<p class="category">Info blu blu blu</p>' +
						         	   '<h4 class="title">Inefficiency Rate</h4>' +
						         	   '<p class="category">The Last Hour</p>' +
						      	  '</div>' +
						      	  '<div class="content">' +
						          	  '<div id="chartHours" class="ct-chart">' +
						             	   '<p class="category"></p>' +
						           	 '</div>' +
						          	  '<div class="footer">' +
						              	  '<div class="legend">' +
						             	       '<i class="fa fa-circle text-success"></i> Efficiency' +
						               	     '<i class="fa fa-circle text-danger"></i> Inefficiency' +
						              	  '</div>' +
						              	  '<hr>' +
						              	  '<div class="stats">' +
						              	      '<i class="fa fa-history"></i> Updated ___ minutes ago' +
						             	   '</div>' +
						            	'</div>' +
						        	'</div>' +
						    	'</div>' +
							'</div>';
		
	}
	$('#autoArea').append(card);
});