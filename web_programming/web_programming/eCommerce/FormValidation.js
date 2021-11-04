//COMPLETE
function validateSubmit()
{
    if(document.UserForm.Username.value == "" || !/^[a-zA-Z0-9]+$/.test(document.UserForm.Username.value))
    {
        document.UserForm.Username.focus();
        alert("Please provide a username.\nIt can only contain numbers and letters and has to be less than 15 characters.");
        return false;
    }
    
    if(!/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(document.UserForm.Email.value))
    {
        document.UserForm.Email.focus();
        alert("Please provide your email in the correct format:\nuser@example.com");
        return false;
    }
    
    if(document.getElementById("Birthday").value == "")
    {
        document.UserForm.Birthday.focus();
        alert("Please provide your birthday.\nIt must be after 01/01/1900.");
        return false;
    }
    
    if(document.UserForm.Password.value == "")
    {
        document.UserForm.Password.focus();
        alert("Please provide a password.");
        return false;
    }
    
    return true;
}



