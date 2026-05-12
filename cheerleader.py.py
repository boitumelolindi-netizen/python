user_word = input("Enter your favourite word: ")

vowels = ["a", "e", "i", "o", "u"]

for letter in user_word:
    if letter.lower() in vowels:
        print(f"Give me an {letter.upper()}!")

    else:
        print (f"Give me a {letter.upper()}!")

print(f"What does it say????? {user_word.upper()}!!!!!")
