from django.shortcuts import render,redirect


from .models import Contact

# Create your views here.
def home(request):
    if "search" in request.GET:
        search = request.GET['search']
        std= Contact.objects.filter(name__icontains=search)
    else:
       std=Contact.objects.all()
    return render(request,"std/home.html", {'std':std})

def std_add(request):
    if request.method=='POST':
        print("Added")
        #retrieve the user inputs
        stds_card=request.POST.get("std_card")
        stds_name=request.POST.get("std_name")
        stds_email=request.POST.get("std_email")
        stds_phone=request.POST.get("std_phone")
        stds_address=request.POST.get("std_address")


        #create an objects for models
        s=Contact()
        s.card=stds_card
        s.name=stds_name
        s.email=stds_email
        s.phone=stds_phone
        s.address=stds_address

        s.save()
        return redirect("/std/home")

    return render(request,"std/add_std.html", {})

def delete_std(request,card):
    s=Contact.objects.get(pk=card)
    s.delete()

    return redirect("/std/home")

def update_std(request,card):
    std=Contact.objects.get(pk=card)

    return render(request,"std/update_std.html",{'std':std})

def do_update_std(request,card):
    std_card=request.POST.get("std_card")
    std_name=request.POST.get("std_name")
    std_email=request.POST.get("std_email")
    std_phone=request.POST.get("std_phone")
    std_address=request.POST.get("std_address")

    std=Contact.objects.get(pk=card)

    std.card=std_card
    std.name=std_name
    std.email=std_email
    std.phone=std_phone
    std.address=std_address

    std.save()
    return redirect("/std/home")