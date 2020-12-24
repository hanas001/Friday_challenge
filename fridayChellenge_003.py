#string = 'hello, how are you?'         #to test
string = input()                       #user input in python 3
#string = raw_input()                    #user input in python 2
newString = []

for i in range(len(string)+1):
    if i > 0:
        newString.append(string[-i])

print (''.join(newString))