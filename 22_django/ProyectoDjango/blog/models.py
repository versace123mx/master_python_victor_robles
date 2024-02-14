from django.db import models
from ckeditor.fields import RichTextField #importando testo enriquesido como wisigin pero este se llama ckeditor
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):#aqui se tiene que heredar de models.Model para poder tener acceos a los modelos
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.CharField(max_length=255, verbose_name='Descripcion')
    create_at = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creacion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='Titulo')
    contenct = RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null',verbose_name='Imagen',upload_to="articles")#upload_to nos dice donde se guardaran las imagenes
    public = models.BooleanField(verbose_name='Publicado')
    user = models.ForeignKey(User,editable=False,verbose_name='Usuario',on_delete=models.CASCADE)
    categoris =models.ManyToManyField(Category,verbose_name='Categorias',null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado el")
    update_at = models.DateTimeField(auto_now=True,verbose_name="Actualizado el") #Este tipo de campo auto_now es para que cuando se realice una actualizacion este se el que se modifique

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-create_at']

    def __str__(self):
        return self.title