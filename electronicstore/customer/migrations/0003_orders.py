# Generated by Django 3.2.8 on 2021-10-13 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
        ('customer', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=250)),
                ('status', models.CharField(choices=[('ordered', 'ordered'), ('packed', 'packed'), ('shipped', 'shipped'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='ordered', max_length=120)),
                ('date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.products')),
            ],
        ),
    ]
