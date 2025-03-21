#Convert a non-negative integer to its English words representation and print in
#reverse if total characters in English words are more than total words in a
#sentence
def numberToWords(num):
    if num == 0:
        return "Zero"

    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    thousands = ["", "Thousand", "Million", "Billion"]

    def helper(n):
        if n == 0:
            return ""
        elif n < 20:
            return below_20[n] + " "
        elif n < 100:
            return tens[n // 10] + " " + helper(n % 10)
        else:
            return below_20[n // 100] + " Hundred " + helper(n % 100)

    res = ""
    i = 0
    while num > 0:
        if num % 1000 != 0:
            res = helper(num % 1000) + thousands[i] + " " + res
        num //= 1000
        i += 1

    return res.strip()

def processNumber(num, sentence):
    words = numberToWords(num)
    char_count = len(words.replace(" ", ""))
    word_count = len(sentence.split())

    if char_count > word_count:
        return words[::-1]
    return words

num = int(input("Enter a number: "))
sentence = input("Enter a sentence: ")
print(processNumber(num, sentence))
