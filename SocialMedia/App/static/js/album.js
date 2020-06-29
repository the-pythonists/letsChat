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

$('.alert').hide();
function createAlbum()
{
  //alert("createAlbum");
	nameAlbum = document.getElementById("createAlbumName").value;
	descriptionAlbum = document.getElementById("createAlbumDescriprion").value;
	accessibilityAlbum = document.getElementById("crreatAlbumAccessibility").value;
  
	$.ajax({
       type:'POST',
      url:'/createAlbumDetails/',
      
      data:{
        name:nameAlbum,
        description:descriptionAlbum,
        accessibility:accessibilityAlbum,
      },
      success:function(e){

        console.log(e.status);
        if(e.status == "allready")
        {

          $('#myImageId').empty()
          for(i=0;i<(e.media).length;i++)
          { 
            $('#myImageId').append('<img src="'+e.media[i]+'" style="width:300px;height:200px;">');
          }
          $('.alert').show();
          $('#exampleModal').modal('hide'); 
          $('#exampleModalLong').modal('show'); 
          document.getElementById("exampleModalLongTitle").innerHTML = nameAlbum;
          document.getElementById("hiddenUploadTextBox").value = nameAlbum;
          document.getElementById("updateDivTextId").value=nameAlbum;
        }

        else
        {
          //$('#myGallerySelectId').append('<option>"'+nameAlbum+'"</option>');
          $('.alert').alert('close');
        }
      },
      error:function(data){
        console.log('Failed');
      }
    })

}


function readURL(input) {
  //document.getElementById("shareSubmitButton").type="submit";
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#imagePlacedID').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#albumSelectFileId").change(function() {
  readURL(this);
});

function functionality(v)
{
  //alert("functionality");
  if(v=="MyImage")
  {
    document.getElementById("myImageId").style.display="block";
    document.getElementById("imageUploadId").style.display="none";
    document.getElementById("settingId").style.display="none";
  }
  else if(v=="Upload")
  {
    document.getElementById("imageUploadId").style.display="block";
    document.getElementById("settingId").style.display="none";
    document.getElementById("myImageId").style.display="none";
  }
  else if(v=="Setting")
  {
    document.getElementById("settingId").style.display="block";
    document.getElementById("myImageId").style.display="none";
    document.getElementById("imageUploadId").style.display="none";
  }
}

function Send()
{
  //alert("Send");
  v = document.getElementById("albumSelectFileId").value;

  if(v.length>0)
  { //alert("Submission");
    $('#uploadFormDivId').submit();
  }

}

function selectContent()
{


  v=document.getElementById("myGallerySelectId").value;
  //alert(v);
  document.getElementById("othersTitleHeading").textContent=v;
  $.ajax({
       type:'POST',
       url:'/createAlbumDetails/',
      
      data:{
       name:v,
      },
      success:function(e){
        
        
        console.log(e);

        if(e.status == "allready")
        {

           $('#otherContentDivId').empty()
          for(i=0;i<(e.media).length;i++)
          { 
            $('#otherContentDivId').append('<div class="col-lg-3 col-md-4 col-sm-6 col-12 "style="border:5px solid #F5F5F5;" ><i class="fas fa-trash-alt" style="red" onclick="deletePicture(\''+e.picId[i]+'\')"></i><a href="'+e.media[i]+'" target="_blank"><img src="'+e.media[i]+'" class="img-fluid col-centered"></a></div>');
            
          }
          
        }

        
      },
      error:function(data){
        console.log('Failed');
      }
    })

}

function Edit()
{
  nameAlbum = document.getElementById("othersTitleHeading").textContent;
  

  //

    $.ajax({
       type:'POST',
      url:'/createAlbumDetails/',
      
      data:{
        name:nameAlbum,
        
      },
      success:function(e){

        console.log(e.status);
        if(e.status == "allready")
        {

          $('#myImageId').empty()
          for(i=0;i<(e.media).length;i++)
          { 
            $('#myImageId').append('<img src="'+e.media[i]+'" style="width:300px;height:200px;">');
          }
          
          $('#exampleModalLong').modal('show'); 
          document.getElementById("exampleModalLongTitle").innerHTML = nameAlbum;
          document.getElementById("hiddenUploadTextBox").value = nameAlbum;
          document.getElementById("updateDivTextId").value=nameAlbum;
        }

        
      },
      error:function(data){
        console.log('Failed');
      }
    })


  //
}


//Initial Tab Look
document.getElementById("deleteRepo").style.display="none";
    document.getElementById("SettingEdit").style.display="block";
function openSettingTab(v)
{
  if(v=="SettingEdit")
  {
    document.getElementById("deleteRepo").style.display="none";
    document.getElementById(v).style.display="block";
    //document.getElementById("updateDivTextId").value=document.getElementById("exampleModalLongTitle").innerHTML;
  }
  else if(v=="deleteRepo")
  {
    document.getElementById("SettingEdit").style.display="none";
    document.getElementById(v).style.display="block";
  }
}

function deleteRepo()
{
  title=document.getElementById("exampleModalLongTitle").innerHTML;
  
  $.ajax({
       type:'POST',
       url:'/deleteAlbumRepo/',
      
      data:{
       title:title,
      },
      success:function(e){
        console.log(e);
      },
      error:function(data){
        console.log('Failed');
      }
    })



}


function updateRepo()
{

  name=document.getElementById("updateDivTextId").value;
  description=document.getElementById("updateTextAreaId").value;
  access=document.getElementById("updateSelectId").value;

    $.ajax({
       type:'POST',
       url:'/UpdateAlbumRepo/',
      
      data:{
       name:name,
       description:description,
       accessibility:access,
      },
      success:function(e){
        console.log(e);
        document.getElementById("updateDivAlertHeding").innerHTML=e.Status;

      },
      error:function(data){
        console.log('Failed');
        document.getElementById("updateDivAlertHeding").innerHTML=e.Status;
      }
    })

}


//Delete Picture
function deletePicture(v)
{
  title=document.getElementById("myGallerySelectId").value;
  alert(v);
  $.ajax({
       type:'POST',
       url:'/deleteAlbumPicture/',
      
      data:{
       pic:v,
       title:title,
      },
      success:function(e){
        console.log(e);
        alert("your picture has deleted");
        selectContent();
      },
      error:function(data){
        console.log('Failed');
        
      }
    })
}