import time 
time_stamp=time.strftime("%H:%M:%S")
print (time_stamp)
timen= int (time.strftime("%H"))
if (timen<12):
    print ("Good morning ")
elif (timen<16):
    print ("good afternoon ")
elif (timen<21):
    print ("good evening ")
else:
    print ("good night ")