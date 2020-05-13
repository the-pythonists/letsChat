from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse
import random
from django.core.mail import send_mail
from django.core.mail import send_mail
from .models import userRegistration,Friend_Requests,UserPost,Likes,AllFriends
from django.contrib.auth.hashers import make_password,check_password
import datetime
import uuid,json
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Q
from django.core import serializers

def index(request):
	if request.session.has_key('user'):
		userInfo = userRegistration.objects.get(userId=request.session['user'])
		userData = UserPost.objects.filter(userId=request.session['user']).order_by('-date') # '-' for descending order
		
		friends = AllFriends.objects.get(userId=request.session['user']).Friends
		# print(friends)
		postList = [userData]
		for name in friends:
			friendsPosts = UserPost.objects.filter(userId=name).order_by('-date')
			postList.append(friendsPosts)
			print(friendsPosts)
		params = {'userInfo':userInfo,'userData':postList}
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
			if userRegistration.objects.filter(userId=email):
				return render(request,'CreateAccount.html',{'message':'Account Already Present with Given Email'})
			elif userRegistration.objects.filter(mobile=mobile):
				return render(request,'CreateAccount.html',{'message':'Account Already Present with Given Mobile Number'}) 
			else:
				accountSave = userRegistration(userId=email, firstName=fName, lastName=lName, userName=username, 
				mobile=mobile,emailAddress = email, password = make_password(pwd))
				accountSave.save()
				AllFriends(userId=email).save()
				return HttpResponseRedirect('/')
			# return HttpResponse('Account Created')
			
		else:
			return HttpResponse("NotSame")
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
	# print(Email)
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

def myfriends(request):
	lt = []
	friendList = AllFriends.objects.get(userId=request.session['user']).Friends
	for name in friendList:
		lt.append(userRegistration.objects.filter(userId=name))
		
	params = {'myFriends':lt}
	return render(request,'MyFriends.html',params)

@csrf_exempt
def postlike(request):
	Id = request.POST.get('postID')
	likes = Likes.objects.get(postId=Id)
	postLikedBy = request.session['user']
	postLikedOf = "To be Written"
	print(Id)
	# return HttpResponse(likes.postLikes)
	return JsonResponse({'Result':likes.postLikes})

def login(request):
	if request.method == 'POST':
		email = request.POST.get("login_Email")
		password = request.POST.get("password")
		loginValidate = userRegistration.objects.get(userId=email)
		encryptPass = loginValidate.password

		if check_password(password,encryptPass) == True:
			request.session['user'] = str(loginValidate.userId)
			name = request.session['user']
			request.session['name'] = str(loginValidate.firstName) + ' ' + str(loginValidate.lastName)
			request.session['pic'] = str(loginValidate.profilePic)
			return HttpResponseRedirect('/')
			
		else:
			return HttpResponse('Error')
			
			# return render(request,'index.html')
	else:
		if request.session.has_key('user'):
			return HttpResponseRedirect('/')
		else:
			return render(request,'index.html')
		
def notifications(request):
	fRequests = Friend_Requests.objects.filter(receiverId=request.session['user'])
	# for i in fRequests:
		
	params = {'request':fRequests}
	return render(request,'Notifications.html',params)

def album(request):
	if request.session.has_key('user'):
		photos = UserPost.objects.filter(userId=request.session['user'])
		params = {'photos':photos}
		return render(request,'Album.html',params)
	else:
		return HttpResponseRedirect('/')

def profile(request):
	# Checking if profile is of other person or self profile
	if request.method == 'POST':
		profileId = request.POST.get('profile')
	else:
		profileId = request.session['user']
	profileDetail = userRegistration.objects.filter(userId=profileId)
	
	# checking if searched person is req receiver or sender
	if Friend_Requests.objects.filter(receiverId=profileId,senderId=request.session['user']):
		isRequest = True
		isRequested = False

	elif Friend_Requests.objects.filter(receiverId=request.session['user'],senderId=profileId):
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
		'isFriend':isFriend,'isRequest':isRequest,'isRequested':isRequested}
	return render(request,'Profile1.html',params)

def Userprofile(request):
	return render(request,'Profile1.html')
	
def userProfileInsert(request):
	if request.method == "POST":
		profileUserId=request.POST.get('ProfileUser','DefaultValue')
		profileImage=request.FILES['profileImage']
		loginUser=request.session['user']
		if profileUserId==loginUser:
			status=userRegistration.objects.filter(userId=loginUser).update(profilePic=profileImage)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
	else:
		return HttpResponse('<center><h1>you did somethong wrong</h1></center>')

def friendSearch(request):
	return render(request,'Friends.html')

@csrf_exempt
def outgoingRequest(request):
	if request.method == "POST":
		liveResult = Friend_Requests.objects.filter(senderId=request.session['user'])
		reciverId=[]
		
		for e in liveResult:
			reciverId.append(e.receiverId)
		return JsonResponse({"reciverId":reciverId})


@csrf_exempt
def incomingRequest(request):
	if request.method == "POST":
		liveResult = Friend_Requests.objects.filter(receiverId=request.session['user'])
		senderName=[]
		senderId=[]
		
		for e in liveResult:
			senderName.append(e.senderName)
			senderId.append(e.senderId)
		return JsonResponse({"senderName":senderName,"senderId":senderId})
		

@csrf_exempt
def liveSearchProcess(request):
	from django.core import serializers
	from django.http import JsonResponse
	if request.method == "POST":
		name=request.POST.get('search','DefaultValue')
		liveResult = userRegistration.objects.filter(Q(firstName__icontains=name) | Q(lastName__icontains=name))
		print(liveResult)
		name=[]
		pic=[]
		uId=[]
		for e in liveResult:
			fullName = e.firstName+ ' ' +e.lastName
			name.append(fullName)
			uId.append(e.userId)
			pic.append(e.profilePic.url)
		print(pic)
		return JsonResponse({"Username":name,"Id":uId,"picture":pic})
		


@csrf_exempt
def addfriend(request):
	profileId = request.POST.get('profileId')
	action = request.POST.get('action')
	request.session['friendProfile'] = profileId

	if action == 'add':
		sendRequest = Friend_Requests(senderId=request.session['user'],receiverId=profileId,senderName=request.session['name'])
		sendRequest.save()
		return JsonResponse({"Result":"Successfully Sent"})

	elif action == 'cancel':
		Friend_Requests.objects.filter(senderId=request.session['user'],receiverId=profileId).delete()
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

		return JsonResponse({"Result":"Successfully Removed"})
	
	elif action == 'confirm':
		print('here')
		return HttpResponseRedirect('/requestConfirm')
		# return JsonResponse({'Result':'Successfully Confirmed'})
	else:
		return JsonResponse({'Result':'Nothing Done'})

@csrf_exempt
def requestConfirm(request):
	if request.method == 'POST':
		friendId = request.POST.get('sender')
		myId = request.session['user']
		action = request.POST.get('action')
	# myId = 'abc@gmail.com'
	# friendId = 'test@gmail.com'
	# action = 1
	else:
		print('called')
		friendId = request.session['friendProfile']
		myId = request.session['user']
		action = 'add'

	if action == 'add':
	
		myList = AllFriends.objects.get(userId=myId)
		myList.Friends.append(friendId)
		myNewList = myList.Friends
		AllFriends.objects.filter(userId=myId).update(userId=myId,Friends=myNewList)
	
		friendList = AllFriends.objects.get(userId=friendId)
		friendList.Friends.append(myId)
		friendNewList = friendList.Friends
		AllFriends.objects.filter(userId=friendId).update(userId=friendId,Friends=friendNewList)
		


	Friend_Requests.objects.filter(senderId=friendId,receiverId=myId).delete()

	return JsonResponse({'Result':'Succuss'})

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
	
		PostStatus=UserPost(postId=Id,userId=user,userName=request.session['name'],post=PostMedia,Message=PostMessage).save()
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
		return HttpResponseRedirect('/')

def userCoverInsert(request):
	if request.method == "POST":
		profileUserId=request.POST.get('coverUser','DefaultValue')
		coverImage=request.FILES['coverImage']
		loginUser=request.session['user']
		if profileUserId==loginUser:
			status=userRegistration.objects.filter(userId=loginUser).update(coverPic=coverImage)
			return HttpResponseRedirect('/')
		else:
			return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
	else:
		return HttpResponse('<center><h1>you did somethong wrong</h1></center>')