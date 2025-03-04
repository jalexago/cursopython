from django.http import HttpResponse
def saludo(request):
    texto = "<html><body><h1>Hola Mundo</h1></body></html>"
    return HttpResponse(texto)