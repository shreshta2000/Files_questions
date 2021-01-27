import os
first_name = input("entre your first name ")
last_name = input("entre your last name ")
password1 = input("entre your password ")
my_dic = {"First_Name":first_name,"Last_Name":last_name,"Password":password1}
my_dic=str(my_dic)
if os.path.isfile(first_name + last_name+".txt"):
    print("this username already exist")
    for_login = input("you want to login or not respectively y/n ")
    if for_login == "y":
        username = input("entre your fullname ")
        password = input("entre your password ")
        if username == first_name + last_name:
            if password1 == password:
                print("login successful")
            else:
                print("wrong password")
        else:
            print("wrong username")
    else:
        print("not login")
else:
    my_file = open(first_name + last_name+".txt","a")
    file1 = my_file.write(my_dic)
     
    