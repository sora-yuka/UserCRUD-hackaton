from mixin import *

class User(RegisterMixin, LoginMixin, ChangePasswordMixin, ChangeUsernameMixin):
    def __init__(self) -> None:
        return None
        
        
class Post(PostProductMixin, GetProductMixin):
    def __init__(self) -> None:
        return None