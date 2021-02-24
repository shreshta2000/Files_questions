import os
first_name = input("entre your first name ")
last_name = input("entre your last name ")
password1 = input("entre your password ")
my_dic = {"First_Name":first_name,"Last_Name":last_name,"Password":password1}
my_dic=str(my_dic)
if os.path.isfile(first_name + last_name+".txt"):
    print("This username already exist")
    for_login = input("you want to login or not y/n ").lower()
    if for_login == "y":
        username = input("entre your fullname ")
        password = input("entre your password ")
        if username == first_name + last_name and  password1 == password:
            print("Login Succesful!")
        else:
            print("Incorrect username or Password")
    else:
        print("Thank You")
else:
    my_file = open(first_name + last_name+".txt","a")
    file1 = my_file.write(my_dic)
    print("SignIn Succesful!")

     
    
