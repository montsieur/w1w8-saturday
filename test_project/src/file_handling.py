# Open a file in write mode
file = open('newFile.txt', 'w')
file.write("This is a new File!!!\n")
file.close()

# Open a file in read mode
file = open('newFile.txt', 'r')
content = file.read()

print(content)
file.close()

# Open the file in append mode
file = open('newFile.txt', 'a')
file.write("This is my second line!!!")
file.close()

file = open('newFile.txt', 'r')
content = file.read()
print(content)
file.close()

# with statement
with open ('newFile.txt', 'a') as file:
    file.write("Third line reporting.")

with open ('newFile.txt', 'r') as file:
    content = file.read()
    print(content)


