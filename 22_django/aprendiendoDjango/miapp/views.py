from django.shortcuts import render,HttpResponse,redirect
from miapp.models import Article
from django.db.models import Q
from django.contrib import messages
# Create your views here.
#aqui se crearia el controlador

layout = """
<h1>Sitio web con Django Gustavo Marchena</h1>
<hr/>
<ul>
    <li><a href='/inicio'>Inicio</a></li>
    <li><a href='/hola-mundo'>Hola mundo</a></li>
    <li><a href='/pagina-pruebas'>Pagina de pruebas</a></li>
    <li><a href='/contacto'>Pagina de contacto</a></li>
</ul>
<hr/>
"""

def index(request):

    return render(request,'index.html', {'range': range(2024,2051)})

def hola_mundo(request):

    return render(request,'hola_mundo.html')


def pagina(request):

    return render(request,'pagina.html')

def contacto(request):

    nombre = 'Gustavo'
    apellido = 'Marchena'

    return render(request,'contacto.html',{'opccional1':nombre,'opccional2':apellido})

def contactoV2(request,nombre,apellido):

    nombre = 'Gustavo'
    apellido = 'Marchena'
    return render(request,'contactoV2.html',{'nombre':nombre,'apellido':apellido})

def crear_articulo(request,title,content,public):
    articulo = Article(
        title=title,
        content =content,
        public = public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} - {articulo.public}")



    """_summary_
    Metodo para obtener un registro en base a su id
    """
def articulo(request):
    articulo = Article.objects.get(id=8)
    return HttpResponse(f"Articulo <br/><b>{articulo.title}-{articulo.content}-{articulo.create_at}</b>")


"""_summary_
    Metodo para obtener un registro en base a su id
"""
def editarArticulo(request,id):
    articulo = Article.objects.get(id=id)
    articulo.title='Batman'
    articulo.content='Pelicula del 2017'
    articulo.partition=True
    articulo.save()
    return HttpResponse(f"Articulo editado: <br/><b>{articulo.title}-{articulo.content}-{articulo.create_at}</b>")

"""_summary_
    Metodo para mostrar todos los registros
"""
def mostrarArticulos(request):
    articulos = Article.objects.all()
    #articulos = Article.objects.all()[:3] limit
    #articulos = Article.objects.order_by('title') ordenacion si le pongo un -title desea de forma decendente
    #return HttpResponse(articulos)
    #return HttpResponse(articulos)
    #articulos = Article.objects.filter(title="prueba Articulo")  filtrando
    #articulos = Article.objects.filter(id__gt=11)  mayores a 11
    #articulos = Article.objects.filter(id__gte=12)  mayores o igual a 12
    #articulos = Article.objects.filter(id__lt=12)  menores a 12
    #articulos = Article.objects.filter(id__lte=12)  menor o igual a 12
    #articulos = Article.objects.filter(id__lte=12)
    #articulos = Article.objects.raw("Select * from miapp_article") utilizando sql raw
    #articulos = Article.objects.filter(Q(title__contains = "2") | Q(public=False)) #or en django
    return render(request,'todoslosarticulos.html',{'articulos':articulos})


"""_summary_
    Metodo para eliminar registro en base a su id
"""
def eliminaArticulo(request,id):
    articulo = Article.objects.get(id=id)
    articulo.delete()

    return redirect('mostrarArticulos')


"""_summary_
    Metodo para crear un registro en base
"""
def create_article(request):
    return render(request,'create_article.html')


"""_summary_
    Metodo para insertar un registro en base a su id
"""
def save_article(request):

    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        public = request.POST['public']
        articulo = Article(
            title = title,
            content = content,
            public = public
        )
        articulo.save()
        #crear mensaje flash
        messages.success(request, f'Registro creado Exitosamente!! Articulo id: {articulo.id}')
        return redirect('mostrarArticulos')
        #return HttpResponse(f"Articulo creado: {articulo.title} - {articulo.content} - {articulo.public}")

    else:

        return HttpResponse(f"No se ha podido crear el articulo: ")
