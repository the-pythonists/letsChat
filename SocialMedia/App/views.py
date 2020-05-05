from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from django.http import JsonResponse
import random
from django.core.mail import send_mail
from django.core.mail import send_mail
from .models import userRegistration,Friend_Requests
from django.contrib.auth.hashers import make_password,check_password


def index(request):
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

def login(request):
	if request.method == 'POST':
		email = request.POST.get("login_Email")
		password = request.POST.get("password")
		loginValidate = userRegistration.objects.filter(userId=email)
		for e in loginValidate:
			holdername = e.firstName + ' ' + e.lastName
			userpass = e.password
			pic = e.profilePic
			print(str(pic))
		if check_password(password,userpass) == True:
			request.session['user'] = email
			request.session['name'] = holdername
			request.session['pic'] = str(pic)
			params = {'name':holdername,'pic':pic}
			return render(request,'DashBoard.html',params)
			# return HttpResponse(holdername+email)
		else:
			return HttpResponse('Invalid')
		
def notifications(request):
	fRequests = Friend_Requests.objects.filter(receiverId=request.session['user'])
	# for i in fRequests:
		
	params = {'request':fRequests}
	return render(request,'Notifications.html',params)

def profile(request):
	if request.method == 'POST':
		name = request.POST.get('profile')
		profileDetail = userRegistration.objects.filter(userId=name)
		params = {'user':profileDetail}
	return render(request,'Profile.html',params)

def addfriend(request):
	if request.method == 'POST':
		profileId = request.POST.get('profileId')
		sendRequest = Friend_Requests(senderId=request.session['user'],receiverId=profileId)
		sendRequest.save()
	return HttpResponse('Sent Successfully')

def search(request):
	if request.method == "POST":
		query = request.POST.get('search').title()
		userProfile = userRegistration.objects.filter(firstName=query) | userRegistration.objects.filter(lastName=query)
		if userProfile:
			params = {'Users':userProfile,'name':request.session['name']}
			return render(request,'Search.html',params)
		else:
			return HttpResponse('No user')
	else:
		return HttpResponse('No POST method')