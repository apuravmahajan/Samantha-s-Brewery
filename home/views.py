from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Food_Item, ProductItem, Booking, Book, BookClubRegistration, Event, EventBooking
from django.contrib import messages
from collections import defaultdict
import json
from datetime import date, timedelta
from django.http import JsonResponse
from django.core.paginator import Paginator

# Create your views here.
def index(request):
     return render(request, 'index.html')

def about(request):
     return render(request, 'about.html')

def contact(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          desc = request.POST.get('desc')
          contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
          contact.save()
          messages.success(request, "Contact Form Submitted.")
     return render(request, 'contact.html')

def products(request):
     items = json.loads(request.GET.get('items', '[]')) 
     cartCount = int(request.GET.get('count', 0))
     product_items = ProductItem.objects.prefetch_related('images').all()
     categories = defaultdict(list)
     for item in product_items:
        categories[item.get_type_display()].append(item)
     categories = dict(categories)
     return render(request,"products.html", {'categories':categories, 'items':items,'cartCount':cartCount})

def process_bookings(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          phone = request.POST.get('phone')
          items= json.loads(request.POST.get('items','[]'))
          bDate = date.today()
          fdate= bDate + timedelta(days=5)
          booking = Booking(name=name, phone=phone, items=items, booking_date=bDate, final_date=fdate)
          booking.save()

          for item in items:
               product = ProductItem.objects.filter(name=item).first()
               if(product):
                    product.stock -= 1
                    product.save()

          is_post = request.method == "POST"
          return render(request, "bookingcart.html",{'cartCount':0,'is_post':is_post,'fdate':fdate, 'products':[], 'itemList':[]})

     return JsonResponse({'error': 'Invalid request'}, status=400)

     

def bookingcart(request):
     items = json.loads(request.GET.get('items', '[]')) 
     cartCount = int(request.GET.get('count', 0))
     product_items=[]
     for item in items:
          product = ProductItem.objects.prefetch_related('images').filter(name=item).first()
          if(product):
                product_items.append(product)
         
     return render(request, "bookingcart.html",{'cartCount':cartCount, 'products':product_items, 'itemList':items})

def bookclub(request, message=""):
     books = Book.objects.all().order_by("-month")
     curBook=books.first()
     archBooks=books[1:]
     paginator=Paginator(archBooks, 3)

     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)

     return render(request,"bookclub.html",{'curBook':curBook, 'page_obj':page_obj, 'message':message})

def process_bookclub_registration(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          registration = BookClubRegistration(name=name, email=email, phone=phone)
          registration.save()
          message = "Registration Successful"
     return bookclub(request, message)

def menu(request):
     food_items = Food_Item.objects.all()
     categories = defaultdict(list)
     for item in food_items:
        categories[item.get_type_display()].append(item)
     categories = dict(categories)
     return render(request, "menu.html", {'categories':categories})

def gallery(request):
     return render(request,'gallery.html')

def events(request, message=''):
     eventList=Event.objects.all().order_by("-date")
     upcomingEvents=[]
     pastEvents=[]
     for event in eventList:
          if event.date>=date.today():
               upcomingEvents.append(event)
          else:
               pastEvents.append(event)

     paginator=Paginator(pastEvents, 3)

     page_number = request.GET.get('page')
     page_obj = paginator.get_page(page_number)

     return render(request,'events.html',{'upcomingEvents':upcomingEvents,'pastEvents':page_obj,'message':message})

def eventBookings(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          eventid = request.POST.get('event')
          event=Event.objects.filter(id=eventid).first()
          registration = EventBooking(name=name, email=email, phone=phone, event=event)
          registration.save()
          message = "Registration Successful"
     return events(request, message)
