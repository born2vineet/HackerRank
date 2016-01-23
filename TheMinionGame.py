# Enter your code here. Read input from STDIN. Print output to STDOUT
s, vowels = raw_input(), "AEIOU" # BANANA
kevsc, stusc = 0, 0
for i in range(len(s)): # 0 1 2 3 4 5
    if s[i] in vowels: # B A N A N A
        kevsc += (len(s) - i) # 0 5 5 5 8 8 9
    else:
        stusc += (len(s) - i) # 6 6 10 10 12 12
if kevsc > stusc:
    print "Kevin", kevsc
elif kevsc < stusc:
    print "Stuart", stusc
else:
    print "Draw"