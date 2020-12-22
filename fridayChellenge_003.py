string = 'hello, how are you?'
newString = []

for i in range(len(string)):
    if i > 0:
        print (i)
        newString.append(string[-i])

print (newString)