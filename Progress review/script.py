for line in open('updatedSchema.txt', 'r+'):
    Array = line.split(",")
   


    print("create table " +Array[0]+"(")
    for x in range(1, len(Array)):
        value = Array[x].split("-")
    
        if value[1].strip() == "P":
            if x == len(Array)-1:
                print(value[0]+" varchar(50) NOT NULL primary key")
            else:
                print(value[0]+" varchar(50) NOT NULL primary key,")
        elif value[1].strip() == "F":
          
            for line in open('test.txt', 'r+'):
                lines = line.split(",")
                for i in range(1, len(lines)):
                    v = lines[i].split("-")
                    if v[1].strip() == "P":
                        if value[0] == v[0]:
                            if x == len(Array)-1:
                                print(value[0]+" varchar(50),")
                                print("CONSTRAINT "+lines[0]+"_"+value[0]+" FOREIGN KEY ("+ value[0] +") REFERENCES "+ lines[0] +" ("+value[0]+")")
                                
                            else:
                                print(value[0]+" varchar(50),")
                                print("CONSTRAINT "+lines[0]+"_"+value[0]+" FOREIGN KEY ("+ value[0] +") REFERENCES "+ lines[0] +" ("+value[0]+"),")
                                break
        else:
            if x == len(Array)-1:
                print(value[0]+" varchar(50) NOT NULL")
            else:
                 print(value[0]+" varchar(50) NOT NULL,")
                
            
    print(");")
    print(" ")
