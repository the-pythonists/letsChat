        //         user = document.getElementById('profile').value;
        //         myself = document.getElementById('currentUserId').innerHTML;
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
                    
                      // if (data.receiver === myself){
                      document.querySelector('#addbtn').value = 'Confirm Request';
                      // alert("jh");
                      // document.getElementById('pageTitle').innerHTML = 'New Request';
                      newRequest(data.receiver,data.sender,data.userFullName,data.userPic);
                      // alert("jkghnfku");
                      // }
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
                  user = document.getElementById('profile').value;
                  userFullName = document.getElementById('currentUserFullName').value;
                  userPic = document.getElementById('currentUserPic').value;
                myself = document.getElementById('currentUserId').innerHTML;

        // THIS IS GLOBAL CHATSOCKET AVAILABLE EVERYWHERE THROUGH SERVER
              //   const chatSocket = new WebSocket(
              //     'ws://'
              //     + window.location.host
              //     + '/ws/chat/'
              //     + 'path'
              //     + '/'
              // );
                  const btn = document.querySelector('#addbtn');
                  const btnValue = btn.value;
                  // console.log(btnValue);
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
                    'receiver':user
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
      action:'changeHTML',
    },
    success:function(e){
      console.log('here');
      // ID = document.getElementById('profile').value;
      try{
      document.getElementById('NotificationNotes').innerHTML = '<img src="'+pic+'" class="profilePic"><b>'+name+'</b> Sent you Friend Request<br><button  onclick="addrequest(\'' + sender + '\')">Add Friend</button><button>Ignore</button>';
      }
      catch(e){
        // pass
      }
    },
    error:function(data){ 
      console.log('Failed');
    }
  })
}