import re
print('start program')
# f = open('test1.txt', 'r')#, encoding='utf-16')
# s = f.readlines()
# # lines = list(s)
# print(s)
# f.close()

with open('test1.txt', 'r+', encoding='utf-8') as file:
    while True:
        #s = file.readline()
        s = file.read()
        if s != "":
            print(s)
            sn = re.sub(r' ', r'', s)
            print(sn)
        else:
            print('Break')
            file.close() #not nesessery with 'with'
            break


