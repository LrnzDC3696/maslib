from django.contrib import admin
from .models import Genre, Tag, Studio, Producer, Country, Show

# Register your models here.
admin.site.register(Show)
admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Producer)
admin.site.register(Country)
admin.site.register(Tag)
