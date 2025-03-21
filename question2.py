#Given an input n, count the total number of digit 1 appearing in all non-
#negative integers less than or equal to n.

def countDigitOne(n):
    count = 0
    for i in range(1, n + 1):  # Loop through all numbers from 1 to n
        count += str(i).count('1')  # Convert number to string and count '1's
    return count

n = int(input("Enter a number: "))  # Take user input
print("Total occurrences of digit '1':", countDigitOne(n))  # Print result

