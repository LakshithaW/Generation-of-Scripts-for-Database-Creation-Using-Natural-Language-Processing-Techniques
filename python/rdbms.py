

f= open("../users/RDBMS.txt" , 'w+')
for line in open("../users/norama.txt" , 'r+'):
    Array = line.split(",")
   


    #print("create table " +Array[0]+"(")
    f.write("create table " +Array[0]+"(")
    f.write('\n') 
    for x in range(1, len(Array)):
        value = Array[x].split("-")
    
        if value[0].strip() == "P":
            #print(len(Array))
            if x == len(Array)-1:
                    
                #print(value[0]+" varchar(50) NOT NULL primary key")
                    
                f.write(value[0]+" varchar(50) NOT NULL primary key")
                f.write('\n') 
                
            else:
                #print(value[0]+" varchar(50) NOT NULL primary key,")
                f.write(value[0]+" varchar(50) NOT NULL primary key,")
                f.write('\n') 
        elif value[0].strip() == "F":
          
            for line in open("../users/entity1.txt" , 'r+'):
                lines = line.split(",")
                for i in range(1, len(lines)-1):
                    v = lines[i].split("-")
                    if v[1].strip() == "P":
                        if value[0] == v[0]:
                            if x == len(Array)-1:
                                    #print(value[0]+" varchar(50),")
                                f.write(value[0]+" varchar(50),")
                                    #print("CONSTRAINT "+lines[0]+"_"+value[0]+" FOREIGN KEY ("+ value[0] +") REFERENCES "+ lines[0] +" ("+value[0]+")")
                                f.write("CONSTRAINT "+lines[0]+"_"+value[0]+" FOREIGN KEY ("+ value[0] +") REFERENCES "+ lines[0] +" ("+value[0]+")")
                                f.write('\n') 
                            else:
                                    #print(value[0]+" varchar(50),")
                                f.write(value[0]+" varchar(50),")
                                    #print("CONSTRAINT "+lines[0]+"_"+value[0]+" FOREIGN KEY ("+ value[0] +") REFERENCES "+ lines[0] +" ("+value[0]+"),")
                                f.write("CONSTRAINT "+lines[0]+"_"+value[0]+" FOREIGN KEY ("+ value[0] +") REFERENCES "+ lines[0] +" ("+value[0]+"),")
                                f.write('\n') 
                                break
        else:
            if x == len(Array)-1:
                    #print(value[0]+" varchar(50) NOT NULL")
                f.write(value[0]+" varchar(50) NOT NULL")
                f.write('\n') 
            else:
                     #print(value[0]+" varchar(50) NOT NULL,")
                f.write(value[0]+" varchar(50) NOT NULL,")
                f.write('\n') 
            
        #print(");")
    f.write(");")
    f.write('\n') 
        #print(" ")
    f.write(" ")

f.close()
