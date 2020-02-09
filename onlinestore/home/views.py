from django.shortcuts import render , redirect
from home.models import Store_items
# Create your views here.

def index(request):
    if request.method == "POST":
        #get the data from the browser
        email = request.POST['ownerEmail']
        title = request.POST['itemTitle']
        type = request.POST['BuiltType']
        price = request.POST['price']
        phone = request.POST['ownerPhone']
        pic = request.FILES['pic']
        # status = request.POST['bought_status']
        try:
            obj =Store_items(ownerEmail = email ,itemTitle =title , BuiltType =type , price =price , ownerPhone=phone, pic=pic)
            obj.save()
        except Exception as e:
            print("error occured")
            print( e)
            return redirect("./add.html")

        else:
            return redirect("/show")

    return render(request , './home/add.html')

def show(request):
    allItems = Store_items.objects.all()
    return render(request,"./home/index.html",{'allItems':allItems})


def details(request, id):
    items = Store_items.objects.get(id = id)
    return render(request,'./home/details.html', {'items':items})
