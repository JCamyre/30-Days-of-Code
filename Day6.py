# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for _ in range(n):
    s = str(input())
    even = s[::2]
    odd = s[1::2]
    print(even + ' ' + odd)
