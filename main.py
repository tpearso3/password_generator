class password_generator:
    def __init__(self, password):
        print("init")
        self.password = password
        pass
    
    def print_password(self):
        print(self.password)



def password_generator_program():
    password = password_generator("Tanner")
    password2 = password_generator("Matthew")
    password3 = password_generator("Brittni")
    password_manager = list()
    password_manager.append(password)
    password_manager.append(password2)
    password_manager.append(password3)
    for i in range(len(password_manager)):
        password_manager[i].print_password()

def main():
    password_generator_program()


if __name__ == "__main__":
    main()
