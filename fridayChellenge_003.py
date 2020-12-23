#string = 'hello, how are you?'  #to test
string = input()                #user input
newString = []

for i in range(len(string)+1):
    if i > 0:
        newString.append(string[-i])

print (''.join(newString))  #for python 3
#print ''.join(newString)    #for python 2.7