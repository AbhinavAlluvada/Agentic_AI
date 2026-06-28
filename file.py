def file_handling():
    print("File Handling!")
    with open("files/note.txt", "w") as file:
        file.write("Hello Protagonist!")

    with open("files/user.txt", "w") as file:
        file.write("Hello user!")

    with open("files/note.txt", "a") as file:
        file.write("\nAgent is currently busy working...")
        file.write("\nAgent just finished its task!")

    with open("files/note.txt", "r") as file:
        content = file.read()
        print(content)
    with open("files/note.txt", "r") as file:
        for line in file:
            print(line.strip())
    with open("files/note.txt", "r") as file:
        content = file.readlines()
        for i in content:
            print(i, end="")

def exception_handling():
    print("Exception Handling!")
    try:
        print(10/0)
    except ZeroDivisionError:
        print("Cant do it man!")
    finally:
        print("This is finally block!")
        
    age = -10
    if age<0:
        raise ValueError("Negative Huh!")

def comprehensions():
    list_v1 = [n*n for n in range(1,6)]
    print(list_v1)

    list_v2 = [n+1 for n in list_v1]
    print(list_v2)

    dict_v1 = {
        n : n+1 for n in range(1,6)
    }
    for i , j in dict_v1.items():
        print(f"{i}: {j}")
        
    for i,j in enumerate(list_v1):
        print(f"{i} - {j}")
        
    for i,j in enumerate(dict_v1):
        print(f"{i} - {j}")
    for i,j in enumerate(dict_v1.items()):
        print(f"{i} - {j}")
        
        
def decorator(func):
    def wrapper():
        print("Good Evening, Welcome to the party!")
        func()
        print("Thank you for coming, have a safe journey home...")
    return wrapper

@decorator
def talk():
    print("Party's downstairs")
    print("Enjoy yourselves")
    print("I see your leaving...")