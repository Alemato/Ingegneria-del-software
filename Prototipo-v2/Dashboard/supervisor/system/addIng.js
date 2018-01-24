$(document).ready(function () {

    var myLink = document.getElementById('salva');

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