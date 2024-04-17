def main():
 with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    return file_contents

def count_words():
   with open("books/frankenstein.txt") as f:
     file_contents = f.read()
   words =[]
   words = file_contents.split()
   print(f"{len(words)} words found in the document")

def count_letters():
   with open("books/frankenstein.txt") as f:
     file_contents = f.read()
# convert all words string to lower words
   lowered_words = file_contents.lower()
#convert the string to list type and sort the items
   all_words = sorted(list(lowered_words))
#remove all non-alphabetic characters in the list
   all_characters = [c for c in all_words if c.isalpha()]
   letter_count = {}
#start to count each letter in the list. If the letter already in the dictionary, skip it
   for i in range(len(all_characters)):
     letter = all_characters[i]
     if letter not in letter_count:
       count = all_characters.count(letter)
       letter_count.update({letter:count})
     else:
       pass
   for letter, count in letter_count.items():
     print(f"The '{letter}' character was found {count} times")

main()
print("--- Begin report of books/frankenstein.txt ---\n")
count_words()
count_letters()
print("--- End report ---")
