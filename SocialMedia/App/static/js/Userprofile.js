//Vertical Tab
function openAboutOpt(evt, cityName) {
  // Declare all variables
  var i, tabcontent, tablinks;

  // Get all elements with class="tabcontent" and hide them
  tabcontent = document.getElementsByClassName("tabcontent5");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Get all elements with class="tablinks" and remove the class "active"
  tablinks = document.getElementsByClassName("tablinks5");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  // Show the current tab, and add an "active" class to the link that opened the tab
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}












$(document).ready(function() {



$(".btn-pref .btn").click(function () {
    $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
    // $(".tab").addClass("active"); // instead of this do the below 
    $(this).removeClass("btn-default").addClass("btn-primary");   
});

val1=document.getElementById("profile").innerHTML;
val2=document.getElementById("profileUser").innerHTML;
if(val1==val2){
  document.getElementById("EditProfileButton").style.display="block";
}
else{
  document.getElementById("addbtn").style.display="block";
}

});

function openCity(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}



//Edit Button
function editOpen(evt, opt) {
  var i, tabcontent, tablinks;
  
  document.getElementById("myModalLabel").innerHTML=opt;
  document.getElementById("noneOpt").style.display="block";
  document.getElementById("noneOpt").dataset.target="#"+opt+"1";

  tabcontent = document.getElementsByClassName("tabcontent1");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks1");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(opt).style.display = "block";
  evt.currentTarget.className += " active";
}

// Get the modal



//Edit Profile Picture
function edit(){
  
	document.getElementById("myModalLabel").innerHTML;
  document.getElementById("introAlertMessage").style.display="none";
	
}


	v=document.getElementById("myModalLabel").innerHTML;
	if(v=="Modal title"){
		document.getElementById("noneOpt").style.display="none";
	}
	


function request(action,user1,user2){

  // user1 == myself // user2 = friend
      
      myself = user1;     // Not in use currentlly
      userProfile = user2;
      btnvalue = action;
      
        if(btnvalue === 'add'){
            $.ajax({
            method:'POST',
            url:'/addfriend/',
            data:{
                profileId:userProfile,
                action:'add' // 1 for adding
            },
            success:function(e){
                document.getElementById('addbtn').value="Cancel Request";
                document.getElementById('addbtn').style.background="grey";

            }
        })
        }
        else if(btnvalue === 'cancel'){
            $.ajax({
            method:'POST',
            url:'/addfriend/',
            data:{
                profileId:userProfile,
                action:'cancel' // 0 for cancelling
            },
            success:function(e){
                document.getElementById('addbtn').value="Add Friend";
            }
        })
        }
        else if(btnvalue === 'unfriend'){
          $.ajax({
          method:'POST',
          url:'/addfriend/',
          data:{
              profileId:userProfile,
              action:'unfriend' // 1 for adding
          },
          success:function(e){
              document.getElementById('addbtn').value="Add Friend";
          }
      })
      }
      else if(btnvalue === 'confirm'){
        console.log('in req');
      console.log(myself);
      console.log(userProfile);
        $.ajax({
        method:'POST',
        // yha pr issue hai ajax url p ni ja rha ye
        url:'/addfriend/',
        data:{
            profileId:userProfile,
            action:'confirm' // 1 for adding
        },
        success:function(e){
          // import notification;
          // notification.confirmNotification(sender,receiver,name,senderPic);

            document.getElementById('addbtn').value="Unfriend";
            document.getElementById('addbtn').style.background="red";
            document.getElementById('addbtn').style.border="2px solid red";
        }
    })
    }
      
        
        
    }




//
document.getElementById("introAlertMessage").style.display="none";
    function introSubmission(){
        
                document.getElementById("IntroButt").innerHTML="Loading..";
                document.getElementById('loader').style.display = 'block';
                //document.getElementById("introLoader").classList.add("classToBeAdded");
                //element.classList.add("spinner-border spinner-border-sm");
                
                quote = document.getElementById("quote").value;
                dOB = document.getElementById("dOB").value;
                gender = document.getElementById("gender").value;
                mobileNumber = document.getElementById("mobileNumber").value;
                countryName = document.getElementById("countryName").value;
                cityName = document.getElementById("cityName").value; 
                currentEducation = document.getElementById("currentEducation").value;
                educationStartYear = document.getElementById("educationStartYear").value;
                educationEndYear = document.getElementById("educationEndYear").value;
                companyName = document.getElementById("companyName").value;
                companyPosition = document.getElementById("companyPosition").value;
                companyCity = document.getElementById("companyCity").value;
                companyDescription = document.getElementById("companyDescription").value;

        
        $.ajax({
            method:'POST',
            url:"/userIntroInsert/",
            data:{
                
                "quote":quote,
                "dOB":dOB,
                "gender":gender,
                "mobileNumber":mobileNumber,
                "countryName":countryName,
                "cityName":cityName,
                "currentEducation":currentEducation,
                "educationStartYear":educationStartYear,
                "educationEndYear":educationEndYear,
                "companyName":companyName,
                "companyPosition":companyPosition,
                "companyCity":companyCity,
                "companyDescription":companyDescription,
                
            },
            success:function(e){
                //document.getElementById()
                document.getElementById('loader').style.display = 'none';
                console.log("Success");
                document.getElementById("Intro1").style.display='none';
            document.getElementById("introAlertMessage").style.display="block";
           document.getElementById("introAlertMessage").className="alert alert-success";
           document.getElementById("introAlertMessage").innerHTML="your data has successfully updated";
           document.getElementById("IntroButt").innerHTML="Save Changes";


           document.getElementById("headerQuote").innerHTML=quote;
           document.getElementById("tableMobile").textContent=mobileNumber;
           document.getElementById("tableGender").textContent=gender;
           document.getElementById("tableDOB").textContent=dOB;
           document.getElementById("tableQuote").textContent=quote;
           document.getElementById("tableCountryName").textContent=countryName;
           document.getElementById("tableCityName").textContent=cityName;
           document.getElementById("tablecurrentEducation").textContent=currentEducation;
           document.getElementById("tableEducationStartYear").textContent=educationStartYear;
           document.getElementById("tableEducationEndYear").textContent=educationEndYear;

           document.getElementById("tableCompanyName").textContent=companyName;
           document.getElementById("tableCompanyPosition").textContent=companyPosition;
           document.getElementById("tableCompanyCity").textContent=companyCity;
           document.getElementById("tableCompanyDescription").textContent=companyDescription;
           

           
            },
            error:function(e){
                console.log('Fail');
                document.getElementById("introAlertMessage").style.display="block";
                document.getElementById("introAlertMessage").className="alert alert-primary";
                document.getElementById("introAlertMessage").innerHTML="your data has not Updated";
           
            }

        })
    }
    document.getElementById('loader').style.display = 'none';
   

