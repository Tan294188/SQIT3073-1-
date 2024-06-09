import csv
import pandas as pd
import os
def claculate_tex_relief():
    tax_relief = 9000
    print("--------------Answer following question--------------")
    child=int(input("How many child under the age of 18 years old(normal) do you have:"))
    tax_relief+=child*2000
    child_full_time_edu=int(input("How many unmarried child of 18 years and above(normal) who is receiving full-time education (A-level, certificate, matriculation or preparatory courses) do you have:"))
    tax_relief+=child_full_time_edu*4000
    child_Uni=int(input("How many unmarried child of 18 years and above(normal)receiving further education in respect of an award of diploma or higher do you have:"))
    tax_relief+=child_Uni*10000
    childD=int(input("How many disabled child do you have:"))
    tax_relief+=childD*6000
    childD_Add=int(input("How many diasbled child age 18 years old and above, not married and pursuing diplomas or above qualification in Malaysia @ bachelor degree or above outside Malaysia in program and in Higher Education Institute that is accredited by related Government authorities do you have:"))
    tax_relief+=childD_Add*8000
    print("--------------Answer following question Y/N--------------")
    OKU=str(input("Disabled individual?Y/N:"))
    if 'Y' in OKU:
        tax_relief+=6000
    disabled=str(input("Do you have disabled husband / wife?Y/N:"))
    if 'Y' in disabled:
        tax_relief+=5000
    print("--------------Answer following question--------------")
    Medical = float(input("Total medical treatment, special needs and carer expenses for parents (Medical condition certified by medical practitioner):"))
    if Medical>8000:
        tax_relief+=8000
    else:
        tax_relief+=Medical
    Purchase=float(input("Total purchase of basic supporting equipment for disabled self, spouse, child or parent:"))
    if Purchase>6000:
        tax_relief+=6000
    else:
        tax_relief+=Purchase
    educationH=float(input("Education fees pay for degree at masters or doctorate level:"))
    educationS=float(input("Education fees pay for course of study undertaken for the purpose of upskilling or self-enhancement:"))
    if educationS>2000:
        educationS=2000
    totaleducation=educationH+educationS
    if totaleducation>7000:
        tax_relief+=7000
    else:
        tax_relief+=totaleducation
    HealthS=float(input("Total expenses of Serious diseases for self, spouse or child,Fertility treatment for self or spouse:"))
    HealthV=float(input("Total expenses of vaccination for self, spouse and child:"))
    HealthP=float(input("Total expenses of Complete medical examination for self, spouse or child/COVID-19 detection test including purchase of self-detection test kit for self, spouse or child/Mental health examination or consultation for self, spouse or child:"))
    HealthC=float(input("Total healthcare expenses for child aged 18 and below(exclude the fee already be recorded above):"))
    if HealthV>1000:
        HealthV=1000
    if HealthP>1000:
        HealthP=1000
    if HealthC>4000:
        HealthC=4000
    TotalHealth=HealthC+HealthP+HealthS+HealthV
    if TotalHealth>10000:
        tax_relief+=10000
    else:
        tax_relief+=TotalHealth
    Lifestyle=float(input("Total expenses of purchase books material, electronic equipment and subsribe internet fee: "))
    Xsport=float(input("Total expenses of sports equipment: "))
    if Xsport>500:
        tax_relief+=500
        Xsport-=500
    else:
        tax_relief+=Xsport
        Xsport=0
    if Lifestyle+Xsport>2500: tax_relief+=2500
    else: tax_relief+=Lifestyle+Xsport
    breath=float(input("Total amount of purchase of breastfeeding equipment for own use for a child aged 2 years and below:"))
    if breath>1000:tax_relief+=1000
    else:tax_relief+=breath
    childcare=float(input("Child care fees to a registered child care centre / kindergarten for a child aged 6 years and below:"))
    if childcare>3000:tax_relief+=3000
    else:tax_relief+=childcare
    deposit=float(input("Net deposit in Skim Simpanan Pendidikan Nasional (Net deposit is the total deposit in 2023 MINUS total withdrawal in 2023):"))
    if deposit>8000:tax_relief+=8000
    else:tax_relief+=deposit
    alimony=float(input("Husband / wife / payment of alimony to former wife:"))
    if alimony>4000:tax_relief+=4000
    else:tax_relief+=alimony
    EPF=float(input("Mandatory contributions to approved schemes or voluntary contributions to EPF (excluding private retirement schemes) or contributions under any written law:"))
    life_ins=float(input("Life insurance premium payments or family takaful contributions or additional voluntary contributions to EPF:"))
    if EPF>4000:
        tax_relief+=4000
    else: tax_relief+=EPF
    if life_ins>3000:
        tax_relief+=3000
    else: tax_relief+=life_ins
    PRS=float(input("Deferred Annuity and Private Retirement Scheme (PRS):"))
    if PRS>3000:tax_relief+=3000
    else: tax_relief+=PRS
    edu_medi_ins=float(input("Education and medical insurance:"))
    if edu_medi_ins>3000:tax_relief+=3000
    else: tax_relief+=edu_medi_ins
    SOCSO=float(input("Contribution to the Social Security Organization (SOCSO):"))
    if SOCSO>350:tax_relief+=350
    else: tax_relief+=SOCSO
    charging_factilities=float(input("Expenses on charging facilities for Electric Vehicle (Not for business use):"))
    if charging_factilities>3500:tax_relief+=3500
    else:tax_relief+=charging_factilities
    return tax_relief
def calculate_tax(income, tax_relief):
    tax=0
    salary_for_tax=income-tax_relief
    if salary_for_tax<5000:
        tax=0
    elif salary_for_tax<20000:
        tax=(salary_for_tax-5000)*0.01
    elif salary_for_tax<35000:
        tax=150+(salary_for_tax-20000)*0.03
    elif salary_for_tax<50000:
        tax=600+(salary_for_tax-35000)*0.06
    elif salary_for_tax<70000:
        tax=1500+(salary_for_tax-50000)*0.11
    elif salary_for_tax<100000:
        tax=3700+(salary_for_tax-70000)*0.19
    elif salary_for_tax<400000:
        tax=9400+(salary_for_tax-10000)*0.25
    elif salary_for_tax<600000:
        tax=84400+(salary_for_tax-400000)*0.26
    elif salary_for_tax<2000000:
        tax=136400+(salary_for_tax-600000)*0.28
    else:tax=528400+(salary_for_tax-2000000)*0.3
    return tax
def verify_user(ic_number, password):
    if len(ic_number)==12:
        verify=True
        if ic_number[-4:]==password[-4:]:
            verify=True
        else: verify=False
    else: verify=False
    print(len(ic_number))
    return verify
def create_password(name,ic_number):
    password=ic_number[-4:]
    print("password:",password)
    headers=["name","ic number","password","Annual income","tax relief","Tax"]
    save_list={"name": [name],"ic number": [ic_number],"password": [password]}
    df=pd.DataFrame(save_list,columns=headers)
    if os.path.isfile('Private.CSV'):
         df.to_csv('Private.CSV', mode='a', index=False, header=False)
    else:
        df.to_csv('Private.CSV', index=False, header=True)
    return password
def save_csv(name, ic_number, password, income, tax_relief, tax, row_number):
    file_path = "Private.CSV"
    save_list = {"name": name, "ic number": ic_number, "password": password, "Annual income": income, "tax relief": tax_relief, "Tax": tax}
    def read_csv(file_path):
        with open(file_path, mode='r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            data = [row for row in csvreader]
        return data
    def write_csv(file_path, data):
        with open(file_path, mode='w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(data)
    def update_row(file_path, target_row_number, save_list):
        data = read_csv(file_path)       
        # Assuming the CSV has a header row and it matches the keys in save_list
        header = data[0]
        new_row_data = [save_list.get(column, "") for column in header]      
        if target_row_number - 1 < len(data):
            data[target_row_number - 1] = new_row_data
            write_csv(file_path, data)
            return True
        else:
            return False
    if update_row(file_path, row_number, save_list):
        print(f'Successfully updated row {row_number} with new data: {save_list}.')
    else:
        print(f'Failed to update row {row_number}. The specified row does not exist.')
def check_row_csv(name):
    file_path="Private.CSV"
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row_number, row in enumerate(csvreader, start=1):
            if any(name in cell for cell in row):
                return row_number
        return-1
def check_password_csv(name,password):
    file_path = "Private.CSV"
    Verify = False 
    try:
        df = pd.read_csv(file_path)
        df['password'] = df['password'].astype(str)
        matching_rows = df[(df["name"] == name) & (df["password"] == str(password))]
        if not matching_rows.empty:
            Verify = True
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return Verify
def header(data, filename):
    headers=["name","ic number","password","Annual income","tax relief","Tax"]
    df = pd.DataFrame(data, columns=headers)
    if os.path.isfile(filename):
         df.to_csv(filename, mode='a', index=False, header=False)
    else:
        df.to_csv(filename, index=False, header=True)
def stop():
    Decision=str(input("Do you want to exit the program?Y/N: "))
    if 'Y' in Decision:verify=True
    else:verify=False
    return verify