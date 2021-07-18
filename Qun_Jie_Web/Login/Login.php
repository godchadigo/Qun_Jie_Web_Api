<!DOCTYPE html>
<html>
<head>
<script src="https://code.jquery.com/jquery-1.11.3.js"></script>
<script src="/js/Session.js"></script>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>登入</title>
<?php header("Access-Control-Allow-Headers: *");?>
</head>

<body>
　      使用者帳號: <input type="text" id = "username" name="Username" >
<br>
　      使用者密碼: <input type="text" id = "password" name="Password">
<br>
        <p id = "test" ></p>
　      
　      <button type="button" onclick="Login();">登入</button>
　      <button type="button" onclick="Test();">測試</button>
    
    <script type="text/javascript" >
        $(function (){

            $("#username").focusout(function (){
                if ( $("#username").val().length == 0 ){
                    $("#test").html("請輸入帳號");
                }
                
            });

            $("#password").focusout(function (){
                if ( $("#password").val().length == 0 ){
                    $("#test").html("請輸入密碼");
                }
                
            });

            
        });
            
        function Test(){
            
            var ss =  $.session.get('key');
            console.log(ss);
            
        }
        
        function Login() {
            
            data = {"Username" : $("#username").val() , "Password" : $("#password").val()};
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:3000/api/Login",
                data: JSON.stringify(data),
                dataType: "json",
                contentType: "application/json",
                success: function (result) {
                    console.log(result[0]['Result']);
                    $("#test").html(result[0]['Result']);
                    
                    if (result[0]['Result'] == "登入成功!"){
                        $.session.set('key', result[0]['Token'])
                        window.location.href = "/../Console/Management_List.php" 
                    }
                    
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