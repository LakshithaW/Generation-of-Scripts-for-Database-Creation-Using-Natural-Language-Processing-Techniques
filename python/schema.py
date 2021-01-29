f= open("../users/schema.txt",'r+')
Entity = []

for line in open('../users/entity2.txt' ):
    lines = line.rstrip('\n')
    lineArray = lines.split(",")
    value1 = lineArray[0].split("-",2)
    value2 = lineArray[2].split("-",2)
# one to one
    if value1[1].strip() == "One" and value2[1].strip() == "One" :
        for l in open("../users/entity1.txt" ):
            ll = l.rstrip('\n')
            Attribute = ll.split(",")
            if Attribute[0] == value1[0]:
                for x in range(1,len(Attribute)-1):
                    att = Attribute[x].split("-",2)
                    if att[1] == "P":
                        primary1 = att[0]
                        
        for l in open("../users/entity1.txt" ):
            ll = l.rstrip('\n')
            Attribute = ll.split(",")            
            if Attribute[0] == value2[0]:
                s = "false"
                #print(Entity)
                for k in range(0,len(Entity)):
                        if Attribute[0] == Entity[k]:
                                #print("hi")
                                s = "true"

                if s == "true":
                        with open('../users/schema.txt' ,'r+') as f:
                            for line in f:
                                 
                            
                                 if line.startswith(Attribute[0]):
                                     
                                        dnew = line.strip()+","+primary1+"-F,"
                                        #print(line)
                                        #print(dnew)
                                        lin = line.replace(line,dnew)
                                        f.write(lin)
                                        f.write("\n")
                                        break

                else:
                    f= open("../users/schema.txt",'a+')
                    f.write(Attribute[0]+",")
                    #print(Attribute[0]+"(", end=" ")
                    for y in range(1, len(Attribute)-1):
                        f.write(Attribute[y]+",")    
                        #print(Attribute[y]+",", end=" ")
                    #print(primary1+"-F )")
                    f.write(primary1+"-F,")
                    Entity.append(Attribute[0])
                    f.write("\n")
#one to many
    elif value1[1] == "one" and value2[1] == "Many" :
        for l in open("../users/entity1.txt" ):
            ll = l.rstrip('\n')
            Attribute = ll.split(",")
            if Attribute[0] == value1[0]:
                for x in range(1,len(Attribute)-1):
                    att = Attribute[x].split("-",2)
                    if att[1] == "P":
                        primary1 = att[0]
                        
        for l in open("../users/entity1.txt" ):
            ll = l.rstrip('\n')
            Attribute = ll.split(",")            
            if Attribute[0] == value2[0]:
                s = "false"
                #print(Entity)
                for k in range(0,len(Entity)):
                        if Attribute[0] == Entity[k]:
                                
                                s = "true"

                if s == "true":
                        with open('../users/schema.txt' ,'r+') as f:
                            for line in f:
                                    #print(line)
                            
                                    if line.startswith(Attribute[0]):
                                        #print("svvree")
                                        dnew = line.strip()+","+primary1+"-F,"
                                        f.write(dnew)
                                        f.write("\n")
                                        break
                else:
                    f= open('../users/schema.txt' ,'a+')
                    f.write(Attribute[0]+",")
                    #print(Attribute[0]+"(", end=" ")
                    for y in range(1, len(Attribute)-1):
                        f.write(Attribute[y]+",")
                        #print(Attribute[y]+",", end=" ")
                    #print(primary1+"-F )")
                    f.write(primary1+"-F,")
                    Entity.append(Attribute[0])
                    f.write("\n")        
#many to one
    elif value1[1] == "Many" and value2[1] == "one" :
        
        for l in open("../users/entity1.txt" ):
            ll = l.rstrip('\n')
            Attribute = ll.split(",")
            if Attribute[0] == value2[0]:
                for x in range(1,len(Attribute)-1):
                    att = Attribute[x].split("-",2)
                    if att[1] == "P":
                        primary1 = att[0]
                        
        for l in open("../users/entity1.txt" ):
            ll = l.rstrip('\n')
            Attribute = ll.split(",")            
            if Attribute[0] == value1[0]:
                s = "false"
                #print(Entity)
                for k in range(0,len(Entity)):
                        if Attribute[0] == Entity[k]:
                                #print("hi")
                                s = "true"

                if s == "true":
                        #print("jjhgh")
                        with open('../users/schema.txt' ,'r+') as f:
                            for line in f:
                                    #print(line)
                            
                                    if line.startswith(Attribute[0]):
                                        #print(line)
                                        dnew = line.strip()+","+primary1+"-F,"
                                        f.write(dnew)
                                        f.write("\n")
                                        break
                else:
                    f= open('../users/schema.txt' ,'a+')
                    f.write(Attribute[0]+",")
                    #print(Attribute[0]+"(", end=" ")
                    for y in range(1, len(Attribute)-1):
                        f.write(Attribute[y]+",")
                         
                    f.write(primary1+"-F,")
                    Entity.append(Attribute[0])
                
                    f.write("\n")       
#many to many
    elif value1[1] == "Many" and value2[1] == "Many" :
            
        for l in open("../users/entity1.txt" ):
            ll = l.rstrip('\n')
            Attribute = ll.split(",")
                
            if Attribute[0] == value1[0]:
                for x in range(1,len(Attribute)-1):
                    att = Attribute[x].split("-",2)
                    if att[1] == "P":
                        primary1 = att[0]
                        
        for l in open("../users/entity1.txt" ):
            ll = l.rstrip('\n')
            Attribute = ll.split(",")            
            if Attribute[0] == value2[0]:
                for y in range(1, len(Attribute)-1):
                    att = Attribute[y].split("-",2)
                    if att[1] == "P":
                        primary2 = att[0]
            
            
        f.write(value1[0]+"_"+value2[0]+","+primary1+"-P ,"+primary2+"-P,")
        f.write("\n")
            
       
    
f= open('../users/schema.txt','a+')
for line in open("../users/entity1.txt" ):
    lines = line.rstrip('\n')
    lineArray = lines.split(",")
    status = "false"
    for k in range(0,len(Entity)):
        if lineArray[0] == Entity[k]:
            status = "true"


    if status == "false":
            f.write(lineArray[0]+",")    
                
            for y in range(1, len(lineArray)):
                        
                    if y == len(lineArray)-1:
                        f.write(lineArray[y])
                    else:
                        f.write(lineArray[y]+",")
                   
                
            f.write("\n")
f.close()

            
    


