from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.profile, name='about'),  
    path('applet/', views.applet, name='applet'),
    path('balok/', views.balok, name='balok'),
    path('kubus/', views.kubus, name='kubus'),
    path('limas/', views.limas, name='limas'),
    path('prisma/', views.prisma, name='prisma'),
    path('profile/', views.profile, name='profile'),
    path('mahasiswa/', views.mahasiswa, name='mahasiswa'),
    path('konsepnotasi/', views.konsepnotasi, name='konsepnotasi'),
    path('kosongsemesta/', views.kosongsemesta, name='kosongsemesta'),
    path('hbagian/', views.hbagian, name='hbagian'),
    path('antarhimpunan/', views.antarhimpunan, name='antarhimpunan'),
    path('operasihimpunan/', views.operasihimpunan, name='operasihimpunan'),
    path('diagramvenn/', views.diagramvenn, name='diagramvenn'),
    
]