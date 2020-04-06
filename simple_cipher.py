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
   

    def data_to_encrypt(cipher_text_file, key_file):
        running = True
        while running:
            try:
                cipher_text_file = open(cipher_text_file, 'r')
                key_file= open(key_file, 'r')
                running = False
            except IOError:
                print('Could not open the file try again.')

        cipher_data = cipher_text_file.readlines()
        key_data = key_file.readlines()
        cipher_data_final = ''.join(map(str, cipher_data))
        cipher_data_final = cipher_data_final.lower()

        key_data_final = ''.join(map(str, key_data))
        key_data_final = key_data_final.lower()

        #We want to strip all elements in this list
        undelimited_line = [s.strip(':') for s in key_data_final]
        # undelimited_line1 = [s.strip('') for s in undelimited_line]
        stripped_line = [s.rstrip() for s in undelimited_line]
        # key_data_final = stripped_line.split(':')
        # print(stripped_line)

        character_list = stripped_line[::4]
        value_list = stripped_line[2::4]
        character_dictionary = dict(zip(character_list, value_list))
        print(character_dictionary)
        # print(character_list)
        # print(value_list)

#list(character_dictionary.keys())[list(character_dictionary.values()).index(char)]
        for char in cipher_data_final:
            plain_text = list()
            if (char in character_dictionary.values()):
                plain_text.append(character_dictionary.keys().index(char))
        print(plain_text)
        # plain_text_string = ''.join(map(str, plain_text))
        # return plain_text_string


        print('The cipher data is:' + cipher_data_final)
        # print('The key data is: \n' + key_data_final)

        # for c in cipher_data_final:
        #     if(c in )

    print(data_to_encrypt('cipher_outfile.txt', 'key_outfile.txt'))
    



