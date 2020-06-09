
var globData
function showAllFriends(){
s=document.getElementById("sortByDisplay").innerHTML;
$("#showFriendSection").empty();
	$.ajax({
        method:'POST',
        url:'/myFriendsProcess/',

        data:{
        	sortBy:s,
        },
        success:function(e){
        	globData=e;
        	document.getElementById("totalConnection").innerHTML=(e.FName).length;
            console.log(e);
            for(var i=0;i<(e.FName).length;i++){
            $('#showFriendSection').append('<div class="friend_Profile"><p><img src="'+e.pPic[i]+'"><span style="vertical-align: middle;font-weight:bold;">'+e.FName[i]+' '+e.lName[i]+'</span><br><span style="line-height:0;" id="userQuote">'+e.quote[i]+'</span><span><i class="fas fa-ellipsis-v pull-right" id="ellipsis"></i><a href="/messages/'+e.EmailId[i]+'/"><button class="pull-right" id="userMessage">Message</button></a></span></p></div><br><hr>');
    }
        },
        error:function(e){
        	console.log("Fail");
        }
    })

}


function serachFriend(){

	$("#showFriendSection").empty();
	
	s=document.getElementById("search").value;

	var v=0;
	for(i=0;i<(globData.FName).length;i++){    
        	document.getElementById("totalConnection").innerHTML="0";
            console.log(globData);
            var e=globData;
            for(var i=0;i<(e.FName).length;i++){
            	l=s.length;
            	fN=e.FName[i]
            	if((fN.slice(0,l)).toUpperCase()==s.toUpperCase()){
            		document.getElementById("totalConnection").innerHTML=(v+1);
            $('#showFriendSection').append('<div class="friend_Profile"><p><img src="'+e.pPic[i]+'"><span style="vertical-align: middle;font-weight:bold;">'+e.FName[i]+' '+e.lName[i]+'</span><br><span style="line-height:0;" id="userQuote">'+e.quote[i]+'</span><span><i class="fas fa-ellipsis-v pull-right" id="ellipsis"></i><a href="/messages/'+e.EmailId[i]+'/"><button class="pull-right" id="userMessage" >Message</button></a></span></p></div><br><hr>');
        }}
    }
        
    
if(s==""){
	document.getElementById("totalConnection").innerHTML=(globData.FName).length;
}

}


function Message(v){
	alert(v);
}

function sortDisplay(v){
	
	document.getElementById("sortByDisplay").innerHTML=v;
	showAllFriends();
}


showAllFriends();


