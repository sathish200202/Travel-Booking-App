from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination

# Create your views here.

#main file
def index(request):
    
    dests = Destination.objects.all() 
    # for dest in dests:
    #     dest.desc = ' '.join(dest.desc.split(' ', 10))

    
   
    return render(request,'index.html', {'dests': dests})

#contact page
def contact(request):
    return render(request, 'contact.html')

#about page
def about(request):
    return render(request, 'about.html')

#news page
def news(request):
    return render(request, 'news.html')

#services page
def services(request):
    return render(request, 'news.html')

#destination
def destination(request, dest_id):
    dest = get_object_or_404(Destination, id=dest_id)
    if request.user.is_authenticated:
        return render(request, 'destination.html', {'dest': dest})
    else:
        return redirect('login')