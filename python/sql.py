
#try:
    #cursor = connection.cursor()
tab = []
el =[]
tt = []
temp = []
dict={}
    
with open("../users/norama.txt" ) as fp:
        
    for lines in fp:
        words = lines.strip()
        data = words.split(',')
            #print(lines)
            
        for li in data:
                if li.endswith('_t'):
                    tt.append(li)
                    key=li
                      
                      
                    temp = []
                       
                         
                else:
                    el=li
                    lineAppend=el+','
                    temp.append(lineAppend)
                    ##print(li)
    
        #dict[key]=temp
        key1=str(key)
        temp1=''.join(temp)
        #print("key",key1)
        ql =  "Insert into test ( u_name, name, attribute) " + " values (%s, %s, %s) "
            #cursor.execute(sql, (user, key1, temp1) )
            #connection.commit() 
            
#finally: 
    #connection.close()
