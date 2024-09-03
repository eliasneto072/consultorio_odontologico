from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

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

            # Adiciona mensagem de sucesso
            messages.success(request, 'Agendamento realizado com sucesso!')
            return redirect('home')
        else:
            # Adiciona mensagem de erro se o formulário não for válido
            messages.error(request, 'Houve um erro ao tentar realizar o agendamento. Verifique os dados e tente novamente.')

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
            
            if created:
                messages.success(request, 'Paciente cadastrado com sucesso.')
            else:
                # Atualiza os campos que não foram preenchidos
                updated = False
                if not paciente.nome:
                    paciente.nome = nome
                    updated = True
                if not paciente.telefone:
                    paciente.telefone = form.cleaned_data.get('telefone', '')
                    updated = True
                if not paciente.endereco:
                    paciente.endereco = form.cleaned_data.get('endereco', '')
                    updated = True
                if updated:
                    paciente.save()
                    messages.success(request, 'Dados do paciente atualizados com sucesso.')
                else:
                    messages.info(request, 'Nenhuma atualização necessária, os dados do paciente já estavam completos.')
                
            return redirect('home')
        else:
            messages.error(request, 'Houve um erro no cadastro. Verifique os dados informados.')
    else:
        form = PacienteForm()

    return render(request, 'cadastro.html', {'form': form})