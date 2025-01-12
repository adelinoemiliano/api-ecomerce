from django.contrib import admin
from django.urls import include, path
from ninja import NinjaAPI

from usuarios.api import cliente_router, auth_router
from produtos.api_produtos import produto_router
from categorias.api_categoria import categoria_router
from pedidos.api_pedidos import pedido_router

api = NinjaAPI()


api.add_router("/clientes/", cliente_router)
api.add_router("/auth/", auth_router)
api.add_router("/produtos/", produto_router)
api.add_router("/categorias/", categoria_router)
api.add_router("/comprar/", pedido_router)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]
