from django.shortcuts import render,HttpResponse

# Create your views here.


def index(request):
    return render(request,'mainapp/index.html',{'title':'Inicio'})# la carpeta donde se encuentra en template a renderizar 'mainapp/index.html'
    #return HttpResponse(f"No se ha podido crear el articulo sasdsa: ")

def about(request):
    return render(request,'mainapp/about.html',{'title':'Sobre nosotros'})# la carpeta donde se encuentra en template a renderizar 'mainapp/index.html'
    #return HttpResponse(f"No se ha podido crear el articulo sasdsa: ")