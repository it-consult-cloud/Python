import time
t = time.time()
print(t)
print(time.ctime(t))
print(time.localtime())
date_struct=time.localtime()
# print(date_struct)
formatedtime = time.strftime('Number %d Mont number %m year %y', date_struct)
print(formatedtime)

print('HELLO')
time.sleep(5)
print('world')


