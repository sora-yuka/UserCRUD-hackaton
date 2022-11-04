from mixin import *

class User(RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin):
    def __init__(self, username: str, userpassword: str) -> None:
        self.username = username
        self.userpassword = self.validate_password(userpassword)
        
    def validate_password(self, userpassword: str) -> None:
        '''Проверка пароля'''
        self.userpassword = userpassword
        if len(self.userpassword) < 8:
            raise Exception('Пароль слишком короткий')
        elif self.userpassword.isdigit() or self.userpassword.isalpha() == True:
            raise Exception('Пароль должен иметь цифры и буквы')
        
        
class Post(CheckOwnerMixin):
    def __init__(self, title: str, description: str, price: int, quantity: int, owner: str) -> None:
        '''Создание поста'''
        self.title = title
        self.description = description
        self.price = price
        self.quantity = quantity
        self.owner = owner