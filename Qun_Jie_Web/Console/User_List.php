<!DOCTYPE html>
<html>
<head>
<script src="https://code.jquery.com/jquery-1.11.3.js"></script>
<script src="/js/Session.js"></script>

<link href="../css/Table.css" rel="stylesheet" type="text/css"/>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>後台</title>
</head>

<body>

<div id = "profile"></div>
<div id = "list"></div>

<button type="button" onclick="Test();">Token</button>

<script type="text/javascript" >
    var token = $.session.get('key');
    $(function (){
        GetProfile();
    });

    function Test(){
        var ss =  $.session.get('key');
        console.log(ss);
        
    }

    function Logout(){
        $.session.clear();
        //window.location.reload();
        window.location.href = "/../Login/Login.php" 
    }

    function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
    };

    function Show(result){
        var el = document.getElementById('list');
        
        $("#profile").html(`<h1>使用者名稱 : ${result['Username']}</h1>`+
                        `<p>電子信箱 : ${result["Email"]}</p>`+
                        `<p>唯一辨識碼 : ${result["Uuid"]}</p>`+
                        `<button type="button" onclick="Logout();">登出</button>`
                        );
        
    }

    function GetProfile(){
        
        if (token == null || token == "") {
            $("#list").html(`<h1>請先登入使用者帳號</h1>`);
            return
        }

        header = {Authorization : "Bearer " + token}
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:3000/api/GetProfile",
                headers: header,
                dataType: "json",
                contentType: "application/json",
                success: function (result) {
                    console.log(result);
                    //profile = result;
                    Show(result);
                    if (result['Permission'] == 1){
                        GetAllProfile(result['Token'])                        
                    }
                },
                error: function (err) {
                    console.log(err);
                    $("#list").html(`<h1>請先登入使用者帳號</h1>`);
                    alert("ERROR");
                }
            });

    }

    function GetAllProfile(token){
        console.log(token);
        if (token == null || token == "") {
            $("#list").html(`<h1>請先登入使用者帳號</h1>`);
            return
        }

        header = {Authorization : "Bearer " + token}
            $.ajax({
                type: "GET",
                url: "http://127.0.0.1:3000/api/GetAllProfile",
                headers: header,
                dataType: "json",
                contentType: "application/json",
                success: function (result) {
                    console.log(result);
                    //profile = result;
                    
                    $("#list").html("<table>");
                    $("#list").append("<thead><th>Uuid</th><th>Username</th><th>Password</th><th>Email</th><th>Createtime</th><th>操作</th></thead>");
                    $("#list").append("<tbody>");
                    result.forEach(function(user){

                        if(user['Token'] == token) return;

                        $("#list").append(`<tr>`+
                                          `<td> ${user['Uuid']} </td> `+
                                          `<td> ${user['Username']} </td> `+
                                          `<td> ${user['Password']} </td> `+
                                          `<td> ${user['Email']} </td> `+
                                          `<td> ${user['Createtime']} </td>`+
                                          `<td><button type="button" onclick="DeleteProfile('${token}','${user['Uuid']}');">刪除</button></td> `+
                                          `</tr>`);

                    });
                    $("#list").append("</tbody></table>");

                },
                error: function (err) {
                    console.log(err);
                    //$("#list").html(`<h1>請先登入使用者帳號</h1>`);
                    alert("ERROR");
                }
            });
            return null;
    }

    function DeleteProfile(token,uuid){
        if (token == null || token == "") {
            $("#list").html(`<h1>請先登入使用者帳號</h1>`);
            return
        }

        header = {Authorization : "Bearer " + token}
            $.ajax({
                type: "DELETE",
                url: "http://127.0.0.1:3000/api/DeleteProfile",
                headers: header,
                dataType: "json",
                data: JSON.stringify({"Uuid" : uuid}),
                contentType: "application/json",
                success: function (result) {
                    console.log(result);
                    GetProfile();
                },
                error: function (err) {
                    console.log(err);
                    $("#list").html(`<h1>請先登入使用者帳號</h1>`);
                    alert("ERROR");
                }
            });


    }


</script>

</body>
</html>