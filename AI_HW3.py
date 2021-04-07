import numpy as np
from functools import reduce


minn = int(input("Min: "))
maxn = int(input("max: "))

#a = np.binary_repr(1)
#print(a)
#initializing Lists
listn = []
listb = []

#Normalization
maxn = maxn - minn
while maxn!=0 :
   # print("*")
  #  print(listn)
  #  print(listb)
    #Convert to binary
    maxb = np.binary_repr(maxn)
    maxbsb = str(maxb)
    nmaxb = len(maxbsb)

 #   print("binary")
 #   print(maxb)

 #   print("number")
 #  print(maxn)

    #variables
    flag = True
    temp = ""

    for i in range(nmaxb):
  #      print("^^^")
   #     print(maxbsb[i])
        if(maxbsb[i]=="0"):
    #        print("&")
            flag = False
            break

    if flag == True:
 #       print("%")
        listn.append(maxn)
        listb.append(nmaxb)
        break
    else:
        listb.append(nmaxb-1)
        for i in range(nmaxb-1):
            temp = temp + "1"
    #    print("temp")
    #    print(temp)
        num = int(temp, 2)
       # num = int(''.join(map(lambda temp: str(int(temp)), temp)), 2)
   #     num = reduce(lambda a,b: 2*a+b, temp)
  #      print("num")
   #     print(num)
        listn.append(num)
        maxn = maxn - int(num)
   #     print("maxn")
   #     print(maxn)

print(f"listn: {listn}")
print(f"listb: {listb}")



