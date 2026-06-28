import os
print(os.getcwd()) #Current working directoory

print(os.listdir()) # List of all the files in your workspace


with open("files/new.txt","w") as file:
    file.write("Hello World!")
try:
    os.remove("files/new2.txt")
    print("Successful!")
except Exception as e:
    print(e)