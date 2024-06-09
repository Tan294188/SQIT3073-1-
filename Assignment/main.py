from function import claculate_tex_relief,calculate_tax,verify_user,create_password,save_csv,check_password_csv,header,check_row_csv,stop
import pandas as pd
import csv
verify=False
name=""
ic_number=""
income=0
tax_relief=0
tax=0
header([],"Private.CSV")
while verify==False:
    register=str(input("Did you register before? Y/N: "))
    if 'N' in register:
            name=str(input("Pls insert you name: "))
            ic_number=str(input("Pls insert you number IC: "))
            password=create_password(name,ic_number)
    else:
        name=str(input("Pls insert you name: "))
        password=str(input("Pls insert you password: "))
        row_number=check_row_csv(name)
        verify=check_password_csv(name,int(password))
        if verify==True:
            print("Correct user name and password.")
            ic_number=str(input("Pls insert you number IC for verify: "))
            verify=verify_user(ic_number,password)
        else:print("Wrong user name and password")
        if verify==False:print("you are not the user, pls get back") 
        else:
            print("Welcome back")
            verify=stop()
            if verify==True:exit()
            else:
                income=float(input('How much of your annual income:'))
                tax_relief=claculate_tex_relief()
                tax=calculate_tax(income, tax_relief)
                print(income,tax_relief,tax)
                save_csv(name,ic_number,password,income,tax_relief,tax,row_number)
                print("Goodbye,have a nice day!")
                exit()