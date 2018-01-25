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

    var myLink = document.getElementById('elimina');

    myLink.onclick = function(){

        $.ajax({
            type: "POST",
            url: 'system/system.php',
            data: {
                    "functionName": "addUser",
                    "name": document.getElementById("name").value,
                    "user": document.getElementById("user").value,
                    "password": document.getElementById("psw").value
            },
            success: function(response) {

                alert(response);
                location.reload();
            }
        });
    }
});