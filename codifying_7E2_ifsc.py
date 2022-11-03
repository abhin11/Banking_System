'''

IFSC module-
MODULE TO RETURN THE IFSC CODE
OF THE BRANCH ENTERED BY THE USER

'''

def ifsc():
        
        try:

             '''
             IFSC_dict is used to store the names of branches as keys
             and its corresponding IFSC code values as values.
             The Branch entered by the user is passed as a key in the
             dictionary and its value is returned as the IFSC code.
             
             '''
             IFSC_dict = {}
             '''
             IFSCcode.txt is a text file that stores a list of branches and
             its IFSC code, this file is read and stored into IFSC_dict.
             
             '''
             inp_file = open("codifying_7E2_IFSCcode.txt","r")
             
             '''
             for loop used to iterate over the lines of the input file
             '''
             for line in inp_file:
                k, v = line.strip().split(',')
                IFSC_dict[k.strip()] = v.strip()
             inp_file.close()
             print("\n")
             print("Cities")
             print(10*"-")
             for key in IFSC_dict.keys(): 
                print(key)
             branch = input("\nEnter Branch: ")
             print("\nIFSC code :", IFSC_dict[branch])

             '''
             If the branch entered doesnt exist in the dictionary,
             the module will throw a KeyError
             
             '''
        except KeyError:
             print("\nInvalid branch")
