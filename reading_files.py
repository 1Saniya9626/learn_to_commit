
from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file" )
print(txt.read())

print("type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
