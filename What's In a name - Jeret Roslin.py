'''
Author: Jeret Roslin
Sources:, Mr. Campbell, ASCII Keys Table
Description: Set of functions that do different things with a certain name
Date: 9/30/2025
Bugs: None
'''



import random

def display_name(name):
    print (f' Hello {name}')
'''
Display's name based on user input
    Args:
        name (str) user input
    Returns: 
        user's name
'''


def count_vowels(name):
    count = 0
    for character in name:
     if character in ['a','e','i','o','u']:
        count+= 1
    print(f'there are {count} vowels in your name')

'''
Counts the amount of certain characters (vowels) in user input
    Args:
        name (str) counts num of vowel in this particular name
    returns:
        (int), the number of vowels in your name
'''




def reverse_name(name):
    return name[::-1] 
'''
displays a reverse version of the user's name
    Args:
        name(str) user input
    returns:
        Reverse name

'''


def palindrome(name):
    '''
determines is reverse is same as regular name
    Args:
        name (str) user input
    returns:
        (bool)if name is a palindrome or not
    '''

    if name == reverse_name:
        print('your name is a palindrome')
    else:
        print ("Your name is not a palindrome")

def lowercase(name):
    '''
    returns name in all lowercase using ASCII Keys
        Args:
            name (str)
        returns: 
            name in all lowercase
    '''

    list_of_name = list(name)
    new_name=[]
    for letter in list_of_name:
        value_letter = ord(letter)
        if value_letter < 91 and  value_letter > 64:
          value_letter +=32
        lower_letter = chr(value_letter)
        new_name.append (lower_letter)
    return (''.join(new_name))

def uppercase(name):
    '''
    returns name in all uppercase using ASCII Keys 
        Args:
        name (str) user's name
        returns:
            user's name in all uppercase 
    '''
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
    '''
    Seperates user's names to only include first name
    Args:
        name (str) user's name
    returns:
        user's first name
    '''
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
    '''
    seperates user's name to only include last name
    Args: 
        name (str) user's name
    returns:
        user's last name 
    '''
    name_reverse = reverse_name(name)
    last_name_reverse = first_name(name_reverse)
    last_name = reverse_name(last_name_reverse)
    return last_name

def count_consonants(name):
    '''
    counts the number of consonsants in user's name
    Args:
        name (str) user's name
    returns:
        (int) number of consonants in user's name
    '''
    count = 0
    for character in name:
        if character not in ['a','e','i','o','u']:
            count += 1 
    print(f'there are {count} consonants in your name')
    
def hyphen_check(name):
    '''
    checks if a hyphen is included in a name
    Args:
        name (str) user's name
    returns: 
        (bool) if there is a hyphen in name or not
    '''
    check = False
    for i in name:
        if i == '-':
            check = True
            print ("There is a hyphen in your name")
            break
    if check == False:
        print("There's not a hyphen in your name")
        
    

def title_check(name):
    '''
    Checks for a special title in user name
    Args:
         (str) user's name
    returns:
         (bool) if there is a hyphen in name or not 
    '''
    titles = ['Dr.', 'Sir.', 'Mr.', 'Esq','Ms.'  'M.d']
    first_space = first_name(name)
    if first_space in titles:
        return True
    else:
        return False

def modify_array(name):
    '''
    shuffles user's name
    Args:
        (str) user's name
    returns:
        (str) user's name shuffled
    '''
    name_list = list(name)
    shuffle_list = []
    while len (name_list) > 0:
        random_int = random.randint(0, (len(name_list) -1))
        letter_selecter = name_list[random_int]
        shuffle_list.append(letter_selecter)
        name_list.remove(letter_selecter)
    return ''.join(shuffle_list)



def indvidual_characters(name):
    '''
    Put's users name in a series of individual characters
        Args:
            (list) user's name in array
        returns:
                User's name in list 

    '''
    user_name = (name)
    char_list = list(user_name)
    return (char_list)
    
def get_initials(name):
    '''
Prints initials of user's name
    Args:
        (str) user's name
    returns:
        user's initials 
    '''
    initials_list = []
    name_list = list(name)
    count = 0
    for letter in name_list:
        if count == 0:
            initials_list.append(letter)
            count +=1
        if letter == ' ':
            count = 0 
    return '.'. join (initials_list)


def middle_name (name):
    '''
   returns user's middle name based on len and spaces
        Args:
            (str) user's name
        returns:
            user's middle name (spaces)
    '''
    begin = 0 
    for i in range(0, len (name)):
        if name [i] == ' ':
            break
        else:
            begin = begin +1
    end = (len(name) -1)
   
    for index in range (len(name) -1):
        if name [index] == ' ':
            break
        else: 
            end = end -1
    return name[begin:end]

def sort_name_alphabetically(name):
    '''
    takes characters and prints them in sorted array
        Args:
            (str) name sorted
        returns:
            name sorted from special characters, numbers, lowercase, uppercase
    '''
    sorted_characters = sorted(name)
    sorted_string = ''.join(sorted_characters)
    print (sorted_string)

def main():

    while True:
        name=input("What is your name? ")
        #asks user their name
        print(f' Welcome {name}')
        # displays user's name
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
    13 Take name and print in indvidual characters
    14 Print name initials
    15 Return middle name 
    16 Print sorted name
    17 Quit 
    
    
    """)
        # printed menu
        if menu == '1':
            count_vowels(name)
        elif menu == '2':
            count_consonants(name)
        elif menu == '3':
            hyphen_check(name)
        elif menu == '4':
            if title_check(name) == True:
             print('There is a special title in your name')
            else:
                print ('There is not a special title in your name')     
        elif menu == '5':
            print (reverse_name(name))
        elif menu == '6':
            palindrome(name)
        elif menu == '7':
            if title_check(name) == False:
                print(first_name(name))
            else:
             no_title = name.replace(first_name(name), '')
             no_title_and_space = no_title.replace(' ', '', 1)
             print (first_name(no_title_and_space))
             

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
        elif menu == '13':
            print (indvidual_characters(name))
        elif menu == '14':
            initials_lowered = get_initials(name)
            print (uppercase(initials_lowered))
        elif menu == '15':
             if title_check(name) == False:
                print(middle_name(name))
             else:
              no_title = name.replace(first_name(name), '')
              no_title_and_space = no_title.replace(' ', '', 1)
              print (middle_name(no_title_and_space))
            
        elif menu == '16':
            sort_name_alphabetically(name)
        elif menu == '17':
            break


#elif statements with options correlated to menu
main()
#recall of main function
