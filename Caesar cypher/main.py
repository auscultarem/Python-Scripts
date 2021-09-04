alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text1 = text, number_shift =  shift):
	alphabet_lenght = len(alphabet)
	text_lenght = len(text1)
	char1 = 0
	encrypt_text = []
		
	for num in range(0, text_lenght):	
		letter = text1[char1]
		
		for char in range(0, alphabet_lenght):
			if letter == alphabet[char]:
				#print(text[char1])
				#print(f"Enter here {text1[char1]} = {alphabet[char]}, {new_value}")
				new_value = int(char + number_shift)
				if new_value > 25:
					new_value -= 26	
					encrypt_text += alphabet[new_value]	
					char1 += 1
					cypher_text = "".join(encrypt_text)

				else:				
					encrypt_text += alphabet[new_value]
					char1 += 1
					cypher_text = "".join(encrypt_text)		

	
	print(encrypt_text)	
	print(cypher_text)


def decrypt(text1 = text, number_shift =  shift):
	alphabet_lenght = len(alphabet)
	text_lenght = len(text1)
	char1 = 0
	encrypt_text = []
		
	for num in range(0, text_lenght):	
		letter = text1[char1]
		
		for char in range(0, alphabet_lenght):
			if letter == alphabet[char]:
				#print(text[char1])
				#print(f"Enter here {text1[char1]} = {alphabet[char]}, {new_value}")
				new_value = int(char - number_shift)
				if new_value < 0:
					new_value += 26	
					encrypt_text += alphabet[new_value]	
					char1 += 1
					cypher_text = "".join(encrypt_text)

				else:				
					encrypt_text += alphabet[new_value]
					char1 += 1
					cypher_text = "".join(encrypt_text)		

	
	print(encrypt_text)	
	print(cypher_text)


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction == "encode":
	encrypt(text, shift)
elif direction == "decode":
	decrypt(text, shift)