from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('products', views.products, name = 'products'),
    path('books', views.books, name='books'),
    path('menu', views.menu, name = 'menu'),
    path('bookingcart', views.bookingcart,name='bookingcart'),
    path('gallery', views.gallery,name='gallery')
]
