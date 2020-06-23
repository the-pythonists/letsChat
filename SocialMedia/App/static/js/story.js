//Global Values
var txt=false,colorValue="grey",fS="none",fF="none";

//Change story text Background
function colorPickerValue(v)
{ 
  document.getElementById("storySectionArea").style.background=v;
  colorValue=v;
}

function storyTextFieldArea()
{
 var v=document.getElementById("storyTextFieldArea").value;
 console.log(v);
 document.getElementById("storyPrintSectionArea").innerHTML=v;
 txt=v;
}

//For Mobile Screen TextArea
function storyTextFieldArea2()
{
 var v=document.getElementById("mobileScreenTextArea").value;
 console.log(v);
 document.getElementById("storyPrintSectionArea").innerHTML=v;
 txt=v;
}

function fontSizeValue()
{
  v=document.getElementById("fontSizeValueDiv").value;
  document.getElementById("storyPrintSectionArea").style.fontSize=v;
  fS = v;
}

//For Mobile Screen
function fontSizeValue1(v)
{
	document.getElementById("storyPrintSectionArea").style.fontSize=v;
	fS = v;
}

function fontFamilyValue()
{
 v=document.getElementById("fontFamilyValueSelect").value;
 document.getElementById("storyPrintSectionArea").style.fontFamily=v; 
 fF=v;
}

//For Mobile Screen
function fontFamilyValue1(v)
{
 document.getElementById("storyPrintSectionArea").style.fontFamily=v; 
 fF = v;
}

function colorPickerValue1()
{
		var v=document.getElementById("colorChooseList").value;
		document.getElementById("storySectionArea").style.background=v;
		colorValue = v;
}

function colorPickerValue2()
{
		var v=document.getElementById("colorChooseList2").value;
		document.getElementById("storySectionArea").style.background=v;
		colorValue = v;
}

//Share
function share(sendValue)
{	
	var images ="";
	var fontSize="";
	if(sendValue == "text")
	{
		v = document.getElementById("storyTextFieldArea").value
		v1 = document.getElementById("mobileScreenTextArea").value;
		alert(sendValue);
		if(v.length == 0 && v1.length == 0)
		{	$('alert').show();
			document.getElementById("alertBar").style.display="block";

		}

		else
		{
			if(v.length == 0)
				v=v1;
			
			//alert(colorValue);
			/*alert(fS);
			alert(fF);*/
			sendValuePortion();
			
			
		}
	}

	

	function sendValuePortion()
	{
        console.log('here')
	$.ajax({
      type: 'POST',
      url:'/storySubmissionForm/',
      data:{
        type:sendValue,
        fontSize:fS,
        fontFamily:fF,
        Caption:v,
        color:colorValue,
        image:images,
        // contentType: false,
        // processData: false,
      },
      success:function(e){
        console.log(e);

        {
		  // Get the snackbar DIV
		  var x = document.getElementById("snackbar");

		  // Add the "show" class to DIV
		  x.className = "show";

		  // After 3 seconds, remove the show class from DIV
		  setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
		}
        
        
      },
      error:function(data){
        console.log('Failed');
      }
    })
}
		
	
}



function readURL(input) {
	document.getElementById("shareSubmitButton").type="submit";
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    
    reader.onload = function(e) {
      $('#imagePlace').attr('src', e.target.result);
    }
    
    reader.readAsDataURL(input.files[0]); // convert to base64 string
  }
}

$("#imagePicker").change(function() {
  readURL(this);
});


//Image Upload Section 

//Write Caption
var maxCharCountVar;
function storyImageTextFieldAreaPlace()
{
	
	var v=document.getElementById("storyImageTextFieldArea").value;
 	var v1=document.getElementById("mobileScreenTextArea").value;
 	if(v.length<1)
 	{	
 		v=v1;
 	}
 		
 	if(v.length<=100){
 		document.getElementById("imageCaption").innerHTML=v;
 		document.getElementById("numberOfWordIndicator").textContent=v.length+"/100";
 		maxCharCountVar = v;
 		document.getElementById("captionInput").value=v;
 	}
 	else{
 		document.getElementById("numberOfWordIndicator").textContent="you can not insert more than 100 words";
 		document.getElementById("numberOfWordIndicator").style.color="red";
 		document.getElementById("storyImageTextFieldArea").value=maxCharCountVar;
 	}
}

//Font Family
function imagefontFamilyValue()
{
 v=document.getElementById("imagefontFamilyValueSelect").value;
 document.getElementById("imageCaption").style.fontFamily=v; 
 document.getElementById("fontFamilyInput").value=v;
}

//Color
function captioncolorPickerValue(v)
{
	document.getElementById("imageCaption").style.color=v; 	
	document.getElementById("colorInput").value=v;
}

function captioncolorPickerValue1()
{
	var v = document.getElementById("captioncolorPickerValueId").value;
	document.getElementById("imageCaption").style.color=v; 	
	
	document.getElementById("colorInput").value=v;
}



//Font Family for Image Story for Mobile Device
function fontFamilyValue2(v)
{
	document.getElementById("imageCaption").style.fontFamily=v;
	document.getElementById("fontFamilyInput").value=v;
}

function colorPickerValue4(v)
{
	document.getElementById("imageCaption").style.color=v;
	document.getElementById("colorInput").value=v;
}

$('#fileup').click(function() {
   $('#files').click();
});