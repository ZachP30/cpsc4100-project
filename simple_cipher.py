import random
import sys

while True:
    choice = int(input("1: Encrypt \n2: Decrypt \n3: Exit \n"))
    if(choice == 1):
        print('You choce choice: ' + str(choice))
        break
    elif(choice == 2):
        print('You choce choice: ' + str(choice))
        break
    elif(choice == 3):
        sys.exit()
    else:
        print('Please enter a valid choice.')


if (choice == 1):
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
    key_outfile = open('key_outfile.txt', 'w')
    for key, value in dict.items(character_dictionary):
        temp = str(key) + ':' + str(value) + '\n'
        dictlist.append(temp)
    print(dictlist)

    for word in dictlist:
        key_outfile.write(word)

    string_of_chardict = str(character_dictionary)
    


    def encrypt(string_data_final, character_dictionary):
        cipher_text = list()
        for char in string_data_final:
            if (char in character_dictionary.keys()):
                cipher_text.append(character_dictionary.get(char))
        cipher_text_string = ''.join(map(str, cipher_text))

        return cipher_text_string

    cipher_outfile = open('cipher_outfile.txt', 'w')
    cipher_outfile.write(encrypt(string_data_final, character_dictionary))


if (choice == 2):
    def data_to_decrypt():
       
        running = True
        while running:
            cipher_file_name = input('Enter the name of the file with cipher text in it: ')
            key_file_name = input('Enter the name of the file with key in it: ')
            try:
                cipher_text_file = open(cipher_file_name, 'r')
                key_file= open(key_file_name, 'r')
                running = False
            except IOError:
                print('Could not open the file try again.')

        cipher_data = cipher_text_file.readlines()
        key_data = key_file.readlines()
        cipher_data_str = ''.join(map(str, cipher_data))
        cipher_data_str = cipher_data_str.lower()
        whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        cipher_data_final = ''.join(filter(whitelist.__contains__, cipher_data_str))
        print(cipher_data_final)

        key_data_final = ''.join(map(str, key_data))
        key_data_final = key_data_final.lower()
        undelimited_line = [s.strip(':') for s in key_data_final]
        stripped_line = [s.rstrip() for s in undelimited_line]
        

        character_list = stripped_line[::4]
        value_list = stripped_line[2::4]
        character_dictionary = dict(zip(character_list, value_list))
        character_dictionary[' '] = ' '
        del character_dictionary['']
        print(character_dictionary)

        plain_text = list()
        for char in cipher_data_final:
            for key, value in character_dictionary.items():
                if(char == value):
                    plain_text.append(key)
        
        plain_text_string = ''.join(map(str, plain_text))
        print('The decrypted text is: ' + plain_text_string)

    data_to_decrypt()
    



