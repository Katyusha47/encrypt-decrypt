import random
import array


def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    max_len = 14
    
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
 
    up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
    
    combine = number + up + low
    
    n = random.choice(number)
    u = random.choice(up)
    l = random.choice(low)
    
    core = n + u + l
    
    for x in range(max_len - 4):
        core = core + random.choice(combine)
        
        lists = array.array('u', core)
        random.shuffle(lists)
        
    generate = ""
    for x in lists:
        generate = generate + x
    
    file = open(generate + filename, "wb")
    file.write(data)
    file.close()
    
def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()
    
    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
        
    
    file = open(filename, "wb")
    file.write(data)
    file.close()
    


choice = ""
while choice != "3":
    print("Please select you option.")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Quit")
    choice = input()
    if choice == "1" or choice == "2":
        key = int(input("Enter a key as int!\n"))
        filename = input("Enter filename with extension:\n")
    if choice == "1":
        Encrypt(filename, key)
    if choice == "2":
        Decrypt(filename, key)
