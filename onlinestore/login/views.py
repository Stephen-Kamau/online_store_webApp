from django.shortcuts import render , redirect
from signup.models import SignUser
# Create your views here.


#create a login function
def login(request):
    error =""
    session = ""
    request.session["items"] = ["Hello world"]

    print("HEllo login page")
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        try:
            loginstatus = SignUser.objects.get(username = username)
        except Exception as e:
            error = "no user with name exists"
            print(error)
            return redirect("/signup/")
        else:
            if loginstatus.password == password:
                #get the session
                request.session["username"] = loginstatus.username
                loginstatus.save()
                # set the username of the currrent user
                session = request.session["username"]
                # set the session variable email address
                request.session["email"] = loginstatus.email
                # Expires immediately th user exits the browser
                request.session.set_expiry(0)
                # redirect users to their home page
                return redirect("/")
            else:
                error = "Wrong password"
                print(error)
                return render(request , "login/login.html" , context = {"error":error ,"session":session})
    else:
        #it will have session and the error variables being returned to the page
        return render(request , "login/login.html" , context = {"error":error ,"session":session})


def signout(request):
    del request.session["username"]
    return redirect("/")
