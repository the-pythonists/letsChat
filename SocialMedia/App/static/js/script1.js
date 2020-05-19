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
  
  function closeLogOut() {
	document.getElementById("myOverlayLogOut").style.display = "none";
  }
  
  function nightMode(){
		var element = document.body;
		element.classList.toggle("dark-mode");
 }  

 
$(document).ready(function () {

// ANIMATEDLY DISPLAY THE NOTIFICATION COUNTER.
$('#noti_Counter')
	.css({ opacity: 0 })
	.text('7')  // ADD DYNAMIC VALUE (YOU CAN EXTRACT DATA FROM DATABASE OR XML).
	.css({ top: '-10px' })
	.animate({ top: '-2px', opacity: 1 }, 500);

$('#noti_Button').click(function () {

	// TOGGLE (SHOW OR HIDE) NOTIFICATION WINDOW.
	$('#notifications').fadeToggle('fast', 'linear', function () {
		if ($('#notifications').is(':hidden')) {
			$('#noti_Button').css('background-color', '#2E467C');
		}
		// CHANGE BACKGROUND COLOR OF THE BUTTON.
		else $('#noti_Button').css('background-color', '#FFF');
	});

	$('#noti_Counter').fadeOut('slow');     // HIDE THE COUNTER.

	return false;
});

// HIDE NOTIFICATIONS WHEN CLICKED ANYWHERE ON THE PAGE.
$(document).click(function () {
	$('#notifications').hide();

	// CHECK IF NOTIFICATION COUNTER IS HIDDEN.
	if ($('#noti_Counter').is(':hidden')) {
		// CHANGE BACKGROUND COLOR OF THE BUTTON.
		$('#noti_Button').css('background-color', '#2E467C');
	}
});

$('#notifications').click(function () {
	return false;       // DO NOTHING WHEN CONTAINER IS CLICKED.
});
});

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
  }, 500000); 