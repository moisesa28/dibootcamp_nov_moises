from anagram_checker import AnagramChecker

checker = AnagramChecker()

print("=== ANAGRAM FINDER ===")
    
while True:
    word = input('Enter a word (or type "q" to quit"): ').strip()

    if word.lower() == "q":
        print("Thank you and goodbye!")
        break

    # Validate: must be one single word
    if len(word.split()) != 1:
        print("Enter just one word")
        continue

    # Validate characters
    if not word.isalpha():
        print("Enter only alphabetic characters")
        continue

    # Check if word exists in dictionary
    if checker.is_valid_word(word):
        print(f"\nYou entered a valid word: {word}")
        anagrams = checker.get_anagrams(word)

        if anagrams:
            print("Anagrams found:", ", ".join(anagrams))
        else:
            print("No anagrams found.")
    else:
        print("Sorry, that's not a valid English word")
  