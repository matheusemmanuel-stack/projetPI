from django.contrib import admin
from .models import Aluno

class AlunoAdmin(admin.ModelAdmin):
   list_display = ('nome',
                   'email',
                   'data_nascimento',
                   'curso',
                   'periodo')
   search_fields = ('nome', )
   list_filter = ('curso', 'periodo')
admin.site.register(Aluno, AlunoAdmin)
