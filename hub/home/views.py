from django.shortcuts import render
from .models import Contact



def home(request):
    return render(request,"home/base_home.html",{})

def contact(request):
    if request.method == "POST":
        #print("kar rha work!!")
        name = request.POST['name']    
        
        email = request.POST['email']
        
        phone = request.POST['phone']
        
        content = request.POST['content']
        details = Contact(name = name, email = email, phone = phone,content = content)
        details.save()
    return render(request,"home/contact.html",{})

def about(request):
    if request.method == "POST":
        print(request.POST)
    return render(request,"home/about.html",{})        