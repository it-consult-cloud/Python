# Создать программу, которая будет выводить информацию о
# компьютере на котором запущена (ОС, Платформа, количество ядер)

import platform
import os

info = platform.uname()
print("OS: " + (info.system) + (info.release))

# print(info.node)
# print(info.machine)

print("CPU type: " + (info.processor))

print (f"CPU count:", + (os.cpu_count()))
print('or')
print (f"CPU count:",   (os.environ['NUMBER_OF_PROCESSORS']))