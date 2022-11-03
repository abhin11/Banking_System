'''

age module-
Module to print the list of age groups

'''

'''

Function to print the list of age group
It takes the list as argument and arrange these values to
a age_dict dictionary. 

'''
def age_grp(l):

    age_dict={}
    age_dict["Below 18"]=age_dict["18-30"]=age_dict["30-45"]=age_dict["45-60"]=age_dict["60 & above"]=0      
    for i in range(len(l)): # for loop to enter the values to the dictionary age_dict
            if l[i]>='0' and l[i]<'18':   
               age_dict["Below 18"]+=1
            elif l[i]>='18' and l[i]<'30':
               age_dict["18-30"]+=1
            elif l[i]>='30' and l[i]<'45':
               age_dict["30-45"]+=1
            elif l[i]>='45' and l[i]<'60':
               age_dict["45-60"]+=1
            else:
               age_dict["60 & above"]+=1
    print('\n')           
    print(30*"-")           
    print("LIST OF AGE GROUPS:")
    print(30*"-")
    for key,val in age_dict.items():
        print("%-10s"%key,":",val)
