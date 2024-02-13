from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name = "Titulo") #cambiando nombres de forma visual en el panel de administracion
    content = models.TextField(verbose_name = "Contenido")
    image = models.ImageField(default='null',verbose_name = "Imagen",upload_to='articles')
    public = models.BooleanField(verbose_name = "Estatus")
    create_at = models.DateTimeField(auto_now_add=True,verbose_name = "Fecha Creación") #cuanto cree el registro por primera vez
    update_at = models.DateTimeField(auto_now=True,verbose_name = "Fecha Actualización") #cuando actualice

    class Meta:
        verbose_name = "Articulo" #Aqui solo estamos cambiando el nombre de la tabla Article a Articulo, pero solo es visual, ya que internamente seguira llamandose article
        verbose_name_plural = "Articulos" #lo mismo que anterior pero cuando sea en plural

    def __str__(self):
        fecha = self.create_at.strftime('%d/%m/%Y')
        public = "(Privado)"
        if self.public:
            public = "(Publicado)"

        return f"{self.title} creado el {fecha}, estatus {public}"

class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name = "Nombre")
    description = models.CharField(max_length=250,verbose_name = "Descripcion")
    created_ad = models.DateField(verbose_name = "Fecha de Creación")#guardado de forma manual

    class Meta:
        verbose_name = "Categoria" #Aqui solo estamos cambiando el nombre de la tabla Article a Articulo, pero solo es visual, ya que internamente seguira llamandose article
        verbose_name_plural = "Categorias" #lo mismo que anterior pero cuando sea en plural