# Enter your code here. Read input from STDIN. Print output to STDOUT
phonebook = {}
n = int(input())
for _ in range(n):
    key, val = input().split()
    phonebook[key] = val

while True:
    try:
        name = input()
    except:
        break
    if phonebook.get(name):
        print('{}={}'.format(name, phonebook.get(name)))
    else:
        print('Not found')
