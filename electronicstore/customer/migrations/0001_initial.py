# Generated by Django 3.2.5 on 2021-10-21 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mobile_number', models.CharField(max_length=15)),
                ('dob', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.products')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('address', models.TextField()),
                ('seller', models.CharField(default=None, max_length=250)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('packed', 'packed'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='ordered', max_length=120)),
                ('date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.products')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('ordernotplaced', 'ordernotplaced'), ('orderplaced', 'orderplaced')], default='ordernotplaced', max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.products')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=50)),
                ('address_line', models.CharField(max_length=255)),
                ('address_line2', models.CharField(max_length=255)),
                ('town_city', models.CharField(max_length=150)),
                ('delivery_instructions', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
