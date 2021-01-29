size = []

ff = open('updatedSchema.txt', "w+")
f = open('test.txt', "r")
for line in f:
    l = line.split(",")
    for newLine in open('schema.txt'):
        if(newLine.startswith(l[0])):
            size.append(newLine)
    if((len(size))>1):
            print(max(size))
            ff.write(max(size))
            ff.write('\n')
    else:
        ff.write(str(size[0]))
        ff.write('\n')
    print(len(size))    
    print(size)
    size = []


with open('updatedSchema.txt','w+') as file:
    for line in file:
        if not line.isspace():
            file.write(line)

ff.truncate()
f.close()
ff.close()
            
    
