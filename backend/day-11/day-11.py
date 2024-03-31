# Open a file for reading
with open('names.txt', 'r') as file:
    names = file.readlines()
    
# Open a file for writing
names.sort()
with open('names.txt', 'w') as file:
    file.writelines(names)
    
# Open a file for appending
# with open('names.txt', 'a') as file:
#    file.write("\nAppending more text!\n")