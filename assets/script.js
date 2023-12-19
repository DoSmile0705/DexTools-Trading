$fleg = true

// $(document).ready(function () {
//     var token = localStorage.getItem('jwtToken'); // Retrieve the jwtToken from local storage

//     if (!token) {
//         var i = 0;
//         do {
//             i++;
//             window.location.replace("index.html");
//         } while (i < 1);
//     }
// });


$(function () {
    $(document).ready(function () {
        $('#login').click(function () {
            var initEmail = "whaleundercover@gmail.com"
            var initPass = "DexTools0705!"
            var newEmail = $('#email').val();
            var newPass = $('#password').val();
            if (newEmail === initEmail && newPass === initPass) {
                $.ajax({
                    type: 'POST',
                    url: 'server/login',
                    data: {
                        email: newEmail,
                        password: newPass,
                    },
                    success: function (response) {
                        if (response) {
                            var jwtToken = response.token;
                            localStorage.setItem('jwtToken', jwtToken);
                            window.location.replace("admin.html");
                        }
                        else {
                            window.location.replace("index.html");
                        }
                    },
                    error: function (xhr, status, error) {
                        console.log(error);
                    }
                });
            }
            if (newEmail === "") {
                $('#errorEmail2').css("display", "block");
                $('#errorEmail1').css("display", "none");
            }
            if (newEmail != initEmail && newEmail != "") {
                $('#errorEmail1').css("display", "block");
                $('#errorEmail2').css("display", "none");
            }
            if (newEmail === initEmail) {
                $('#errorEmail1').css("display", "none");
                $('#errorEmail2').css("display", "none");
            }
            if (newPass === "") {
                $('#errorPass1').css("display", "none");
                $('#errorPass2').css("display", "block");
            }
            if (newPass != initEmail && newPass != "") {
                $('#errorPass1').css("display", "block");
                $('#errorPass2').css("display", "none");
            }
            if (newPass === initPass) {
                $('#errorPass1').css("display", "none");
                $('#errorPass2').css("display", "none");
            }
        })

    });
});


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
                // success: function (response) {
                //     console.log(response)
                // }
            })
        }
        else {
            $("#loading-gif").css("display", "none");
            $("#startBtn").html("Start Server!");
            $("#serverStatus").html('Server Stopped Now!');
            $fleg = true;
            $.ajax({
                type: 'POST',
                url: 'server/stop',
                // success: function (response) {
                //     console.log(response)
                // }
            })
        }
    })
});