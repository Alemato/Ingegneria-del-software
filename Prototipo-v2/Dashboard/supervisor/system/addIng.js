$(document).ready(function () {

    var myLink = document.getElementById('salva');

    myLink.onclick = function(){

        var elem = document.getElementById("stato"),
        selected = elem.options[elem.selectedIndex].value;

        $.ajax({
            type: "POST",
            url: 'system/system.php',
            data: {
                    "functionName": "addUser",
                    "name": document.getElementById("name").value,
                    "user": document.getElementById("user").value,
                    "password": document.getElementById("psw").value,
                    "type": selected
            },
            success: function(response) {

                alert(response);
                location.reload();
            }
        });
    }
});