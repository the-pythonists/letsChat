from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse
import random
from django.core.mail import send_mail
from .models import userRegistration,Friend_Requests,UserPost,Likes,AllFriends,Notifications,Story,Album,Photos
from django.contrib.auth.hashers import make_password,check_password
import datetime
import uuid
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q
from django.core import serializers
from itertools import chain

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
			for item in friends:
				t = UserPost.objects.filter(userId=item).order_by('-date')
				u = Photos.objects.filter(Album='Profile Pictures',PhotoID=item).order_by('-date')
				print(item)
				for i in t:
					yield i

		AllPost = chain(UserAllPost(), FriendPosts())
		for item in AllPost:
			postList.append(item)
		postList.sort(key=lambda x: x.date,reverse = True)      #for reversed :  (reverse = True)
		like=[]; colorPost = []
		for i in postList:
			likes = Likes.objects.get(postId=i.postId)
			like.append(len(likes.postLikedBy))
			if request.session['user'] in likes.postLikedBy:
				colorPost.append("rgba(0, 150, 136,1)")
			else:
				colorPost.append("grey")
		date_now = datetime.datetime.now()
		params = {'userInfo':userInfo,'userData':zip(postList, like,colorPost),"date_now":date_now}
		return render(request,'DashBoard.html',params)
	else:
		return render(request,'index.html')

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
				accountSave = userRegistration(userId=username, firstName=fName, lastName=lName, userName=username, 
				mobile=mobile,emailAddress = email, password = make_password(pwd))
				accountSave.save()
				# Creating Blank Frined List
				AllFriends(userId=username).save()
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
	Email=request.POST.get('Email','DefaultValue')
	RandomValue=random.randint(1001,99999)
	RandomValue="LetsChat"+str(RandomValue)
	print(RandomValue)
	message=f"Your Email Address  {Email}  Your OTP is {RandomValue} Do not share your password to anyone."
	send_mail(
    	'LetsChat',
    	message,
    	settings.EMAIL_HOST_USER,
    	[Email],
    	fail_silently=False)
	request.session["Otp"]=RandomValue
	# request.session["Email"]=Email
	return JsonResponse({'Result':"Successfully"})

def story(request):
	
	if request.method == 'POST':
		userStory = request.FILES['story']

		Story(userId=request.session['user'],media=userStory).save()
		return HttpResponseRedirect('/')
	else:
		return render(request,'Story.html')

@csrf_exempt
def storydelete(request):
	from datetime import timedelta 
	tm1 = (datetime.datetime.now() - timedelta(minutes=5)   )
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
	Id = request.POST.get('postID')
	likes = Likes.objects.get(postId=Id)
	isLiked=True
	count=0
	for i in (likes.postLikedBy):
		count=count+1
		if(i==request.session['user']):
			isLiked=False
			
	if isLiked:
		if likes.postId==Id:
			postLikedBy = request.session['user']
			postLikedOf = "To be Written"
			likes.postLikedBy.append(request.session['user'])
			likeList=[]
			likeList=likes.postLikedBy
			Likes.objects.filter(postId=Id).update(postLikedBy=likeList)
			return JsonResponse({'Result':(count+1),'color':"rgba(0, 150, 136,1)"})
	else:
		if likes.postId==Id:
			postLikedBy = request.session['user']
			postLikedOf = "To be Written"
			likes.postLikedBy.remove(request.session['user'])
			likeList=[]
			likeList=likes.postLikedBy
			Likes.objects.filter(postId=Id).update(postLikedBy=likeList)
			return JsonResponse({'Result':(count-1),'color':"grey"})

@csrf_exempt
def automaticallylike(request):
	userInfo = userRegistration.objects.get(userId=request.session['user'])
	userData = UserPost.objects.filter(userId=request.session['user']).order_by('-date') # '-' for descending order
	friends = AllFriends.objects.get(userId=request.session['user']).Friends
	postList = []
	def UserAllPost():
		for item in userData:
			yield item
	def FriendPosts():
		for item in friends:
			t = UserPost.objects.filter(userId=item)
			for i in t:
				Id = i.postId
				yield i
	FriendPosts()
	AllPost = chain(UserAllPost(), FriendPosts())
	postsId = []
	for item in AllPost:
		postsId.append(item.postId)
		postList.append(item)
	postList.sort(key=lambda x: x.date,reverse = True)      #for reversed :  (reverse = True)
		
	like=[]
	for i in postsId:
		likes = Likes.objects.get(postId=i)
		like.append(len(likes.postLikedBy))
	date_now = datetime.datetime.now()
	params = {'userData':postsId,"date_now":date_now,'like':like}
	return JsonResponse(params)

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
			messages.warning(request,'Please Check Your Email and Password.!!')
			return render(request,'index.html')
	else:
		if request.session.has_key('user'):
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
	
	params = {'request':zip(fRequests,picsList),'notification':zip(notification,picsList1),'UserName':uname}
	return render(request,'Notifications.html',params)


def album(request):
	if request.session.has_key('user'):
		photos = UserPost.objects.filter(userId=request.session['user'])
		profilePhotos = Photos.objects.filter(Album='Profile Pictures',PhotoID=request.session['user'])
		coverPhotos = Photos.objects.filter(Album='Cover Photos',PhotoID=request.session['user'])
		params = {'photos':photos,'profilePhotos':profilePhotos,'coverPhotos':coverPhotos}
		
		if request.method == 'POST':
			name = request.POST.get('album').title()
			if not Album.objects.filter(AlbumID=request.session['user'],Name=name):
				Album(AlbumID=request.session['user'],Name=name).save()
			return render(request,'Album.html',params)
		else:
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
	profileDetail = userRegistration.objects.filter(userId=user)
	
	# checking if searched person is req receiver or sender
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

	request.session['Watchprofile'] = profileId
	params = {'user':profileDetail,'currentUserId':request.session['user'],
		'isFriend':isFriend,'isRequest':isRequest,'isRequested':isRequested,
		'ActiveUserName':ActiveUserName,'ActiveUserPic':ActiveUserPic,'ActiveUser':ActiveUser.userName}
	return render(request,'Profile.html',params)

def Userprofile(request):
	return render(request,'Userprofile.html')
	
def userProfileInsert(request):
	if request.method == "POST":
		profileUserId=request.POST.get('ProfileUser')
		profileImage=request.FILES['profileImage']
		loginUser=request.session['user']
		if profileUserId==loginUser:
			status=userRegistration.objects.get(userId=loginUser)
			status.profilePic = profileImage
			status.save()
			UserPost.objects.filter(userId=loginUser).update(userPic='/media/'+str(userRegistration.objects.get(userId=loginUser).profilePic))
			if not Album.objects.filter(AlbumID=request.session['user']):
				Album(AlbumID=request.session['user'],Name='Profile Pictures').save()
			
			Photos(Album='Profile Pictures',PhotoID=request.session['user'],Image=profileImage).save()
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

	return JsonResponse({'Result':'Succuss','name':senderName})

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
		Id = uuid.uuid4().hex	
		user = request.session['user']
		PostMessage = request.POST.get('Post_Title','DefaultValue')
		PostMedia = request.FILES.get('MediaFile')
	
		PostStatus=UserPost(postId=Id,userId=user,userName=request.session['name'],post=PostMedia,
		Message=PostMessage,userPic='/media/'+str(userRegistration.objects.get(userId=user).profilePic)
		).save()
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
		messages.warning(request,'You are already logout. Please login...')
		return render(request,'index.html')

def test(request):
	# del request.session['user']
	img = '/media/cover.jpg'
	i = img.url
	return render(request,'MyFriends.html',{'img':''})

def userCoverInsert(request):
	if request.method == "POST":
		profileUserId = request.POST.get('coverUser','DefaultValue')
		coverImage = request.FILES['coverImage']
		loginUser = request.session['user']
		if profileUserId==loginUser:
			status = userRegistration.objects.get(userId=loginUser)
			status.coverPic = coverImage
			status.save()
			if not Album.objects.filter(AlbumID=request.session['user'],Name='Cover Photos'):
				Album(AlbumID=request.session['user'],Name='Cover Photos').save()
			
			Photos(Album='Cover Photos',PhotoID=request.session['user'],Image=coverImage).save()
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
			reciverId.append(e.receiverId)
		return JsonResponse({"reciverId":reciverId})

@csrf_exempt
def incomingRequest(request):
	if request.method == "POST":
		liveResult = Friend_Requests.objects.filter(receiver=request.session['user'])
		senderName = []
		senderId = []
		
		for e in liveResult:
			senderName.append(e.senderName)
			senderId.append(e.senderId)
		
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
	return render(request,'MyFriends.html')


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
	print("okkkkk")
	Email=request.POST.get("Email",'DefaultValue')
	print(request.method)
	if request.method == "POST" and Email!="DefaultValue" and Email!="":
		print("okkkkk")
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
			print("SuccessFully")
			del request.session['forgetOtp']
			userRegistration.objects.filter(emailAddress=Email).update(password=make_password(fPassword))
			print(Email)
			return JsonResponse({"Status":"Successfully"})
		else:
			print("UnSuccessFully")
			return JsonResponse({"Status":"UnSuccessfully"})
	else:
		return HttpResponseRedirect("/")