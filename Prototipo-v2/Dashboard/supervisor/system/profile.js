$(document).ready(function () {

    $.ajax({
        type: "POST",
        url: 'system/system.php',
        data: {
                "functionName": "lsUsers",
                "name": 0,
                "user": 0,
                "password": 0,
                "type": 0
        },
        success: function(response) {

            $('#auto').append(response);
        }
    });
});

function del_click(value, type) {      

    $.ajax({
        type: "POST",
        url: 'system/system.php',
        data: {
                "functionName": "removeUser",
                "name": 0,
                "user": value,
                "password": 0,
                "type": type
        },
        success: function(response) {

            location.reload();
        }
    });
}