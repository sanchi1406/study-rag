from app.main import app
from fastapi.routing import APIRoute

print("Registered API Routes:\n")

for route in app.routes:
    if isinstance(route, APIRoute):
        print(route.path, route.methods)