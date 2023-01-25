choice = input("would you like to Read, Write, or Append? (use first letter lowercase)")
file_name = input("input a file name of a file in the same folder")
file = open(file_name, choice)
lis = file.readlines()
for i in lis:
    print(i)
file.close
