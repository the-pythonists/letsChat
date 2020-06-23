// GLOBAL SOCKET FOR SENDING LIKES NOTIFICATIONS

const likeSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/like/'
    + 'postlike'
    + '/'
    );
    var loggedUser = document.getElementById('currentUserId').value;

function postLiker(id,postLikedOf,postLikedBy){
        const postId = id;
        var postLikedOf = postLikedOf;
        var postLikedBy = postLikedBy;
       
    likeSocket.send(JSON.stringify({
        'postId' : postId,
        'postLikedOf' : postLikedOf,
        'postLikedBy' : postLikedBy,
        'loggedUser':loggedUser
    }));
}

likeSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
    };
        
    likeSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        
        like(data.postId, data.postLikedOf, data.postLikedBy)            
    };

function like(postId, postLikedOf, postLikedBy){
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
            if(postLikedOf == loggedUser && postLikedOf != postLikedBy && message === 'liked'){
                console.log('like')
            //** IF PERSON LIKES OWN POST OR DISLIKES ANY POST, NO NOTIFICATION WILL BE SENT **//
                document.getElementById('noti_Counter').innerHTML = 'Liked';
            }
        }
    })
}