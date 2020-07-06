// GLOBAL SOCKET FOR SENDING LIKES NOTIFICATIONS

const commentSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/comment/'
    + 'postcomment'
    + '/'
    );
    var loggedUser = document.getElementById('currentUserId').value;

function comments(id,postCommentedOf,postCommentedBy){
    console.log('called',id)
        const postId = id;
        var postCommentedOf = postCommentedOf;
        var postCommentedBy = postCommentedBy;
         try{
        comment = document.getElementById('Comment'+postId).value;
         }catch{}
        console.log(postCommentedOf, postCommentedBy,postId,comment)
       
        commented(postId, postCommentedOf, postCommentedBy,comment)

    commentSocket.send(JSON.stringify({
        'postId' : postId,
        'postCommentedOf' : postCommentedOf,
        'postCommentedBy' : postCommentedBy,
        'loggedUser':loggedUser,
        'comment':comment,
    })
    );
}

commentSocket.onclose = function(e) {
    console.error('Chat socket closed unexpectedly');
    };
        
    commentSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log(data.postCommentedOf,loggedUser)
        document.getElementById('Comment'+postId).value='';
        try{
            document.getElementById('NewComment'+data.postId).innerHTML = data.comment;
        }catch{}
        
           
        if(data.postCommentedOf == loggedUser && data.postCommentedOf != data.postCommentedBy){
        //** IF PERSON LIKES OWN POST OR DISLIKES ANY POST, NO NOTIFICATION WILL BE SENT **//
            try{document.getElementById('noti_Counter').innerHTML = 'New Comment';
        }catch{}
        }
    changeNotification(data.postCommentedBy,action='notification')
       
    };

function commented(postId, postCommentedOf, postCommentedBy,comment){
    $.ajax({
        method:'POST',
        url:'/postcomment/',
        data:{
            postId:postId,
            postCommentedOf:postCommentedOf,
            postCommentedBy:postCommentedBy,
            comment:comment
        },
        success:function(e){
        }
    })
}

function changeNotification(postCommentedBy,action){
    $.ajax({
        method:'POST',
        url:'/postcomment/',
        data:{
            action:action,
            postCommentedBy:postCommentedBy,
        },
        success:function(e){
            try{
            document.getElementById('likeComment').innerHTML = '<img src="'+e.pic+'">'+e.commenter + ' Commented on Your Post'
            }catch{}
        }
    })
}