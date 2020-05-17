//All Deshboard Contents
//Post Alert Close

function PostAlertClose(){
  alert('Done');
 document.getElementById("PostAlert").style.display="none";
}


function visibleButton(){
	
	status=document.getElementById("TextPost").value;
	
	if(status!=""){
		document.getElementById("SubmitPost").style.display="block";
	}
	else{
		document.getElementById("SubmitPost").style.display="none";
	}

}


function openSearch() {
  document.getElementById("myOverlay").style.display = "block";
}

function closeSearch() {
  document.getElementById("myOverlay").style.display = "none";
}


//LogOut Section
function openLogOut() {
	document.getElementById("myOverlayLogOut").style.display = "block";
  }
  
  $(document).on('click', '.alink', function () {
    var url = $("#Url").attr("data-url");
});  

  function closeLogOut() {
	document.getElementById("myOverlayLogOut").style.display = "none";
  }
  
  function nightMode(){
	  alert("Night Mode Code to be Written.....");
	  
  }
  
  //Validation for Post Image
$(":file").on("change", function(e) {

	console.log(this.files[0].type);
	document.getElementById("SubmitPost").style.display="block";
  
  })
  
  
 
  setInterval(function()
  {
    console.log('Running');
  $.ajax({
    
        method:'POST',
        url:'/storydelete/',
        
        success:function(e){
          console.log('Deleted');
          }
        ,
        error:function(e){
          console.log('Failed');
        }
      });
  }, 5000); 
