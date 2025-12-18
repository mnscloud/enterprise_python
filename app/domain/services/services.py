from app.domain.models.models import User
from app.infrastructure.repositories.user_repo import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register_user(self, email: str) -> User:
        # Business logic: Check if user already exists
        if self.repo.get_by_email(email):
            raise ValueError("User already registered")
        
        new_user = User(email=email)
        return self.repo.save(new_user)