# ex 1: writing data in to text file.
# file=open("D:\Pavan sir\Python Programming\HandlledFile.txt",'w')    #(location,'w':to write)('r':reading)('a':append,add (something) to the end of a written document.)
#
# file.write("this is my first statement.....\n")     #\n keyword: represent new line in program.
# file.write("this is my second statement......\n")   #\n keyword: represent new line in program.
# file.write("this is my third statement........\n")
# file.write("this is my last statement...........\n")
# file.close()
# print("program is completed")


## ex 2: reading data from text file.
# file=open("D:\Pavan sir\Python Programming\HandlledFile.txt",'r')
# # print(file.read())        #reads all lines
#
# print(file.readline())  #this is my first statement.....(reads only first line)

# file.close()

## ex 3: append(adding) the data into text file.
file=open("D:\Pavan sir\Python Programming\HandlledFile.txt",'a')
file.write("this is my append line")
print("program is completed")