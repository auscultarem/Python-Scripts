#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# open the file and insert the content inside de variable content
with open("./Input./Letters/starting_letter.txt") as file:
            content = file.read()
            print(content)

# open the file and insert the names inside a list
names_file = open("./Input./Names/invited_names.txt", "r")
names_list = names_file.readlines()
print(names_list)

# clear caracteres that are no necesary
names =[]
for name in names_list:
    txt = name
    x = txt.strip("\n")
    names.append(x)
print(names)

# replace names inside the content
mails =[]
for name in names:
    txt = content
    new_content = txt.replace("[name]", name)
    # create a file for each name
    mails.append(new_content)
    with open(f"./Output./ReadyToSend/Mail for {name}.txt", "w") as new_letter:
        new_letter.write(new_content)





