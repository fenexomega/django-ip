from django.shortcuts import render
from django.http import HttpResponse
from ipware.ip import get_trusted_ip,get_ip

def index(request):
    ip = get_trusted_ip(request)
    if ip == None:
        ip = get_ip(request)
    return HttpResponse(ip)

# Create your views here.
