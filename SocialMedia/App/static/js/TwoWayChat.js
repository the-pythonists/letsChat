
var roomId = document.getElementById('inboxId').value ; 

// console.log(roomId)

friend = document.getElementById('friend').value;
myself = document.getElementById('loggedUser').value;

var socket = new WebSocket('ws://127.0.0.1:8000/ws/chat/'+roomId+'/');
	socket.onopen = websocket_welcome;
	socket.onmessage = websocket_message_show;

	document.querySelector('#Chatform').onclick = function(e){
		e.preventDefault();
		message_data = {
			'username':myself,
			'loggedUserFullName':$('input[name="loggedUserFullName"]').val(),
			'loggedUserPic':$('input[name="loggedUserPic"]').val(),
			'message' : $('input[name="message"]').val(),
			'sender':myself,
			'receiver':friend
		}
		socket.send(JSON.stringify(message_data));
		const messageInputDom = document.querySelector('#message');
		messageInputDom.value = '';
		
	};

function websocket_welcome(){
	// alert("welcome to chat room")
}
function websocket_message_show(e){
	
	var today = new Date();
	var time = today.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
	
	var message_data = JSON.parse(e.data);
	console.log(message_data.message)
	if(message_data.sender==myself && message_data.receiver==friend){
		message_save(message_data.message);
	coding ='<p class="sender"><img src="'+message_data.loggedUserPic+'" class="personProfilePicture"><strong class="ml-2">'+message_data.loggedUserFullName+'</strong><br><span class="ml-5">'+message_data.message+'</span><span class="float-right">'+time+'</span></p><br>';
	}
	else if (message_data.sender==friend && message_data.receiver==myself){
		coding ='<p class="reciver"><img src="'+message_data.loggedUserPic+'" class="personProfilePicture"><strong class="ml-2">'+message_data.loggedUserFullName+'</strong><br><span class="ml-5">'+message_data.message+'</span><span class="float-right">'+time+'</span></p><br>';
		// coding = "<p class='reciver'><img src="+"'message_data.loggedUserPic'"+ "class='personProfilePicture'><strong >"+message_data.username+"</strong><br><span class='ml-5'>"+message_data.message+"</span><span class='float-right'>"+time+"</span></p>";
	}

	$('.wrapperClassBlock').append(coding);
	console.log('coding');
}
function message_save(message){
$.ajax({
	method:'POST',
	url:'/saveMessage/',
	data:{
		inboxId : roomId,
		user1:myself,
		user2:friend,
		sender:myself,
		receiver:friend,
		Message:message,
	},
	success:function(e){
		console.log(e)
	},
	error:function(e){
		console.log('Failed');
	}
})
// console.log(Users);
}