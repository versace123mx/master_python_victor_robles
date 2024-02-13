from django.contrib import admin
from .models import Article,Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)

#configurar el titulo del panel del administracion
admin.site.site_header = 'Master en Python 1'
admin.site.site_title = 'Master en Python 2'
admin.site.index_title = 'Master en Python 3'