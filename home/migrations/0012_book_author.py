# Generated by Django 5.1.4 on 2024-12-28 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_books_book_rename_bookings_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='', max_length=122),
        ),
    ]