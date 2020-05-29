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
  // console.log(Id);
    senderId = Id
    sender = document.getElementById('profile').value
    
    $.ajax({
      method:'POST',
      url:'/requestConfirm/',
      data:{
        sender : senderId,
        action:'add'
      },
      success:function(e){
        name = e['name']
        console.log(userProfile)
        receiver = e['receiver']
        senderPic = e['senderPic']
        
        document.getElementById("user"+Id).innerHTML = "<b> " + name + "</b> <br><span style='margin-left:30px;'><span class='ml-5'>Request Accepted</span></span>";
        console.log('calling fun');
        confirmNotification(sender,receiver,name,senderPic);
      },
      error:function(data){
        console.log('Failed');
      }
    })
  };


  const chatSocket1 = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/chat/'
    + 'confirmPath'
    + '/'
  );
  // FOR SENDING REQUEST CONFIRM NOTIFICATION
  function confirmNotification(sender,receiver,name,senderPic){
console.log('called');

 // THIS IS GLOBAL CHATSOCKET FOR REQUEST CONFIRM NOTIFICATION AVAILABLE EVERYWHERE THROUGH SERVER

// console.log('sendng data');
// console.log(sender);
// console.log(receiver);
// console.log(name);
// console.log(senderPic);
chatSocket1.send(JSON.stringify({
  'action':'add',
  'sender': sender,
  'receiver':receiver,
  'name':name,
  'senderPic':senderPic,
})
),

// THIS FUNCTION RECEIVES DATA FROM consumers.py FILE AND PROCESSES ACCORDINGLY
chatSocket1.onmessage = function(e) {
  console.log('receiving data');
  const data = JSON.parse(e.data);

  
      if (data.receiver === sender){
      document.querySelector('#allNotifications').value = name + ' Accepted your Friend Request';
      
      
      }
    
  
};
  

chatSocket1.onclose = function(e) {
  console.error('Chat socket closed unexpectedly');
};
  }