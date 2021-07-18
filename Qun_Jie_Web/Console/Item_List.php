<!DOCTYPE html>
<html>
<head>
<script src="https://code.jquery.com/jquery-1.11.3.js"></script>
<script src="/js/Session.js"></script>

<link href="../css/Table.css" rel="stylesheet" type="text/css"/>

<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>管理頁面</title>
</head>

<body>

<div id = "profile"></div>
<div id = "list"></div>



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

    function Show(result = ""){
        var el = document.getElementById('list');
        
        $("#profile").html(`<button type="button" onclick="User_List();">User List</button>`);
        $("#profile").append(`<button type="button" onclick="Item_List();">Item List</button>`);
        $("#profile").append(`<button type="button" onclick="Logout();">Logout</button>`);
        
    }

    function User_List(){
        window.location.href = "/../Console/User_List.php" 
    }

    function Item_List(){
        window.location.href = "/../Console/Item_List.php" 
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
                    Show();
              
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