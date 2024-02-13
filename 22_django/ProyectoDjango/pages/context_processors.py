from pages.models import Page #importamos el modelo que esta en la carpte de models

def get_pages(request):

    #vamos a retornar un diccionario y ahora solo queda cargarlo en el archivo de settings en context_processors
    pages = Page.objects.values_list('id','title','slug').order_by('order')
    return {'pages':pages}