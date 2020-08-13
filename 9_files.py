## operating with files

reader = open('files/sample.txt','r')
#read and print lines
for line in reader:
    print(line.rstrip())

# write files
reader = open('files/sample.txt','r')
writer = open('files/file.txt', 'w')
for line in reader:
    print(line)
    writer.writelines(line)

# close files
reader.close()
writer.close()
