from ninja.security import HttpBearer
from datetime import datetime, timedelta
from usuarios.models import Cliente
import jwt # type: ignore


# Configurações do JWT
SECRET_KEY = "sua_chave_secreta"  # Substitua por uma chave forte
ALGORITHM = "HS256"
TOKEN_EXPIRATION_MINUTES = 60


# Classe de segurança para autenticação com JWT
class JWTAuth(HttpBearer):
    def authenticate(self, request, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user = Cliente.objects.get(id=payload["user_id"])
            return user
        except (jwt.ExpiredSignatureError, jwt.DecodeError, Cliente.DoesNotExist):
            return None

auth = JWTAuth()
