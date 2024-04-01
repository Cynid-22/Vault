from DBconnection import DBconnection
from LoginDetails import LoginDetails
from LD_mgr import LD_mgr
from getpass import getpass

tmp =-1
while tmp != 0:
    print("1. Input")
    print("2. Output")
    print("0. Exit")
    tmp = int(input("chon: "))
    if tmp == 1:
        k = LD_mgr()
        new = LoginDetails()
        new.SetInfo()
        k.create_user(new)
    elif tmp == 2:
        k = LD_mgr()
        tmpname = input("Input your Username: ")
        tmppass = getpass("Input your Password: ")
        print(k.Check_user_return_data(tmpname, tmppass))
        