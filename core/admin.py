from django import forms
from django.contrib import admin

from easy_maps.widgets import AddressWithMapWidget

# Register your models here.
from .models import *


# Register your models here.
admin.site.register(Suggestion)
admin.site.register(Comments)
admin.site.register(Vote)

