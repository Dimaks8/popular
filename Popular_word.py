def getText():
    text = []
    while True:
        new_string = input()
        if not new_string:
            break
        text.extend(new_string.split())
    return(text)

text = getText()

dictionary = {}
for word in text:
    count = dictionary.get(word, 0)
    dictionary[word] = count + 1

max_count = 0
popularest = 1
for word in dictionary:
    if max_count < dictionary[word]:
        max_count = dictionary[word]
        popular_word = word
        popularest = 1
    elif max_count == dictionary[word]:
        popularest = 0

if popularest:
    print(popular_word)
else:
    print("Nope")
