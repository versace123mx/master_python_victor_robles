from django.shortcuts import render,HttpResponse
from blog.models import Category,Article
# Create your views here.
def list(request):
    articles = Article.objects.all()

    #return HttpResponse(articles)
    return render(request,'articles/list.html',{'title':f'Articles','otroTexto':'asadsadsadsadsasa','nombrePagina':'Articulos','articulos':articles})
