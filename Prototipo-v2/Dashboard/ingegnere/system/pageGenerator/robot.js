$.ajax({
    type: "POST",
    url: 'system/pageGenerator/countFilesSys.php',
    data: {
    		"functionName": "robot",
    		"nArea":1,
    		"nCluster":1
    	  },
    success: function(response) {

        $(document).ready(function () {

			$('#autoRobot').append(response);
		});
    }
});