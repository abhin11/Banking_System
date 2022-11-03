'''
The pickle module implements binary protocols for serializing and de-serializing a Python object structure.
Pickling is the process whereby a Python object hierarchy is converted into a byte stream,
and unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.
In our program we are using pickle.dump() and pickle.load()
'''
import pickle
'''
The OS module in Python provides functions for interacting with the operating system.
In our program we are using os.remove and os.rename.
os.rename() method in Python is used to rename a file or directory.
os.remove() method in Python is used to remove or delete a file path.
'''
import os

'''
MODULES
'''

import codifying_7E2_ifsc           # Module to return the IFSC CODE of the branch entered by the user                
import codifying_7E2_age as ag      # Module to print the list of age groups                                              
import codifying_7E2_check_holiday  # Module to check if the entered date is a bank holiday or not.

'''
class defined to store account details of the client,
'''

class account(object):
    def _init_(a):
        a.acno = 0
        a.name = ""
        a.age = ""
        a.gender = ""
        a.city = ""
        a.deposit = 0
        a.acc_type=""
        a.pin = ""
        
    '''
    Functions to get data from the user
    Minimum balance for current account is Rs1000
    Minimum balance for savings account is Rs500
    '''   

    def create_account(a):                                                                                  
        name=input("\nEnter the name of the account holder: ")
        a.name=name.capitalize()
        a.age =input("\nEnter the age of the account holder: ")
        gender =input("\nEnter the gender of the account holder (M/F): ")
        a.gender= gender.capitalize()
        acc_type=input("\nEnter type of the account (C-Current/S-savings): ")
        a.acc_type=acc_type.upper()
        if a.acc_type == 'C':                                                                               
            deposit = int(input("\nEnter initial amount >= 1000 for current account: "))
            if deposit >= 1000:
                a.deposit = deposit
            else:
                raise Exception("\nTo create a current account, you need a minimum balance of Rs 1000!")
        elif a.acc_type  == 'S':
            deposit = int(input("\nEnter initial amount >= 500 for savings account: "))
            if deposit >= 500:
                a.deposit = deposit
            else:
                raise Exception("\nTo create a savings account, you need a minimum balance of Rs 500!")        
        else:
            print("\nEnter a valid input(C/S)")
        a.pin = input("\nEnter a 4 digit pin: ")
        

    def show_account(a):    #function to show data on screen                                                
        print ("\nAccount No. :", a.acno)
        print ("\nAccount holder name: ", a.name)
        print ("\nType of account", a.acc_type )
        print ("\nBalance amount: ", a.deposit)
  


    def modify_acc(a,choice):          #function to get new data from user                                  
        print ("\nAccount No. : ", a.acno)
        if choice == '1':                                                                                   
            a.name=input("\n\nEnter the name of account holder: ")
        elif choice == '2':
            a.age=input("\n Enter the age: ")
        elif choice == '3':
            a.pin = input("\n Enter a 4 digit pin: ")
        else:
            print("Invalid choice!!")

 

    def add_amount(a,x):           #function to accept amount and add to balance
        a.deposit+=x

    def sub_amount(a,x):          #function to accept amount and subtract from balance amount
        a.deposit-=x

    def show_details(a):          #function to show data in tabular format
        print ("%-10s"%a.acno,"%-20s"%a.name,"%-10s"%a.acc_type,"%-10s"%a.deposit,"%-10s"%a.age)

    def return_acno(a):         #function to return account number
        return a.acno

    def return_balance(a):      #function to return balance amount 
        return a.deposit

    def return_actype(a):         #function to return type of account
        return a.acc_type
    
    def return_pin(a):
        return a.pin           #function to return pin

    def ret_age(a):            #function to return age
        return a.age
    
"""-----------------------------------------------------------------------------
                    FUNCTION TO GENERATE UNIQUE ACCOUNT NUMBER -                
--------------------------------------------------------------------------------"""

def generate_acno():                                                                                        
    
    try:                                                                                    
    
        
        '''
        codifying_7E2_acc.txt is a file used to generate a unique account number.
        We manually entered an initial account number in the file
        and later for every new account created, the value stored
        in the file is increemented by 1.
        This increemented value is returned as the new account number
        '''
        
        inFile=open("codifying_7E2_acc.txt","r")  #file read operation 
        n=int(inFile.read())
       
        n+=1
        inFile.close()
        
        inFile=open("codifying_7E2_acc.txt","w")  #file write operation
        inFile.write(str(n))
        inFile.close()
        
        
        return n
        """
        when an input/output operation fails, such as the print statement or the open() function
        when trying to open a file that does not exist.
    
        """
    except IOError:
        print ("I/O error occured")

"""-----------------------------------------------------------------------------
                    FUNCTION TO WRITE RECORD IN BINARY FILE
--------------------------------------------------------------------------------"""

def write_account():                                                                                        
    
    try:                                                                                                                                                                                                          
        
        ac=account()
        '''
        codifying_7E2_account.dat file is used to store account details of clients as
        a binary database.The details entered by the user is converted into a
        binary text using pickle.dump()
        
        '''
        outFile=open("codifying_7E2_account.dat","ab") #binary file append operation
        
        ac.acno= generate_acno()    
       
        ac.create_account()
        pickle.dump(ac,outFile)
        outFile.close()
        print ("\n\n Account Created Successfully")
        print ("\n\n YOUR ACCOUNT NUMBER IS: ",ac.return_acno())
    except Exception as e :
            print("Error",e)
            pass
        
"""-----------------------------------------------------------------------------
                FUNCTION TO DISPLAY ACCOUNT DETAILS GIVEN BY USER
--------------------------------------------------------------------------------"""

def display_separate(n,l):                                                                                      
    flag=0
    try:
        inFile=open("codifying_7E2_account.dat","rb")
        print("\n")
        print(20*"-")
        print ("BALANCE DETAILS")
        print(20*"-")
        while True:
            ac=pickle.load(inFile)
            
            if ac.return_acno()==int(n)and ac.return_pin() == l:
                ac.show_account()
                flag=1
                
        '''
        when pickle.load() function hits an end-of-file condition (EOF)
        without reading any data.
        '''
    except EOFError:
        inFile.close()
        
        '''
        if the entered account number and pin doesn't match with any record in
        codifying_7E2_account.dat file, then flag will be 0.
        
        '''
        
        if flag==0:
            print ("\n\nAccount number does not exist or Incorrect pin ")

    except IOError:
        print ("File could not be open !! Press any Key...")   
        

"""----------------------------------------------------------------------------
                        FUNCTION TO MODIFY RECORD OF FILE
--------------------------------------------------------------------------------"""       


def modify_account(n,l):                                                                                        
    found=0
    try:
        inFile=open("codifying_7E2_account.dat","rb")
        '''
        codifying_7E2_temp.dat is a file used to make any modifications in the codifying_7E2_account.dat file.
        The existing details are read from the codifying_7E2_account.dat file and updates are written
        in codifying_7E2_temp.dat file.
        Later we will remove codifying_7E2_account.dat file and rename codifying_7E2_temp.dat file as the updated
        codifying_7E2_account.dat file using os module.
        
        '''
        outFile=open("codifying_7E2_temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.return_acno()==int(n) and ac.return_pin()== l:
                print (30*"-")
                ac.show_account()
                print (30*"-")
                print("\n")
                print("1. to change the name of the account holder")
                print("2. to change the age of the account holder")
                print ("3. to change the pin of the account")
                choice=input("\nEnter option(1-3): ")
                ac.modify_acc(choice)
                pickle.dump(ac,outFile)
                print ("\n\n\tRecord Updated")
                found=1
            else:
                pickle.dump(ac,outFile)
             
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nRecord Not Found ")

    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("codifying_7E2_account.dat")
    os.rename("codifying_7E2_temp.dat","codifying_7E2_account.dat")


"""-----------------------------------------------------------------------------
                    FUNCTION TO DELETE RECORD OF FILE
---------------------------------------------------------------------------------"""

def delete_account(n,l):                                                                                        
    found=0

    try:
        inFile=open("codifying_7E2_account.dat","rb")
        outFile=open("codifying_7E2_temp.dat","wb")
        while True:
            ac=pickle.load(inFile)
            if ac.return_acno()==int(n)and ac.return_pin()== l:
                found=1
                print ("\n\n\tRecord Deleted ..")
            else:
                pickle.dump(ac,outFile)

    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nAccount number does not exist or Incorrect pin ")

    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("codifying_7E2_account.dat")
    os.rename("codifying_7E2_temp.dat","codifying_7E2_account.dat")
    
    
"""------------------------------------------------------------------------------
                    FUNCTION TO DISPLAY ALL ACCOUNT DETAILS
--------------------------------------------------------------------------------"""


def display_all():                                                                                               
    print ("\n\n\tACCOUNT HOLDER LIST")
    print ("  ",30*"-",'\n')
    print (60*"=")
    print ("%-10s"%"A/C No.","%-20s"%"Name","%-10s"%"Type","%-10s"%"Balance","%-10s"%"Age")
    print (60*"=","\n")
    try:
        inFile=open("codifying_7E2_account.dat","rb")
        while True:
            ac=pickle.load(inFile)
            ac.show_details()
        inFile.close()   
    except EOFError:
        inFile.close()
        
    except IOError:
        print ("File could not be open !! Press any Key...")


"""----------------------------------------------------------------
                 FUNCTION TO DEPOSIT AMOUNT FOR GIVEN ACCOUNT
--------------------------------------------------------------------"""


def deposit_amt(n,l):                                                                                           
    found=0

    try:
        inFile=open("codifying_7E2_account.dat","rb")
        outFile=open("codifying_7E2_temp.dat","wb")

        while True:
            ac=pickle.load(inFile)
           
            if ac.return_acno()==int(n)and ac.return_pin()== l :
                ac.show_account()
                print (" ",30*"-")
                print ("\tTO DEPOSIT AMOUNT")
                print (" ",30*"-")
                amt=int(input("\nEnter the amount to be deposited: "))
                ac.add_amount(amt)

                pickle.dump(ac,outFile)
                found=1
                print ("\n\n\tRecord Updated")
            else:
                pickle.dump(ac,outFile)
                
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nAccount number does not exist or Incorrect pin ")
    
    except IOError:
        print ("File could not be open !! Press any Key...")

    os.remove("codifying_7E2_account.dat")
    os.rename("codifying_7E2_temp.dat","codifying_7E2_account.dat")

"""-----------------------------------------------------------
        FUNCTION TO WITHDRAW AMOUNT FOR GIVEN ACCOUNT
----------------------------------------------------------------"""    


def withdraw_amt(n,l):                                                                                          
    found=0

    try:
        inFile=open("codifying_7E2_account.dat","rb")
        outFile=open("codifying_7E2_temp.dat","wb")

        while True:
            ac=pickle.load(inFile)
           
            if ac.return_acno()==int(n)and ac.return_pin()== l :
                ac.show_account()
                print (" ",30*"-")
                print ("\tTO WITHDRAW AMOUNT")
                print (" ",30*"-")
                amt=int(input("\nEnter amount to be withdraw: "))
                bal=ac.return_balance()-amt

                if ((bal<500 and ac.return_actype()=="S")or(bal<1000 and ac.return_actype()=="C")):
                    print ("\nINSUFFICIENT BALANCE")
                else:
                    ac.sub_amount(amt)
                pickle.dump(ac,outFile)
                found=1
                print ("\n\n\tRecord Updated")
            else:
                pickle.dump(ac,outFile)
                
    except EOFError:
        inFile.close()
        outFile.close()
        if found==0:
            print ("\n\nAccount number does not exist or Incorrect pin ")
    
    except IOError:
        print ("\nFile could not be open !! Press any Key...")

    os.remove("codifying_7E2_account.dat")
    os.rename("codifying_7E2_temp.dat","codifying_7E2_account.dat")

"""-----------------------------------------------------------
        FUNCTION TO PRINT THE LIST OF AGE GROUP 
----------------------------------------------------------------""" 
  
def age_group():                                                                                                
    l=[]               # List to append the age of the user

    inFile=open("codifying_7E2_account.dat","rb")
    while True:
        try:
            ac=pickle.load(inFile)
            l.append(ac.ret_age())
        except EOFError:
            break
    inFile.close()

    
    ag.age_grp(l)
    

"""  ************************
              MAIN
     ************************        """

print(" ")

print (30*"*")
print ("\tWELCOME !!")
print (3*" ","NETBANKING SYSTEM")
print (30*"*")    
print ("\n",30*"-")
print (" ","MADE BY : ABHIN and KRISHNAVENI ")
print (" ","Team ID : codifying-7E2")
print (30*"-")


while True:
    print (3*"\n",60*"=")
    print ("\tMAIN MENU")
    print (" ",30*"-")
    print("""
    1. NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY
    5. ALL ACCOUNT HOLDER LIST
    6. CLOSE AN ACCOUNT
    7. MODIFY AN ACCOUNT
    8. CHECK IFSC CODE
    9. LIST OF AGE GROUPS
    10.HOLIDAY LIST
    0. EXIT
    """)
    print(" ",30*"-")

    try:
        ch=input("\n  Enter Your Choice(0-10): ")
        if ch=='1':
            write_account()
        
        elif ch=='2':
            num=input("\n\nEnter Account Number: ")
            upin = input("\nEnter pin :")
            deposit_amt(num,upin)

        elif ch=='3':
            num=input("\n\nEnter Account Number: ")
            upin = input("\nEnter pin :")
            withdraw_amt(num,upin)

        elif ch=='4':
            num=input("\n\nEnter Account Number: ")
            upin = input("\nEnter pin :")
            display_separate(num,upin)

        elif ch=='5':
            display_all()

        elif ch=='6':
            num=input("\n\nEnter Account Number: ")
            upin = input("\nEnter pin :")
            delete_account(num,upin)
        
        elif ch=='7':
            num=input("\n\nEnter Account Number: ")
            upin = input("\nEnter pin: ")
            modify_account(num,upin)

        elif ch == '8':
            
            codifying_7E2_ifsc.ifsc()
            
        elif ch=='9':
            age_group()  

        elif ch == "10":
            print (" ",30*"-")
            month =input("  Enter month : ")
            month=month.capitalize()
            date = input("  Enter date: ")
            print (" ",30*"-","\n")
            inp_date = month+" "+date
            codifying_7E2_check_holiday.check(inp_date)
                    
        elif ch=='0':
            break

        else:
            print("\nPlease Input  a correct choice.....(0-10)")

    except :
       
        print ("Error")
        
input("\n\n\n\n\nTHANK YOU\n\nPress any key to exit...")

