import json
file = open('user.json')
data = json.load(file)

class RegisterMixin:
    def register(self, name, password):
        '''Класс отвечающий за регистрацию
            пользователя в базу данных'''
        self.name = name
        self.password = password
        
        '''Создание ID, проверка пользователя в базе данных'''
        maxid = max([i['id'] for i in data])
        user_data = [username for username in data if username['name'] == name]
        
        if user_data:
            raise Exception('Такой юзер уже существует')
        
        else:
            '''Добавление пользователя в базу данных'''
            data.append ({
                'id': maxid + 1,
                'name': name,
                'password': password
            })
            
            json.dump(data, open('user.json', 'w'))
            return 'Successfully registered'
        

class LoginMixin:
    def login(self, name, password):
        '''Класс отвечающий за вход
        пользователя из базы данных'''
        self.name = name
        self.password = password
        
        '''Проверка правльного ввода имени пользователя'''
        user_data = [username for username in data if username['name'] == name]
        
        if user_data:
            user_index = data.index(user_data[0])
            if data[user_index]['password'] == password:
                return 'Вы успешно залогинились'
            raise Exception('Неверный пароль!')
        return 'Нет такого зарегестрированного юзера в Базе Данных'
        

class ChangePasswordMixin:
    def change_password(self, name, old_password, new_password):
        '''Класс отвечающий за смену пароля пользователя'''
        self.name = name
        self.userpassword = old_password
        self.new_password = self.validate_password(new_password)
        
        user_data = [username for username in data if username['name'] == name]
        
        '''Проверка правильного ввода имени пользователя'''
        if user_data:
            '''Проверка правильного ввода старого пароля'''
            user_index = data.index(user_data[0])
            if data[user_index]['password'] == old_password:
                '''Изменение старого пароля на новый'''
                data[user_index]['password'] = new_password
                json.dump(data, open('user.json', 'w'))
                return'Password changed successfully!'
            raise Exception('Старый пароль указан не верно!')
        return 'Имя юзера введен не правильно!'
        

class ChangeUsernameMixin:
    def change_name(self, old_name, new_name):
        '''Класс отвечающий за смену имени
        пользователя'''
        self.username = old_name
        self.new_name = new_name
        
        user_data = [username for username in data if username['name'] == old_name]
        
        '''Проверка имени на наличие пользователя'''
        if user_data:
            user_index = data.index(user_data[0])
            '''Смена имени пользователя'''
            while new_name != old_name:
                print('Пользователь с таким именем уже существует!')
                new_name = input('Введите новое имя:\t')
                break
            '''Запись нового имени пользователя'''
            data[user_index]['name'] = new_name
            json.dump(data, open('user.json', 'w'))
            return 'Username changed successfully!'
        raise Exception('Нет такого зарегестрированного пользователя в Базе Данных!')
        
        
class CheckOwnerMixin:
    def check(self, owner):
        self.owner = owner
        
        '''Проверка подлинности поста'''
        user_data = [username for username in data if username['name'] == owner]
        
        '''Подтверждение создания поста'''
        if user_data:
            if owner:
                return 'Успешно создан'
        raise Exception('Нет такого пользователя!')