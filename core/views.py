from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy  
from .models import Tarefa
from .forms import TarefaForm

class TarefaListView(ListView):
    model = Tarefa
    template_name = 'tarefa_list.html'
    context_object_name = 'tarefas'

class TarefaCreateView(CreateView):
    model = Tarefa
    fields = ['titulo', 'descricao', 'data_conclusao', 'categoria', 'concluida']
    template_name = 'tarefa_form.html'
    success_url = reverse_lazy('tarefa_list')

class TarefaUpdateView(UpdateView):
    model = Tarefa
    form_class = TarefaForm
    template_name = 'tarefa_form.html'
    success_url = reverse_lazy('tarefa_list')

class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = 'tarefa_confirm_delete.html'
    success_url = reverse_lazy('tarefa_list')
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)