import string 
import random 

def passgen():
    lenpass=int (input("Enter thr length of the pssword :"))
    # s1 = string.ascii_letters 
    # s2= string.ascii_uppercase
    # s3= string.ascii_lowercase
    # s4=string.digits
    # s5= string.punctuation

    s6= list (string.printable)
    random.shuffle(s6)
    password = ("".join(s6[0:lenpass ]))
    print (password )
passgen()