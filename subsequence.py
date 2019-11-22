#using recursion
def subsequence(m,n):
    if len(m) == 0 or len(n) == 0:
        return 0
    elif m[-1] == n[-1]:
        return 1+subsequence(m[:len(m)-1], n[:len(n)-1])
    else:
        return max(subsequence(m[:len(m)-1], n[:len(n)]), subsequence(m[:len(m)], n[:len(n)-1]))

print(subsequence("i am mad", "iaadr"))
