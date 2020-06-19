
function otpGeneration(){

	var username=document.getElementById("userName").value;
	alert(username);
	document.getElementById("otpTigger").style.display="none";
	document.getElementById("loading").style.display="block";
	
	$.ajax({
      type: "POST",
      url:'/forgetPasswordOTP/',
      data:{
      	Email:username,
      },
     
      success:function(e){
      	if (e.Result=="Successfully"){
	      	document.getElementById("otpMessage").style.display="block";
	      	document.getElementById("otp").style.display="block";
	      	document.getElementById("loading").style.display="none";
	      	document.getElementById("otpSubmissionTigger").style.display="block";
	      	document.getElementById("otpSubmissionTigger").type="submit";

	      	console.log(e);
	      }	

      	else if(e.Result=="UnSuccessfully"){
      		document.getElementById("loading").style.display="none";
      		$('.alert-dismissible').show();
      	}
	    
      },
      error:function(data){
      	document.getElementById("loading").style.display="none";
      	$('.alert-dismissible').show();
        console.log('Failed');
      }
    })
}


//Close Alert when we Cut Alert
function closeAlert() {
  // do something...
  $('.alert-dismissible').hide();
}


$('.alert-dismissible').hide();

