const likeSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/like/'
    + 'postlike'
    + '/'
    );
    var loggedUser = document.getElementById('currentUserId').value;
    console.log(loggedUser);
function postLiker(id,postLikedOf,postLikedBy){
        console.log('fn me');
        const postId = id;
        var postLikedOf = postLikedOf;
        var postLikedBy = postLikedBy;
        
        // console.log(postId);
        // console.log(postLikedOf);
        // console.log(postLikedBy);
        
    likeSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
    };
        
    likeSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        // console.log('data',data.postId);
        console.log('data',data.postLikedBy);
        console.log('data',data.loggedUser);
        
        like(data.postId, data.postLikedOf, data.postLikedBy)
        if(data.postLikedBy == data.loggedUser){
            document.getElementById('noti_Counter').innerHTML = 'Liked';
        }
            
    };

    likeSocket.send(JSON.stringify({
        'postId' : postId,
        'postLikedOf' : postLikedOf,
        'postLikedBy' : postLikedBy,
        'loggedUser':loggedUser
    }));
}


function like(postId, postLikedOf, postLikedBy){
    console.log('like funsction');
    $.ajax({
        method:'POST',
        url:'/postlike/',
        data:{
            postId:postId,
            postLikedOf:postLikedOf,
            postLikedBy:postLikedBy,
        },
        success:function(e){
            var totalLikes = e.totalLikes;
            var message = e.message;

            document.getElementById('Counter'+postId).innerHTML = totalLikes + ' Likes';
            if(message === 'liked'){
                document.getElementById(postId).style.color = 'rgba(0, 150, 136,1)';
            }
            else{
                document.getElementById(postId).style.color = 'grey';
            }
            if (postLikedOf !== postLikedBy){
                // console.log(postLikedOf);
                // console.log(loggedUser);
                
                // checking if person liked own post 
            
            }
        }
    })
}