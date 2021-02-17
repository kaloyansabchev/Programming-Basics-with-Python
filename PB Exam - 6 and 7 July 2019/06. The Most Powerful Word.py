import math
word = input()

longest_word = 0
longest_word_str = ""
vowels = "aeiouyAEIOUY"
letter_is_true = True

while word != "End of words":
    total_sum = 0
    for index, letters in enumerate(word):
        total_sum += ord(letters)
    for letter in vowels:
        if letter in word[0]:
            total_sum *= len(word)
            letter_is_true = False
    if letter_is_true:
        total_sum /= len(word)
        total_sum = math.floor(total_sum)
    if total_sum > longest_word:
        longest_word = total_sum
        longest_word_str = word

    word = input()
print(f"The most powerful word is {longest_word_str} - {longest_word}")