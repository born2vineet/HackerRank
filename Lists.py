# Enter your code here. Read input from STDIN. Print output to STDOUT
L = []
N = int(raw_input())
for i in range(1, N+1):
    lst = raw_input().split()
    command = lst[0]
    args = lst[1:]
    if command != "print":
        command += "("+",".join(args) +")"
        eval("L."+command)
    else:
        print L