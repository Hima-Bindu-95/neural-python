# Enter your code here. Read input from STDIN. Print output to STDOUT

Length,Width=map(int,input().split())

half_L=int((Length+1)/2)
half_W=int((Width+1)/2)


for i in range(0,2*(half_L-1),2):
     print(((i+1)*('.|.')).center(Width,'-'))
     

print('WELCOME'.center(Width,'-'))


for i in range(0,2*(half_L-1),2):
     print(((2*half_L-i-3)*('.|.')).center(Width,'-'))
