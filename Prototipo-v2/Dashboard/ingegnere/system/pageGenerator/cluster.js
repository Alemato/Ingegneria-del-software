function getURLParameter(name) {
	return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(location.search) || [null, ''])[1].replace(/\+/g, '%20')) || null;
}

$(document).ready(function () {

    $.ajax({
        type: "POST",
        url: 'system/pageGenerator/countFilesSys.php',
        data: {
                "functionName": "cluster",
                "nArea": getURLParameter('area').replace('A', ''),
                "nCluster": 0
            },
        success: function(response) {

            $('#autoCluster').append(response);
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
            
            while ($("#C" + i).length != 0) {
                
                array[i-1] = ('C'+i);
                if(!(document.getElementById("searchTXT").value.toUpperCase() == ("C" + i))) {
                    
                    document.getElementById('C'+i).style.display = 'none';
                }
                i++;
            }
        } else {

            array.forEach(function(item, index){ 

                document.getElementById(item).style.display = 'block'; 
            });

            while ($("#C" + i).length != 0) {

                if(!(document.getElementById("searchTXT").value.toUpperCase() == ("C" + i))) {

                    document.getElementById('C'+i).style.display = 'none';
                }
                i++;
            }
        }
    });
});