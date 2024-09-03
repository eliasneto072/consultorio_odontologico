from django.contrib import admin
from .models import *

admin.site.register(Servico)
admin.site.register(Contato)
admin.site.register(Paciente)
admin.site.register(Agendamento)
admin.site.register(Comentario)
admin.site.register(Sobre)