//All Deshboard Contents
//Post Alert Close

function getCookie(){
  var nameEQ = "Mode" + "=";
      var ca = document.cookie.split(';');
      for(var i=0;i < ca.length;i++) {
          var c = ca[i];
          while (c.charAt(0)==' ') c = c.substring(1,c.length);
          if (c.indexOf(nameEQ) == 0) {
            return c.substring(nameEQ.length,c.length)
            
          }
      }
  
  }
  
  function autoMode(){
    v=getCookie();
     
      if(v=="darkMode"){
        document.getElementById("modeId").innerHTML="day Mode";
        nightMode(); 
      }
  
      else{
        document.getElementById("modeId").innerHTML="Night Mode";
        dayMode();
      }
  
  }
  
  autoMode();
  function PostAlertClose(){
    
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
    
  
    function Mode(){
  
        var v=document.getElementById("modeId").innerHTML;
        
        if(v=="Night Mode"){
          nightMode();
          document.getElementById("modeId").innerHTML="day Mode";
        }
  
        else{
          dayMode();
          document.getElementById("modeId").innerHTML="Night Mode";
        }
  
  
    }
  
    function nightMode(){
  
      document.cookie = "Mode=darkMode";
      var element = document.body;
  
      element.classList.toggle("dark-mode");
      document.getElementById("body").style.background="grey";
      
      document.getElementById("logOutDiv").style.background="black";
      document.getElementById("hamBurgerId").style.background="black";
      document.getElementById("top_navbarId").style.background="black";
      document.getElementById("slidebarId").style.background="black";
  
      document.getElementById("TextPost").style.background="black";
      document.getElementById("TextPost").style.color="white";
      document.getElementById("PostWrapper").style.background="black";
      document.getElementById("PostWrapper").style.color="white";
      document.getElementById("PostOpt").style.background="black";
      document.getElementById("PostOpt").style.color="white";
      document.getElementById("wrapperstorySectionId").style.background="black";
      document.getElementById("wrapperstorySectionId").style.color="white";
      document.getElementById("postAllSectionId").style.background="black";
      document.getElementById("postAllSectionId").style.color="white";
      document.getElementById("PostAlert").style.background="black";
      document.getElementById("PostAlert").style.color="white";
      document.getElementById("searchBtnId").style.background="black";
      document.getElementById("searchBtnId").style.border="1px solid white";
      var bt=document.getElementById("searchBtnSubmitId") 
      bt.style.background="black";
      bt.style.border="1px solid white";
      bt.style.color="white";
  
   }  
  
  
  function dayMode(){
  
      document.cookie = "Mode=dayMode";
      var element = document.body;
      element.classList.toggle("day-mode");
      document.getElementById("body").style.backgroundImage="url(static/images/body-light.jpg)";
      document.getElementById("logOutDiv").style.background="white";
      document.getElementById("hamBurgerId").style.background="white";
      document.getElementById("top_navbarId").style.background="white";
      document.getElementById("slidebarId").style.background="rgba(0, 150, 136, 0.8)";
  
      document.getElementById("TextPost").style.background="white";
      document.getElementById("TextPost").style.color="black";
      document.getElementById("PostWrapper").style.background="rgba(191, 191, 191, 0.5)";
      document.getElementById("PostWrapper").style.color="black";
      document.getElementById("PostOpt").style.background="rgba(191, 191, 191, 0.5)";
      document.getElementById("PostOpt").style.color="black";
      document.getElementById("wrapperstorySectionId").style.background="rgba(191, 191, 191, 0.5)";
      document.getElementById("wrapperstorySectionId").style.color="black";
      document.getElementById("postAllSectionId").style.background="rgba(191, 191, 191, 0.5)";
      document.getElementById("postAllSectionId").style.color="black";
      document.getElementById("PostAlert").style.background="rgba(191, 191, 191, 0.5)";
      document.getElementById("PostAlert").style.color="black";
      document.getElementById("searchBtnId").style.background="white";
      document.getElementById("searchBtnId").style.border="1px solid white";
      var bt=document.getElementById("searchBtnSubmitId") 
      bt.style.background="white";
      bt.style.border="1px solid white";
      bt.style.color="black";
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
  $("#file1").on("change", function(e) {
  
    console.log(this.files[0].type);
    document.getElementById("SubmitPost").style.display="block";
    
    
    })
    
    
  
  //Story Slider
  $(document).ready(function() {
      $('#autoWidth').lightSlider({
          autoWidth:true,
          loop:false,
          controls:true,
          onSliderLoad: function() {
              $('#autoWidth').removeClass('cS-hidden');
  
          } 
      });  
  
    });
  
  
  
  
  var trigger = document.querySelector(".trigger");
  var closeButton = document.querySelector(".close-button");
  
  function toggleModal() {
      modal.classList.toggle("show-modal");
  }
  
  function windowOnClick(event) {
      if (event.target === modal) {
          toggleModal();
      }
  }
  
  trigger.addEventListener("click", toggleModal);
  closeButton.addEventListener("click", toggleModal);
  window.addEventListener("click", windowOnClick);
  