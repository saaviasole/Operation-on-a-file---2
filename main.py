with open('codingal.txt','w') as file:
    file.write("Hi! I am Saavi And I am 12 yr old.")
file.close()

with open('codingal.txt', 'r') as  file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print (word)
file.close()


new_file = open('New_file.txt', 'x')
new_file.close()

import os
print("Checking if my_file exist or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exist")

my_file = open("my_file.txt", "w")
my_file.write("Hi! Hello to all my friends.")

os.remove('Codingal.txt')

os.rmdir('Folder')


input_file = open("Repeated.txt", "r")

output_file = open("UpdatedFile.txt", "w")

seen_lines = seet()

print("Removing duplicate lines...")

for line in input_file:

    if line not in seen_lines:

        output_file.write(line)

        seen_lines.add(line)

input_file.close()
output_file.close()

print("Done! Duplicate line removed")