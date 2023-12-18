$fleg = true

document.getElementById("startBtn").innerHTML = "Start Server!";
document.getElementById("serverStatus").innerHTML = 'Server Stopped, Please Click "Start Server" Button!';

// document.getElementById('startBtn').onclick = function () {
// }

$(document).ready(function () {
    $('#startBtn').click(function () {
        if ($fleg === true) {
            $("#loading-gif").css("display", "block");
            $("#startBtn").html("Stop Server!");
            $("#serverStatus").html("Server is Running Now!");
            $fleg = false;
            $.ajax({
                type: 'POST',
                url: 'server/start',
                success: function (response) {
                    alert(response, "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                }
            })
        }
        else {
            $("#loading-gif").css("display", "none");
            $("#startBtn").html("Start Server!");
            $("#serverStatus").html('Server Stopped, Please Click "Start Server" Button!');
            $fleg = true;
            $.ajax({
                type: 'POST',
                url: 'server/stop',
                success: function (response) {
                    alert(response, "werfewaffewafawf")
                }
            })
        }
    })
});