
primary = []
multi = []
table = []
tempM=[]
h=(',')


f = open("../users/norama.txt" , "w");

with open('../users/output1.txt' ) as fp:

    for lines in fp:
        words = lines.strip()
        data = words.split(',')
        #print('\n')
        count=0

        for temp2 in data: #find "P"
            if temp2.endswith('P'):
                Pk = temp2
        
        count2=0
        for line in data:

                if line.endswith('M'):#find "M"
                        

                        lineAppend=line+'_t,'+line+','#+Pk
                        tempM.append(lineAppend)
                        #print("tempm",tempM)


                elif line.endswith('P'):
                    f.write(','+line)
                    #print(','+line,end="")

                else:
                    if(count2==0):
                        write2=line+"_t"
                        f.write(write2)
                        #print(write2,end="")
                    else:
                        #if(count2<)
                            
                        write=","+line
                            
                            #print(write,end="")
                            #print("data",count2+1<int(len(data)))
                            
                        if(int(count2)<  int(len(data))):
                            f.write(write)
                                
                            

                            #print(line+" , ",end="")
                            
                        
                count2=count2+1;
                        
            #f.write("ID print")        
        for appended in tempM:
            f.write('\n')
            f.write(appended)
            
        tempM=[]


        f.write('\n')


f.close()        
        
                    


