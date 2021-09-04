#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
variable = random.randint(0, (len(word_list) - 1))

word_s = word_list[variable]
letters = len(word_s)
counter = len(word_s)
print(word_s)
#print(word_s)
#print(len(word_s))
guest_word = []

for num in range(0 , letters):
  guest_word += " "

while counter > 0:
  letter = input("Guess a letter: ")
  
  for num in range(0 , letters):
      if letter == word_s[num]:
            guest_word[num] = letter
            word = "".join(guest_word)
            print(word)
  
  if word_s == word:
    print("You win!!")
    counter = 0
  else:
    counter -= 1

if counter == 0:
   print("You losse!!!")
     
  
 




    











#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
