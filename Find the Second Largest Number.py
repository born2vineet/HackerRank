# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
n = list(map(int, raw_input().split()))
max_n = max(n)
while max(n) == max_n:
    n.remove(max_n)
print max(n)