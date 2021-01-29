size = []

ff = open('../users/updatedSchema.txt', "w+")
f = open("../users/entity1.txt" , "r")
for line in f:
    l = line.split(",")
    for newLine in open('../users/schema.txt'):
        if(newLine.startswith(l[0])):
            size.append(newLine)
    if((len(size))>1):
            #print(max(size))
            ff.write(max(size))
            ff.write('\n')
    else:
        ff.write(str(size[0]))
        ff.write('\n')
    #print(len(size))    
    #print(size)
    size = []



with open('../users/updatedSchema.txt','w+') as file:
    for line in file:
        array= line.split(",")
        for l in range(0, len(array)):
            if(len(array) == l):
                file.write(array[l])
            else:
                file.write(array[l]+",")

ff.truncate()
f.close()
ff.close()
            
    
