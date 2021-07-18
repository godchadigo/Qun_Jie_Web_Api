<!DOCTYPE html>
<html>
<head>
<script src="https://code.jquery.com/jquery-1.11.3.js"></script>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>註冊</title>
<?php header("Access-Control-Allow-Headers: *");?>
</head>

<body>


　      使用者帳號: <input type="text" id = "username" name="Username" >
<br>
　      使用者密碼: <input type="text" id = "password" name="Password">
<br>
　      Email: <input type="text" id = "email" name="Email">
<br>
        <p id = "test" ></p>
　      <button type="button" onclick="Login();">註冊</button>


    
    <script type="text/javascript" >
        $(function (){
        });

        function Login() {
            data = {"Username" : $("#username").val() , "Password" : $("#password").val() , "Email" : $("#email").val() };
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:3000/api/Register",
                data: JSON.stringify(data),
                dataType: "json",
                contentType: "application/json",
                success: function (result) {
                    $("#test").html(result[0]['Result']);
                },
                error: function (err) {
                    console.log(err);
                    alert("ERROR");
                }
            });
        }

    </script>
</body>
</html>