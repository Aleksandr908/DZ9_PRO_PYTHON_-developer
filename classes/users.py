import hashlib
#import uuid
class User:
    """
    Базовый класс, представляющий пользователя.
    Классы User, Customer и Admin:
   - Базовый класс `User` управляет общими характеристиками пользователей и предоставляет методы для хеширования и проверки паролей.
   - Класс `Customer` добавляет адрес как дополнительное свойство.
   - Класс `Admin` включает методы для управления пользователями: `list_users` и `delete_user`.
    """
    users = []  # Список для хранения всех пользователей

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
        User.users.append(self)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(stored_password, provided_password):
        return stored_password == User.hash_password(provided_password)

    def get_details(self):
        return {'username': self.username, 'email': self.email}

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address

    def get_details(self):
        details = super().get_details()
        details['address'] = self.address
        return details

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level

    def get_details(self):
        details = super().get_details()
        details['admin_level'] = self.admin_level
        return details

    @staticmethod
    def list_users():
        """
        Выводит список всех пользователей.
        """
        return [user.get_details() for user in User.users]

    @staticmethod
    def delete_user(username):
        """
        Удаляет пользователя по имени пользователя.
        """
        for user in User.users:
            if user.username == username:
                User.users.remove(user)
                return f"Пользователь {username} удален."
        return f"Пользователь {username} не найден."
