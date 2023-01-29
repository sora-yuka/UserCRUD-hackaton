from views import User, Post

def main():
    while True:
        print(
            "Function:\n"
            "1 - sign up\n"
            "2 - sign in\n"
            "3 - change password\n"
            "4 - change username\n"
            "5 - post product\n"
            "6 - get products\n"
            "0 - exit"
        )
        function = int(input("\nEnter the number:  "))
        user = User()
        post = Post()
        
        if function == 1:
            username = input("Enter username:  ")
            password = input("Enter password:  ")
            user.register(username, password)
            print("Successfully signed up.\n")
        
        if function == 2:
            username = input("Enter username:  ")
            password = input("Enter password:  ")
            user.login(username, password)
            print("Successfully signed in.\n")
            
        if function == 3:
            username = input("Enter username:  ")
            old_password = input("Enter old_password:  ")
            new_password = input("Enter new_password:  ")
            user.change_password(username, old_password, new_password)
            print("Successfully changed.\n")
        
        if function == 4:
            old_username = input("Enter username:  ")
            new_username = input("Enter new username:  ")
            user.change_name(old_username, new_username)
            print("Successfully changed.\n")
            
        if function == 5:
            title = input("Enter a product title:  ")
            description = input("Enter a product description:  ")
            price = int(input("Enter a product price:  "))
            quantity = input("Enter a product quantity:  ")
            owner = input("Enter a product owner:  ")
            post.add_product(title, description, price, quantity, owner)
            print("Successfully created.\n")
            
        if function == 6:
            print(post.get())
        
        if function == 0:
            print("Good luck!")
            break
        
        
if __name__ == "__main__":
    print("\nHey, welcom to account CRUD, below are the available function.\n")
    main()