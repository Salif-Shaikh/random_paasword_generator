#first we will import to modules import and math
import random
import math

#Declaring variables with different characters
alhpa = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
special = "@#$%&*"

#taking the password length
pass_len = int(input("Enter the password length: "))

#lenght of password by 50-30-20 formula
alpha_len = pass_len//2
num_len = math.ceil(pass_len * 30/100)
special_len = pass_len-(alpha_len + num_len)

#creating a password list
password = []

def generate_pass(lenght, array, is_aplha = False ):
    for i in range(lenght):
        index = random.randint(0, len(array) - 1)
        character = array[index]
        if is_aplha:
            case = random.randint(0, 1)
            if case == 1:
                character = character.upper()
        password.append(character)

#alpha password
generate_pass(alpha_len, alhpa, True)

#numeric password
generate_pass(num_len, num)

#special password
generate_pass(special_len, special)

#shuffling the generated password list
random.shuffle(password)

#converting the list into string
gen_password = ""

for i in password:
    gen_password = gen_password + str(i)
print("output:\n", "\t", gen_password)