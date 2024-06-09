Name= str(input("Pls give your name:"))
IC=str(input("Give me your IC no:"))
Password= str(Name[0:3]+IC[8:12])
print("Your password is ",Password[-4:])
