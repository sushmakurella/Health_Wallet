from django.shortcuts import render,redirect,HttpResponse
import smtplib
from .models import DiagCenter, Hospital, PatientDetails,Pres,pdfs,Patient
from django.contrib import messages
from django.template import loader
from geopy.geocoders import Nominatim
import folium
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout
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
hid=""
pid=""
def hospitalLogin(request):
    if request.method == 'POST':
        hid = request.POST['hid']
        hpswd = request.POST['hpswd']
        hobj = Hospital.objects.get(hid = hid)
        if(hobj.pswd == hpswd):
            return render(request, 'hospitalhome.html',{'hname': hobj.hname})
    return render(request,'hospitalLogin.html')
def diaglogin(request):
    if request.method=='POST':
        did = request.POST['did']
        dpswd = request.POST['dpswd']
        dobj = DiagCenter.objects.get(dcid=did)
        if(dobj.pswd==dpswd):
            return render(request,'diaghome.html',{'dname':dobj.dcname})
    return render(request,'diaglogin.html')
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
       
def setDpswd(request,did):
    if request.method=='POST':
        pswd=request.POST["pswd"]
        cpswd=request.POST["cpswd"]
        did1=request.POST["did"]
        print("hiii")
        if(pswd==cpswd):
            obj=DiagCenter.objects.get(dcid=did1)
            obj.pswd=pswd
            obj.save()
            return redirect('home')
    did1=did
    return render(request,'setDpswd.html',{"did":did1})

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
       obj.save()
       name="sushma"
       '''subject="it's me, SUSHMA"
        msg="hello, HOw are you? I hope you all fine."
        rl=['suahmakurella@gmail.com']
        send_mail(subject,msg,EMAIL_HOST_USER,rl,fail_silently=False)'''
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.starttls()

# Authentication
       #s.login("suahmakurella@gmail.com", "zbxnecargpjugmpn")
       #s.login("suahmakurella@gmail.com", "gxgiipbvtpzveujj")
       s.login("sushmadilakshmikurella@gmail.com","hsbulcezfkfrhcdz")
    #    s.login

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
       return redirect("adminhome")
    #return render(request,'sendmail.html')
    return render(request,"addHospital.html")

def addDiag(request):
    if request.method=="POST":
       did=request.POST["did"]
       dnumber=request.POST['dnumber']
       mail=request.POST["dmail"]
       dname=request.POST["dname"]
       pincode=request.POST["pincode"]
       state=request.POST["state"]
       dist=request.POST["dist"]
       Address=request.POST["Address"]
       obj=DiagCenter.objects.create(dcid=did,dcname = dname, pincode = pincode, state = state, dist = dist, Address = Address, dmail = mail)
       obj.save()
       name="sushma"
       '''subject="it's me, SUSHMA"
        msg="hello, HOw are you? I hope you all fine."
        rl=['suahmakurella@gmail.com']
        send_mail(subject,msg,EMAIL_HOST_USER,rl,fail_silently=False)'''
       s = smtplib.SMTP('smtp.gmail.com', 587)
       s.starttls()

# Authentication
       #s.login("suahmakurella@gmail.com", "zbxnecargpjugmpn")
       #s.login("suahmakurella@gmail.com", "gxgiipbvtpzveujj")
       s.login("sushmadilakshmikurella@gmail.com","hsbulcezfkfrhcdz")
    #    s.login

# message to be sent
       m="http://192.168.24.248:8000/setDpswd/"+did
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
    return render(request, "addDiag.html")

       
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


def patientRegister(request):
    if request.method == 'POST':
        adhno = request.POST['adhno']
        pswd = request.POST['pswd']
        cpswd=request.POST['cpswd']
        pname = request.POST['pname']
        pincode = request.POST['pincode']
        state = request.POST['state']
        dist = request.POST['dist']
        Address = request.POST['Address']
        gender = request.POST['gender']
        dob = request.POST['dob']
        diab = request.POST['diab']
        bp = request.POST['bp']
        weight = request.POST['weight']
        height = request.POST['height']
        phno = request.POST['phno']
        email = request.POST['email']
        if(pswd!=cpswd):
           render(request,"patientRegister.html",{"msg":"password mismatch"})
        else:
            obj = Patient.objects.create(
            adhno=adhno,
            pswd=pswd,
            pname=pname,
            pincode=pincode,
            state=state,
            dist=dist,
            Address=Address,
            gender=gender,
            dob=dob,
            diab=diab,
            bp=bp,
            weight=weight,
            height=height,
            phno=phno,
            emial=email
        )
        obj.save();
        name="sushma"
       
        s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
        s.starttls()
        s.login("sushmadilakshmikurella@gmail.com","hsbulcezfkfrhcdz")

# message to be sent
        m="http://192.168.24.248:8000/setHpswd/"+hid
        msg="""Congratulations"""
        msg2="""you have registered succeesfully in Health Wallet website
            now your data is safe and secure.
        """

# sending the mail
        s.sendmail("sushmadilakshmikurella@gmail.com",email, msg+pname+msg2)

# terminating the session
        s.quit()
        return redirect('home')
    return render(request,"patientRegister.html")
def uploadDetails(request):
    return render(request,"uploadDetails.html")
def storeDetails(request):
    if request.method=="POST":
        date = request.POST["date"]
        disease = request.POST["disease"]
        diagnosis = request.POST["diagnosis"]
        #prescription = request.POST["prescription"]
        remarks = request.POST["remarks"]
        adhno = request.POST["adhno"]
        hid = request.POST["hid"]
        hname = request.POST["hname"]
        dname = request.POST["dname"]
        dm1=int(request.POST["dm1"])
        dm2=int(request.POST["dm2"])
        obj=PatientDetails.objects.create(
            date=date,
            disease=disease,
            diagnosis=diagnosis,
            #prescription=prescription,
            remarks=remarks,
            adhno=adhno,
            hid=hid,
            hname=hname,
            dname=dname
        )
        obj.save();
        for i in range(1,dm1+1):
            m=request.POST["m"+str(i)]
            t=request.POST["t"+str(i)]
            e=request.POST["e"+str(i)]
            obj1=Pres.objects.create(
                date=date,
                hid=hid,
                hname=hname,
                medicine=m,
                time=t,
                adhno=adhno,
                lunch=e
                )
            obj1.save();
        for i in range(1,dm2+1):
            pdf=request.FILES["pdf"+str(i)]
            pdfname=request.POST["pdfname"+str(i)]
            obj2=pdfs.objects.create(
                date=date,
                hid=hid,
                hname=hname,
                pdf=pdf,
                pdfname=pdfname,
                adhno=adhno
                )
            obj2.save();
    return redirect("home")
import numpy as np 
import pandas as pd
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import hstack
from sklearn.feature_extraction.text import TfidfVectorizer
def recommend_medicines_by_usage(medicine_name, tfidf_matrix_uses, clean_df):
    # Get the index of the medicine
    medicine_index = clean_df[clean_df['Medicine Name'] == medicine_name].index[0]
    
    # Calculate cosine similarity between the given medicine and others based on usage
    sim_scores = cosine_similarity(tfidf_matrix_uses, tfidf_matrix_uses[medicine_index])
    
    # Get indices of top similar medicines (excluding the queried one)
    sim_scores = sim_scores.flatten()
    similar_indices = sim_scores.argsort()[::-1][1:6]  # Top 5 similar medicines
    
    # Get recommended medicine names
    recommended_medicines = clean_df.iloc[similar_indices]['Medicine Name'].tolist()
    
    return recommended_medicines
def recommend_medicines_by_symptoms(symptoms, tfidf_vectorizer, tfidf_matrix_uses, clean_df):
    # Create a string from the given symptoms
    symptom_str = ' '.join(symptoms)
    
    # Transform the symptom string using the TF-IDF vectorizer
    symptom_vector = tfidf_vectorizer.transform([symptom_str])
    
    # Calculate cosine similarity between the symptom vector and all medicine vectors
    sim_scores = cosine_similarity(tfidf_matrix_uses, symptom_vector)
    
    # Get indices of top similar medicines
    sim_scores = sim_scores.flatten()
    similar_indices = sim_scores.argsort()[::-1][:5]  # Top 5 similar medicines
    
    # Get recommended medicine names
    recommended_medicines = clean_df.iloc[similar_indices]['Medicine Name'].tolist()
    
    return recommended_medicines
def recommendMedicine(request):
    if request.method=='POST':
        # for dirname, _, filenames in os.walk(r"/Users/jvmohanakrishnainty/Desktop/Med_Recommend/Medical2/Medicine_Details.csv"):
        #     for filename in filenames:
        #         print(os.path.join(dirname, filename))
        df = pd.read_csv(r'C:/Users/Dell/OneDrive/Desktop/djpro/medicalProject/Medicine_Details.csv')
        #df.head()
        clean_df = df.drop_duplicates()
        tfidf_vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix_uses = tfidf_vectorizer.fit_transform(clean_df['Uses'].astype(str))
        tfidf_matrix_composition = tfidf_vectorizer.fit_transform(clean_df['Composition'].astype(str))
        tfidf_matrix_side_effects = tfidf_vectorizer.fit_transform(clean_df['Side_effects'].astype(str))
        min_rows = min(tfidf_matrix_uses.shape[0], tfidf_matrix_composition.shape[0], tfidf_matrix_side_effects.shape[0])

    # Trim matrices to have the same number of rows
        tfidf_matrix_uses = tfidf_matrix_uses[:min_rows]
        tfidf_matrix_composition = tfidf_matrix_composition[:min_rows]
        tfidf_matrix_side_effects = tfidf_matrix_side_effects[:min_rows]

        tfidf_matrix_combined = hstack((tfidf_matrix_uses, tfidf_matrix_composition, tfidf_matrix_side_effects))

        cosine_sim_combined = cosine_similarity(tfidf_matrix_combined, tfidf_matrix_combined)

        # query = "Lobet 20mg Injection"
        # recommended_medicines = recommend_medicines_by_usage(query, tfidf_matrix_uses, clean_df)
        # print(recommended_medicines)

    

        # Create a TF-IDF vectorizer for symptoms
        tfidf = TfidfVectorizer(stop_words='english')

        # Fit and transform the 'Uses' column to create the TF-IDF matrix for symptoms
        tfidf_matrix_uses = tfidf.fit_transform(clean_df['Uses'])

    # Now, you can call the recommend_medicines_by_symptoms function
        query = request.POST["ds"] # Convert the single symptom to a list
        print(query)
        recommended_medicines = recommend_medicines_by_symptoms(query, tfidf, tfidf_matrix_uses, clean_df)
        print(recommended_medicines)
        #****************************************model one completed**********************************
        return render(request,"displayMedicine.html",{"data":recommended_medicines})
    return render(request,"recommendMedicine.html")

def adminhome(request):
    return render(request,"adminhome.html")
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pswd']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or any other page
            return redirect('adminhome')
        else:
            # Authentication failed, display an error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'adminlogin.html', {'error_message': error_message})
    else:
        return render(request, 'adminlogin.html')

def patientLogin(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        ppswd = request.POST['ppswd']
        pobj = Patient.objects.get(adhno = pid)
        if(pobj.pswd == ppswd):
            return render(request, 'patientHome.html',{'pname': pobj.pname})
    return render(request,'patientLogin.html')
from django.http import HttpResponseRedirect
def adminlogout(request):
    # logout(request)
    if request.method=='POST':
        return redirect('home')
    return redirect('adminhome')
    

def patientLogin(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        ppswd = request.POST['ppswd']
        pobj = Patient.objects.get(adhno = pid)
        if(pobj.pswd == ppswd):
            return render(request, 'patientHome.html',{'pname': pobj.pname})
    return render(request,'patientLogin.html')

def patientloginregister(request):
    return render(request, "patientlr.html")