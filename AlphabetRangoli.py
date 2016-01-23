# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

x = ['-'.join(sublist) for sublist in [[alph for alph in alphabet[i:N]][::-1] + [alph for alph in alphabet[i:N]][1:] for i in range(N)]]

x = x[::-1] + x[1:N]

for i in range(len(x)):
    print (x[i]).center(len(x[N-1]),'-')