function getURLParameter(name) {
	return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search) || [null, ''])[1].replace(/\+/g, '%20')) || null;
}

$(document).ready(function () {

    $.ajax({
        type: "POST",
        url: 'system/pageGenerator/countFilesSys.php',
        data: {
                "functionName": "robot",
                "nArea": getURLParameter("area").replace('A', ''),
                "nCluster": getURLParameter("cluster").replace('C', '')
            },
        success: function(response) {

            $('#autoRobot').append(response);
        }
    });

    setInterval(function(){
        location.reload();
    },60000);

    var click = 0
    var array = [];
    $("#search").click(function(){

        click++;
        var i = 1;
        if(!(click >= 2)) {
            
            while ($("#R" + i).length != 0) {
                
                array[i-1] = ('R'+i);
                if(!(document.getElementById("searchTXT").value.toUpperCase() == ("R" + i))) {
                    
                    document.getElementById('R'+i).style.display = 'none';
                }
                i++;
            }
        } else {

            array.forEach(function(item, index){ 

                document.getElementById(item).style.display = 'block'; 
            });

            while ($("#R" + i).length != 0) {

                if(!(document.getElementById("searchTXT").value.toUpperCase() == ("R" + i))) {

                    document.getElementById('R'+i).style.display = 'none';
                }
                i++;
            }
        }
    });
});