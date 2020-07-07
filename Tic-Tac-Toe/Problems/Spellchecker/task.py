dictionary = ["aa", "abab", "aac", "ba", "bac", "baba", "cac", "caac"]
word = input()
i = 0
x = 0
while i <= 7:
    if word == dictionary[i]:
        x = 1
    i += 1
if x == 1:
    print('Correct')
else:
    print('Incorrect')