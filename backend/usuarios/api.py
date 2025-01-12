from utils.auth import SECRET_KEY
from utils.auth import auth
from usuarios.schema import CategoriaSchema, CategoriaSchema2, ClienteSchema, CompraSchema, PedidoSchema, ProdutoSchema
from .models import Cliente

from ninja import Router



from ninja.security import HttpBearer
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta
import jwt # type: ignore
from utils.auth import TOKEN_EXPIRATION_MINUTES, ALGORITHM, SECRET_KEY

# Routers
cliente_router = Router()
auth_router = Router()

# Classe de segurança para autenticação com JWT

"""
class UsuarioSchema(ModelSchema):
    class Config:
        model = Usuario
        model_fields = ["nome", "email", "senha"]
"""
"""    
@categoria_router.get("p/", response=list[ProdutoSchema])
def listar_categorias(request):
    return Produto.objects.all()
"""



#*******************************inicio de cliente ************************************************

# Routers
cliente_router = Router()
auth_router = Router()

# Endpoints de autenticação
@auth_router.post("/login")
def login(request, email: str, password: str):
    #Realiza o login e retorna um token JWT
    cliente = get_object_or_404(Cliente, email=email)
    if not cliente.check_senha(password):
        return {"error": "Credenciais inválidas"}
    
    payload = {
        "user_id": cliente.id,
        "exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES),
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}
"""
@auth_router.get("/me", response=ClienteSchema, auth=auth)
def get_current_user(request, user: Cliente = auth):
    #Retorna os dados do cliente autenticado
    user = request.auth  # Aqui, auth retorna o usuário autenticado
    return ClienteSchema.from_orm(user)
"""
# Endpoints CRUD para clientes
@cliente_router.get("/", response=list[ClienteSchema], auth=auth)
def listar_clientes(request):
    #Lista todos os clientes
    return Cliente.objects.all()

@cliente_router.get("/{cliente_id}", response=ClienteSchema, auth=auth)
def obter_cliente(request, cliente_id: int):
    """Obtém um cliente específico pelo ID"""
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return cliente

@cliente_router.post("/", response=ClienteSchema)
def criar_cliente(request, data: ClienteSchema):
    """Cria um novo cliente"""
    data.senha = make_password(data.senha)  # Criptografar a senha ao criar
    cliente = Cliente.objects.create(**data.dict(exclude_unset=True))
    return cliente

@cliente_router.put("/{cliente_id}", response=ClienteSchema)
def atualizar_cliente(request, cliente_id: int, data: ClienteSchema):
    """Atualiza um cliente existente"""
    cliente = get_object_or_404(Cliente, id=cliente_id)
    for field, value in data.dict(exclude_unset=True).items():
        if field == "senha":  # Atualizar a senha apenas se fornecida
            value = make_password(value)
        setattr(cliente, field, value)
    cliente.save()
    return cliente

@cliente_router.delete("/{cliente_id}", auth=auth)
def deletar_cliente(request, cliente_id: int):
    """Deleta um cliente pelo ID"""
    cliente = get_object_or_404(Cliente, id=cliente_id)
    cliente.delete()
    return {"success": f"Cliente {cliente_id} deletado com sucesso"}
    
#******************************* Fim de Clientes ************************************************

