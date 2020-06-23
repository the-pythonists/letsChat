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



 
    $(document).ready(function () {

        // ANIMATEDLY DISPLAY THE NOTIFICATION COUNTER.
        // $('#noti_Counter')
        //     .css({ opacity: 0 })
        //     .text('7')  // ADD DYNAMIC VALUE (YOU CAN EXTRACT DATA FROM DATABASE OR XML).
        //     .css({ top: '-10px' })
        //     .animate({ top: '-2px', opacity: 1 }, 500);

        // $('#noti_Button').click(function () {

        //     // TOGGLE (SHOW OR HIDE) NOTIFICATION WINDOW.
        //     $('#notifications').fadeToggle('fast', 'linear', function () {
        //         if ($('#notifications').is(':hidden')) {
        //             $('#noti_Button').css('background-color', '#2E467C');
        //         }
        //         // CHANGE BACKGROUND COLOR OF THE BUTTON.
        //         else $('#noti_Button').css('background-color', '#FFF');
        //     });

        //     $('#noti_Counter').fadeOut('slow');     // HIDE THE COUNTER.

        //     return false;
        // });

        // // HIDE NOTIFICATIONS WHEN CLICKED ANYWHERE ON THE PAGE.
        // $(document).click(function () {
        //     $('#notifications').hide();

        //     // CHECK IF NOTIFICATION COUNTER IS HIDDEN.
        //     if ($('#noti_Counter').is(':hidden')) {
        //         // CHANGE BACKGROUND COLOR OF THE BUTTON.
        //         $('#noti_Button').css('background-color', '#2E467C');
        //     }
        // });

        $('#notifications').click(function () {
            return false;       // DO NOTHING WHEN CONTAINER IS CLICKED.
        });
	});

//Validation for Post Image
$("#file1").on("change", function(e) {

	console.log(this.files[0].type);
	document.getElementById("SubmitPost").style.display="block";
  
	
  })
  


function emojiCreater(){
    $("#TextPost").emojioneArea({
            pickerPosition: "bottom",
            tonesStyle: "bullet",
            
    });
    
document.getElementById("SubmitPost").style.display="block";

  }
  
  // function likePost(data){
    
  //   Id = data
    
  //   $.ajax({
  //     method:'POST',
  //     url:'/postlike/',
  //     data:{
  //       postID : Id
  //     },
  //     success:function(e){
  //       likeCount = e['Result']
        
  //       document.getElementsByName(Id)[0].style.color=e['color'];
  //       document.getElementById(Id).innerHTML=likeCount+" Likes";
  //     },
  //     error:function(data){
  //       console.log('Failed');
  //     }
  //   })
  // }



//Automatically Check Like Request
// setInterval(function()
// {
// $.ajax({
//       method:'POST',
//       url:'/automaticallylike/',
      
//       success:function(e){
        
        
//         for(i=0;i<((e.like).length);i++){
          
//           document.getElementById(e.userData[i]).innerHTML=e.like[i]+" Likes";
//         }
//       },
//       error:function(data){
//         console.log('Failed');
//       }
//     });
// }, 5000); 


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



function emojiCreater(){
    $("#TextPost").emojioneArea({
            pickerPosition: "bottom",
            tonesStyle: "bullet",
            
    });
    
document.getElementById("SubmitPost").style.display="block";
Mode();

  }
  
  // function likePost(data){
    
  //   Id = data
    
  //   $.ajax({
  //     method:'POST',
  //     url:'/postlike/',
  //     data:{
  //       postID : Id
  //     },
  //     success:function(e){
  //       likeCount = e['Result']
        
  //       document.getElementsByName(Id)[0].style.color=e['color'];
  //       document.getElementById(Id).innerHTML=likeCount+" Likes";
  //     },
  //     error:function(data){
  //       console.log('Failed');
  //     }
  //   })
  // }



//Automatically Check Like Request
// setInterval(function()
// {
// $.ajax({
//       method:'POST',
//       url:'/automaticallylike/',
      
//       success:function(e){
        
        
//         for(i=0;i<((e.like).length);i++){
          
//           document.getElementById(e.userData[i]).innerHTML=e.like[i]+" Likes";
//         }
//       },
//       error:function(data){
//         console.log('Failed');
//       }
//     });
// }, 5000); 



//Set Image on input type =File
    $( "#FileInput" ).change(function() {
      $( "#Up" ).click();
    });


//
function searchPeople()
{ 
  document.getElementById("brandSection").style.display="none";
  document.getElementById("searchBoxSectionContainer").style.display="block";
}

function closeTopSearchBar()
{
  document.getElementById("brandSection").style.display="block";
  document.getElementById("searchBoxSectionContainer").style.display="none";
}



function nightMode(){
  //alert("Okkk");

    document.cookie = "Mode=darkMode";
    document.getElementById("body").style.background="grey";
    document.getElementById("header").style.background="black";
    document.getElementById("header").style.color="rgba(0, 150, 136, 1)";
    document.getElementById("header").style.boxShadow="0px 0px 23px 0px rgba(0, 150, 136, 1)";
    document.getElementById("leftFixDiv").style.background="black";

    document.getElementById("profilePicImage").style.border="2px solid rgba(0, 150, 136, 1)";
    document.getElementsByClassName("maquee_text")[0].style.color="rgba(0, 150, 136, 1)";

    var y = document.getElementsByClassName("icon");
    var z = document.getElementsByClassName("title");
    for (i = 0; i < y.length; i++) {
    y[i].style.color="rgba(0, 150, 136, 1)";
    
  }

  for (i = 0; i < z.length; i++) {
    z[i].style.color="rgba(0, 150, 136, 1)";
  }
    document.getElementById("profileInsideHR").style.background = "rgba(0, 150, 136, 1)";
    document.getElementById("accountRightSectionPlaceModel").style.background = "black";


 }  


function dayMode(){

    document.cookie = "Mode=dayMode";
    var element = document.body;
    element.classList.toggle("day-mode");
    document.getElementById("body").style.background="white";
    document.getElementById("header").style.background="#E9ECEF";
    document.getElementById("header").style.color="rgba(0, 150, 136, 1)";
    document.getElementById("header").style.boxShadow="0px 0px 23px 0px rgba(0,0,0,0.5)";
    document.getElementById("leftFixDiv").style.background="rgba(0, 150, 136, 0.6)";

    document.getElementById("profilePicImage").style.border="2px solid white";
    document.getElementsByClassName("maquee_text")[0].style.color="white";

    var y = document.getElementsByClassName("icon");
    var z = document.getElementsByClassName("title");
    for (i = 0; i < y.length; i++) {
    y[i].style.color="white";
    
  }

  for (i = 0; i < z.length; i++) {
    z[i].style.color="white";
  }
    document.getElementById("profileInsideHR").style.background="white";
   
     document.getElementById("body").style.backgroundImage="url(static/images/body-light.jpg)";
    document.getElementById("accountRightSectionPlaceModel").style.background = "white";
    /*document.getElementById("PostAlert").style.background="rgba(191, 191, 191, 0.5)";
    document.getElementById("PostAlert").style.color="black";
    document.getElementById("searchBtnId").style.background="white";
    document.getElementById("searchBtnId").style.border="1px solid white";
    var bt=document.getElementById("searchBtnSubmitId") 
    bt.style.background="white";
    bt.style.border="1px solid white";
    bt.style.color="black";
    */
 }

 function storySetPlace(v,v1,v2,v3,v4,v5)
 {
  alert(v);
  document.getElementById("storyTextContent").innerHTML=v;
  document.getElementById("storyTextContent").style.color=v4;
  document.getElementById("storyTextContent").style.fontFamily=v5;
  document.getElementById("storyVisiblePersonName").innerHTML=v1;
  document.getElementsByClassName("storyProfileSection")[0].src=v2;
  document.getElementById("VisibleStoryBodySection").style.backgroundImage="url("+v3+")";

 }

 //
 function storyTextSetPlace(color,textContent,size,family,name,pic)
 {
    alert(color);
    document.getElementById("VisibleStoryTextBodySection").style.backgroundColor = color;
    document.getElementById("textStoryTextContent").style.fontFamily=family;
    document.getElementById("textStoryTextContent").innerHTML=textContent;
    document.getElementById("textStoryTextContent").style.fontSize=size;
    document.getElementsByClassName("storyProfileSection")[1].src=pic;
    document.getElementById('textStoryVisiblePersonName').innerHTML=name;
 }

 //Post Result by Internet
 function liveSearchPostResult(result)
 {

  document.getElementById("searchPostResultModel").src="https://www.bing.com/search?q="+result;
  document.getElementById("PostResultSearchModel").innerHTML="Search : "+result;
 }

function storyTextSetPlaceManager(media,storydate,storyType,family,size,textContent,color,lenCaption,name,pic)
 {

    $("#storySlidesId").empty();
    console.log("media = "+media);
    console.log("storydate = "+storydate);
    console.log("storyType = "+storyType);
    console.log("family = "+family);
    console.log("size = "+size);
    console.log("textContent = "+textContent);
    console.log("color"+color);
    var storyTypeLocal = storyType.split("@");
    var familyLocal = family.split("@");
    var sizeLocal = size.split("@");
    var colorLocal = color.split("@");
    var mediaLocal = media.split("@");
    var lenCaptionLocal = lenCaption.split("@");

    var startLen = 0;
  for(var i=0 ; i< (storyTypeLocal.length)-1; i++) {
    console.log("startLen ",startLen);
    
    console.log(textContent.slice(startLen,lenCaptionLocal[i]));

    if(storyTypeLocal[i] == "image")
    {
      if(i==0){
        $("#storySlidesId").append('<div class="carousel-item active" ><div id="VisibleStoryBodySection"><img src="'+mediaLocal[i]+'" style="width:100%;height:70vh;" alt="..."><h5 id="storyTextContent" style="color:'+colorLocal[i]+';font-family:'+familyLocal[i]+';">'+textContent.slice(startLen,lenCaptionLocal[i])+'</h5></div></div>');
      }

      else{
      $("#storySlidesId").append('<div class="carousel-item" ><div id="VisibleStoryBodySection"><img src="'+mediaLocal[i]+'" style="width:100%;height:70vh;" alt="..."><h5 id="storyTextContent" style="color:'+colorLocal[i]+';font-family:'+familyLocal[i]+';">'+textContent.slice(startLen,parseInt(lenCaptionLocal[i])+startLen)+'</h5></div></div>');
      }
    }
    else{

      if(i==0){
        $("#storySlidesId").append('<div class="carousel-item active" ><div style="width:100%;height:70vh;padding:2%;background:'+colorLocal[i]+';" ><p style="font-family:'+familyLocal[i]+';font-size:'+sizeLocal[i]+';">'+textContent.slice(startLen,lenCaptionLocal[i])+'</p></div></div>');
      }

      else{
      $("#storySlidesId").append('<div class="carousel-item" ><div style="width:100%;height:70vh;padding:2%;background:'+colorLocal[i]+'; " ><p style="font-family:'+familyLocal[i]+';font-size:xx-large;">'+textContent.slice(startLen,parseInt(lenCaptionLocal[i])+startLen)+'</p></div></div>');
      }


    }

    startLen = startLen + parseInt(lenCaptionLocal[i]);


 }
  
  console.log("none Section Execute"+name);
  if(name==" Me")
  {
    console.log("none Section Execute");
    document.getElementById("StoryReplySectionPlaceId").style.display="none";
  }
  else
  {
    document.getElementById("StoryReplySectionPlaceId").style.display="block";
  }
    

    document.getElementsByClassName("storyProfileSection")[0].src=pic;
    document.getElementById('textStoryVisiblePersonName').innerHTML=name;
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

//Tag People Function1
var taggedWholeFriendList;
function tagPeopleFun1()
{
  
  document.getElementById("tagLoader").style.display="block";
  $.ajax({
      method:'POST',
      url:'/taggedSearchFriends/',
      
      success:function(e){
        taggedWholeFriendList = e;
        $('#tagPeoplenameArea').empty();
        console.log(e);
        document.getElementById("tagLoader").style.display="none";
        for(i=0;i<(e.name).length;i++)
        {
         $('#tagPeoplenameArea').append('<span id="'+e.userId[i]+'"  onclick="tagging(\''+e.userId[i]+'\')" ><label for="'+e.userId[i]+'"><span><img src="'+e.pic[i]+'" style="width:45px;height:45px;border-radius:50%;margin:8px;"></span>'+e.name[i]+'</label></span><br>');
        }

      },
      error:function(data){
        console.log('Failed');
      }
    })

}

function tagFriendPeopleTextBox()
{
  $('#tagPeoplenameArea').empty();
  var frnd = document.getElementById("tagFriendsTextBoxId").value;
   for(i=0;i<(taggedWholeFriendList.name).length;i++)
        {
          if(((taggedWholeFriendList.name[i].toUpperCase()).search(frnd.toUpperCase()))!=-1)
          {
            $('#tagPeoplenameArea').append('<span id="'+taggedWholeFriendList.userId[i]+'" onclick="tagging(\''+taggedWholeFriendList.userId[i]+'\')"><label for="'+taggedWholeFriendList.userId[i]+'"><span><img src="'+taggedWholeFriendList.pic[i]+'" style="width:45px;height:45px;border-radius:50%;margin:8px;"></span>'+taggedWholeFriendList.name[i]+'</label></span><br>');
          }
         
        }

}
var seperator="";

function tagging(val){
  console.log('here',val)
  if(seperator.search(val)<0)
  {
    seperator=seperator+","+val;
  $("#selectedPeople").append('<span class="badge badge-primary" id="Badge'+val+'">'+val+'<button type="button" class="close" aria-label="Dismiss"  ><span aria-hidden="true" onclick="closeBadge(\''+val+'\')">&times;</span></button></span>');
  }
}

function closeBadge(v)
{
  console.log("seperator = "+seperator);
  console.log(v);
  
  seperator=seperator.replace(v,"");
 
  document.getElementById("Badge"+v).remove();
}

function tagSave(){
  val = document.getElementById('selectedPeople')
  console.log(val)
}
