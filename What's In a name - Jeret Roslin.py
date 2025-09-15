import random

def display_name(name):
    print (f' Hello {name}')



def count_vowels(name):
    count = 0
    for character in name:
     if character in ['a','e','i','o','u']:
        count+= 1
    print(f'there are {count} vowels in your name')

def reverse_name(name):
    return name[::-1] 

def palindrome(name):
    if name == reverse_name:
        print('your name is a palindrome')
    else:
        print ("Your name is not a palindrome")

def lowercase(name):
    name_list = list(name)
    new_name=[]
    for letter in name_list:
        value_letter = ord(letter)
        if value_letter < 91 and  value_letter > 64:
          value_letter +=32
        lower_letter = chr(value_letter)
        new_name.append (lower_letter)
    return (''.join(new_name))

def uppercase(name):
    name_list = list(name)
    new_name=[]
    for letter in name_list:
        value_letter = ord(letter)
        if value_letter > 96 and value_letter < 123:
            value_letter -=32
        upper_letter = chr(value_letter)
        new_name.append (upper_letter)
    
    return (''.join(new_name))


def first_name(name):
    name_list = list(name)
    count=0
    for i in name_list:
        if i == ' ':
            break
        else:
            count += 1
    first_name_list = name_list[0:count]
    return ("".join(first_name_list))

def last_name(name):
    name_reverse = reverse_name(name)
    last_name_reverse = first_name(name_reverse)
    last_name = reverse_name(last_name_reverse)
    return last_name

def count_consonants(name):
    count = 0
    for character in name:
        if character not in ['a','e','i','o','u']:
            count += 1 
    print(f'there are {count} consonants in your name')
    
def hyphen_check(name):
    check = False
    for i in name:
        if i == '-':
            check = True
            print ("There is a hyphen in your name")
            break
    if check == False:
        print("There's not a hyphen in your name")
        
      
def title_check(name):
    special_title = False
    for i in name:
        if i in ['Dr.','Sir','Esq','Mr.','Ms.']:
            special_title = True
    if special_title == True:
        print('there is a special title')
    else:
        print ('There is not a special title in your name')
        

def modify_array(name):
    char_list = list(name)
    random.shuffle(char_list)
    return ''.join(char_list)



    


def main():
        name=input("What is your name? ")
        print(f' Welcome {name}')
        menu=input("""Which function would you like to see?
    1 count the amount of vowels in your name
    2 count the amount of consonants in your name
    3 Check if there is a hyphen in your name   
    4 Check to see if your name contains a special title         
    5 Reverse your name
    6 Check if your name is a palindrome
    7 Return first name
    8 Return last name
    9 Convert name to  all lowercase
    10 Convert name to all uppercase
    11 Display Name 
    12 Shuffle a name
    
    """)
        if menu == '1':
            count_vowels(name)
        elif menu == '2':
            count_consonants(name)
        elif menu == '3':
            hyphen_check(name)
        elif menu == '4':
            title_check(name)
        elif menu == '5':
            print (reverse_name(name))
        elif menu == '6':
            palindrome(name)
        elif menu == '7':
            print (first_name(name))
        elif menu == '8':
            print (last_name(name))
        elif menu == '9':
            print (lowercase(name))
        elif menu == '10':
            print (uppercase(name))
        elif menu == '11':
            display_name(name)
        elif menu == '12':
            print (modify_array(name))

main()
