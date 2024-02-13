"""aprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from miapp import views # tenemos que importar de aqui por que aqui esta la aplicacion views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('inicio/', views.index,name='inicio'),
    path('hola-mundo/', views.hola_mundo,name='holamundo'),
    path('pagina-pruebas/', views.pagina,name='pagina'),
    #path('contacto/<int:id>/<str:nombre>', views.contacto,name='contacto'),
    path('contacto/', views.contacto,name='contacto'),
    path('contactoV2/<str:nombre>/<str:apellido>', views.contactoV2,name='contactoV2'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', views.crear_articulo,name='crear_articulo'),
    path('articulo', views.articulo,name='articulo'),
    path('editar_articulo/<int:id>', views.editarArticulo,name='editar_articulo'),
    path('mostrarArticulos', views.mostrarArticulos,name='mostrarArticulos'),
    path('eliminaArticulo/<int:id>', views.eliminaArticulo,name='eliminaArticulo'),
    path('save_article/', views.save_article,name='save_article'),
    path('create_article/', views.create_article,name='create_article'),
]

#configuracion para imagenes
#comprobar si estamos en debug ya que para produccion ya sabe a que carpeta ir
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
