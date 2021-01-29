
previousLine=None
tempLineTowrite=None
    
text_file = open("../users/norama.txt" ,  "r") 
fileContent=text_file.readlines()
LineCount= len(fileContent)

text_file.close()

toWrite = open("../users/norama.txt" ,  "w") 



with open("../users/3nf.txt" , 'r+') as f:
        Temp3nf=f.readline().replace(" ","")
        f.seek(0)
        first_line = f.readline().replace(" ","").split(',')
    
        tableName=first_line.pop(0)
    
    
      
        for lin in fileContent:
                tempArr=lin.strip().split(',')
        
                for word in first_line:
            
                #print("----"+word+"----")
        
                        for searchMatch in tempArr:
                        
                                if(searchMatch==word  or searchMatch==" "+word ):
                                        lin=lin.replace(', '+word,'')
                                        #print(searchMatch)
                                else:
                                        lin=lin
                        
                toWrite.write(lin)
   
toWrite.write(tableName+"_t," +Temp3nf)
    
f.close()
toWrite.close()
