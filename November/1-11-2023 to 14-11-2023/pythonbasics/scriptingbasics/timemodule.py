import time

epc=time.time()
print(epc)

localtime=time.localtime(epc)
print(localtime)

print(time.ctime(epc))