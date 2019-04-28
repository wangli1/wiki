from django.contrib import admin
from .models import person
from .models import articles
from .models import Blog
# Register your models here.

admin.site.register(person)
admin.site.register(articles)
admin.site.register(Blog)
