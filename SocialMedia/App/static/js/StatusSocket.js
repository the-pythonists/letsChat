// GLOBAL SOCKET FOR STATUS

const statusSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/letschat/'
    + 'status'
    + '/'
    );

    $.post('/update_session/', function(data) {
        loggedUser = data;
        console.log(loggedUser,'global');
    });

statusSocket.onclose = function(e) {
    // $.post('/update_session/', function(data) {
    //     loggedUser = data;
    //     action = 'offline';
    // });
    
    try{
        console.log(loggedUser,'disconnected','online'+ loggedUser)
    document.getElementById('online'+ loggedUser).className = 'fa fa-eye-slash'
    }catch{}
    console.error('Chat socket closed unexpectedly');
    };
        
    statusSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        // console.log(data['userId'])
        // console.log('online'+ data['userId'])
        try{
        document.getElementById('online'+ data['userId']).className = 'fa fa-eye'
        }catch{}
      };

// sleep time expects milliseconds
function sleep (time) {
    return new Promise((resolve) => setTimeout(resolve, time));
  }
  
  sleep(5000).then(() => {
    
    statusSocket.send(JSON.stringify({
        'userId' : loggedUser,
    }));
    
});


//   window.addEventListener("beforeunload", function () {      
//       console.log("Working ");
//     $.ajax({
//         type: "POST",
//         url: "/update_session/",
//         data:{action: 'offline'},
//         success:function(e){
//             console.log('Done');
//             },
//             error:function(data){ 
//               console.log('Failed');
//             }

//     });
//     return;
//   });
