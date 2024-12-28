from django.db import models
from PIL import Image
from multiselectfield import MultiSelectField
from datetime import date


# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name
    
class Food_Item(models.Model):
    APPETIZERS = "AP"
    SALADS = "SD"
    WRAPS = "WP"
    SANDWICHES = "SW"
    PASTAS = "PT"
    BURGERS = "BG"
    PIZZAS = "PZ"
    MAIN_COURSES ="MC"
    BREAKFAST = "BF"
    DESSERTS = "DS"
    BEVERAGES = "BV"
    SNACKS = "SN"
    CHINESE = "CN"

    FOOD_TYPE_CHOICES =[
        (APPETIZERS, "Appetizers"),
        (SALADS, "Salads"),
        (WRAPS, "Wraps"),
        (SANDWICHES, "Sandwiches"),
        (PASTAS, "Pastas"),
        (BURGERS, "Burgers"),
        (PIZZAS, "Pizzas"),
        (MAIN_COURSES, "Main_Courses"),
        (BREAKFAST,"Breakfast"),
        (DESSERTS, "Desserts"),
        (BEVERAGES,"Beverages"),
        (SNACKS,"Snacks"),
        (CHINESE,"Chinese")
    ]

    name = models.CharField(max_length=122)
    type = models.CharField(max_length=2,choices=FOOD_TYPE_CHOICES)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/food_items/')
    price = models.IntegerField()

    '''def save(self, *args, **kwargs):
        # Resize the image before saving
        if self.image:
            img = Image.open(self.image)
            img = img.convert("RGB")  # Convert to RGB to avoid issues with certain image formats
            img.thumbnail((500, 500))  # Resize to 500x500 or any other size you prefer

            # Save the resized image back to the ImageField
            img.save(self.image.path)

        super(Food_Item, self).save(*args, **kwargs)'''

    def __str__(self):
        return self.name
    
class ProductItem(models.Model):
    BREWING_ESSENTIALS = "BE"
    HERBS_AND_BOTANICALS = "HB"
    WELLNESS_AND_AROMATHERAPY = "WA"
    MERCHANDISE = "MC"
    LOCAL_ARTISAN_PRODUCTS = "LP"
    PRODUCT_TYPE_CHOICES =[
        (BREWING_ESSENTIALS, "Brewing Essentials"),
        (HERBS_AND_BOTANICALS, "Herbs and Botanicals"),
        (WELLNESS_AND_AROMATHERAPY, "Wellness and Aromatherapy"),
        (MERCHANDISE, "Merchandise"),
        (LOCAL_ARTISAN_PRODUCTS, "Local Artisan Products"), ]
    name = models.CharField(max_length=122)
    type = MultiSelectField(choices=PRODUCT_TYPE_CHOICES)
    desc = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
       return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    caption = models.CharField(max_length=200, blank=True)

class Booking(models.Model):
    name=models.CharField(default="", max_length=122)
    phone=models.CharField(default="", max_length=12)
    items=models.TextField(default="")
    booking_date = models.DateField(default=date.today)
    final_date = models.DateField(default=date.today)

    def __str__(self):
        return self.name

class Book(models.Model):
    name=models.CharField(default="", max_length=122)
    author=models.CharField(default="", max_length=122)
    month=models.DateField(default=date.today)
    image=models.ImageField(upload_to='images/books/')
    desc=models.TextField(default="")

    def __str__(self):
        return self.name