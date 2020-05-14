$(document).ready(function() {
  $(".btn-pref .btn").click(function () {
      $(".btn-pref .btn").removeClass("btn-primary").addClass("btn-default");
      // $(".tab").addClass("active"); // instead of this do the below 
      $(this).removeClass("btn-default").addClass("btn-primary");   
  });
  
  $('#search').keyup(function(){
      
      $("ul").empty()
  
     var searchField = $('#search').val();
     console.log(searchField);
  if(searchField.length)
    $.ajax({
                  method:'POST',
                  url:'/liveSearchProcess/',
                  data:{
                    search:searchField
                  },
                  success:function(data){
                    console.log(data);
                    
                    for(var i=0;i<(data.Id).length;i++)
                    {
                      
                       $('#result').append('<li class="list-group-item link-class" ><img src="'+data.picture[i]+'" height="40" width="40" class="img-thumbnail" />'+data.Username[i]+' | <span class="text-muted">'+data.Id[i]+'</span></li>');
                      }
                   incomingRequest();
                   outgoingRequest();
              
                  },
                  error:function(data){
                      console.log('Error!');
                      
                  }
  
              });
  else{
    incomingRequest();
    outgoingRequest();
  }
  
  });
  
    $('#result').on('click', 'li', function() {
    var click_text = $(this).text().split('|');
    $('#search').val($.trim(click_text[0]));
    $('#personId').val($.trim(click_text[1]));
    $("#result").html('');
   });
  });
  
  //Incoming Request
  function incomingRequest(){
  $.ajax({
                  method:'POST',
                  url:'/incomingRequest/',
                  
                  success:function(data){
                    console.log(data);
                    for(var i=0;i<(data.senderId).length;i++)
                    {
                      
                       $('#incomingResult').append('<a href="'+data.senderId[i]+'"><li class="list-group-item link-class" >'+data.senderName[i]+' | <span class="text-muted">'+data.senderId[i]+'</span></li></a><button class="btn btn-info">See</button>');
                      }
  
  
    },
     error:function(data){}
   })
  
  }
  
  
  //Incoming Request
  function outgoingRequest(){
  $.ajax({
                  method:'POST',
                  url:'/outgoingRequest/',
                  
                  success:function(data){
                    console.log(data);
                    for(var i=0;i<(data.reciverId).length;i++)
                    {
                      
                       $('#outgoingResult').append('<a href="'+data.reciverId[i]+'"><li class="list-group-item link-class" ><span class="text-muted">'+data.reciverId[i]+'</span></li></a><button class="btn btn-info">See</button>');
                      }
  
  
    },
     error:function(data){}
   })
  
  }
  
  incomingRequest();
  
  outgoingRequest();