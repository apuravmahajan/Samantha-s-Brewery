from django.contrib import admin
from home.models import Contact, Food_Item,ProductItem, ProductImage, Bookings
# Register your models here.
admin.site.register(Contact)
admin.site.register(Food_Item)
admin.site.register(ProductItem)
admin.site.register(ProductImage)
admin.site.register(Bookings)