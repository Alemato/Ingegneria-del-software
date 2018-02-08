function emptyString() {

    var text = document.getElementById('searchTXT').value;
    if(text == "" || text == null) 
    location.reload();
}

$(document).ready(function () {

    $.ajax({
        type: "POST",
        url: 'system/pageGenerator/countFilesSys.php',
        data: {
                "functionName": "area",
                "nArea": 0,
                "nCluster": 0,
                "value": 0
            },
        success: function(response) {

            $('#autoArea').append(response);
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
            
            while ($("#A" + i).length != 0) {
                
                array[i-1] = ('A'+i);
                if(!(document.getElementById("searchTXT").value.toUpperCase() == ("A" + i))) {
                    
                    document.getElementById('A'+i).style.display = 'none';
                }
                i++;
            }
        } else {

            array.forEach(function(item, index){ 

                document.getElementById(item).style.display = 'block'; 
            });

            while ($("#A" + i).length != 0) {

                if(!(document.getElementById("searchTXT").value.toUpperCase() == ("A" + i))) {

                    document.getElementById('A'+i).style.display = 'none';
                }
                i++;
            }
        }
    });

    document.getElementById("searchTXT").addEventListener("input", emptyString);
});