with open('../users/updatedSchema.txt') as infile, open('../users/output.txt', 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output



    
