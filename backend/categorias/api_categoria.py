from ninja import Router
from categorias.models import Categoria
from produtos.models import Produto
from utils.auth import auth
from usuarios.schema import CategoriaSchema, CategoriaSchema2, ProdutoSchema


categoria_router = Router()


@categoria_router.get("/{categoria_id}/produtos/", response=list[ProdutoSchema])
def listar_produtos_por_categoria(request, categoria_id: int):
  
    #Retorna todos os produtos associados a uma categoria específica.
    #"nome", "descricao", "preco", "estoque", "categoria", "imagem"
    produtos = Produto.objects.filter(categoria_id=categoria_id)
    return produtos
 

@categoria_router.get("/categoriacomlinkProduto/", response=list[CategoriaSchema])
def listar_categoriasPorLink(request):

    #Lista todas as categorias, incluindo um link para acessar os produtos de cada categoria.
   
    categorias = Categoria.objects.all()
    return [
        {
            "nome": categoria.nome,
            "descricao": categoria.descricao,
            "link_produtos": f"http://127.0.0.1:8000/api/categorias/{categoria.id}/produtos/"
        }
        for categoria in categorias
    ]


#*******************


@categoria_router.get("/", response=list[CategoriaSchema2], auth=auth)
def listar_categorias(request):
    return Categoria.objects.all()

@categoria_router.get("/{categoria_id}", response=CategoriaSchema2)
def listar_categoria(request, categoria_id: int):
    return Categoria.objects.get(id=categoria_id)

@categoria_router.post("/", response=CategoriaSchema2)
def criar_categoria(request, data: CategoriaSchema2):
    categoria = Categoria.objects.create(**data.dict())
    return categoria

@categoria_router.put("/{categoria_id}", response=CategoriaSchema2)
def atualizar_categoria(request, categoria_id: int, data: CategoriaSchema2):
    try:
        categoria = Categoria.objects.get(id=categoria_id)
        for field, value in data.dict().items():
            setattr(categoria, field, value)
        categoria.save()
        return categoria
    except Categoria.DoesNotExist:
        return {"error": "Categoria não encontrada"}

@categoria_router.delete("/{categoria_id}")
def deletar_categoria(request, categoria_id: int):
    try:
        categoria = Categoria.objects.get(id=categoria_id)
        categoria.delete()
        return {"success": f"Categoria {categoria_id} deletada com sucesso"}
    except Categoria.DoesNotExist:
        return {"error": "Categoria não encontrada"}
