import random

choice = True
while choice:
    try:
        mode = input('Type the number indicating the mode you wish to use: \n 1: Encrypt from .txt File \n 2: Decrypt\n')
        choice == False
    except:
        print('Please choose a valid option.')
        

running = True
while running:
    file_name = input('Enter a file name to read from: ')
    try:
        input_file = open(file_name, 'r')
        running = False
    except IOError:
        print('Could not open the file try again.')
        

data_to_encrypt = input_file.readlines()
string_data = ''.join(map(str, data_to_encrypt))
string_data = string_data.lower()

whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
string_data_final = ''.join(filter(whitelist.__contains__, string_data))
print(string_data_final)

character_list = list()
scrambled_characters = list()

for c in range(97,123):
    character_list.append(chr(c))
    scrambled_characters.append(chr(c))

random.shuffle(scrambled_characters)

character_dictionary = dict(zip(character_list, scrambled_characters))
character_dictionary[chr(32)] = chr(32)

dictlist = list()
for key, value in dict.items(character_dictionary):
    temp = str(key) + ':' + str(value)
    dictlist.append(temp)
print(dictlist)

string_of_chardict = str(character_dictionary)
key_outfile = open('key_outfile.txt', 'w')
line_breaker=9
i=1
for word in dictlist:
    if("." in word or i==line_breaker):
        key_outfile.write(word.strip('\n')+"\n")
        i=0
    else:
        key_outfile.write(word.strip('\n')+" ")

    i+=1


def encrypt(string_data_final, character_dictionary):
    cipher_text = list()
    for char in string_data_final:
        if (char in character_dictionary.keys()):
            cipher_text.append(character_dictionary.get(char))
    cipher_text_string = ''.join(map(str, cipher_text))

    return cipher_text_string

# def data_to_encrypt

    
cipher_outfile = open('cipher_outfile.txt', 'w')
cipher_outfile.write(encrypt(string_data_final, character_dictionary))


