
try{
    user = document.getElementById('profile').value;   // friend id
    userFullName = document.getElementById('currentUserFullName').value;  // logged user name
    userPic = document.getElementById('currentUserPic').value;            // logged user pic
  myself = document.getElementById('currentUserId').value;                // logges user id
  
}

catch(e){
  // myself = document.getElementById('currentUserId').value;
  myself = 'sarthak26';
}

// // THIS IS GLOBAL CHATSOCKET AVAILABLE EVERYWHERE THROUGH SERVER
        const chatSocket = new WebSocket(
          'ws://'
          + window.location.host
          + '/ws/chat/'
          + 'path'
          + '/'
      );
// THIS FUNCTION RECEIVES DATA FROM consumers.py FILE AND PROCESSES ACCORDINGLY
      chatSocket.onmessage = function(e) {
          const data = JSON.parse(e.data);
          if (data.action === 'add'){
            
              if (data.receiver === myself){
              document.querySelector('#addbtn').value = 'Confirm Request';
              
              newRequest(data.receiver,data.sender,data.userFullName,data.userPic);
              }
            }
          else if (data.action === 'cancel'){
            if (data.receiver === myself){
            document.querySelector('#addbtn').value = 'Add Friend';
            }
          }
          else if (data.action === 'confirm'){
            if (data.receiver === myself){
            document.querySelector('#addbtn').value = 'Unfriend';
            }
            if (data.receiver === myself){
              // console.log(data)
              
              requestConfirmNotification(sender = data.sender, receiver = data.receiver)
              dashboardNotification(sender = data.sender, receiver = data.receiver)
            }
          }
          else if (data.action === 'unfriend'){
            if (data.receiver === myself){
            document.querySelector('#addbtn').value = 'Add Friend';
            }
          }
      };
          

      chatSocket.onclose = function(e) {
          console.error('Chat socket closed unexpectedly');
      };
// THIS FUNCTION IS STARTING POINT, IT RECEIVES BUTTON VALUE AND PROCESSES ACCORDINGLY
        document.querySelector('#addbtn').onclick = function(e) {
        
          const btn = document.querySelector('#addbtn');
          const btnValue = btn.value;
          
        if (btnValue === 'Add Friend'){
             chatSocket.send(JSON.stringify({
                  'action':'add',
                  'sender': myself,
                  'receiver':user,
                  'userFullName':userFullName,
                  'userPic':userPic

            }));
            request('add', myself, user);
        }
        else if (btnValue === 'Cancel Request'){
          chatSocket.send(JSON.stringify({
            'action':'cancel',
            'sender': myself,
            'receiver':user
            }));
            request('cancel', myself, user);
        }
        else if (btnValue === 'Confirm Request'){
         
          chatSocket.send(JSON.stringify({
            'action':'confirm',
            'sender': myself,
            'receiver':user,
            'name':name,
            'userPic':userPic
            }));
            request('confirm', myself, user);
        }
        else if (btnValue === 'Unfriend'){
          chatSocket.send(JSON.stringify({
            'action':'unfriend',
            'sender': myself,
            'receiver':user
            }));
            request('unfriend', myself, user);
        }
        else{console.log('Else Part');}
                    
                    // console.log(message);
                };
        ;
function newRequest(receiver,sender,name,pic){

$.ajax({
method:'POST',
url:'/addfriend/',
data:{
profileId:receiver,
action:'changeRequestHTML',
},
success:function(e){
// ID = document.getElementById('profile').value;
try{
document.getElementById('NotificationNotes').innerHTML = '<span ><img src="'+pic+'" class="profilePic"><span id="user'+sender+'" class="ml-1"><b>'+name+'</b> Sent you Friend Request<br><span style="margin-left:30px;" id="user'+sender+'"><button  onclick="addrequest(\'' + sender + '\')" class="btn btn-danger ml-5 p-1" >Confirm</button><button class="btn btn-success ml-2 p-1" >Ignore</button></span></span></span>';
}
// try{
//   document.getElementById("noti_Counter").innerHTML="Ho gya";
// }
catch(e){
// pa
}
},
error:function(data){ 
console.log('Failed');
}
});
}

function requestConfirmNotification(sender = data.sender, receiver = data.receiver){
  $.ajax({
    method:'POST',
    url:'/addfriend/',
    data:{
    profileId:sender,
    action:'changeNotificationHTML',
    },
    success:function(e){
      try{
        console.log(e.name, e.pic, sender,receiver)
        document.getElementById('allNotifications').innerHTML = '<span ><img src="'+e.pic+'" class="profilePic"><span id="user'+sender+'" class="ml-1"><b>'+e.name+'</b> Accepted Your Friend Request<br><span style="margin-left:30px;" id="user'+sender+'"></span></span></span>';
        
      }
      catch(e){
    // pass
    }
    },
    error:function(data){ 
    console.log('Failed');
    }
    });
}

function dashboardNotification(sender = data.sender, receiver = data.receiver){
  console.log(sender,receiver)
  // document.getElementById("noti_Counter").innerHTML="Ho gya";
  $.ajax({
    method:'POST',
    url:'/addfriend/',
    data:{
    profileId:sender,
    action:'changeDashboardHTML',
    },
    success:function(e){
      console.log(sender,receiver,'success')
      try{
        console.log("Doing Work");
        // console.log(e.name, e.pic, sender,receiver)
        // document.getElementById('allNotifications').innerHTML = '<span ><img src="'+e.pic+'" class="profilePic"><span id="user'+sender+'" class="ml-1"><b>'+e.name+'</b> Accepted Your Friend Request<br><span style="margin-left:30px;" id="user'+sender+'"></span></span></span>';
        // document.getElementById("NotificationCount").innerHTML="Ho gya";
        v10=document.getElementById("pageiId").innerHTML;
        console.log(v10);
        if(v10=="Page1"){
        $('#noti_Counter').text('7')  // ADD DYNAMIC VALUE (YOU CAN EXTRACT DATA FROM DATABASE OR XML).
        }
        else{
          console.log("Else part Executed");
        }
	;

        
      }
      catch(e){
    // pass
    console.log('val')
    document.getElementById("NotificationCount").innerHTML="Ho gya";
    }
    },
    error:function(data){ 
    console.log('Failed');
    }
    });

}