import random

normal = [chr(i) for i in range(97, 123)] 
capital = [chr(i) for i in range(65, 91)]  
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
special_c = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
mastersec = ["ç", "ñ"]
password = []

def main():
    generate_password(get_level())
    print(password)
    


def generate_password(lev,lth):
    if lev == 1:
        for i in range(lth - 1):
            password.append(normal[random.randint(0, len(normal) - 1)])
    
    elif lev == 2:
        for i in range(lth - 1):
            if random.choice["more", "less"] == "more":
                password.append(capital[random.randint(0, len(capital) - 1)])
            else: 
                password.append(normal[random.randint(0, len(normal - 1))])

    elif lev == 3:
        for i in range(lth - 1):
            x = random.choice("more", "normal", "less")
            if x == "more":
                password.append(numbers[random.randint(0, len(numbers)- 1)])
            elif x == "normal":
                password.append(capital[random.randint(0, len(capital) - 1)])
            elif x == "less":
                password.append(normal[random.randint(0, len(normal - 1))])
    
    elif lev == 4:
        for i in range(lth - 1):
            x = random.choice("super", "more", "normal", "less")
            if x == "super":
                password.append(special_c[random.randint(0, len(special_c)- 1)])
            elif x == "more":
                password.append(numbers[random.randint(0, len(numbers)- 1)])
            elif x == "normal":
                password.append(capital[random.randint(0, len(capital) - 1)])
            elif x == "less":
                password.append(normal[random.randint(0, len(normal - 1))])
    else:
        for i in range(lth - 1):
            x = random.choice("mega", "super", "more", "normal", "less")
            if x == "mega":
                password.append(mastersec[random.randint(0,len(mastersec - 1))])
            elif x == "super":
                password.append(special_c[random.randint(0, len(special_c)- 1)])
            elif x == "more":
                password.append(numbers[random.randint(0, len(numbers) - 1)])
            elif x == "normal":
                password.append(capital[random.randint(0, len(capital - 1))])
            elif x == "less":
                password.append([normal[random.randint(0, len(normal - 1))]])

        

def get_level():
    while True:
        level = input("What level of security are you looking for? (1-5) : ")
        try:
            if 0 < int(level) < 6:
                break
            else:
                print("Enter a Number between 1 and 5 please!")
                continue
        except ValueError:
            print("Enter a Number please!")
            continue
    
    while True:
        length = input("How many characters?")
        try:
            if int(length) > 0:
                break
            else:
                print("Enter a Number greater than 0!")
                continue
        except ValueError:
            print("Enter a Number please!")
            continue
    return int(level), int(length)
    


main()
