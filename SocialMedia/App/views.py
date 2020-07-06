from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse
import random
from django.core.mail import send_mail
#from .models import userRegistration,Friend_Requests,UserPost,Likes,AllFriends,Notifications,Story,Album,Photos,Messages,TempRoom,Comments
from .models import *
from django.contrib.auth.hashers import make_password,check_password
import datetime, time
import uuid
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q
from itertools import chain
from django.urls import reverse
from django.db.models import Subquery


@csrf_exempt
def update_session(request):
	if not request.is_ajax() or not request.method=='POST':
		return HttpResponseNotAllowed(['POST'])
	userRegistration.objects.filter(userId=request.session['user']).update(is_online=True)
	return HttpResponse(request.session['user'])

def index(request):
	if request.session.has_key('user'):
		userInfo = userRegistration.objects.get(userId=request.session['user'])
		userData = UserPost.objects.filter(userId=request.session['user']).order_by('-date') # '-' for descending order
		
		friends = AllFriends.objects.get(userId=request.session['user']).Friends
		
		postList = []
		def UserAllPost():
			for item in userData:
				yield item

		def FriendPosts():
			for friend in friends:
				friendPost = UserPost.objects.filter(userId=friend).order_by('-date')
				for post in friendPost:

					yield post
		# FriendPosts()
		storyList = []
		StoryOwnerList = []
		tempStoryList = []
		tempStoryOwner = ""
		tempMedia = ""
		tempUploadTime = ""
		tempStoryType = ""
		tempFontFamily = ""
		tempFontSize = ""
		tempCaption = ""
		tempColor = ""
		lenthCaption = ""
		#Check myself Stories
		myStories = Story.objects.filter(userId=request.session['user'])
		if myStories.exists():
			StoryOwner = userRegistration.objects.get(userId=request.session['user'])
			for l in myStories:
				lenthCaption =lenthCaption + str(len(l.Caption)) +"@"
				tempMedia = tempMedia + "/media/"+str(l.media) +"@"
				tempUploadTime = tempUploadTime + str(l.uploadTime) +"@"
				tempStoryType = tempStoryType + l.storyType +"@"
				tempFontFamily = tempFontFamily + l.fontFamily +"@"
				tempFontSize = tempFontSize + l.fontSize +"@"
				tempCaption = tempCaption + l.Caption 
				tempColor = tempColor + l.color +"@"
				
				tempStoryOwner = "Me" + ","
				StoryOwner.userName = " Me"
			StoryOwnerList.append(StoryOwner)
			tempStoryList.insert(0,tempMedia)
			tempStoryList.insert(1,tempUploadTime)
			tempStoryList.insert(2,tempStoryType)
			tempStoryList.insert(3,tempFontFamily)
			tempStoryList.insert(4,tempFontSize)
			tempStoryList.insert(5,tempCaption)
			tempStoryList.insert(6,tempColor)
			tempStoryList.insert(7,lenthCaption)		
			
			storyList.append(tempStoryList)
			
			
		#Get Friends Stories
		for friend in friends:
			#print(friend)
			allStories = Story.objects.filter(userId=friend)
			#print(allStories)
			if allStories.exists():
				StoryOwner = userRegistration.objects.get(userId=friend)
				print(len(allStories))
				tempStoryList = []
				tempStoryOwner = ""
				tempMedia = ""
				tempUploadTime = ""
				tempStoryType = ""
				tempFontFamily = ""
				tempFontSize = ""
				tempCaption = ""
				tempColor = ""
				lenthCaption = ""
				for l in allStories:
					lenthCaption =lenthCaption + str(len(l.Caption)) +"@"
					tempMedia = tempMedia + "/media/"+str(l.media) +"@"
					tempUploadTime = tempUploadTime + str(l.uploadTime) +"@"
					tempStoryType = tempStoryType + l.storyType +"@"
					tempFontFamily = tempFontFamily + l.fontFamily +"@"
					tempFontSize = tempFontSize + l.fontSize +"@"
					tempCaption = tempCaption + l.Caption 
					tempColor = tempColor + l.color +"@"
					
				StoryOwnerList.append(StoryOwner)
				tempStoryList.insert(0,tempMedia)
				tempStoryList.insert(1,tempUploadTime)
				tempStoryList.insert(2,tempStoryType)
				tempStoryList.insert(3,tempFontFamily)
				tempStoryList.insert(4,tempFontSize)
				tempStoryList.insert(5,tempCaption)
				tempStoryList.insert(6,tempColor)
				tempStoryList.insert(7,lenthCaption)		
				
				storyList.append(tempStoryList)
					#storyList.append(l)	
					#StoryOwnerList.append(StoryOwner)

		storiesFullData = zip(StoryOwnerList,storyList)
		AllPost = chain(UserAllPost(), FriendPosts())
		for item in AllPost:
			postList.append(item)
		postList.sort(key=lambda x: x.date,reverse = True) 
		like=[]; colorPost = []
		for i in postList:
			likes = Likes.objects.get(postId=i.postId)
			like.append(len(likes.postLikedBy))
			if request.session['user'] in likes.postLikedBy:
				colorPost.append("rgba(0, 150, 136,1)")
			else:
				colorPost.append("grey")
		qry =[]
		lnth = []
		for item in postList:
			poId=item.postId
			try:
				s =(TaggedPeople.objects.get(postId=poId).taggedPersons)
				qry.append(userRegistration.objects.filter(userId=s[0]))
				lnth.append(len(s)-1)
			except:
				qry.append("")
				lnth.append("")
					
		commentContent = []
		commentName = []
		commentPic = []
		commentId = []
		for i in postList:
			commentData = []
			commentData.append(Comments.objects.filter(postId=i.postId).order_by('-date'))
			for j in commentData:
				print("j value = ",j)
				if j:
					for k in j:
						commentContent.append(k.comment)
						commentName.append(k.userInfo.firstName + ' ' + k.userInfo.lastName)
						commentPic.append(k.userInfo.profilePic)
						commentId.append(k.commentId)
				else:
					commentContent.append("")
					commentName.append("")
					commentPic.append("")
					commentId.append("")
					 	
				break


		
		print(commentContent,commentName)



		
		notification = Notifications.objects.filter(receiver=request.session['user']).order_by('-date')
		picsList1 = []
		uname = ''   # IF USER HAS NO NOTIFICATION
		for Id in notification:
			senderDetail = userRegistration.objects.filter(userId=Id.sender)
			for detail in senderDetail:
				
				uname = detail.userName
				picUrl = detail.profilePic
				picsList1.append(picUrl.url)
		params = {'userInfo':userInfo,'userData':zip(postList, like,colorPost,qry,lnth,commentContent,commentName,commentPic,commentId),'date_now':datetime.datetime.now(),
		'allComments':zip(postList),"storyData":storiesFullData,'notification':zip(notification,picsList1)}
		return render(request,'DashBoard.html',params)
	else:
		return render(request,'index.html')

def textStory(request):
	return render(request,'textStory.html')

def imageStory(request):
	return render(request,'imageStory.html')

@csrf_exempt
def story(request):
	if request.method == 'POST':
		image = request.FILES.get('image')
		fontSize = request.POST.get('fontSize',"defaultValue")
		storyType = request.POST.get('type',"defaultValue")
		fontFamily = request.POST.get('fontFamily',"defaultValue")
		Caption = request.POST.get('Caption',"defaultValue")
		color = request.POST.get('color',"defaultValue")
		

		#media=image,

		Story(userId=request.session['user'],media=image,storyType=storyType,fontFamily=fontFamily,fontSize=fontSize,Caption=Caption,color=color).save()
		return JsonResponse({"Status":"Successfully"})
	else:
		stories = Story.objects.all()
		return JsonResponse({"Status":"UnSuccessfully"})

def imageStorySubmissionForm(request):
	if request.method == 'POST':
		image = request.FILES.get('image')
		fontSize = request.POST.get('fontSize',"defaultValue")
		storyType = request.POST.get('type',"defaultValue")
		fontFamily = request.POST.get('fontFamily',"defaultValue")
		Caption = request.POST.get('Caption',"defaultValue")
		color = request.POST.get('color',"defaultValue")
		
		#media=image,

		Story(userId=request.session['user'],media=image,storyType=storyType,fontFamily=fontFamily,fontSize=fontSize,Caption=Caption,color=color).save()
		return HttpResponseRedirect("/")
	else:
		stories = Story.objects.all()
		return JsonResponse({"Status":"UnSuccessfully"})

def signup(request):
	if request.method == "POST":
		fName = request.POST.get('firstName').title()
		lName = request.POST.get('lastName').title()
		username = request.POST.get('userName')
		email = request.POST.get('Email')
		otp = request.POST.get('OneTimePass')
		pwd = request.POST.get('Password')
		mobile = request.POST.get('Mobile')
		
		if((otp == request.session["Otp"])):
			if userRegistration.objects.filter(emailAddress=email):
				return render(request,'CreateAccount.html',{'message':'Account Already Present with Given Email'})
			elif userRegistration.objects.filter(mobile=mobile):
				return render(request,'CreateAccount.html',{'message':'Account Already Present with Given Mobile Number'}) 
			else:
				userRegistration(userId=username, firstName=fName, lastName=lName, userName=username, 
				mobile=mobile,emailAddress = email, password = make_password(pwd)).save()
				# Creating Blank Frined List
				AllFriends(userId=username).save()
				code = str(username + "profile").encode('utf-8')
				createAlbum(userId = username,albumName="profile",albumId=code.hex()).save()
				
				code = str(username + "cover").encode('utf-8')
				createAlbum(userId = username,albumName="cover",albumId=code.hex()).save()
				# messages.success(request,'Account Created Successfully !!')
				return HttpResponseRedirect('/')
			
		else:
			return render(request,'CreateAccount.html',{'message':'Incorrect OTP'})
	else:
		return render(request,'CreateAccount.html')

@csrf_exempt
def uservalidate(request):
	username = request.POST.get('username')
	if userRegistration.objects.filter(userName=username):
		return JsonResponse({'Result':1})
	else:
		return JsonResponse({'Result':0})

@csrf_exempt
def OtpGeneration(request):
	Email = request.POST.get('Email','DefaultValue')
	RandomValue = random.randint(1001,99999)
	RandomValue = "LetsChat"+str(RandomValue)
	request.session["Otp"] = RandomValue
	print(RandomValue)
	message = f"Your Email Address  {Email}  Your OTP is {RandomValue} Do not share your password to anyone."
	send_mail(
    	'LetsChat',
    	message,
    	settings.EMAIL_HOST_USER,
    	[Email],
    	fail_silently=False)
	return JsonResponse({'Result':"Successfully"})

@csrf_exempt
def storydelete(request):
	from datetime import timedelta 
	tm1 = (datetime.datetime.now() - timedelta(minutes=1)   )
	s = Story.objects.filter(uploadTime__lte= tm1 ).delete()	
	return JsonResponse({'Result':'Deleted'})

def changepassword(request):
	if request.method == 'POST':
		currentPass = request.POST.get('currentPass')
		newPass = request.POST.get('newPass')
		confirmPass = request.POST.get('confirmPass')
		if newPass != confirmPass:
			message = "Password Do not match"
			return render(request,'changepwd.html',{'message':message})
		else:
			encryptCurrentPass = userRegistration.objects.get(userId=request.session['user']).password

			if check_password(currentPass,encryptCurrentPass) == True:
				userRegistration.objects.filter(userId=request.session['user']).update(password=make_password(newPass))
				# return render(request,'changepwd.html',{'message':'Password Changed Successfully.Please Login Again'})
				
				del request.session['user']
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('pasword not match')
	else:
		return render(request,'changepwd.html')

@csrf_exempt
def postlike(request):
	postId = request.POST.get('postId')
	postLikedOf = request.POST.get('postLikedOf')
	postLiker = request.POST.get('postLikedBy')

	likes = Likes.objects.get(postId=postId)
	if postLiker in likes.postLikedBy: # Checking if friend has already liked 
		likes.postLikedBy.remove(postLiker)
		LikesList = likes.postLikedBy
		Likes.objects.filter(postId=postId).update(postId=postId,postLikedBy=LikesList)
		totalLikes = len(LikesList)

		Notifications.objects.filter(postId=postId,notificationType='like',sender=postLiker).delete()
		return JsonResponse({'Result':'Success','totalLikes':totalLikes,'message':'unliked'})

	else:
		likes.postLikedBy.append(postLiker)
		LikesList = likes.postLikedBy
		Likes.objects.filter(postId=postId).update(postId=postId,postLikedBy=LikesList)
		totalLikes = len(LikesList)

		if postLikedOf != postLiker:
			postLikedByPerson = userRegistration.objects.get(userId=postLiker)
			postLikedByPersonName = str(postLikedByPerson.firstName) + ' ' + str(postLikedByPerson.lastName)
			notificationMessage = postLikedByPersonName + ' Liked your Post'
			Notifications(postId=postId,notificationType='like',fullName=postLikedByPersonName,sender=postLiker,
				receiver=postLikedOf,notification=notificationMessage,viewed=False).save()
		return JsonResponse({'Result':'Success','totalLikes':totalLikes,'message':'liked'})

@csrf_exempt
def postcomment(request):
	commentedBy = request.POST.get('postCommentedBy')

	commenter = userRegistration.objects.get(userId=commentedBy)
	if request.POST.get('action'):
		return JsonResponse({'Result':'Success','commenter':str(commenter),'pic':str(commenter.profilePic.url)})

	postId = request.POST.get('postId')
	commentedOf = request.POST.get('postCommentedOf')
	# commentedBy = request.POST.get('postCommentedBy')
	comment = request.POST.get('comment')
	commentId = 'comment'+str(uuid.uuid4().hex)
	name = userRegistration.objects.get(userId=commentedBy)
	fullname = commenter.firstName + ' ' + commenter.lastName
	notify = fullname + ' commented on your post'

	Comments(postId=postId,commentedOf=commentedOf,commentedBy=commentedBy,comment=comment,commentId=commentId,
	userInfo=name).save()
	Notifications(postId=postId,notificationType='comment',fullName=name,sender=commentedBy,receiver=commentedOf,
	notification=notify,viewed=False).save()
	return JsonResponse({'Result':'Success','comment':comment})

@csrf_exempt
def reply(request):
	postId = request.POST.get('postId')
	commentId = request.POST.get('commentId')
	replyId = 'reply'+str(uuid.uuid4().hex)
	repliedBy = request.POST.get('repliedBy')
	repliedOn = request.POST.get('repliedOn')
	reply = request.POST.get('reply')
	user = userRegistration.objects.get(userId=repliedBy)
	
	Replies(postId=postId,commentId=commentId,replyId=replyId,repliedBy=repliedBy,repliedOn=repliedOn,reply=reply,
	userInfo=user).save()
	if repliedBy != repliedOn:
		notify = str(user) + ' Replied to your Comment'
		Notifications(postId=postId,notificationType='reply',fullName=str(user),sender=repliedBy,receiver=repliedOn,
		notification=notify,viewed=False).save()
	return JsonResponse({'Success':'Done'})

@csrf_exempt
def login(request):
	if request.method == 'POST':
		email = request.POST.get("login_Email")
		password = request.POST.get("password")
		loginValidate = userRegistration.objects.get(emailAddress=email)
		encryptPass = loginValidate.password

		if check_password(password,encryptPass) == True:
			request.session['user'] = str(loginValidate.userId)
			request.session['name'] = str(loginValidate.firstName) + ' ' + str(loginValidate.lastName)
			# request.session['pic'] = str(loginValidate.profilePic)
			return HttpResponseRedirect('/')
			
		else:
			# messages.warning(request,'Please Check Your Email and Password.!!')
			return render(request,'index.html')
	else:
		if request.session.has_key('user'):
			return HttpResponseRedirect('/')
		elif request.session.keys():
			return HttpResponseRedirect('/')
		else:
			return render(request,'index.html')
		
def notifications(request):
	# IT IS INCOMPLETE ONLY DIPLAYS FRIEND REQUESTS AND ACCEPT NOTIFICATIONS
	fRequests = Friend_Requests.objects.filter(receiver=request.session['user']).order_by('-date')
	picsList = []
	for Id in fRequests:
		senderPic = userRegistration.objects.filter(userId=Id.sender)
		for pic in senderPic:
			picUrl = pic.profilePic
			picsList.append(picUrl.url)
	
	notification = Notifications.objects.filter(receiver=request.session['user']).order_by('-date')
	picsList1 = []
	uname = ''   # IF USER HAS NO NOTIFICATION
	for Id in notification:
		senderDetail = userRegistration.objects.filter(userId=Id.sender)
		for detail in senderDetail:
			
			uname = detail.userName
			picUrl = detail.profilePic
			picsList1.append(picUrl.url)
	
	params = {'request':zip(fRequests,picsList),'notification':zip(notification,picsList1),'UserName':uname,'userProfile':request.session['user']}
	return render(request,'Notifications.html',params)

def album(request):
	if request.session.has_key('user'):
		photos = UserPost.objects.filter(userId=request.session['user'])
		myGallery = createAlbum.objects.filter(userId=request.session['user'])
		code = str(request.session['user'] + "profile").encode('utf-8')
		code = code.hex()
		profileData = AlbumImageData.objects.filter(albumId = code)
		# profiledataList = []
		# for item in profileData:
		# 	profiledataList.append(item.media.url)
		code = str(request.session['user'] + "cover").encode('utf-8')
		code = code.hex()
		coverData = AlbumImageData.objects.filter(albumId = code)
		# coverdataList = []
		# for item in coverData:
		# 	profiledataList.append(item.media.url)
		print(myGallery)
		print("photos = ",photos)
		

		params = {'photos':photos,'myGallery':myGallery,'profileData':profileData,'coverData':coverData}
		return render(request,'Album.html',params)
	else:
		return HttpResponseRedirect('/')


def searchProfile(request):
	profile = request.POST.get('profile')
	username = userRegistration.objects.get(userId=profile).userName
	return HttpResponseRedirect('/profile/'+username+'/')

def profile(request,user):
	ActiveUser = userRegistration.objects.get(userId=request.session['user'])
	ActiveUserName = ActiveUser.firstName
	ActiveUserPic = ActiveUser.profilePic

	profileId = user
	profileDetail = userRegistration.objects.get(userId=user)
	userPic = profileDetail.profilePic

	if Friend_Requests.objects.filter(receiver=profileId,sender=request.session['user']):
		isRequest = True
		isRequested = False

	elif Friend_Requests.objects.filter(receiver=request.session['user'],sender=profileId):
		isRequested = True
		isRequest = False
	else:
		isRequest = False
		isRequested = False

	# Extracting friend list of searched user
	friends = AllFriends.objects.get(userId=request.session['user']).Friends
	# Logic for setting button of Add Friend, Unfriend
	if profileId in friends:
		isFriend = True
	else:
		isFriend = False

	# request.session['Watchprofile'] = profileId
	postList = []
	postData = UserPost.objects.filter(userId=user).order_by('-date')
	like=[]; colorPost = []
	for post in postData:
		postList.append(post)
	for post in postList:
		likes = Likes.objects.get(postId=post.postId)
		like.append(len(likes.postLikedBy))
		if request.session['user'] in likes.postLikedBy:
				colorPost.append("rgba(0, 150, 136,1)")
		else:
			colorPost.append("grey")
	 
	
	params = {'data':profileDetail,'currentUserId':request.session['user'],'currentUserFullName':request.session['name'],
		'currentUserPic':userPic.url,'isFriend':isFriend,'isRequest':isRequest,'isRequested':isRequested,'ActiveUserPic':ActiveUserPic,'ActiveUser':ActiveUser.userName
	,'ActiveUserName':ActiveUserName,'postData':zip(postData, like,colorPost)}
	return render(request,'Profile.html',params)

def Userprofile(request):
	return render(request,'Userprofile.html')
	
def userProfileInsert(request):
	if request.method == "POST":
		profileUserId=request.POST.get('ProfileUser')
		profileImage=request.FILES['profileImage']
		loginUser=request.session['user']
		postType = 'profilePhoto'
		Id = uuid.uuid4().hex	
		user = request.session['user']
		PostMessage = ''
	
		if profileUserId==loginUser:
			status=userRegistration.objects.get(userId=loginUser)
			status.profilePic = profileImage
			status.save()
			UserPost.objects.filter(userId=loginUser).update(userPic='/media/'+str(userRegistration.objects.get(userId=loginUser).profilePic))
			GroupChat.objects.filter(sender=loginUser).update(senderPic='/media/'+str(userRegistration.objects.get(userId=loginUser).profilePic))
			
			PostStatus = UserPost(PostType=postType,postId=Id,userId=user,userName=request.session['name'],post=profileImage,
			Message = PostMessage,userPic='/media/'+str(userRegistration.objects.get(userId=user).profilePic)
			).save()
			likes = Likes(postId=Id).save()
			code = str(request.session['user'] + "profile").encode('utf-8')
			img = []
			picId = []
			t = time.localtime()
			current_time = time.strftime("%H:%M:%S", t)	
			current_time =(str(current_time).encode('utf-8')).hex()+code.hex() 
			AlbumImageData(albumId=code.hex(),media=profileImage,picAlbumId=current_time).save()

			return HttpResponseRedirect('/profile/'+loginUser+'/')
		else:
			return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
	else:
		return HttpResponse('<center><h1>you did somethong wrong</h1></center>')

@csrf_exempt
def addfriend(request):
	profileId = request.POST.get('profileId')
	action = request.POST.get('action')
	request.session['friendProfile'] = profileId # USED IN NEXT FUNCTION FOR REQUEST CONFIRM

	if action == 'add':
		sendRequest = Friend_Requests(sender=request.session['user'],receiver=profileId,senderName=request.session['name'])
		sendRequest.save()
		return JsonResponse({"Result":"Successfully Sent"})

	elif action == 'cancel':
		Friend_Requests.objects.filter(sender=request.session['user'],receiver=profileId).delete()
		return JsonResponse({"Result":"Successfully Canceled"})
	
	elif action == 'unfriend':
		friend = AllFriends.objects.get(userId=request.session['user'])
		friend.Friends.remove(profileId)
		friendList = friend.Friends
		AllFriends.objects.filter(userId=request.session['user']).update(userId=request.session['user'],Friends=friendList)
		
		friend1 = AllFriends.objects.get(userId=profileId)
		friend1.Friends.remove(request.session['user'])
		friendList1 = friend1.Friends
		AllFriends.objects.filter(userId=profileId).update(userId=profileId,Friends=friendList1)
# Deleting Notifications 
		Notifications.objects.filter(notificationType='friend',sender=request.session['user'],receiver=profileId).delete()
		Notifications.objects.filter(notificationType='friend',sender=profileId,receiver=request.session['user']).delete()
		return JsonResponse({"Result":"Successfully Removed"})

	elif action == 'confirm':
		return HttpResponseRedirect('/requestConfirm')
	
	elif action == 'changeRequestHTML':
		return JsonResponse({"Result":"Successfully Removed"})

	elif action == 'changeNotificationHTML':
		senderDetail = userRegistration.objects.get(userId=profileId)
		senderName = str(senderDetail.firstName) + ' ' + str(senderDetail.lastName)
		senderPic = str(senderDetail.profilePic.url)
		return JsonResponse({"Result":"Successfully Removed","name":senderName,"pic":senderPic})
	
	elif action == 'changeDashboardHTML':
		return JsonResponse({"Result":"Successfully Removed"})	
	else:
		return JsonResponse({'Result':'Nothing Done'})


@csrf_exempt
def requestConfirm(request):
	if request.method == 'POST':
		friendId = request.POST.get('sender')
		myId = request.session['user']
		action = request.POST.get('action')
	
	else:
		# myId = 'mohammad.danish2694@gmail.com'
		# friendId = 'sj27754@gmail.com'
		# action = 1

		friendId = request.session['friendProfile'] # GETTING VALUE FROM PREVIOUS FUNCTION ADD FRIEND
		myId = request.session['user']
		action = 'add'
	if action == 'add':
		# Friend Add in Logged user List
		myList = AllFriends.objects.get(userId=myId)
		if friendId in myList.Friends: # Checking if friend is already added 
			pass
		else:
			myList.Friends.append(friendId)
			myNewList = myList.Friends
			AllFriends.objects.filter(userId=myId).update(userId=myId,Friends=myNewList)

		# Friend Add in Sender user List
		friendList = AllFriends.objects.get(userId=friendId)
		if myId in friendList.Friends: # Checking if friend is already added 
			pass
		else:
			friendList.Friends.append(myId)
			friendNewList = friendList.Friends
			AllFriends.objects.filter(userId=friendId).update(userId=friendId,Friends=friendNewList)
		

		senderName = Friend_Requests.objects.get(sender=friendId).senderName
	notify = request.session['name'] + ' accepted your Friend Request.'

	Notifications(notificationType='friend',sender=myId,receiver=friendId,fullName=request.session['name'],
	notification=notify,viewed=False).save()

	Friend_Requests.objects.filter(sender=friendId,receiver=myId).delete()
	senderPic = userRegistration.objects.get(userId=myId).profilePic
	return JsonResponse({'Result':'Succuss','name':senderName,'receiver':friendId,'senderPic':senderPic.url})


@csrf_exempt
def search(request):
	if request.method == "POST":
		query = request.POST.get('search').title()
		userProfile = userRegistration.objects.filter(firstName=query) | userRegistration.objects.filter(lastName=query)
		if userProfile:
			params = {'Users':userProfile,'name':request.session['user']}
			return render(request,'Search.html',params)
		else:
			return HttpResponse('No user')
	else:
		return HttpResponse('No POST method')

def PostSubmission(request):
	if request.session.has_key('user'):
		postType = 'post'
		Id = uuid.uuid4().hex	
		user = request.session['user']
		PostMessage = request.POST.get('Post_Title','DefaultValue')
		PostMedia = request.FILES.get('MediaFile')
	
		PostStatus = UserPost(PostType=postType,postId=Id,userId=user,userName=request.session['name'],post=PostMedia,
		Message = PostMessage,userPic='/media/'+str(userRegistration.objects.get(userId=user).profilePic)
		).save()
		tagging = TaggedPeople(taggedId=request.session['name']+Id,postId=Id).save()
		likes = Likes(postId=Id).save()
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')
	# return render(request,'DashBoard.Html',{"flag":"Your post has uploaded"})

def logout(request):
	if request.session.has_key('user'):
		del request.session['user']
		return HttpResponseRedirect('/')
	else:
		#messages.warning(request,'You are already logout. Please login...')
		return render(request,'index.html')

def test(request):
	# del request.session['user']
	#Likes(postId = 'cd2d8468aa37496899616e746f30be4b').save()
	myId = 'shubham31'
	friendId = 'danishcool'
	AllFriends(userId=myId).save()
	AllFriends(userId=friendId).save()
	return render(request,'test.html')

def userCoverInsert(request):
	if request.method == "POST":
		profileUserId = request.POST.get('coverUser','DefaultValue')
		coverImage = request.FILES['coverImage']
		loginUser = request.session['user']
		postType = 'coverPhoto'
		Id = uuid.uuid4().hex	
		user = request.session['user']
		PostMessage = ''
		if profileUserId==loginUser:
			status = userRegistration.objects.get(userId=loginUser)
			status.coverPic = coverImage
			status.save()
			
			PostStatus = UserPost(PostType=postType,postId=Id,userId=user,userName=request.session['name'],post=coverImage,
			Message = PostMessage,userPic='/media/'+str(userRegistration.objects.get(userId=user).profilePic)
			).save()
			likes = Likes(postId=Id).save()
			Photos(Album='Cover Photos',PhotoID=request.session['user'],Image=coverImage).save()
			code = str(request.session['user'] + "cover").encode('utf-8')
			img = []
			picId = []
			t = time.localtime()
			current_time = time.strftime("%H:%M:%S", t)	
			current_time =(str(current_time).encode('utf-8')).hex()+code.hex() 

			AlbumImageData(albumId=code.hex(),media=coverImage,picAlbumId=current_time).save()
			return HttpResponseRedirect('/profile/'+loginUser+'/')
		else:
			return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
	else:
		return HttpResponse('<center><h1>you did somethong wrong</h1></center>')

#Friend Page
@csrf_exempt
def friendSearch(request):
	return render(request,'Friends.html')

@csrf_exempt
def outgoingRequest(request):
	if request.method == "POST":
		liveResult = Friend_Requests.objects.filter(sender=request.session['user'])
		reciverId=[]
		
		for e in liveResult:
			reciverId.append(e.receiver)
		return JsonResponse({"reciverId":reciverId})

@csrf_exempt
def incomingRequest(request):
	if request.method == "POST":
		liveResult = Friend_Requests.objects.filter(receiver=request.session['user'])
		senderName = []
		senderId = []
		
		for e in liveResult:
			senderName.append(e.senderName)
			senderId.append(e.sender)
		
		return JsonResponse({"senderName":senderName,"senderId":senderId})

@csrf_exempt
def liveSearchProcess(request):
	if request.method == "POST":
		name = request.POST.get('search','DefaultValue')
		liveResult = userRegistration.objects.filter(Q(firstName__icontains=name) | Q(lastName__icontains=name))
		name = []
		pic = []
		uId = []
		uname = []
		for e in liveResult:
			fullName = e.firstName+ ' ' +e.lastName
			name.append(fullName)
			uId.append(e.userId)
			pic.append(e.profilePic.url)
			uname.append(e.userName)

		return JsonResponse({"Username":name,"Id":uId,"picture":pic,"uname":uname})

@csrf_exempt
def userIntroInsert(request):
	if request.method == "POST":
		v1 = request.session['Watchprofile']
		v2 = request.session['user']
		if  v1 == v2:
			quote = request.POST.get('quote','DefaultValue')
			dOB = request.POST.get('dOB','DefaultValue')
			gender = request.POST.get('gender','DefaultValue')
			if(gender == "Gender"):
				gender = ""
			mobileNumber = request.POST.get('mobileNumber','DefaultValue')
			countryName = request.POST.get('countryName','DefaultValue')
			cityName = request.POST.get('cityName','DefaultValue')
			currentEducation = request.POST.get('currentEducation','DefaultValue')
			educationStartYear = request.POST.get('educationStartYear','DefaultValue')
			educationEndYear = request.POST.get('educationEndYear','DefaultValue')
			companyName = request.POST.get('companyName','DefaultValue')
			companyPosition = request.POST.get('companyPosition','DefaultValue')
			companyCity = request.POST.get('companyCity','DefaultValue')
			companyDescription = request.POST.get('companyDescription','DefaultValue')
			status=userRegistration.objects.filter(userId=v2).update(quote=quote,dOB=dOB,gender=gender,mobile=mobileNumber,countryName=countryName,
				cityName=cityName,currentEducation=currentEducation,educationStartYear=educationStartYear,educationEndYear=educationEndYear,companyName=companyName,companyPosition=companyPosition,companyCity=companyCity,companyDescription=companyDescription)

			return HttpResponse("<h1>Done</h1>")

#Shows login user list of all friends
def myfriends(request):
	friends = AllFriends.objects.get(userId=request.session['user']).Friends
	friendList = []
	for friend in friends:
		friendData = userRegistration.objects.filter(userId=friend)
		friendList.append(friendData)
	params = {'friendList':friendList}
	return render(request,'MyFriends.html',params)

@csrf_exempt
def myFriendsProcess(request):
	if request.method == 'POST':
		sortBY=request.POST.get("sortBy",'DefaultValue')
		lt = []
		friendList = AllFriends.objects.get(userId=request.session['user']).Friends
		for name in friendList:
			lt.append(userRegistration.objects.get(userId=name))
		firstName=[]
		lastName=[]
		prfilePic=[]
		Id=[]
		quote=[]
		sortList = []
		if sortBY=="firstName":
			for j in lt:
				sortList.append(j)
				sortList.sort(key=lambda x: x.firstName)
		else :
			for j in lt:
				sortList.append(j)
				sortList.sort(key=lambda x: x.lastName)
		for j in sortList:
			firstName.append(j.firstName)
			lastName.append(j.lastName)
			prfilePic.append(j.profilePic.url)
			Id.append(j.userId)
			quote.append(j.quote)
		return JsonResponse({"FName":firstName,"lName":lastName,"pPic":prfilePic,"EmailId":Id,"quote":quote})
	else :
		return HttpResponse("<center><h1>You did something wrong</h1></center>")

#Forget Password
def forgetPassword(request):
	return render(request,'forgetPassword.html')

@csrf_exempt
def forgetPasswordOTP(request):
	Email=request.POST.get("Email",'DefaultValue')
	if request.method == "POST" and Email!="DefaultValue" and Email!="":
		RandomValue=random.randint(1001,99999)
		RandomValue="LetsChat"+str(RandomValue)
		print(RandomValue)
		message=f"Your Email Address  {Email}  Your OTP is {RandomValue} for Forget Password Do not share your password to anyone."
		send_mail(
	    	'LetsChat',
	    	message,
	    	settings.EMAIL_HOST_USER,
	    	[Email],
	    	fail_silently=False)
		request.session["forgetOtp"]=RandomValue
		return JsonResponse({'Result':"Successfully"})
	else:
		return JsonResponse({'Result':"UnSuccessfully"})

#Forget Password Process
@csrf_exempt
def forgetPasswordProcess(request):
	if request.method == "POST":
		OTP = request.POST.get('Otp','DefaultValue')
		Email = request.POST.get('userName','DefaultValue')
		if(request.session["forgetOtp"]==OTP):
			print("OTP MATCH")
			return render(request,'forgetPasswordProcess.html',{"Email":Email})
		else:
			return HttpResponse("<center><h1>Your Password is Incorrect<h1><center>")
	return HttpResponseRedirect("/")

@csrf_exempt
def changeForgetPasword(request):
	if request.method == "POST":
		Email = request.POST.get('Email','DefaultValue')
		fPassword = request.POST.get('fPassword','DefaultValue')
		sPassword = request.POST.get('sPassword','DefaultValue')
		if fPassword == sPassword:
			del request.session['forgetOtp']
			userRegistration.objects.filter(emailAddress=Email).update(password=make_password(fPassword))
			return JsonResponse({"Status":"Successfully"})
		else:
			return JsonResponse({"Status":"UnSuccessfully"})
	else:
		return HttpResponseRedirect("/")

def friends(request):
	friendList = []; MessageList = []
	friends = AllFriends.objects.get(userId=request.session['user']).Friends
	for friend in friends:
		friendData = userRegistration.objects.filter(userId=friend)
		unreadMessage = Messages.objects.filter(is_read=False,sender=friend,receiver=request.session['user']).count()
		MessageList.append(unreadMessage)
		# print(unreadMessage)
		friendList.append(friendData)
		# print(friendData)
	friendMessageList = zip(friendList,MessageList)
	GroupsList = []
	groups = userRegistration.objects.get(userId=request.session['user']).Groups
	for group in groups:
		allGroups = Groups.objects.filter(groupId=group)
		GroupsList.append(allGroups)
	# MyclubUser.objects.in_bulk([1, 3, 7])
	return friendMessageList,GroupsList

def messages(request):
	if request.session.has_key('user'):
		friendList,GroupsList = friends(request)
		myData = userRegistration.objects.get(userId=request.session['user'])
		params = {'friendList':friendList,'myData':myData,'groups':GroupsList}
		return render(request,'chat.html',params)

def inbox(request,user):
	myId = request.session['user']
	friendId = user
	is_Inbox = Inbox.objects.filter(Users=[myId,friendId]) | Inbox.objects.filter(Users=[friendId,myId])
	seenMessage(request,user,request.session['user'])
	if is_Inbox:
		for msg in is_Inbox:
			inboxId = msg.inboxId
			messageInbox = msg.id
		allMessages = Messages.objects.filter(Inbox=messageInbox)
		unread = allMessages.filter(is_read=False,sender=user).count()
	else:
		inboxId = uuid.uuid4().hex
		Inbox(inboxId=inboxId,Users=[myId,friendId]).save()
		allMessages = ''
	myData = userRegistration.objects.get(userId=request.session['user'])
	friendData = userRegistration.objects.get(userId = user)
	friendList,groups = friends(request)

	return render(request,'chat.html',{"inbox":True,"friendData":friendData,'inboxId':inboxId,
		'myData':myData,'allMessages':allMessages,'friendList':friendList,'groups':groups})

def groups(request,group):
	myId = request.session['user']
	allMessages = GroupChat.objects.filter(groupId=group)
	
	myData = userRegistration.objects.get(userId=request.session['user'])
	friendList,groups = friends(request)
	groupInfo = Groups.objects.get(groupId=group)
	return render(request,'chat.html',{"groupChat":True,'groupId':group,'myData':myData,
	'friendList':friendList,'groups':groups,'allMessages':allMessages,'groupInfo':groupInfo})

@csrf_exempt
def saveMessage(request):
	inboxId = request.POST.get('inboxId')
	messageid = 'privatemessage'+str(uuid.uuid4())
	sender = request.POST.get('sender')
	receiver = request.POST.get('receiver')
	message = request.POST.get('Message')
	Messages(Inbox=Inbox.objects.get(inboxId=inboxId),MessageID=messageid,sender=sender,
	receiver=receiver,is_read=False,Message=message).save()
	return JsonResponse({'Result':'Success'})

@csrf_exempt
def groupMessage_Save(request):
	groupId = request.POST.get('groupId')
	sender = request.POST.get('sender')
	message = request.POST.get('Message')
	messageid = 'groupmessage'+str(uuid.uuid4())

	senderDetail = userRegistration.objects.get(userId=sender)
	GroupChat(groupId=groupId,messageID=messageid,sender=sender,is_read=False,Message=message,
	senderName=senderDetail.firstName+' '+senderDetail.lastName,senderPic='/media/'+str(senderDetail.profilePic),
	).save()
	return JsonResponse({'Result':'Success'})

@csrf_exempt
def seenMessage(request,sender,receiver):
	Messages.objects.filter(is_read=False,sender=sender,receiver=receiver).update(is_read=True)
	return JsonResponse({'Result':'Success'})

def reportGetPost(request):
	if request.method == "POST":
		pic = request.POST.get('pic',"defaultValue")
		msg = request.POST.get('msg',"defaultValue")
		postId = request.POST.get('postId',"defaultValue")
		if(pic=="defaultValue"):
			pic=False
		param={"pic":pic,"msg":msg,"postId":postId}
		return render(request,'report.html',param)

@csrf_exempt
def reportSubmission(request):
	if request.method == "POST":
		postId = request.POST.get("postID")
		reportTitle = request.POST.get("reportTitle")
		Report(postId=postId,reportTitle=reportTitle).save()
		return JsonResponse({"status":True})

@csrf_exempt
def taggedSearchFriends(request):
	if request.method == "POST":
		if request.POST.get('action') == 'friend':
			friend = request.POST.get('id')
			friends = AllFriends.objects.get(userId=friend).Friends	
			username = []
			pic = []
			userId = []
			for i in friends:
				userId.append(i)
				friendName = userRegistration.objects.get(userId=i)
				username.append(friendName.firstName + ' ' +friendName.lastName)
				pic.append(friendName.profilePic.url)
				
			return JsonResponse({"name":username,"pic":pic,'userId':userId})
		else:
			friends = AllFriends.objects.get(userId=request.session['user']).Friends
			pid = request.POST.get('postId')
			tagPerson = TaggedPeople.objects.filter(postId=pid)
			for person in tagPerson:
				tagPersonList = person.taggedPersons
			else:
				tagPersonList = []
			taggedUsers = [userRegistration.objects.filter(userId=user) for user in tagPersonList]
			allName = []
			for userQuerySet in taggedUsers:
				for user in userQuerySet:
					fname = user.firstName
					lname = user.lastName
					allName.append(fname+' '+lname)
			username = []
			pic = []
			userId = []
			for i in friends:
				userId.append(i)
				friendName = userRegistration.objects.get(userId=i)
				username.append(friendName.firstName + ' ' +friendName.lastName)
				pic.append(friendName.profilePic.url)
				
			return JsonResponse({"name":username,"pic":pic,'userId':userId,'allTaggedList':tagPersonList,'allName':allName})
		

@csrf_exempt
def tagSubmissionForm(request):
	tagPerson = request.POST.get('tagPerson')
	postId = request.POST.get('postId')
	tagPersonList = list(tagPerson.split(","))
	taggedBy = request.session['user']
	taggedByPerson = userRegistration.objects.get(userId=taggedBy)
	notify = "You and "  +str(int(len(tagPersonList))-2)+ " others are tagged in " + str(taggedByPerson)+ "\'s post"
	TaggedPeople.objects.filter(postId=postId).update(taggedPersons=tagPerson[1:])
	print(notify)
	for taggedUser in tagPersonList:
		if taggedUser == '':
			pass
		else:
			name = userRegistration.objects.get(userId=str(taggedUser))
			Notifications(postId=postId,notificationType='tag',fullName=str(taggedByPerson),sender=taggedBy,receiver=taggedUser,
			notification=notify,viewed=False).save()
	return HttpResponse(tagPerson) 

@csrf_exempt
def showAllTagPerson(request):
	postId = request.POST.get('postId')
	qry = TaggedPeople.objects.get(postId = postId).taggedPersons
	Fname =[]
	Lname =[] 
	for person in qry:
		qry1=userRegistration.objects.get(userName=person)
		Fname.append(qry1.firstName)
		Lname.append(qry1.lastName)

	return JsonResponse({"status":"successfully","userName":qry,"FName":Fname,"LName":Lname})

@csrf_exempt
def CommentShow(request):
	ParentcommentByList = []
	ParentComment = []
	parentcommentName = []
	ParentcommentId = []
	ParentcommentUserpic = []
	childComment=[]
	childCommentBy = []
	childcommentId=[]
	childcommentName=[]
	childcommentUserpic = []
	comments = Comments.objects.filter(postId=request.POST.get("postId"))
	for comment in comments:
		ParentcommentByList.append(comment.commentedBy)
		ParentComment.append(comment.comment)
		ParentcommentId.append(comment.commentId)
		parentcommentName.append(comment.userInfo.firstName +' '+ comment.userInfo.lastName)
		ParentcommentUserpic.append(comment.userInfo.profilePic.url)
		childComments = Replies.objects.filter(commentId=comment.commentId)
		for child in childComments:
			childCommentBy.append(child.repliedBy)
			childComment.append(child.reply)
			childcommentId.append(child.commentId)
			childcommentName.append(child.userInfo.firstName +' '+ child.userInfo.lastName)
			childcommentUserpic.append(child.userInfo.profilePic.url)
	return JsonResponse({"ParentcommentByList":ParentcommentByList,"ParentComment":ParentComment,"ParentcommentId":ParentcommentId,"parentcommentName":
	parentcommentName,"childcommentId":childcommentId,"ChildComment":childComment,"childcommentName":childcommentName,
	"childCommentBy":childCommentBy,"ParentcommentUserpic":ParentcommentUserpic,"childcommentUserpic":childcommentUserpic})

@csrf_exempt
def createAlbumDetails(request):
	if request.method == "POST":
		name = request.POST.get('name',"defaultValue")
		
		result = createAlbum.objects.filter(Q(userId=request.session['user']) & Q(albumName=name))
		status = ""
		# code = str(request.session['user'] + name).encode('utf-8')
		# print(code.hex())
		if result.exists():
			status = "allready"

			album_Id =""
			for i in result:
				album_Id=i.albumId
				break
			imgList = AlbumImageData.objects.filter(albumId=album_Id)
			img = []
			picId = []
			for image in imgList:
				img.append(image.media.url)
				picId.append(image.picAlbumId)

			return JsonResponse({"status":status,"media":img,"picId":picId})
		else:
			description = request.POST.get('description',"defaultValue")
			accessibility = request.POST.get('accessibility',"defaultValue")
			code = str(request.session['user'] + name).encode('utf-8')
			
			createAlbum(userId=request.session['user'],albumName=name,albumDescription=description,albumAccessibility=accessibility,albumId=code.hex()).save();
			status = "created"
			return JsonResponse({"status":status})

@csrf_exempt
def UploadAlbumImage(request):
	print("Hellllllllllllloooooo")
	if request.method == "POST":
		image = request.FILES.get('theFile')
		Reponame = request.POST.get('repoName',"defaultValue")
		code = str(request.session['user'] + Reponame).encode('utf-8')
		img = []
		picId = []
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)	
		current_time =(str(current_time).encode('utf-8')).hex()+code.hex() 
			
		AlbumImageData(albumId=code.hex(),media=image,picAlbumId=current_time).save()
		return HttpResponseRedirect("/album/")
		# photos = UserPost.objects.filter(userId=request.session['user'])
		# myGallery = createAlbum.objects.filter(userId=request.session['user'])
		# print(myGallery)
		# print("Donnnnnnnnnnnnnne")
		# params = {'photos':photos,'myGallery':myGallery}
		# return render(request,'Album.html',params)

@csrf_exempt
def deleteAlbumRepo(request):
	if request.method == "POST":
		title = request.POST.get('title',"defaultValue")
		code = str(request.session['user'] + title).encode('utf-8')
		code = code.hex()
		createAlbum.objects.get(albumId = code).delete()
		AlbumImageData.objects.filter(albumId=code).delete()
		return JsonResponse({"Status":"successfully"})

@csrf_exempt
def UpdateAlbumRepo(request):
	if request.method == "POST":
		name = request.POST.get('name',"defaultValue")
		description = request.POST.get('description',"defaultValue")
		accessibility = request.POST.get('accessibility',"defaultValue")
		code = str(request.session['user'] + name).encode('utf-8')
		query=createAlbum.objects.get(albumId = code.hex())
		query.albumDescription = description
		query.albumAccessibility=accessibility
		query.save()
		return JsonResponse({"Status":"successfully"})

@csrf_exempt
def deleteAlbumPicture(request):
	if request.method == "POST":
		name = request.POST.get('pic',"defaultValue")
		title = request.POST.get('title',"defaultValue")
		code = str(request.session['user'] + title).encode('utf-8')
		code = code.hex()
		AlbumImageData.objects.filter(picAlbumId=name).delete()
		return JsonResponse({"Status":"successfully"})
		
def showPost(request,postid):
	postData = UserPost.objects.get(postId=postid)
	allComments = Comments.objects.filter(postId=postid)
	allLikes = Likes.objects.get(postId=postid).postLikedBy
	totalLikes = len(allLikes)
	if request.session['user'] in allLikes:
		colorPost = "rgba(0, 150, 136,1)"
	else:
		colorPost = "grey"

	params = {'postData':postData,'allComments':allComments,
	'totalLikes':totalLikes,'colorPost':colorPost,'loggedUser':request.session['user']}
	return render(request,'showPost.html',params)

@csrf_exempt
def deshboarDeletePost(request):
	if request.method == "POST":
		postId = request.POST.get("postId")
		UserPost.objects.get(postId = postId).delete()
		return JsonResponse({"status":"success"})