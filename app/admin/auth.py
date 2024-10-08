from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from fastapi.responses import Response
from app.users.auth import (authenticate_user_auth,
                            create_access_token)
from app.users.dependencies import get_current_admin


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        email, password = form["username"], form["password"]
        user = await authenticate_user_auth(email, password)
        if user:
            access_token = create_access_token({"sub":str(user.id),"id":user.id,"role":user.role})
            request.session.update({"token": access_token})
        return True
    
    
    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()  
        return True
    
    
    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            request.session.clear()
            return False
        user = await get_current_admin(token)
        
        if not user:
            request.session.clear()
        
            return False
            
        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key="...")
# admin = Admin(app=..., authentication_backend=authentication_backend، ...)
