
function validate() {  
	var result = "";	
	result += validateName(); 	
	result += validateEmail();
	result += validatePassword();
	result += validateTerms();
	
	if (result == "") return true;
	
	alert("Validation Result:\n\n" + result);
	return false;	
}
function validateName() {
	var name = document.getElementsByName("uname")[0].value;
	if (name.length <= 3)
		return "Name should be at least three characters.\n";	
	return "";
}

function validatePassword() {
	var password = valueOf("pass");
	var retype = valueOf("confirmpass");
	
	if (password.length <= 6) 
		return "Password should be at least 6 characters.\n";
	
	if (password != retype) 
		return "Passwords do not match.\n";	
	return "";
}

function validateEmail() {
	var email = valueOf("email");
    if(email == "")
        return "Please fill the email idx` field";
    if(email.indexOf('@') <= 0 )
        return " Email @ Invalid ";
        
    if((email.charAt(email.length-4)!='.') && (email.charAt(email.length-3)!='.'))
        return " Please Ennter valid email";
    
    return "";
}

function validateTerms() {
	var terms = document.getElementsByName("registering")[0];
	if (!terms.checked)
		return "Please accept the Terms of Service and Privacy Policy";	
	return "";
}

function valueOf(name) {
	return document.getElementsByName(name)[0].value;
}
function validation(){

    var uname = document.getElementById('uname').value;
    var pass = document.getElementById('pass').value;
    var confirmpass = document.getElementById('conpass').value;
    var mobileNumber = document.getElementById('mobileNumber').value;
    var emails = document.getElementById('emails').value;
    var genderM = document.getElementById('genderM').value;
    var genderF = document.getElementById('genderF').value;

     
    if(genderM == "" || genderF == ""){
        document.getElementById('gender').innerHTML =" ** Please Select gender";
        return false;
    }

    if(uname == ""){
        document.getElementById('uname').innerHTML =" ** Please fill the username field";
        return false;
    }
    if((uname.length <= 3) || (uname.length > 10)) {
        document.getElementById('uname').innerHTML =" ** Username lenght must be between 3 and 10";
        return false;	
    }
    if(!isNaN(uname)){
        document.getElementById('uname').innerHTML =" ** only characters are allowed";
        return false;
    }

    if(pass == ""){
        document.getElementById('pass').innerHTML =" ** Please fill the password field";
        return false;
    }
    if((pass.length <= 6) || (pass.length > 20)) {
        document.getElementById('passwords').innerHTML =" ** Passwords lenght must be between  6 and 20";
        return false;	
    }

    if(pass!=confirmpass){
        document.getElementById('confrmpass').innerHTML =" ** Password does not match the confirm password";
        return false;
    }

    if(confirmpass == ""){
        document.getElementById('confrmpass').innerHTML =" ** Please fill the confirmpassword field";
        return false;
    }
    
    if(contact == ""){
        document.getElementById('contact').innerHTML =" ** Please fill the mobile NUmber field";
        return false;
    }
    if(isNaN(contact)){
        document.getElementById('contact').innerHTML =" ** user must write digits only not characters";
        return false;
    }
    if(contact.length!=10){
        document.getElementById('contact').innerHTML =" ** Mobile Number must be 10 digits only";
        return false;
    }

    if(email == ""){
        document.getElementById('emailids').innerHTML =" ** Please fill the email idx` field";
        return false;
    }
    if(email.indexOf('@') <= 0 ){
        document.getElementById('email').innerHTML =" ** @ Invalid Position";
        return false;
    }

    if((email.charAt(email.length-4)!='.') && (email.charAt(email.length-3)!='.')){
        document.getElementById('email').innerHTML =" ** '.' Invalid Position";
        return false;
    }
}


