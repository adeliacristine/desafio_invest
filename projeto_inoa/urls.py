from django.contrib import admin
from django.urls import path
from app_inoa import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.monitora, name='monitora'),
    path('get_ativos', views.get_ativos, name='get_ativos'),
    path('cotacao/', views.cotacao, name='cotacao'),
    path('remover_item/<int:item_id>/', views.remover_item, name='remover_item'),
    path('remover_monitorado/<int:item_id>/', views.remover_monitorado, name='remover_monitorado'),
    path('adicionar_item/<str:item_nome>/', views.adicionar_item, name='adicionar_item'),
    path('cadastrar_item/', views.cadastro, name='cadastrar_item')
]



