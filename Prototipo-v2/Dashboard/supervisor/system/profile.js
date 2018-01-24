$(document).ready(function () {

    $.ajax({
        type: "POST",
        url: 'system/system.php',
        data: {
                "functionName": "lsSupervisor",
                "name": 0,
                "user": 0,
                "password": 0
        },
        success: function(response) {

            $('#auto').append(response);
        }
    });
});