def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

para = input("Enter a paragraph: ")

words = para.split()

if words: # if word is present then it will run
    longest_word = max(words, key=len)
else:
    longest_word = ""

print("Total Words:", len(words))
print("Longest Word:", longest_word)
print("Vowel Count:", count_vowels(para))
print("Character Count:", len(para))