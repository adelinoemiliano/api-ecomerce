from django.db import models
from django.contrib.auth.hashers import make_password, check_password



# Criar um novo pedido (carrinho vazio)
#pedido = Pedido.objects.create(cliente=cliente, completo=False)

# Adicionar um item ao pedido
#item = ItemPedido.objects.create(produto=produto, pedido=pedido, quantidade=2)

# Finalizar o pedido
#pedido.completo = True
#pedido.save()

# MODELS



class Cliente(models.Model):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=200)
    senha = models.CharField(max_length=128, editable=False)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    def set_senha(self, raw_password):
        self.senha = make_password(raw_password)

    def check_senha(self, raw_password):
        return check_password(raw_password, self.senha)

class EnderecoEntrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Endereço de entrega para {self.cliente}"




