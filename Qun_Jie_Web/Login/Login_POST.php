<?php

     api1();

     function api1() { 
        $Username = $_POST['Username'];
        $Password = $_POST['Password'];
        $url = "http://127.0.0.1:3000/api/Login";    
        $data = json_encode(["Username" => $Username , "Password" => $Password]);
        $curl = curl_init($url);
        curl_setopt($curl, CURLOPT_HEADER, false);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_HTTPHEADER, array("Content-type: application/json"));
        curl_setopt($curl, CURLOPT_POST, true);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
        $result =  curl_exec($curl);

        $ib = json_decode($result);

        echo $ib[0]->Result;

        //echo ($result[0]["Result"]);
        curl_close($curl);
        
        } 
        header("Refresh:2; url:http://127.0.0.1/Login/Login.php"); 
?>