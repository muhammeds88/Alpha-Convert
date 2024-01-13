def to_code_language(word):
    # Initialize an empty string for the translation
    translation = ' '

    # Iterate through each letter in the input word
    for letter in word:
        # Check if the lowercase version of the letter matches a specific case
        if letter.lower() == 'a':
            translation += '#'  # Replace 'a' with '#'
        elif letter.lower() == 'e':
            translation += '*'  # Replace 'e' with '*'
        elif letter.lower() == 'i':
            translation += '%'  # Replace 'i' with '%'
        elif letter.lower() == 'o':
            translation += '!'  # Replace 'o' with '!'
        elif letter.lower() == 'u':
            translation += '$'  # Replace 'u' with '$'
        elif letter.lower() == 'y':
            translation += '^'  # Replace 'y' with '^'
        elif letter.lower() == 't':
            translation += '+'  # Replace 't' with '+'
        elif letter.lower() == 'n':
            translation += '-'  # Replace 'n' with '-'
        elif letter.lower() == 's':
            translation += ':'  # Replace 's' with ':'
        elif letter.lower() == 'h':
            translation += '/'  # Replace 'h' with '/'
        elif letter.lower() == 'r':
            translation += '@'  # Replace 'r' with '@'
        elif letter.lower() == 'd':
            translation += '('  # Replace 'd' with '('
        elif letter.lower() == 'm':
            translation += ')'  # Replace 'm' with ')'
        elif letter.lower() == 'l':
            translation += '_'  # Replace 'l' with '_'
        else:
            translation += letter  # Keep other characters unchanged

    return translation


def to_normal_language(word):
    # Initialize an empty string for the translation
    translation = ' '

    # Iterate through each letter in the input word
    for letter in word:
        # Check if the lowercase version of the letter matches a specific case
        if letter.lower() == '#':
            translation += 'a'  # Replace '#' with 'a'
        elif letter.lower() == '*':
            translation += 'e'  # Replace '*' with 'e'
        elif letter.lower() == '%':
            translation += 'i'  # Replace '%' with 'i'
        elif letter.lower() == '!':
            translation += 'o'  # Replace '!' with 'o'
        elif letter.lower() == '$':
            translation += 'u'  # Replace '$' with 'u'
        elif letter.lower() == '^':
            translation += 'y'  # Replace '^' with 'y'
        elif letter.lower() == '+':
            translation += 't'  # Replace '+' with 't'
        elif letter.lower() == '-':
            translation += 'n'  # Replace '-' with 'n'
        elif letter.lower() == ':':
            translation += 's'  # Replace ':' with 's'
        elif letter.lower() == '/':
            translation += 'h'  # Replace '/' with 'h'
        elif letter.lower() == '@':
            translation += 'r'  # Replace '@' with 'r'
        elif letter.lower() == '(':
            translation += 'd'  # Replace '(' with 'd'
        elif letter.lower() == ')':
            translation += 'm'  # Replace ')' with 'm'
        elif letter.lower() == '_':
            translation += 'l'  # Replace '_' with 'l'
        else:
            translation += letter  # Keep other characters unchanged

    return translation


def rules():
    # Display the mapping of alphabets to symbols
    print("\nThe following alphabets are replaced by these symbols (Just remember it).")
    print("a = #\ne = *\ni = %\no = !\nu = $\ny = ^\nt = +\nn = -\ns = :\nh = /\nr = @\nd = (\nm = )\nl = _")
    print("If you are converting Code language to Normal language, just type the alphabet if you don't see the symbol in the given list.")


# Print an introduction and display the rules
print("Hey, This Python code efficiently translates words into a coded language and decodes them, demonstrating a concise and user-friendly implementation for text transformation.")
rules()

# Use a while loop to repeatedly prompt the user for input
while True:
    # Get the user's choice
    choice = input("\nEnter 'c' to convert Normal language to Code language and 'n' to convert Code language to Normal language (Enter 'q' to exit the program): ")

    if choice == 'c':
        # Convert Normal language to Code language
        input_word = input("Enter the Normal language to convert it into Code language: ")
        result_translation = to_code_language(input_word)
        print("Code language translation: ", result_translation)

    elif choice == 'n':
        # Convert Code language to Normal language
        input_code = input("Enter the code language to convert it into Normal language: ")
        result_decoding = to_normal_language(input_code)
        print("Normal language translation: ", result_decoding)

    elif choice == 'q':
        # Quit the program if 'q' is entered
        print("Program Ended...")
        quit()