# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
data = [[raw_input(), float(raw_input())] for _ in range(N)]
second_highest = sorted(list(set([marks for names, marks in data])))[1]
print ('\n'.join([a for a, b in sorted(data) if b == second_highest]))