 from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from random import randint, choice
from datetime import datetime
from uuid import uuid4

app = FastAPI()

# Разрешаем CORS для всех источников, методов и заголовков
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Разрешаем все домены
    allow_credentials=True,
    allow_methods=["*"],       # Разрешаем все методы
    allow_headers=["*"]        # Разрешаем все заголовки
)

@app.get("/policy")
async def get_policy():
    fake_user_data = {
        "id": str(uuid4()),
        "username": f"user{randint(1000, 9999)}",
        "email": f"user{randint(1000, 9999)}@example.com",
        "is_active": choice([True, False]),
        "created_at": datetime.utcnow().isoformat(),
        "last_login": datetime.utcnow().isoformat(),
        "age": randint(18, 80),
        "country": choice(["US", "DE", "FR", "IN", "JP"]),
        "subscription": choice(["free", "premium", "enterprise"]),
        "policyurl": "https://habittracker.eu/CompanyPolicy"
    }
    return fake_user_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
