import numpy as np

encrypt_String = input("Enter the string to encrypt: ")
encrypt_String = encrypt_String.replace(" ", "") #takes the spaces out of the encryption string
encrypt_String = encrypt_String.lower() #lowercases the encryption screen for uniformity

for c in range(0,len(encrypt_String)+1):
    if c<len(encrypt_String)-1:
        if encrypt_String[c]==encrypt_String[c+1]: #Check to see if two letters next to each other are the same
            encrypt_String=encrypt_String[:c+1]+'x'+encrypt_String[c+1:] #If they are then append the letter 'X'

if len(encrypt_String)%2!=0: #If the length of the list is not even we need to pad characters
        encrypt_String=encrypt_String[:]+'x' #Appends the letter 'X' as a pad

print(encrypt_String) #This is used as a test to check our string for encryption

#break the string to encrypt in groups of 2 for encrpytion
encrypt_letter_groups = list()
encrypt_letter_groups =  [(encrypt_String[i:i+2]) for i in range(0, len(encrypt_String), 2)]
print(encrypt_letter_groups) #tested and works


#Now we need to make a key and a matrix if they key has j in it, make it an i
key = input("\nEnter the key to be used: ")
key = key.replace(" ", "")#takes the spaces out of the key
key = key.lower() #lowercase the whole key for uniformity

character_list = list()
for char in key: #This makes a list with the characters of our key in it
    if (char == 'j'):
        character_list.append('i')
    else:
        character_list.append(char)

print("\nThe key letters in a list is this: ")
print(character_list) 

#Our character list should exclude j, if j exists in the plaintext, it is replaced by i
for c in range(97,123): #ascii chars for lowercase 
    if chr(c) not in character_list: #appends the remaining characters of the alphabet that are not in our key
        if (chr(c) != 'j'):
            character_list.append(chr(c))

decrypt_Matrix = [[0 for i in range(5)] for j in range(5)] #make a defualt matrix
k = 0 #edclaring the new iterator
for i in range(0,5): #fill the matrix with the appopriate letters
    for j in range(0,5):
        decrypt_Matrix[i][j] = character_list[k] #fills the matrix
        k = k+1 #had to use a different iterator to make this work
decrypt_array = np.array(decrypt_Matrix) #making the list of lists a 2D array
print(decrypt_array) #testing 2D array

#Debugging Comments:
#print('\nThis is the test')
# print('x:' + str(np.argwhere((decrypt_array == 'y'))[0][0])) #row
# print('y:' + str(np.argwhere((decrypt_array == 'y'))[0][1])) #column
# #Going to see if we can compare using it

#Making a dict to 'map' the letters and their indecies
index_dict = {}
for i, ele in enumerate(decrypt_array): 
    for j, element in enumerate(ele):
        index_dict[element] = (i,j)
    
print('\n\nDictionary of Index')
print(index_dict)
#We get a dictionary of the items with the characters as the key
# print(decrypt_array[:,0])

#Function for getting the key associated with a value
def get_key(val): 
    for key, value in index_dict.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

#Encryption Magic
def encrypt(encrypt_String, decrypt_array, index_dict):
    new_string = list()
    for lettergroup in encrypt_letter_groups:
        # print(lettergroup)
        # print(lettergroup[0])
        # print(lettergroup[1])
        match = "False"
        x = 0
        while match is "False" and x < 5:
            if (lettergroup[0] in decrypt_array[x] and lettergroup[1] in decrypt_array[x]):
                location1 = index_dict.get(lettergroup[0])
                location2 = index_dict.get(lettergroup[1])
                # print(location1)
                # print(location2)
                new_location1 = (((location1[0]),(location1[1]+1)%5))
                new_location2 = (((location2[0]),(location2[1]+1)%5))
                # print(new_location1)
                # print(new_location2)
                new_string.append(get_key(new_location1))
                new_string.append(get_key(new_location2))
                # print(new_string)
                # print(x)
                match = "True"

            elif (lettergroup[0] in decrypt_array[:,x] and lettergroup[1] in decrypt_array[:,x]):
                location3 = index_dict.get(lettergroup[0])
                location4 = index_dict.get(lettergroup[1])
                # print(location3)
                # print(location4)
                new_location3 = (((location3[0]+1)%5),location3[1])
                new_location4 = (((location4[0]+1)%5),location4[1])
                # print(new_location3)
                # print(new_location4)
                new_string.append(get_key(new_location3))
                new_string.append(get_key(new_location4))
                # print(new_string)
                # print(x)
                match = "True"

            else:
                # print("poop")
                # print(x)
                x += 1
            
        if (match == "False"):
            location5 = index_dict.get(lettergroup[0])
            location6 = index_dict.get(lettergroup[1])
            # print(location5)
            # print(location6)
            new_location5 = (((location5[0]),(location6[1])%5))
            new_location6 = (((location6[0])%5),location5[1])
            new_string.append(get_key(new_location5))
            new_string.append(get_key(new_location6))
            # print(new_string)
            # print(new_location5)
            # print(new_location6)
    
    return new_string




#Encrypt Magic Runnning :)
cipher_text = encrypt(encrypt_String, decrypt_array, index_dict)

cipher_text = ''.join(map(str, cipher_text))
print('\nThis is the cipher text')
print(cipher_text)

cipher_letter_groups = list()
cipher_letter_groups =  [(cipher_text[i:i+2]) for i in range(0, len(cipher_text), 2)]
print('\n Cipher Letter Groups')
print(cipher_letter_groups) #tested and works

def decrypt(cipher_text, decrypt_array, index_dict):
    new_string1 = list()
    for lettergroup in cipher_letter_groups:
        # print(lettergroup)
        # print(lettergroup[0])
        # print(lettergroup[1])
        match = "False"
        x = 0
        while match is "False" and x < 5:
            if (lettergroup[0] in decrypt_array[x] and lettergroup[1] in decrypt_array[x]):
                location1 = index_dict.get(lettergroup[0])
                location2 = index_dict.get(lettergroup[1])
                # print('Old Location:')
                # print(location1)
                # print(location2)
                new_location1 = (((location1[0]),(location1[1]-1)%5))
                new_location2 = (((location2[0]),(location2[1]-1)%5))
                # print('New Location:')
                # print(new_location1)
                # print(new_location2)
                new_string1.append(get_key(new_location1))
                new_string1.append(get_key(new_location2))
                # print(new_string1)
                # print(x)
                match = "True"

            elif (lettergroup[0] in decrypt_array[:,x] and lettergroup[1] in decrypt_array[:,x]):
                location3 = index_dict.get(lettergroup[0])
                location4 = index_dict.get(lettergroup[1])
                # print('Old Location:')
                # print(location3)
                # print(location4)
                new_location3 = (((location3[0]-1)%5),location3[1])
                new_location4 = (((location4[0]-1)%5),location4[1])
                # print('New Location:')
                # print(new_location3)
                # print(new_location4)
                new_string1.append(get_key(new_location3))
                new_string1.append(get_key(new_location4))
                # print(new_string1)
                # print(x)
                match = "True"

            else:
                # print("poop")
                # print(x)
                x += 1
            
        if (match == "False"):
            location5 = index_dict.get(lettergroup[0])
            location6 = index_dict.get(lettergroup[1])
            # print('Old Location:')
            # print(location5)
            # print(location6)
            new_location5 = (((location5[0]),(location6[1])%5))
            new_location6 = (((location6[0])%5),location5[1])
            new_string1.append(get_key(new_location5))
            new_string1.append(get_key(new_location6))
            # print(new_string1)
            # print('New Location:')
            # print(new_location5)
            # print(new_location6)
    
    return new_string1

plain_text = decrypt(cipher_text, decrypt_array, index_dict)

plain_text = ''.join(map(str, plain_text))
print('\nThis is the plain text')
print(plain_text)



    









