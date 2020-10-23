from ..fast_users.authentication import JWTAuthentication

SECRET = "SECRET"


jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600, tokenUrl="/auth/jwt/login")
