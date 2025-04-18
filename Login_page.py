users={}

def login():
    username = input('Enter your username')
    password = input('Enter your password')

    if username in users and users[username]==password:
        print('login successfull')
    else:
        print('wrong user name or password')

def create_account():
    username = input('enter your username')
    if username in users:
        print('username already exist')
    else:
        password = input('Enter your password')
        users[username]=password
        print('account created successfully')
def display_users():
    admin = input('Enter you username')
    if admin == 'ahmed' or admin == 'admin':
        print('you are an authorize to display all users')
        for i in users:
            print(i)
    else:
        print('you are not authorized to display all users')

def delete_account():
    admin = input('Enter your username')
    if admin == 'ahmed' or admin == "admin":
        print('you are authorized to delete account')
        removed_username = input('Enter the user name you want to remove')
        users.pop(removed_username)
        print(f'{removed_username} have been deleted')
    else:
        print('you are not authorized to delete account')


while True:
    print('\n *** login page ***')
    print('1. login')
    print('2. create_account')
    print('3. display_users')
    print('4. exit')
    print('5. delete_account')

    choice = int(input('Enter your choise'))

    if choice ==1:
        login()
    elif choice == 2:
        create_account()
    elif choice == 3:
        display_users()
    elif choice == 4:
        print('exit')
        break
    elif choice ==5:
        delete_account()
    else:
        print('invalid choice')
