# SCHEMAS
from ninja import ModelSchema, Schema


from typing import List


class CategoriaSchema(Schema):
    nome: str
    descricao: str
    #imagem: str | None  
    link_produtos: str

class CategoriaSchema2(Schema):
    nome: str
    descricao: str
    imagem: str | None  


class ProdutoSchema(Schema):
    nome: str
    descricao: str | None
    preco: float
    estoque: int
    categoria: CategoriaSchema2 | None    
    imagem: str | None    

class ClienteSchema(Schema):
    email: str
    nome: str | None
    senha: str | None
    telefone: str | None


class PedidoSchema(Schema):
    id: int
    #nome_cliente: str
    #data_pedido: str
    completo: bool
    transacao_id: str
    total_pedido: int


class ItemPedidoSchema(Schema):
    id: int
    produto: ProdutoSchema
    pedido: PedidoSchema
    quantidade: int
    total_item: float


class EnderecoEntregaSchema(Schema):
    id: int
    cliente: ClienteSchema
    cidade: str
    pais: str


class ItemCompraSchema(Schema):
    produto_id: int
    quantidade: int


class CompraSchema(Schema):
    cliente_id: int
    itens: list[ItemCompraSchema]





