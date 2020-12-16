import socket
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Seja bem vindo a PASTELARIA DEVOPS')

def mymachine(request):
    hostname = socket.gethostname()
    return HttpResponse(f'Essa aplicação está rodando no host {hostname}')

def healthcheck(request):
    return HttpResponse(f'App is alive')