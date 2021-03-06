import threading 

from threading import*
import time

d={} #'d' is the dictionary in which we store data

#create operation 
def create(key,value,timeout=0):
    if key in d:
        print("Error: This key already exists") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
            else:
                print("Error: Memory limit exceeded!! ")
        else:
            print("Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")

#read operation
def read(key):
    if key not in d:
        print("Error: Given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("Error: Time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#delete operation
def delete(key):
    if key not in d:
        print("Error: Given key does not exist in database. Please enter a valid key") 
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("Key is successfully deleted")
            else:
                print("Error: time-to-live of",key,"has expired") 
        else:
            del d[key]
            print("Key is successfully deleted")

