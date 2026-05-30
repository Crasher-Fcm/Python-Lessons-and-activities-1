# Take input of a word
string = input("Enter your own preferred word: ")
# Take input of a character
char = input("Enter the character you want to find: ")
i = 0
count = 0
# Loop will to find the occurence of character
while(i < len(string)): # string operation

    if(string[i] == char): # condition
        count = count + 1
    i = i + 1

    # Display the result
print("The total Number of Times", char, "has Occurred = ", count)