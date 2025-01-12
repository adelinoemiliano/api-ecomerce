#******************* inicio de produtos **********************************
from ninja import Router

from produtos.models import Produto
from usuarios.schema import ProdutoSchema


produto_router = Router()
"""
@produto_router.get("/p", response=list[ProdutoSchema])
def listar_produtos(request):
    produtos = Produto.objects.select_related("categoria").all()
    return produtos
"""
@produto_router.get("/", response=list[ProdutoSchema])
def listar_produtos(request):
    return Produto.objects.all()

@produto_router.get("/{produto_id}", response=ProdutoSchema)
def listar_produto(request, produto_id: int):
    return Produto.objects.get(id=produto_id)

@produto_router.post("/", response=ProdutoSchema)
def criar_produto(request, data: ProdutoSchema):
    produto = Produto.objects.create(**data.dict())
    return produto

@produto_router.put("/{produto_id}", response=ProdutoSchema)
def atualizar_produto(request, produto_id: int, data: ProdutoSchema):
    try:
        produto = Produto.objects.get(id=produto_id)
        for field, value in data.dict().items():
            setattr(produto, field, value)
        produto.save()
        return produto
    except Produto.DoesNotExist:
        return {"error": "Produto não encontrada"}

@produto_router.delete("/{produto_id}")
def deletar_produto(request, produto_id: int):
    try:
        produto = Produto.objects.get(id=produto_id)
        produto.delete()
        return {"success": f"Produto {produto_id} deletado com sucesso"}
    except Produto.DoesNotExist:
        return {"error": "Produto não encontrado"}
    
#*********************************fim de produtos ************************************************
