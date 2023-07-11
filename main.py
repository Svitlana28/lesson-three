#d1
text = input("Enter:")
print(len(text))
#d2
text = input("Enter:")
print(text)

#D3
original_text = input("Enter the original string:")
word_first = input("Enter the world to replace:")
replacement_word = input("Enter the replacement word:")
modified_string = original_text
modified_string = original_text.replace(word_first,replacement_word)
print("modified_string:" + modified_string )


   #d4
sentence = "Hello World"
for letter in sentence:
    print(sentence[2:3:])
    print(sentence[9:10:])
    print(sentence[0:6])
    print(sentence[0:9])
    print(sentence[0:10:2])
    print(sentence[1:10:2])
    print(sentence[ : : -1])
    print(sentence[ : : -2])
    print(len(sentence))
