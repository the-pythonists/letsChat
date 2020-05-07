from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse
import random
from django.core.mail import send_mail
from django.core.mail import send_mail
from .models import userRegistration,Friend_Requests,UserPost,Likes
from django.contrib.auth.hashers import make_password,check_password
import datetime
import uuid


def index(request):
	if request.session.has_key('user'):
		userInfo = userRegistration.objects.get(userId=request.session['user'])
		userData = UserPost.objects.filter(userId=request.session['user']).order_by('-date') # '-' for descending order
		params = {'userInfo':userInfo,'userData':userData}
		return render(request,'DashBoard.html',params)
	else:
		return render(request,'index.html')

def signup(request):
	if request.method == "POST":
		fName = request.POST.get('firstName').title()
		lName = request.POST.get('lastName').title()
		# userName = request.POST.get('userName','DefaultValue')
		email = request.POST.get('Email')
		otp = request.POST.get('OneTimePass')
		pwd = request.POST.get('Password')
		mobile = request.POST.get('Mobile')
		
		if((otp == request.session["Otp"])):
			accountSave = userRegistration(userId=email, firstName=fName, lastName=lName, mobile=mobile,
				emailAddress = email, password = make_password(pwd))
			accountSave.save()
			return HttpResponse('Account Created')
			
		else:
			return HttpResponse("NotSame")
	else:
		return render(request,'CreateAccount.html')

@csrf_exempt
def OtpGeneration(request):
	Email=request.POST.get('Email','DefaultValue')
	# print(Email)
	RandomValue=random.randint(1001,99999)
	RandomValue="LetsChat"+str(RandomValue)
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
			return render(request,'index.html')
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
	if request.method == 'POST':
		name = request.POST.get('profile')
		profileDetail = userRegistration.objects.filter(userId=name)
		params = {'user':profileDetail}
	return render(request,'Profile.html',params)

@csrf_exempt
def addfriend(request):
	profileId = request.POST.get('profileId')
	action = int(request.POST.get('action'))

	if action == 1:
		sendRequest = Friend_Requests(senderId=request.session['user'],receiverId=profileId,senderName=request.session['name'])
		sendRequest.save()
		return JsonResponse({"Result":"Successfully Sent"})

	elif action == 0:
		Friend_Requests.objects.filter(senderId=request.session['user'],receiverId=profileId).delete()
		return JsonResponse({"Result":"Successfully Canceled"})
	else:
		return JsonResponse({'Result':'Nothing Done'})

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
	
		PostStatus=UserPost(postId=Id,userId=user,post=PostMedia,Message=PostMessage).save()
		likes = Likes(postId=Id).save()
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')
	# return render(request,'DashBoard.Html',{"flag":"Your post has uploaded"})

def test(request):
	del request.session['user']
	import uuid
	return HttpResponse(uuid.uuid4().hex)
