import os
import hashlib
from datetime import datetime

if os.path.isdir('./DB') == True:
    print("DB ready successful!")
elif os.path.isdir('./DB/') == False:
    os.mkdir('./DB')
    os.mkdir('./DB/user')
    print("DB make!")
    print("DB ready successful!")
else:
    print('exit Error : not found directory or not make directory')
    os.system("pause")

#this function by bing AI
def enc(input_string, key):
    # 입력 문자열과 키를 결합합니다.
    combined_input = input_string + key

    # SHA256 해시 객체를 생성합니다.
    encres = hashlib.sha256(combined_input.encode()).hexdigest()

    return encres

username = input("Enter your username : ")
password = input("Enter your password : ")
path = './DB/'+username
pathU = './DB/user/'+username
pathB = os.getcwd()

def pay(name, money):
    print('?')

def check_login():
    global path, username, password, login
    os.chdir(pathB)
    if username not in os.listdir("./DB/user"):
        checkacchave = input('Do you have a account? (y/n) : ')
        if checkacchave == 'n':
            os.system("cls")
            checkAutoSingup = input('Do You need auto Sing up? (y/n) : ')
            if checkAutoSingup == 'y':
                print('Sing up Start!')
                os.mkdir(path)
                os.chdir(path)
                with open(username +' is password'+'.txt', 'w') as file:
                    file.write(password)
                with open(username +'.txt', 'w') as file:
                    file.write(username)
                with open(username +'.txt', 'a') as file:
                    a = str(datetime.today())
                    file.write("\n"+a)
                with open(username +' is asset'+'.txt', 'w') as file:
                    file.write("1000000\n0")
                print("Sing up successful!")
                check_login()
            elif checkAutoSingup == 'n':
                print('Sing up Start!')
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                path = './DB/'+username
                os.mkdir(pathU)
                os.chdir(pathU)
                with open(username +' is password'+'.txt', 'w') as file:
                    file.write(password)
                with open(username +'.txt', 'w') as file:
                    file.write(username)
                with open(username +'.txt', 'a') as file:
                    a = str(datetime.today())
                    file.write("\n"+a)
                with open(username +' is asset'+'.txt', 'w') as file:
                    file.write("1000000\n0")
                print("Sing up successful!")
                check_login()
        elif checkacchave == 'y':
            print("Login failed!")
            print("Please check your username and password!")
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            check_login()
    else:
        os.chdir(pathU)
        fp = open(username +' is password'+'.txt', 'r')
        fn = open(username +'.txt', 'r')
        username_from_DB = fn.read().split('\n')
        print(username_from_DB)
        password_from_DB = fp.read()
        if username == username_from_DB[0] and password == password_from_DB:
            os.system("cls")
            print("Login successful!")
            print("Welcome back, " + username + "!")
            login = True
            system()
        else:
            print("Login failed!")
            print("Please check your password!")
            print("")
            password = input("Enter your password: ")
            print("")
            check_login()

def system():
    print("")
    print('help = "?" enter')
    print("")
    command = input("Enter command : ")
    if command == '?':
        os.system("cls")
        print('[ COMMANDS ]')
        print("")
        print("? - commands print")
        print("info - my info print")
        print('exit - exit')
        print('member_list - member list print')
        print("buy - buy stock")
        print("sell - sell stock")
        system()
    elif command == "info":
        print("")
        os.chdir(pathU)
        fp = open(username +' is password'+'.txt', 'r')
        fn = open(username +'.txt', 'r')
        fm = open(username +' is asset'+'.txt', 'r')
        username_from_DB = fn.read().split('\n')
        password_from_DB = fp.read()
        asset_from_DB = fm.read().split('\n')
        os.system("cls")
        print("[ MY INFO ]")
        print("")
        print("name : "+username_from_DB[0])
        money_from_DB = int(asset_from_DB[0])
        print("money : "+format(money_from_DB, ",")+"won")
        print("stock : "+asset_from_DB[1])
        print("Account created date : "+username_from_DB[1][:-7])
        system()
    elif command == "exit":
        os.system("cls")
        os.system("pause")
        os.chdir("./DB")
    elif command == "member_list":
        os.system("cls")
        os.chdir(pathB+"/DB/user")
        users = os.listdir()
        print("")
        print("[ MEMBER_LIST ]")
        print("")
        for i in range(len(users)):
                print(users[i])
        system()
    elif command == "buy":
        fm = open(username +' is asset'+'.txt', 'r')
        asset_from_DB = fm.read().split('\n')
        money_from_DB = int(asset_from_DB[0])
        os.system("cls")
        os.chdir(pathB)
        os.chdir(pathU)
        print("one stock = 1,000")
        buynum = int(input("Please enter as much as you want to buy stocks : "))
        if buynum <= 0:
            print("stock buy failed, please retry")
            print("Please dont set negative numbers and zero")
            system()
        elif 1000*buynum <= int(asset_from_DB[0]):
            with open(username +' is asset'+'.txt', 'w') as file:
                x = int(money_from_DB)-1000*buynum
                a = int(asset_from_DB[1])+buynum
                file.write(str(x)+"\n")
                file.write(str(a))
            fm = open(username +' is asset'+'.txt', 'r')
            asset_from_DB = fm.read().split('\n')
            money_from_DB = int(asset_from_DB[0])
            print("stock buy completed!")
            print("your money is now "+format(money_from_DB, ",")+"won")
            print("your stock is now "+asset_from_DB[1])
            system()
        else:
            print("stock buy failed, please retry")
            print("your money is "+format(money_from_DB, ",")+"won")
            system()
        system()
    elif command == "sell":
        fm = open(username +' is asset'+'.txt', 'r')
        asset_from_DB = fm.read().split('\n')
        money_from_DB = int(asset_from_DB[0])
        os.system("cls")
        os.chdir(pathB)
        os.chdir(pathU)
        print("one stock = 1,000")
        sellnum = int(input("Please enter as much as you want to sell stocks : "))
        if sellnum <= 0:
            print("stock sell failed, please retry")
            print("Please dont set negative numbers and zero")
            system()
        elif sellnum <= int(asset_from_DB[1]):
            with open(username +' is asset'+'.txt', 'w') as file:
                x = int(money_from_DB)+1000*sellnum
                a = int(asset_from_DB[1])-sellnum
                file.write(str(x)+"\n")
                file.write(str(a))
            fm = open(username +' is asset'+'.txt', 'r')
            asset_from_DB = fm.read().split('\n')
            money_from_DB = int(asset_from_DB[0])
            print("stock sell completed!")
            print("your money is now "+format(money_from_DB, ",")+"won")
            print("your stock is now "+asset_from_DB[1])
            system()
        else:
            print("stock sell failed, please retry")
            print("your money is "+asset_from_DB[1])
            system()
    else:
        print("")
        print("wrong command")
        system()

check_login()

