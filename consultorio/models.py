from django.db import models

class Paciente(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name='email', max_length=100, blank=True, null=True, unique=True)
    telefone = models.CharField(verbose_name='telefone', max_length=11, blank=True, null=True)
    endereco = models.CharField(verbose_name='endereco', max_length=100, blank=True, null=True)
    img = models.ImageField(upload_to='pacientes', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Pacientes'

    def __str__(self) -> str:
        return f'{self.nome} | {self.email}'

class Servico(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='servicos', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Serviços'

    def __str__(self) -> str:
        return self.nome

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, blank=True, null=True, related_name='agendamentos')
    data = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.SET_NULL, blank=True, null=True, related_name='agendamentos')

    class Meta:
        verbose_name_plural = 'Agendamentos'
    
    def __str__(self) -> str:
        return f'{self.paciente} | {self.data} | {self.hora} | {self.servico}'
    
class Sobre(models.Model):
    descricao = models.TextField()
    missao = models.CharField(max_length=255, blank=True, null=True)
    visao = models.CharField(max_length=255, blank=True, null=True)
    valores = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='sobre', blank=True, null=True) 

    def __str__(self) -> str:
        return "Sobre a Clínica"

class Contato(models.Model):
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    horario_funcionamento = models.CharField(max_length=255)
    mapa = models.ImageField(upload_to='contato/', blank=True, null=True)  # Adicionado campo de imagem

    class Meta:
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.email} | {self.endereco}'
    
class Comentario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, blank=True, null=True, related_name='comentarios')
    texto = models.TextField(blank=True, null=True)
    criado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Comentarios'
    
    def __str__(self) -> str:
        return f'{self.paciente} | {self.texto}'


class Parceiros(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    img = models.ImageField(upload_to='parceiros', blank=True, null=True)