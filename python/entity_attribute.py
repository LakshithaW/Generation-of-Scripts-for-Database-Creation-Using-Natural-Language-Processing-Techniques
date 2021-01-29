import nltk
import language_check
#nltk.data.path.append('C:/Users/hp/AppData/Roaming/nltk_data/')
import copy
tool = language_check.LanguageTool('en-US')

import inflect
p = inflect.engine()

File = open("../users/mydata.txt" ,"r") #open file
lines = File.read() #read all lines
i=0

matches = tool.check(lines)
out=language_check.correct(lines, matches)
sentences = nltk.sent_tokenize(out) #tokenize sentences

nouns = [] #empty to array to hold all nouns
Attribute = [] #empty to array to hold all attribute
Entity_att = []
Multivalue = []
Entity = []
relationship = []
primary = []
count = 0
count1 = 0
ffrom = 0
ent = []
cc = 0
f= open("../users/Entity_attribute.txt","w+")
for sentence in sentences:
    
     for word in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
             
             nouns.append(word)
#print(nouns)
#--------------------------------------------------------------#
for i in range(0,len(nouns)):
     if(i < len(nouns)-1):
     
        
             if((nouns[i][1] == 'NNP'or nouns[i][1] == 'NNPS')):
                     Entity.append(nouns[i][0])
             if(nouns[i][0] == 'is'and (nouns[i+1][0] == 'a' or nouns[i+1][0] == 'an')  and nouns[i+2][1] == 'NN'):
                     Entity.append(nouns[i+2][0])
             if(nouns[i][0] == 'NNP' or nouns[i][1] == 'NNPS' or nouns[i][1] == 'NN' or nouns[i][1] == 'NNS') and (nouns[i+1][0]=='has' or nouns[i+1][0]=='have' ):
                      Entity.append(nouns[i][0])
go =[]
go=list(set(Entity))
att=list(set(Entity))
for pp in range(0,len(go)):
     if(p.singular_noun(go[pp]) is False):
          go.append(p.plural(go[pp]))
     else:
          go.append(p.singular_noun(go[pp]))
          


tagged=[]
chunked=[]
#sent_text = nltk.sent_tokenize(out)

for i in range(0,len(sentences)):
           
           tokenized_text = nltk.word_tokenize(sentences[i])
           
     
           for z in range(0, len(tokenized_text)):
                 for j in range(0,len(go)):
                      if(go[j].lower() == tokenized_text[z].lower()):
                           
                           count1 = count1+ 1
                           
                           if(p.singular_noun(go[j]) is False):
                                ent.append(go[j]+"-one")
                           else:
                                ent.append(p.singular_noun(go[j])+"-Many")
           if(count1 == 2):
                tagged= nltk.pos_tag(nltk.word_tokenize((sentences[i])))
                for i in range(0 , len(tagged)):
                     if(tagged[i][1].startswith('VB')): 
                          
                          
                          relationship.append(tagged[i][0])
                f.write("entity_relation : " + ent[0] +'\n')
                f.write("relationship : ")
                for i in range(len(relationship)):
                                 f.write( relationship[i] + " ")
                f.write('\n') 
                f.write("entity_relation : " + ent[1] +'\n')
                              
           
           f.write('\n')         
           count1 = 0
           ent = []
           relationship = []


#------------------------------------------------------------------------#

            

for i in range(0,len(nouns)):
     if(i < len(nouns)-1):
     
          if((nouns[i][1] == 'NN'or nouns[i][1] == 'NNS') and(nouns[i+1][1] == 'NN'or nouns[i+1][1] == 'NNS')):
                  Attribute.append(nouns[i+1][0])
          if(nouns[i][1] == 'DT' and (nouns[i+1][1] == 'JJ' or nouns[i+1][1] == 'JJR' or nouns[i+1][1] == 'JJS') and(nouns[i+2][1] == 'NN'or nouns[i+2][1] == 'NNS') ):
                  Attribute.append(nouns[i+2][0])
          if(nouns[i][1] == 'PRP' and (nouns[i+1][1] == 'NN' or nouns[i+1][1] == 'NNS')):
                   Attribute.append(nouns[i+1][0])
          if((nouns[i+1][1] == 'JJ' or nouns[i+1][1] == 'JJR' or nouns[i+1][1] == 'JJS') and (nouns[i+1][1] == 'NN' or nouns[i+1][1] == 'NNS') ):
                    Attribute.append(nouns[i+1][0])
          if(nouns[i][1] == 'DT' and (nouns[i+1][1] == 'NN'or nouns[i+1][1] == 'NNS')):
                   Attribute.append(nouns[i+1][0]) 
          if((nouns[i][0] == 'has' or nouns[i][0] == 'have') and (nouns[i+1][1] == 'NN'or nouns[i+1][1] == 'NNS')):
                   Attribute.append(nouns[i+1][0])
          if(nouns[i][1] == ',' and (nouns[i+1][1] == 'NN'or nouns[i+1][1] == 'NNS')):
                   Attribute.append(nouns[i+1][0])
          if(nouns[i][0] == 'and' and (nouns[i+1][1] == 'NN'or nouns[i+1][1] == 'NNS')): #should be edit
                   Attribute.append(nouns[i+1][0])         
cc = 0
pri =[]
primary = []
Attribute1 = []
Attribute1 = list(set(Attribute)) # remove duplicate

#print(Attribute1)
# Remove entity from the attribute list
for e in go:
     ee = (e.lower())# change entity to lower case
     for n in Attribute1:
          nn = n.lower() # change attriute to lower case
          if(ee == nn):
               
               Attribute1.remove(ee)
 


#print(att)
Attribute2 = Attribute1 



for e in att:

     f.write("entity :" + e + "\n")
     #Entity_att.append(e)
     for i in range(0,len(nouns)):
          
          
          if(nouns[i][0].lower() == e.lower()):
               
               #print(e)
               for j in range(i , len(nouns)):
                    if(j == 0):
                         ffrom = 0
                    if(nouns[j][0] == '.'):
                         upto = j
                         
                         break
               for z in range(i , 0 , -1):
                    if(nouns[z][0] == '.'):
                         #print(z)
                         ffrom = z
                   
                         
                         break
               for x in range(ffrom, upto):
                    if(x < upto):
                             if(nouns[x][0] == "unique" or nouns[x][0] == "uniquely" or nouns[x][0] == "uniqueness"):
                                   
                                   if(nouns[x][0] == "unique" and nouns[x+1][1] == 'NN'):
                                        pri.append(nouns[x+1][0])
                                        
                                        Entity_att.append(nouns[x+1][0]+"-p")
                                   for key in range(ffrom , upto):
                                        
                                        for p in range(0,len(Attribute1)) :
                                             if(Attribute1[p] == nouns[key][0]):
                                                   
                                                   cc = cc +1
                                                                 
                                                  
                                   #if(cc == 1):
                                        
                                        #Entity_att.append(primary[1]+"-p")
                                        #for att in range(0,len(Attribute1)):
                                        #     if(Attribute1[att] == primary[0]):
                                        #          count = count+1
                                        #          Attribute1[att] = (primary[0]+"-p")
                                   
                                   for att in range(0,len(Attribute1)):
                                        for at in range(0,len(pri)):
                                             if(Attribute1[att] == pri[at] ):
                                                  count = count+1
                                                  Attribute1[att] = (pri[at]+"-p")
                                   cc = 0
                                   primary = []
                                   pri = []
                                   
                    #print(Attribute1)                    
                    for a in range(0,len(Attribute1)):
                       
                        
                         if(Attribute1[a] == nouns[x][0]):
                              
                              #for row in data:  #derived attribute
                              #if(Attribute1[a] == row[0] ):
                                   #Attribute1[a] = (row[1]+":D")
                                        
                                 
                              
                              if(nouns[x][1] == 'NNS'):  #identify multivalue
                                   Attribute1[a] = (Attribute1[a]+"-M")
                                   Entity_att.append(Attribute1[a])
                                   count = count +1
                                   
                              else:
                                   Entity_att.append(Attribute1[a]+"-N") 

                                   count = count +1    
                              
     Entity_att1 = []
     Entity_att1 = list(set(Entity_att))
     k=len(Entity_att1)
     c = str(len(Entity_att1))
     #print(c)
     #print(k)
     f.write("att_count :" + c +  "\n")
     f.write("attributes : ")
     
     #print(count)
     #print(Entity_att1)
     #print(len(Entity_att1))
     for i in range(0 , len(Entity_att1)):
          
          if( i == count):
              
              f.write( Entity_att1[i])
          else:    
               f.write( Entity_att1[i] + ",")
     
     count = 0
     Entity_att1 = []
     Entity_att = []
     Attribute1 = Attribute2
   
     f.write("\n")
     f.write("\n")




f.close()
 

