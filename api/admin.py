from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Movie),
admin.site.register(Actor),
admin.site.register(MovieCast),
admin.site.register(Genres),
admin.site.register(Reviewer),
admin.site.register(Rating),
admin.site.register(Director),

