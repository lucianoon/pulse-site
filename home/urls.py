from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),
    path('servicos/', views.ServicosView.as_view(), name='servicos'),
    path('contato/', views.ContatoView.as_view(), name='contato'),
]
