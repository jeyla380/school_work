/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

function hobbies(data)
{
    //console.log(data);
    var file = "HobbiesInfo.json";
    var http_request = new XMLHttpRequest();
    
    try 
    {
        http_request = new XMLHttpRequest();
    }
    catch (e)
    {
        try
        {
            http_request = new ActiveXObject("Msxm12.XMLHTTP");
        }
        catch (e)
        {
            try
            {
                http_request = new ActiveXObject("Microsoft.XMLHTTP");
            }
            catch (e)
            {
                alert("Your browser broke! Something went wrong!");
                return false;
            }
        }
    }
    
    http_request.onreadystatechange = function()
    {
        if(http_request.readyState == 4)
        {
            var jsonFile = JSON.parse(http_request.responseText);
            var info = "";
            for (var i = 0; i < jsonFile.hobbies.length; i++)
            {
                if(jsonFile.hobbies[i].id == data)
                {
                    info = info + "<br>" + jsonFile.hobbies[i].Information;
                    var select = i;
                }
            }
            document.getElementById("info").innerHTML = info;
        }
    }
    
    http_request.open("GET", file, true);
    http_request.send();
}
