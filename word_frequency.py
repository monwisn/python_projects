# Word frequency task

# Write a program that counts the frequency of all words from a given input.

frequency = {}
sentence = input('Enter your sentence: ')

for word in sentence.split():
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)

# or

frequency = {}
sentence = input('Enter your sentence: ')

for word in sentence.split():
    frequency[word] = frequency.get(word, 0) + 1

words = frequency.keys()
words = sorted(words)

for item in words:
    print(f'{item} = {frequency[item]}')
