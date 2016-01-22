# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y, z, n = (int(input()) for _ in range(4))
print [[xi, yi, zi] for xi in range(x+1) for yi in range(y+1) for zi in range(z+1) if xi + yi + zi != n]