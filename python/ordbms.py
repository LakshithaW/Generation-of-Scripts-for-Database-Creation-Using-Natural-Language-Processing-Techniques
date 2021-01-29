import sys

f= open("../users/ORDBMS.txt" ,"w+") 
for line in open('../users/output1.txt', 'r+'):
    y = line.rstrip(',')
    primary = 0;
    foreign_key = 0;
    foreign_origin = 0;
    exists = 0;
    lst = [];
    e = 0;
    Array = y.split(",")
    #print("create type " +Array[0]+"_type as object"+"(")
    f.write("create type " +Array[0]+"_type as object"+"(")
    f.write('\n')
    for x in range(1, len(Array)):
        value1 = Array[x].strip()
        value = value1.split("-")
    
        if value[1].strip() == "P":
            e = 1
            if x == len(Array)-1:
                primary = value[0]
                #print(primary+" varchar(50),")
                f.write(primary+" varchar(50)")
                f.write('\n')
            else:
                primary = value[0]
                #print(primary+" varchar(50),")
                f.write(primary+" varchar(50),")
                f.write('\n')
        elif value[1].strip() == "F":
          
            for line in open('../users/entity1fin.txt', 'r+'):
                lines = line.split(",")
                for i in range(1, len(lines)):
                    vv = lines[i].strip()
                    v = vv.split("-")
                    if v[1].strip() == "P":
                        if value[0] == v[0]:
                            foreign_key = value[0]
                            foreign_origin = lines[0]
                            exists = 1
                            if x == len(Array)-1:
                                f.write(foreign_key+" Ref "+foreign_origin+"_type")
                                #print(foreign_key+" Ref "+foreign_origin+"_type,")
                                f.write('\n')
                            else:
                                #print(value[0]+" Ref "+lines[0]+"_type,")
                                f.write(value[0]+" Ref "+lines[0]+"_type,")
                                f.write('\n')
                                break
        else:
            if x == len(Array)-1:
                #print(value[0]+" varchar(50)")
                f.write(value[0]+" varchar(50)")
                f.write('\n')
                lst.append(value[0])
            else:
                    #print(value[0]+" varchar(50),")
                f.write(value[0]+" varchar(50),")
                f.write('\n')
                lst.append(value[0])                

            
        #print(");")
    f.write(");")
    f.write('\n')
    
    
        #print("create table "+Array[0]+"_table of "+Array[0]+"_type(" )
    f.write("create table "+Array[0]+"_table of "+Array[0]+"_type(" )
    f.write('\n')
    if e == 1:
        #print(primary+" primary key not null,")
        f.write(primary+" primary key not null,")
        f.write('\n')
    for item in lst:
        #print( item+" not null,")
        f.write( item+" not null,")
        f.write('\n')
    if exists == 1:
        f.write("constraint "+str(foreign_origin)+"_"+str(foreign_key)+" foreign key("+str(foreign_key)+") references "+str(foreign_origin)+"_table")
        #print("constraint "+str(foreign_origin)+"_"+str(foreign_key)+" foreign key("+str(foreign_key)+") references "+str(foreign_origin)+"_table")
        f.write('\n')
    #print(");")
    f.write(");")
    #print(" ")
    f.write(" ")
    f.write('\n')
    f.write('\n')
f.close()
 
