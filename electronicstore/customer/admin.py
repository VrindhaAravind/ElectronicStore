from django.contrib import admin
from .models import Userdetails,Cart,Orders,Review
# Register your models here.

admin.site.register(Userdetails)
admin.site.register(Cart)
admin.site.register(Orders)
admin.site.register(Review)