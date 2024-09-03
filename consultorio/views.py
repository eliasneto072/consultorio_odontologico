from django.shortcuts import render, redirect
from .models import Paciente, Servico, Agendamento
from .forms import PacienteForm, AgendamentoForm

def homeView(request):
    servicos = Servico.objects.all()
    agendamentoform = AgendamentoForm()
    
    if request.method == 'POST' and 'agendamentoform' in request.POST:
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('data')
            hora = form.cleaned_data.get('hora')
            servico = form.cleaned_data.get('servico')
            nome = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')

            # Verifica se o paciente já existe
            paciente, created = Paciente.objects.get_or_create(
                email=email,
                defaults={
                    'nome': nome,
                    'telefone': form.cleaned_data.get('telefone', ''),
                    'endereco': form.cleaned_data.get('endereco', ''),
                }
            )

            # Cria o agendamento
            agendamento = Agendamento(
                paciente=paciente,
                data=data,
                hora=hora,
                servico=servico
            )
            agendamento.save()
            return redirect('home')

    context = {
        'servicos': servicos,
        'agendamentoform': agendamentoform,
    }
    return render(request, 'home.html', context)


def pacienteCadastroView(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            nome = form.cleaned_data['nome']

            # Verifica se o paciente já existe
            paciente, created = Paciente.objects.get_or_create(
                email=email,
                defaults={
                    'nome': nome,
                    'telefone': form.cleaned_data.get('telefone', ''),
                    'endereco': form.cleaned_data.get('endereco', ''),
                }
            )
            
            if not created:
                # Atualiza os campos que não foram preenchidos
                if not paciente.nome:
                    paciente.nome = nome
                if not paciente.telefone:
                    paciente.telefone = form.cleaned_data.get('telefone', '')
                if not paciente.endereco:
                    paciente.endereco = form.cleaned_data.get('endereco', '')
                paciente.save()

            return redirect('home')

    else:
        form = PacienteForm()

    return render(request, 'cadastro.html', {'form': form})