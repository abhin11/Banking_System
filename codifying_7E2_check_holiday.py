'''

Check_holiday module
Module to check if the entered date
is a bank holiday or not.

'''

'''

bank_holidays_2021.txt is a text file that stores the list of all the bank holidays in the
year 2021 in the format: [Month] [Date],[Day],[Holiday]\n

'''

holiday_file = open("codifying_7E2_bank_holidays_2021.txt","r")

'''

After reading the input file the values of each line are split into 3 lists.
The date given by the user is compared to all the strings in date[] list.
If any of the strings match with the entered date string, the module returns
the date, day and reason for holiday. If no matches are found, the module prints
that it is not a bank holiday.

'''
date = []
day = []
holiday = []
    
for line in holiday_file:
    temp_list = []
    temp_list = line.strip().split(',')
    date.append(temp_list[0])
    day.append(temp_list[1])
    holiday.append(temp_list[2])
        

holiday_file.close()

n = len(date)



def check(check_date):  
    flag = 0
   
    for i in range(0,n):
        if date[i] == check_date:
            flag = 1
            print (20*"*")
            print ("Bank holiday")
            print (20*"*")
            print ("YEAR : 2021")
            print (70*"-")
            print ("%-20s"%"DATE:","%-20s"%"DAY","%-10s"%"HOLIDAY")
            print (70*"-")
            print ("%-20s"%date[i],"%-20s"%day[i],"%-10s"%holiday[i])
            print (70*"-")
            break
    if flag == 0:
        print("\nNot a Bank holiday\n")
        
