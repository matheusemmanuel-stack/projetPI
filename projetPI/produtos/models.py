from django.db import models

class Aluno(models.Model):

  TIPO_CURSO_CHOICES = (
      ('Técnico', 'Técnico'),
      ('Graduação', 'Graduação'),
      ('Pós-graduação', 'Pós-graduação'),
   )
  nome = models.CharField(max_length=100)
  email = models.EmailField()
  data_nascimento = models.DateField()
  nome_mae = models.CharField(max_length=200)
  telefone = models.CharField(max_length=20)
  observacoes = models.TextField(blank=True, null=True)
  curso = models.CharField(max_length=100, 
choices=TIPO_CURSO_CHOICES)
  periodo = models.CharField(max_length=20)

  def __str__(self):
      return self.nome
