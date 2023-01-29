import json
FILE_PATH = ("user.json")

"""Проверка пароля"""
def validate_password(userpassword: str) -> None:
    userpassword = userpassword
    if len(userpassword) < 8:
        raise Exception("Password too short.")
    elif userpassword.isdigit() or userpassword.isalpha() == True:
        raise Exception("Password must contain letters and numbers.")


class RegisterMixin:
    def register(self, name: str, password: str) -> None:
        """
        Класс отвечающий за регистрацию
        пользователя в базу данных
        """
        self.name = name
        self.password = validate_password(password)
        
        """Создание ID, проверка пользователя в базе данных"""
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
        
        try:
            max_id = max([i["id"] for i in data])
        except ValueError:
            max_id = 0
        user_data = [username for username in data if username["name"] == name]
        
        if user_data:
            raise Exception("User with username is alredy exist.")
        
        else:
            """Добавление пользователя в базу данных"""
            data.append(
                {
                    "id": max_id + 1,
                    "name": name,
                    "password": password
                }
            )
            
            json.dump(data, open(FILE_PATH, "w"))


class LoginMixin:
    def login(self, name: str, password: str) -> None:
        """
        Класс отвечающий за вход
        пользователя из базы данных
        """
        self.name = name
        self.password = password
        
        """Проверка правльного ввода имени пользователя"""
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
        
        user_data = [username for username in data if username["name"] == name]
        
        if user_data:
            user_index = data.index(user_data[0])
            if data[user_index]["password"] == password:
                return "You successfully sign out."
            raise Exception("Invalid password!")
        return "User with this username doesn't exist!"
        

class ChangePasswordMixin:
    def change_password(self, name: str, old_password: str, new_password: str) -> None:
        """Класс отвечающий за смену пароля пользователя"""
        self.name = name
        self.userpassword = old_password
        self.new_password = validate_password(new_password)
        
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
        
        user_data = [username for username in data if username["name"] == name]
        
        """Проверка правильного ввода имени пользователя"""
        if user_data:
            """Проверка правильного ввода старого пароля"""
            user_index = data.index(user_data[0])
            if data[user_index]["password"] == old_password:
                """Изменение старого пароля на новый"""
                data[user_index]["password"] = new_password
                json.dump(data, open("user.json", "w"))
                return "Password changed successfully!"
            raise Exception("Entered invalid password!")
        return "Invalid username!"
        

class ChangeUsernameMixin:
    def change_name(self, old_name: str, new_name: str) -> None:
        """
        Класс отвечающий за смену имени
        пользователя
        """
        self.username = old_name
        self.new_name = new_name
        
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            
        user_data = [username for username in data if username["name"] == old_name]
        
        """Проверка имени на наличие пользователя"""
        if user_data:
            user_index = data.index(user_data[0])
            """Смена имени пользователя"""
            while new_name != old_name:
                print("User with this username is already exist!")
                new_name = input("Enter the new name:  ")
                break
            """Запись нового имени пользователя"""
            data[user_index]["name"] = new_name
            json.dump(data, open("user.json", "w"))
            return "Username changed successfully!"
        raise Exception("Invaild username! User with this username doesn't exist!")
        
        
class GetProductMixin:
    def get(self):
        with open("product.json") as file:
            data = json.load(file)
        
        
class PostProductMixin:
    def add_product(self, title: str, description: str, price: int, quantity: int, owner: str) -> None:
        with open("user.json", "r") as file:
            user_data = json.load(file)
        user = [i for i in user_data if i["name"] == owner]
        
        if user:
            with open("product.json", "r") as file:
                data = json.load(file)
            
            try:
                max_id = max([i for i in data if i["id"] == id])
            except ValueError:
                max_id = 0
            
            data.append(
                {
                    "id": max_id + 1,
                    "title": title,
                    "description": description,
                    "price": price,
                    "quantity": quantity,
                    "owner": owner,
                }
            )
            with open("product.json", "w") as file:
                json.dump(data, file)