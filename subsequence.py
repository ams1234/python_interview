#using recursion
def subsequence(m,n):
    if len(m) == 0 or len(n) == 0:
        return 0
    elif m[-1] == n[-1]:
        return 1+subsequence(m[:len(m)-1], n[:len(n)-1])
    else:
        return max(subsequence(m[:len(m)-1], n[:len(n)]), subsequence(m[:len(m)], n[:len(n)-1]))

print(subsequence("i am mad", "iaadr"))

'''Explination for above problem.
1. if length of any of the string is zero , then we know that longest common subsequence is zero, so that is our base case. 
2. we now compare the last characters of both ths strings, if they match then we increment the count by 1 and leave out the last character and 
compute longest common subsequence for the rest of the strings. 
3. if the last characters doesn't match, then we take max of string1 and string2(excluding the last character and string2 and string1(excluding the last character)

As you can see in the example the max length if subsequnece is 4. 
'''
