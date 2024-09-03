# forms.py
from django import forms
from .models import Paciente, Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data', 'hora', 'servico']
    
    nome = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'email', 'telefone', 'endereco']
