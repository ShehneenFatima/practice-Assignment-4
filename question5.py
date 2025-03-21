#Given a string containing just the characters '(' and ')', find the length of the longest
#and shortest valid (well-formed) parentheses substring.
#For "(()", the longest valid parentheses substring is "()", which has length = 2.
#Another example is ")()())", where the longest valid parentheses substring is "()()",
#which has length = 4.
def find_longest_shortest_valid_parentheses(s):
    stack = [-1]
    max_length = 0
    min_length = float('inf')

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                length = i - stack[-1]
                max_length = max(max_length, length)
                min_length = min(min_length, length)
            else:
                stack.append(i)

    return max_length, min_length if min_length != float('inf') else 0

s = input("Enter a string of parentheses: ")
longest, shortest = find_longest_shortest_valid_parentheses(s)

print("Longest Valid Parentheses Length:", longest)
print("Shortest Valid Parentheses Length:", shortest)
