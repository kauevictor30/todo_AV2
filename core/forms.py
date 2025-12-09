from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_conclusao', 'categoria', 'concluida']
        widgets = {
            'data_conclusao': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'concluida': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }