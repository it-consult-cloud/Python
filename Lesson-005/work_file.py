
file = open('test_file.txt', encoding='utf-8')

for line in  file:
    print(line.strip())

    # r = file.readlines()
    # print(r)
    print(line.strip())
    r = file.readlines()
    print(r)

for i in range(10,20):
    file.write(str(i))

    file.close()
