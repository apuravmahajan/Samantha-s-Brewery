# Generated by Django 5.1.4 on 2024-12-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_productitem_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='food_item',
            name='type',
            field=models.CharField(choices=[('AP', 'Appetizers'), ('SD', 'Salads'), ('WP', 'Wraps'), ('SW', 'Sandwiches'), ('PT', 'Pastas'), ('BG', 'Burgers'), ('PZ', 'Pizzas'), ('MC', 'Main_Courses'), ('BF', 'Breakfast'), ('DS', 'Desserts'), ('BV', 'Beverages'), ('SN', 'Snacks'), ('CN', 'Chinese')], max_length=2),
        ),
    ]
