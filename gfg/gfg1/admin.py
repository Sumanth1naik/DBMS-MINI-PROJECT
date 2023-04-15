from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Entrepreneur)
admin.site.register(Funders)
admin.site.register(Donaters)
admin.site.register(Innovaters)