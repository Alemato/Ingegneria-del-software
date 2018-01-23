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
});