from django.contrib import admin

from .models import User
#from .models import login
from .models import tweet

#Register your models here.

admin.site.register(User)
#admin.site.register(login)
admin.site.register(tweet)
