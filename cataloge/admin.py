from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Author)
admin.site.register(models.Book)
admin.site.register(models.Bookinstance)
admin.site.register(models.Genere)
admin.site.register(models.Language)