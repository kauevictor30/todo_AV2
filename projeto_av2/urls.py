from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.TarefaListView.as_view(), name='tarefa_list'),
    
    path('criar/', views.TarefaCreateView.as_view(), name='tarefa_create'),
    
    path('editar/<int:pk>/', views.TarefaUpdateView.as_view(), name='tarefa_update'),
    
    path('excluir/<int:pk>/', views.TarefaDeleteView.as_view(), name='tarefa_delete'),
]