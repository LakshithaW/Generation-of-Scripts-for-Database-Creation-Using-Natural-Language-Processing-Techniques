import language_check

import nltk

import pymysql



File = open("../users/mydata.txt","r" ) #open file
lines = File.read() #read all lines


tool = language_check.LanguageTool('en-US')

matches = tool.check(lines)
out=language_check.correct(lines, matches)

lines = lines.replace(lines, out)


# Write the file out again
with open('../users/mydata.txt', 'w') as file:
    file.write(lines)
