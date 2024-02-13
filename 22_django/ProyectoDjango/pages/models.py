from django.db import models
from ckeditor.fields import RichTextField #importando testo enriquesido como wisigin pero este se llama ckeditor

# Create your models here.
class Page(models.Model): #heredamos de models para poder crear los modelos
    title = models.CharField(max_length=50,verbose_name="Titulo") # el verbose_name="Titulo" es para la configuracion del administrador
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True,max_length=50,verbose_name="URL amigable")
    visible = models.BooleanField(verbose_name="Visible")
    create_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True,verbose_name="Actualizado el") #Este tipo de campo auto_now es para que cuando se realice una actualizacion este se el que se modifique

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"

    def __str__(self): #Esto sirve para que en el panel de administracion muestre el nombre del titulo y la fecha
        fecha = self.create_at.strftime('%d/%m/%Y')
        public = "(Privado)"
        if self.visible:
            public = "(Publicado)"

        return f"{self.title} --- creado el {fecha}, estatus: {public}"
