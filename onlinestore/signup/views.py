from django.shortcuts import render , redirect
#import the table data fields into this PAage
from signup.models import SignUser
# Create your views here.


#create a function to do data saving
def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST["email"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        password =request.POST["password"]

        try:
            signupuser = SignUser(username = username , fname = fname , lname = lname  , email=email , password = password)
            signupuser.save()
        except Exception as e:
            print("error occured")
            print(e)
            return render(request , "signup/signup.html")
        else:
            return redirect("/login/")

    else:
        return render(request , "signup/signup.html")
