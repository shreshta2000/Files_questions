file_name=open("student.txt","r")
for i in file_name:
    if "Delhi" in i:
        new_file = open("Delhi.txt","a")
        data = new_file.write(i)
    elif " Maharshtra" in i:
        new_file = open(" Maharshtra.txt","a")
        data = new_file.write(i)
    else:
        new_file = open(" other.txt","a")
        data = new_file.write(i)


