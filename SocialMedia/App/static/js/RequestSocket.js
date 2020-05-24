user = document.getElementById('profile').value;
                  myself = document.getElementById('currentUserId').innerHTML;
          // THIS IS GLOBAL CHATSOCKET AVAILABLE EVERYWHERE THROUGH SERVER
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
                        document.getElementById('likeComment').innerHTML = 'New Request'
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
                    // console.log(btnValue);
                  if (btnValue === 'Add Friend'){
                      chatSocket.send(JSON.stringify({
                      'action':'add',
                      'sender': myself,
                      'receiver':user
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