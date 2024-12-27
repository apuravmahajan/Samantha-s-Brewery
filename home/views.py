from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Food_Item, ProductItem, Bookings
from django.contrib import messages
from collections import defaultdict
import json
from datetime import date, timedelta
from django.http import JsonResponse

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
          booking = Bookings(name=name, phone=phone, items=items, booking_date=bDate, final_date=fdate)
          booking.save()
          print(f"Name: {name}, Phone: {phone}, Items: {items}, Booking Date: {bDate}, Final Date: {fdate}")
          return bookingcart(request)
     return JsonResponse({'error': 'Invalid request'}, status=400)

     

def bookingcart(request):
     is_post = request.method == "POST"
     items = json.loads(request.GET.get('items', '[]')) 
     cartCount = int(request.GET.get('count', 0))
     product_items=[]
     for item in items:
          product = ProductItem.objects.prefetch_related('images').filter(name=item).first()
          if(product):
                product_items.append(product)
         
     return render(request, "bookingcart.html",{'cartCount':cartCount, 'products':product_items, 'itemList':items, 'is_post':is_post})

def books(request):
     return render(request,"books.html")

def menu(request):
     food_items = Food_Item.objects.all()
     categories = defaultdict(list)
     for item in food_items:
        categories[item.get_type_display()].append(item)
     categories = dict(categories)
     return render(request, "menu.html", {'categories':categories})

def gallery(request):
     return render(request,'gallery.html')