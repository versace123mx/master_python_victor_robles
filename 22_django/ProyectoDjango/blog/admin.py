from typing import Any
from django.contrib import admin
from .models import Category,Article


#esto se genera para que sean campos de solo lectura en el administrador
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','create_at','update_at')

    #Esto se hizo  por que se queria que en el front del admino so se tenga que seleccionar que usuario creo el post
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()


# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
