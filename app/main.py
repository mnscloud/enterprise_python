from fastapi import FastAPI, Depends, HTTPException
from app.domain.services.services import UserService
from app.infrastructure.repositories.user_repo import UserRepository

app = FastAPI(title="Enterprise Python API")

# Dependency Injection setup
def get_user_service():
    # In production, pass a real DB session here
    repo = UserRepository(db_session=None)
    return UserService(repo)

@app.post("/users/", response_model=None)
def create_user(email: str, service: UserService = Depends(get_user_service)):
    try:
        return service.register_user(email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))