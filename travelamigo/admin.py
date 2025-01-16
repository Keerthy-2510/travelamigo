from django.contrib import admin
from .models import Route, Bus, Schedule

admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Schedule)
