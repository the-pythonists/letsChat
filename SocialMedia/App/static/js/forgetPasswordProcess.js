//Close Alert when we Cut Alert
function closeAlert() {
    // do something...
    $('.alert-dismissible').hide();
  }
  
  
  $('.alert-dismissible').hide();
  
  
  function finalSubmission(){
      var p1=document.getElementById("fPassword").value
      var p2=document.getElementById("sPassword").value
      var Email=document.getElementById("finalEmail").value
  
      
      if(p1!=p2){
          $('.alert-dismissible').show();		
      }
      else{
          $('.alert-dismissible').hide();		
          
      
      $.ajax({
        type: "POST",
        url:'/changeForgetPasword/',
        data:{
            Email:Email,
            fPassword:p1,
            sPassword:p2,
        },
       
        success:function(e){
            console.log(e);
            if(e.Status=="Successfully"){
                myFunction();
            }
            else{
                $('.alert-dismissible').show();			
            }
          
        },
        error:function(data){
            
            $('.alert-dismissible').show();
          console.log('Failed');
        }
      })
  
      }
  }
  
  
  function myFunction() {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar");
  
    // Add the "show" class to DIV
    x.className = "show";
  
    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
  }