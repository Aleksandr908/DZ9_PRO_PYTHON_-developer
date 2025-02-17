#import hashlib
#import uuid
from classes.users import Customer, Admin
from classes.authentication import AuthenticationService

# Пример использования
auth_service = AuthenticationService()

# Регистрация пользователей
print(auth_service.register(Customer, "Vasya", "john@example.com", "password123", "123 Main St"))
print(auth_service.register(Admin, "admin", "admin@example.com", "adminpassword", "super"))

# Аутентификация пользователей
print(auth_service.login("Vasya", "password12")) #Немножко неверный пароль
print(auth_service.login("Vasya", "password123")) #Верный пароль
print(auth_service.login("admin", "adminpassword"))

# Получение текущего пользователя
print(auth_service.get_current_user())

# Администрирование
admin_user = auth_service.current_user
if isinstance(admin_user, Admin):
    print(Admin.list_users())
    print(Admin.delete_user("Vasya"))
    print(Admin.list_users())

# Выход
print(auth_service.logout())