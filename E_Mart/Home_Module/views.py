from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .Serializer import CustomerSerializer
from .models import Customer
from django import forms

# Create your views here.

@csrf_exempt
def cust_api(request,name=''):
    if request.method=="GET":
        if len(name)!=0:
            try:
                cust=Customer.objects.get(pk=name)
                cust_serializer=CustomerSerializer(cust)
                return JsonResponse(cust_serializer.data,safe=False)      
            except Customer.DoesNotExist:
                return JsonResponse(None,safe=False)
                              
        customers=Customer.objects.all()
        cust_serializer=CustomerSerializer(customers,many=True)
        return JsonResponse(cust_serializer.data,safe=False)
    elif request.method=="POST":
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cust=Customer(email=email,username=username,password=password)
        cust.save()
        # cust_data=JSONParser().parse(request) #converting data into json form
        # cust_serializer=CustomerSerializer(data=cust_data) #using serializer to convert into model type
        # if cust_serializer.is_valid():
        #     cust_serializer.save() # saving data into database           
        return HttpResponseRedirect('/')
       

# Create your views here.
def login(request):
    if request.method=="POST":
        username= request.POST['username']
        password= request.POST['password']
        
        try:
            if 'chkbox1' in request.POST:
                 isChecked = request.POST['chkbox1']
            else:
                 isChecked = False
            if request.session.get('is_Login', False):
                  return HttpResponse("You are already login.") 
            if isChecked:  
                request.session['is_Login'] = True
            cust = Customer.objects.get(username=username,password=password)
            return render(request,"Home_Module/Home.html",context={"LoginCust":cust})
        except Customer.DoesNotExist:
            ErrorMessage="Login faild!,Invalid Username or Password"
            return render(request,"Home_Module/SignUp.html",context={"ErrorMessage":ErrorMessage})
           
        
def home(request):
    isLogin = request.session.get('is_Login', False)
    if isLogin:
        return render(request,"Home_Module/Home.html")
    else:
        return render(request,"Home_Module/signup.html")
def signup(request):
    isLog = request.session.get('is_Login', False)
    if isLog:
       return HttpResponse("You are already login.")
    else:
        return render(request,"Home_Module/signup.html")
def forget(request):
    return render(request,"Home_Module/ForgetPass.html")
def contact(request):
    return render(request,"Home_Module/contact.html")