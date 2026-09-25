from app.models.user import UserCreate


class AuthService:
    def __init__(self):
        self.users_db = []

    def register_user(self, user: UserCreate):
        user_data = {
            "email": user.email,
            "full_name": user.full_name,
            "password": user.password,
        }
        self.users_db.append(user_data)
        return user_data

    def login_user(self, email: str, password: str):
        for user in self.users_db:
            if user["email"] == email and user["password"] == password:
                return {"message": "Login successful", "email": email}
        return {"message": "Invalid credentials"}
