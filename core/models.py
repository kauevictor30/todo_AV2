from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    data_conclusao = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo