
import os
import time



for i in range (1,5000):
    f = time.sleep(10)    # pauses for 5 seconds
    o = open("test1.py", "w")
    o.write("{} print('This is a Django/Python file for testing pupose')".format(i))


    os.system(r"C:\Users\test\Desktop\test\test\m.bat")