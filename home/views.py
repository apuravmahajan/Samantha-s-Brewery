from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact, Food_Item, ProductItem
from django.contrib import messages
from collections import defaultdict
import json

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
     product_items = ProductItem.objects.prefetch_related('images').all()
     categories = defaultdict(list)
     for item in product_items:
        categories[item.get_type_display()].append(item)
     categories = dict(categories)
     return render(request,"products.html", {'categories':categories})

def bookingcart(request):
     items = json.loads(request.GET.get('items', '[]')) 
     cartCount = int(request.GET.get('count', 0))
     product_items=[]
     for item in items:
          product = ProductItem.objects.prefetch_related('images').filter(name=item).first()
          if(product):
               product_items.append(product)
     return render(request, "bookingcart.html",{'cartCount':cartCount, 'products':product_items})

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