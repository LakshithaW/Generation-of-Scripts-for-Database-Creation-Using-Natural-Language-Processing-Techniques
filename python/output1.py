f = open("../users/output1.txt"  , 'w+')
with open('../users/output.txt' ) as fp:
    for lines in fp:
            words = lines.strip('\n')
            array = words.split(',')
            for l in range(0 , len(array)-1):
                if(len(array)-2 == l):
                     
                    f.write(array[l])
                    f.write('\n')
                    #print(array[l])
                else:
                    f.write(array[l]+',')
                    #print(array[l]+',')
             

f.close()


fd = open("../users/entity1fin.txt"  , 'w+')
with open('../users/entity1.txt' ) as fp1:
    for lines in fp1:
            words = lines.strip('\n')
            array = words.split(',')
            for l in range(0 , len(array)-1):
                if(len(array)-2 == l):
                     
                    fd.write(array[l])
                    fd.write('\n')
                    #print(array[l])
                else:
                    fd.write(array[l]+',')
                        #print(array[l]+',')
             

fd.close()
