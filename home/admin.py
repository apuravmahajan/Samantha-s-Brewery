from django.contrib import admin
from home.models import Contact, Food_Item,ProductItem, ProductImage, Booking, Book, BookClubRegistration, Event, EventBooking
# Register your models here.
admin.site.register(Contact)
admin.site.register(Food_Item)
admin.site.register(ProductItem)
admin.site.register(ProductImage)
admin.site.register(Booking)
admin.site.register(Book)
admin.site.register(BookClubRegistration)
admin.site.register(Event)
admin.site.register(EventBooking)