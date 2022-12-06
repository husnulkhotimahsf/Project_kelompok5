from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from . models import Mahasiswa

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())
def applet(request):
    template = loader.get_template('applet.html')
    return HttpResponse(template.render())
def balok(request):
    template = loader.get_template('balok.html')
    return HttpResponse(template.render())
def kubus(request):
    template = loader.get_template('kubus.html')
    return HttpResponse(template.render())
def limas(request):
    template = loader.get_template('limas.html')
    return HttpResponse(template.render())
def prisma(request):
    template = loader.get_template('prisma.html')
    return HttpResponse(template.render())
def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())
def mahasiswa(request):
    template = loader.get_template('mahasiswa.html')
    return HttpResponse(template.render())
def konsepnotasi(request):
    template = loader.get_template('konsepnotasi.html')
    return HttpResponse(template.render())
def kosongsemesta(request):
    template = loader.get_template('kosongsemesta.html')
    return HttpResponse(template.render())
def hbagian(request):
    template = loader.get_template('hbagian.html')
    return HttpResponse(template.render())
def antarhimpunan(request):
    template = loader.get_template('antarhimpunan.html')
    return HttpResponse(template.render())
def operasihimpunan(request):
    template = loader.get_template('operasihimpunan.html')
    return HttpResponse(template.render())
def diagramvenn(request):
    template = loader.get_template('konsepnotasi.html')
    return HttpResponse(template.render())