Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: D:/Freshworkers/mainfile.py =====================
>>> import mainfile as test
>>> 
>>> #create function
>>> test.create("Shree",70)
>>> test.create("Jazz",50,120)
>>> #here 120 seconds is the Time-to-live value
>>> 
>>> test.read("Shree")
'Shree:70'
>>> test.read("Jazz")
'Jazz:50'
>>> 
>>> test.create("Santa",60)
>>> test.create("Jazzshree",345)
>>> 
>>> #delete function
>>> test.delete("Jazz")
Error: time-to-live of Jazz has expired
>>> test.read("Jazz")
Error: Time-to-live of Jazz has expired
>>> #here the 120seconds has expired and returns an error
>>> 
>>> test.delete("Shree")
Key is successfully deleted
>>> 
>>> test.read("Shree")
Error: Given key does not exist in database. Please enter a valid key
>>> 
>>> test.create("Jazz")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    test.create("Jazz")
TypeError: create() missing 1 required positional argument: 'value'
>>> test.create("Santa",30)
Error: This key already exists
>>> 
>>> #trying to give a key_name with special characters
>>> test.create("sas34",10)
Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> test.create("shree@",20)
Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> test.create("key name",35)
Error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers
>>> test.create("annauniversity",7316)
>>> test.read("annauniversity")
'annauniversity:7316'
>>> test.delete("annauniverrsity")
Error: Given key does not exist in database. Please enter a valid key
>>> test.delete("annauniversity")
Key is successfully deleted
>>> 