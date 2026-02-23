M=input()
#set_M=set(list(map(int,input().split())))
set_M = set(map(int, input().split()))
N=input()
set_N=set(map(int,input().split()))


D1=((set_M.difference(set_N)))
D2=(set_N.difference(set_M))

for item in D2:
    D1.add((item))


D=sorted(D1)
for item in D:
   print(item)
