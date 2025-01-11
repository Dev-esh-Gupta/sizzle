from django.shortcuts import render
from django.http import HttpResponse
from .models import BookTable, AboutUs, Feedback, ItemList, Items

# Create your views here.

def home(request):
    reviews = Feedback.objects.all()
    return render(request, 'home.html', {'reviews' : reviews})

def about(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html', {'data' : data})

def menu(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'list': list, 'items': items})

def bookTable(request):
    if request.method == 'POST' :
       name = request.POST.get('name')
       phone_number = request.POST.get('phone_number')
       email = request.POST.get('email')
       total_person = request.POST.get('total_person')
       booking_date = request.POST.get('booking_date')

       if name != '' and phone_number != '' and email != '' and total_person != '' and booking_date != '':
           data = BookTable(name = name, phone_number = phone_number, email = email, total_person = total_person, booking_date = booking_date)
           data.save()

    return render(request, 'book_table.html')

def feedback(request):
    # return HttpResponse('Hi, This is feedback page')
    if request.method == 'POST' :
        name = request.POST.get('name')
        feed = request.POST.get('feed')
        rating = request.POST.get('rating')
        image = 'items/'+ request.POST.get('image')
        
        if name != '' and feedback != '' and rating != '' and image != '':
            data = Feedback(user_name = name, description = feed, rating = rating, image = image)
            data.save()

    return render(request, 'feedback.html')
