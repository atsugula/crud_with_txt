

# Displaying the contents of the text file
file = open("programas.txt", "r")
content = file.readlines()

s = str(content)

temp = s.split(",")

print(f'proando: {temp}')

print(content)
file.close()