from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import *

# Register your models here.
admin.site.register(Suggestion)
admin.site.register(Comments)
admin.site.register(Vote)
>>>>>>> b36305de2d14cb77f2669caefd3f1b6f6d8f9afe
