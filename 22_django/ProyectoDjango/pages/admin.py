from django.contrib import admin
from .models import Page
# Register your models here.


# Register your models here.
admin.site.register(Page)


#confguracion de texto del panel
header = 'Panel de Gestion 1'
title = 'Panel de Gestion 2'
subtitle = 'Proyecto Django 3'
#url = '/inicio' nos redireccionara a inicio
admin.site.site_header = header
admin.site.site_title = title
admin.site.index_title = subtitle
#admin.site.site_url = url #en el panel de administracion hay una opccion de ver sitio si cambiamos esto es a donde nos redireccionara por defaul Djano te redirecciona al localhost del servidor mientras no se cambie 