# Enter your code here. Read input from STDIN. Print output to STDOUT
raw_input()
M = set(map(int, raw_input().split()))
raw_input()
N = set(map(int, raw_input().split()))

result = M.symmetric_difference(N)
for i in sorted(result):
    print i