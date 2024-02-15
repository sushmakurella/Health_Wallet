from django.shortcuts import render,redirect,HttpResponse
import smtplib
from .models import Hospital
from django.contrib import messages
from django.template import loader
from geopy.geocoders import Nominatim
import folium


import math, random
 
# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable  
    # which stores all digits 
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP
# Create your views here.
def hospitalLogin(request):
    return render(request,'hospitalLogin.html')
def home(request):
    return render(request,"home.html")
def savepswd(request):
    if request.method=='POST':
        pswd=request.POST["pswd"]
        cpswd=request.POST["cpswd"]
        hid1=request.POST["hid"]
        print("hiii")
        if(pswd==cpswd):
            obj=Hospital.objects.get(hid=hid1)
            obj.pswd=pswd
            obj.save()
            return redirect('home')
    return render(request,'setHpswd.html')
def setHpswd(request,hid):
    if request.method=='POST':
        pswd=request.POST["pswd"]
        cpswd=request.POST["cpswd"]
        hid1=request.POST["hid"]
        print("hiii")
        if(pswd==cpswd):
            obj=Hospital.objects.get(hid=hid1)
            obj.pswd=pswd
            obj.save()
            return redirect('home')
    hid1=hid
    return render(request,'setHpswd.html',{"hid":hid1})
       
       
def addHospital(request):
    if request.method=="POST":
       hid=request.POST["hid"]
       hnumber=request.POST['hnumber']
       mail=request.POST["hmail"]
       hname=request.POST["hname"]
       pincode=request.POST["pincode"]
       state=request.POST["state"]
       dist=request.POST["dist"]
       Address=request.POST["Address"]
       speciality=request.POST["speciality"]
       obj=Hospital.objects.create(hid=hid,hmail=mail,hname=hname,pincode=pincode,state=state,dist=dist,Address=Address,speciality=speciality,hnumber=hnumber)
       obj.save();
       name="sushma"
       '''subject="it's me, SUSHMA"
        msg="hello, HOw are you? I hope you all fine."
        rl=['suahmakurella@gmail.com']
        send_mail(subject,msg,EMAIL_HOST_USER,rl,fail_silently=False)'''
       s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
       s.starttls()

# Authentication
       #s.login("suahmakurella@gmail.com", "zbxnecargpjugmpn")
       #s.login("suahmakurella@gmail.com", "gxgiipbvtpzveujj")
       s.login("sushmadilakshmikurella@gmail.com","hsbulcezfkfrhcdz")

# message to be sent
       m="http://192.168.24.248:8000/setHpswd/"+hid
       msg="""
       hello,
       password reset link is provided below it will expired with in 10minitues
       """
       """msg = MIMEText(u'<a href="www.google.com">abc</a>')
       msg['Subject'] = 'subject'
       msg['From'] = 'xxx'
       msg['To'] = 'xxx'"""

       """s = smtplib.SMTP(xxx, 25)
       s.setpassword(xxx, xxx, msg.as_string())
       message = "hello this is sushma. and this is an automated gmail message."
       """

# sending the mail
       s.sendmail("sushmadilakshmikurella@gmail.com",mail, msg+m)

# terminating the session
       s.quit()
       messages.info(request,"email succesfully sent")
       return render(request,"home.html")
    #return render(request,'sendmail.html')
    return render(request,"addHospital.html")
def map(request):
    geolocator = Nominatim(user_agent="my_user_agent")

    # Enter the pin code
    pincode = "534202"  # Example pin code for Buckingham Palace
    p2="534101"
    # Perform geocoding with pin code
    loc = geolocator.geocode(pincode)
    loc2= geolocator.geocode(p2)
    mymap=folium.Map(location=[loc.latitude,loc.longitude],zoom_start=9)
    folium.Marker([loc.latitude,loc.longitude],popup="myloc").add_to(mymap)
    folium.Marker([loc2.latitude,loc2.longitude],popup="myloc").add_to(mymap)  
    folium_map_html = mymap._repr_html_()  
    return render(request,"map.html",{"folium_map_html": folium_map_html})