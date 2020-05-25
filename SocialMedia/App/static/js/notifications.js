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

function addrequest(Id){
  console.log(Id);
    // btnValue = document.getElementById("add").value;
    // alert(Id);

    sender = Id
    // console.log(sender);
    $.ajax({
      method:'POST',
      url:'/requestConfirm/',
      data:{
        sender : sender,
        action:'add'
      },
      success:function(e){
        name = e['name']
        // console.log(e['name'])
        // document.getElementById(Id).style.display="none";
        // Need timer to remove this line after 2 seconds
        document.getElementById(Id).innerHTML="You and " + name + " are now Friends.";
        // time.sleep(3)
        // document.getElementById(Id).style='none';
        // setTimeout(doMoreStuff, 1000);
        
      },
      error:function(data){
        console.log('Failed');
      }
    })
  };

  