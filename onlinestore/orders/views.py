from django.shortcuts import render , redirect
from signup.models import SignUser
from django.http import HttpResponse
from  home.models import Store_items
from django.core.mail import send_mail
from .models import OrderItems
# Create your views here.
def orders(request):
    # print(request.session["username"])
    # print("\n\n\n\nyeess")
    # print(request.method)
    # print(request.GET['id'])
    if(request.method=="GET"):
        # print(request.method=="GET")
        id = request.GET["id"]

        # print(request.session["items"])
        try:
            # request.session["items"].append("Hello")
            data = Store_items.objects.get(itemId = id)
            price = data.price
            email = data.ownerEmail
            itemId = data.itemId
            user = request.session["username"]
            buyerId = SignUser.objects.get(username = user).userId
            OrderItems.objects.create(ownerEmail = email , itemId_id = itemId , buyerId_id =buyerId , price = price )

            print(data)
            print(request.session["items"])
        except Exception as e:
            print(e)
            print("\n\n\n\n")
            return render(request , "./home/details.html")
        else:
            return HttpResponse("Item added to the cart")
            # return render(request , "./orders/cart.html" , {"data":data})
    else:
        return render(request , "./home/details.html")
    #function to show the items
    # return redirect("/show/")
    # return HttpResponse("<h1>Hello there My people</h2>")

def displayCart(request):
    try:
        request.session["username"]
# print("Hello display cart \n\n\n")

    except Exception as e:
        return redirect("/login/")
    else:
        cartItems = OrderItems.objects.filter(buyerId_id = SignUser.objects.get(username = request.session["username"]).userId)
        return render(request , "orders/cart.html"  , {"cartItems":cartItems , "username":request.session["username"]})


def buy(request):
    #function to buy ordered items
    #function to send receit through mails
    try:
        # print("\n\n\n\n\nYes am here in first trial")
        request.session["username"]
    except Exception as e:
        print("An error Occured" + str(e))
        # print("\n\n\n\n\nYes am here in first trial2")
        return redirect("/login/")
    else:
        try:
            #admin email is stiveckamash@gmail.com
            adminMail = "stiveckamash@gmail.com"
            messageBody = "Hello We Have send you the email with the invoice...Please be carefull When awaiting it to reach you!"
            messageHead = "Invoice List for the ordered Produscts!"
            #check the regestered mail
            checkMail = SignUser.objects.get(username = request.session["username"]).email
            # print(checkMail)
            sendEmail = send_mail(messageHead ,messageBody , checkMail , [adminMail])
        except Exception as e:
            print("Error Occured here "+str(e))
            # return HttpResponse("An error Occured! Please Resubmit Again")
            return render(request , "orders/error.html" , {"e":e})
        else:
            return redirect("/buy")

    return HttpResponse("OOPS!")
def delete(request):
    # print(request.method)
    # print("\n\n\n\n\n")
    #function to remove an item from the cartcd
    if(request.method=="GET"):
        id = request.GET["id"]
        try:
            remove = OrderItems.objects.filter(itemId_id = id).delete()
        except Exception as e:
            return render(request , "orders/error.html" , {"e":e})
            print(e)
        else:
            # print("Removed Successful")
            # return HttpResponse("Item removed Successfully!")
            cartItems = OrderItems.objects.filter(buyerId_id = SignUser.objects.get(username = request.session["username"]).userId)
            return render(request , "orders/cart.html"  , {"cartItems":cartItems , "username":request.session["username"]})


    else:
        return HttpResponse("OOPS! Something Went Wrong!")
        # print("No id")
