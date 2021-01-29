ff = open("../users/norama.txt" , "a")
with open("../users/3nf.txt" , 'r+') as f:
    first_line = f.readline().replace(" ","")
    ff.write(first_line)
    
ff.close()
