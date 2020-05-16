from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse
import random
from django.core.mail import send_mail
from django.core.mail import send_mail
from .models import userRegistration,Friend_Requests,UserPost,Likes,AllFriends,Notifications
from django.contrib.auth.hashers import make_password,check_password
import datetime
import uuid,json
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
				for i in t:
					# Id = i.postId
					# print(Id)
					yield i
		# FriendPosts()
		AllPost = chain(UserAllPost(), FriendPosts())
		for item in AllPost:
			postList.append(item)
		# print(postList)
		postList.sort(key=lambda x: x.date,reverse = True) 
		# print(postList)
		
		params = {'userInfo':userInfo,'userData':postList,'date_now':datetime.datetime.now()}
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
				mobile=mobile,emailAddress = email, password = makemake_password(pwd))
				accountSave.save()
				# Creating Blank Frined List
				AllFriends(userId=email).save()
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
	RandomValue="LetsChat"+str(random.randint(1001,99999))
	# print(RandomValue)
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
	fList = []
	friendList = AllFriends.objects.get(userId=request.session['user']).Friends
	for name in friendList:
		fList.append(userRegistration.objects.filter(userId=name))
		
	params = {'myFriends':fList}
	return render(request,'MyFriends.html',params)

@csrf_exempt
def postlike(request):
	# INCOMPLETE AS OF NOW
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
			request.session['pic'] = str(loginValidate.profilePic) # THIS LINE IS CURRENTLY NOT IN USE 
			return HttpResponseRedirect('/')
		else:
			return render(request,'index.html',{'message':'Please Check Your Email and Password'})
	else:
		if request.session.has_key('user'):
			return HttpResponseRedirect('/')
		else:
			return render(request,'index.html')
		
def notifications(request):
	# IT IS INCOMPLETE ONLY DIPLAYS FRIEND REQUESTS
	fRequests = Friend_Requests.objects.filter(receiverId=request.session['user'])
	picsList = []
	for Id in fRequests:
		senderPic = userRegistration.objects.filter(userId=Id.senderId)
		for pic in senderPic:
			picUrl = pic.profilePic
			picsList.append(picUrl.url)
		
	params = {'request':zip(fRequests,picsList)}
	return render(request,'Notifications.html',params)

def album(request):
	if request.session.has_key('user'):
		photos = UserPost.objects.filter(userId=request.session['user'])
		profilePhotos = userRegistration.objects.filter(userId=request.session['user'])
		params = {'photos':photos,'profilePhotos':profilePhotos}
		return render(request,'Album.html',params)
	else:
		return HttpResponseRedirect('/')

def searchProfile(request):
	profile = request.POST.get('profile')
	username = userRegistration.objects.get(userId=profile).userName
	return HttpResponseRedirect('/profile/'+username+'/')

def profile(request,user):
	
	profileId = userRegistration.objects.get(userName=user).userId
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
		profileUserId=request.POST.get('ProfileUser')
		profileImage=request.FILES['profileImage']
		print(profileUserId,profileImage)
		loginUser=request.session['user']
		if profileUserId==loginUser:
			status=userRegistration.objects.get(userId=loginUser)
			status.profilePic = profileImage
			status.save()
			UserPost.objects.filter(userId=loginUser).update(userPic='/media/'+str(userRegistration.objects.get(userId=loginUser).profilePic))
			
			return HttpResponseRedirect('/profile/')
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
		uname = []
		for e in liveResult:
			fullName = e.firstName+ ' ' +e.lastName
			name.append(fullName)
			uId.append(e.userId)
			pic.append(e.profilePic.url)
			uname.append(e.userName)
		# print(pic)
		return JsonResponse({"Username":name,"Id":uId,"picture":pic,"uname":uname})
		


@csrf_exempt
def addfriend(request):
	profileId = request.POST.get('profileId')
	action = request.POST.get('action')
	request.session['friendProfile'] = profileId # USED IN NEXT FUNCTION FOR REQUEST CONFIRM

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
		

		senderName = Friend_Requests.objects.get(senderId=friendId).senderName
	
	Friend_Requests.objects.filter(senderId=friendId,receiverId=myId).delete()

	return JsonResponse({'Result':'Succuss','name':senderName})

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
		return HttpResponseRedirect('/')

def userCoverInsert(request):
	if request.method == "POST":
		profileUserId=request.POST.get('coverUser')
		coverImage=request.FILES['coverImage']
		loginUser=request.session['user']
		if profileUserId==loginUser:
			status = userRegistration.objects.get(userId=loginUser)
			status.coverPic = coverImage
			status.save()
			return HttpResponseRedirect('/profile/')
		else:
			return HttpResponse('<center><h1>you did somethong wrong</h1></center>')
	else:
		return HttpResponse('<center><h1>you did somethong wrong</h1></center>')

def test(request):
	myId = 'mohammad.danish2694@gmail.com'
	friendId = 'sj27754@gmail.com'
	myList = AllFriends.objects.get(userId=myId)
	if friendId in myList.Friends:
		print('found')
	print(myList.Friends)
	
	myList.Friends.append(friendId)
	myNewList = myList.Friends
	AllFriends.objects.filter(userId=myId).update(userId=myId,Friends=myNewList)
	# return render(request,'changepwd.html',{'img':img})
	return HttpResponse('done')
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