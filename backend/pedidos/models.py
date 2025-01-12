from django.db import models

from produtos.models import Produto
from usuarios.models import Cliente

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    completo = models.BooleanField(default=False)
    transacao_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"Pedido {self.id} por {self.cliente}"

    @property
    def total_pedido(self):
        return sum(item.total_item for item in self.itens.all())


class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens")
    quantidade = models.PositiveIntegerField(default=1)
    data_adicionado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade} de {self.produto.nome}"

    @property
    def total_item(self):
        return self.produto.preco * self.quantidade
