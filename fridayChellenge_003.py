string = 'hello, how are you?'
newString = []

for i in range(len(string)+1):
    if i > 0:
        newString.append(string[-i])

#print (type(newString))
#print (newString, sep="")  #for python 3
print "".join(newString)    #for python 2.7