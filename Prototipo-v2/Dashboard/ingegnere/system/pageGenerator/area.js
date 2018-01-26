$(document).ready(function () {

    $.ajax({
        type: "POST",
        url: 'system/pageGenerator/countFilesSys.php',
        data: {
                "functionName": "area",
                "nArea": 0,
                "nCluster": 0
            },
        success: function(response) {

            $('#autoArea').append(response);
        }
    });

    setInterval(function(){
        location.reload();
    },60000);

    $("#search").click(function(){
        $("#A1").remove();
    });
});