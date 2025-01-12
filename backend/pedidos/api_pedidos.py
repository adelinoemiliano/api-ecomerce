#*******************************inicio de pedidos ************************************************
from ninja import Router
from pedidos.models import ItemPedido, Pedido
from produtos.models import Produto
from utils.auth import auth
from usuarios.models import Cliente
from usuarios.schema import CompraSchema, PedidoSchema


pedido_router = Router()


@pedido_router.post("/", response=PedidoSchema, auth=auth)
def realizar_compra(request, dados: CompraSchema):
    from django.db import transaction

    try:
        # Obter cliente
        cliente = Cliente.objects.get(id=dados.cliente_id)
        print(cliente.email)
        # Criar pedido
        with transaction.atomic():
            pedido = Pedido.objects.create(cliente=cliente, completo=False, transacao_id="12345389")
            print(cliente.email)
            # Adicionar itens ao pedido
            for item in dados.itens:
                produto = Produto.objects.get(id=item.produto_id)
                
                # Verificar estoque
                if produto.estoque < item.quantidade:
                    raise ValueError(f"Estoque insuficiente para o produto: {produto.nome}")

                # Criar item de pedido
                ItemPedido.objects.create(
                    produto=produto,
                    pedido=pedido,
                    quantidade=item.quantidade
                )
                # Atualizar estoque
                produto.estoque -= item.quantidade
                produto.save()
            return pedido
    except Cliente.DoesNotExist:
        return {"error": "Cliente não encontrado"}
    except Produto.DoesNotExist:
        return {"error": "Produto não encontrado"}
    except ValueError as e:
        return {"error": str(e)}