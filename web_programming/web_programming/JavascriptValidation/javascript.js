function validateUpdate()
{
    if(document.getElementById("idPlayers").value == "")
    {
        document.myForm.idPlayers.focus();
        alert("Please enter an ID");
        return false;
    }
    
    if(document.myForm.FirstName.value == "" || !/^[A-Za-z]+$/.test(myForm.FirstName.value))
    {
        document.myForm.FirstName.focus();
        alert("Please provide your first name.\nIt needs to only contain letters.");
        return false;
    }
    
    if(document.myForm.LastName.value == "" || !/^[A-Za-z]+$/.test(myForm.LastName.value))
    {
        document.myForm.LastName.focus();
        alert("Please provide your last name.\nIt needs to only contain letters.");
        return false;
    }
    
    if(!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(myForm.Email.value))
    {
        document.myForm.Email.focus();
        alert("Please provide your email in the correct format: \nuser@example.com");
        return false;
    }
    
    if(document.getElementById("Birthdate").value == "")
    {
        document.myForm.Birthdate.focus();
        alert("Please provide your birthday.\nIt must be before 01/01/1900.");
        return false;
    }
    
    if(document.myForm.Password.value == "")
    {
        document.myForm.Password.focus();
        alert("Please provide a password.");
        return false;
    }
    
    return true;
}

function validateSearch()
{
    if(document.getElementById("idPlayers").value == "")
    {
        document.myForm.idPlayers.focus();
        alert("Please enter an ID");
        return false;
    }
    
    return true;
}

function validateAdd()
{
    
    if(document.myForm.FirstName.value == "" || !/^[A-Za-z]+$/.test(myForm.FirstName.value))
    {
        document.myForm.FirstName.focus();
        alert("Please provide your first name.\nIt needs to only contain letters.");
        return false;
    }
    
    if(document.myForm.LastName.value == "" || !/^[A-Za-z]+$/.test(myForm.LastName.value))
    {
        document.myForm.LastName.focus();
        alert("Please provide your last name.\nIt needs to only contain letters.");
        return false;
    }
    
    if(!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(myForm.Email.value))
    {
        document.myForm.Email.focus();
        alert("Please provide your email in the correct format:\nuser@example.com");
        return false;
    }
    
    if(document.getElementById("Birthdate").value == "")
    {
        document.myForm.Birthdate.focus();
        alert("Please provide your birthday.\nIt must be before 01/01/1900.");
        return false;
    }
    
    if(document.myForm.Password.value == "")
    {
        document.myForm.Password.focus();
        alert("Please provide a password.");
        return false;
    }
    
    return true;
}

