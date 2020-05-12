import os
import platform

login = os.getlogin()
print(login)
cwd =os.getcwd()
print(cwd)
print('folder')
folder = os.system('dir')

info = platform.uname()
print(info.system)
print(info.node)
print(info.release)
print(info.machine)
print(info.processor)


