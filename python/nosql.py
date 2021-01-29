
f= open("../users/NOSQL.txt" ,"w+")
for line in open('../users/output1.txt' , 'r+'):
    Array = line.split(",")
   


    #print("db."+Array[0]+".insert"+ "({")
    f.write("db."+Array[0]+".insert"+ "({")
    f.write('\n')
    for x in range(1, len(Array)):
        value = Array[x].split("-")
    
        if value[1].strip() == "P":
            if x == len(Array)-1:
                #print(value[0]+": ,")
                f.write(value[0]+": ,")
                f.write('\n')
            else:
                #print(value[0]+": "",")
                f.write(value[0]+": "",")
                f.write('\n')
        elif value[1].strip() == "F":
          
            for line in open('../users/entity1.txt' , 'r+'):
                lines = line.split(",")
                for i in range(1, len(lines)-1):
                    v = lines[i].split("-")
                    if v[1].strip() == "P":
                        if value[0] == v[0]:
                            if x == len(Array)-1:
                                #print(value[0]+": "",")
                                f.write(value[0]+": "",")
                                f.write('\n')
                                #print(lines[0]+"_"+value[0]+": db."+ lines[0] +".find()[0]._id")
                                f.write(lines[0]+"_"+value[0]+": db."+ lines[0] +".find()[0]._id")
                                f.write('\n')
                            else:
                                #print(value[0]+": "",")
                                f.write(value[0]+": "",")
                                f.write('\n')
                                #print(lines[0]+"_"+value[0]+": db."+ lines[0] +".find()[0]._id")
                                f.write(lines[0]+"_"+value[0]+": db."+ lines[0] +".find()[0]._id")
                                f.write('\n')
                                break
        else:
            if x == len(Array)-1:
                #print(value[0]+": "",")
                f.write(value[0]+": "",")
                f.write('\n')
            else:
                #print(value[0]+": "",")
                f.write(value[0]+": "",")
                f.write('\n')
                
            
    #print("});")
    f.write("});")
    f.write('\n')
    #print(" ")
    f.write('\n')
    f.write(" ")
f.close()
