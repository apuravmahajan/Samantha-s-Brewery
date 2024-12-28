from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('products', views.products, name = 'products'),
    path('bookclub', views.bookclub, name='bookclub'),
    path('menu', views.menu, name = 'menu'),
    path('bookingcart', views.bookingcart,name='bookingcart'),
    path('gallery', views.gallery,name='gallery'),
    path('book-form',views.process_bookings,name='book-form'),
    path('events',views.events,name='events'),
    path('process-club-registration',views.process_bookclub_registration,name='process_bookclub_registration'),
    path('event-bookings',views.eventBookings,name='event-bookings')
]
