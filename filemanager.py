from time import sleep

x = input('Type whatever you want: ')

with open('file.txt', 'w') as myFile:
    myFile.write(x)

sleep(1)

with open('file.txt', 'r') as myFile:
    print(myFile.read())

