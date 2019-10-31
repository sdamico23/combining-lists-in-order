inp = input("Please enter list 1: ")
inp2 = input("Please enter list 2: ")
ls1 = [int(x) for x in inp.split()]
ls2 = [int(x) for x in inp2.split()]
ans = []
for i in range(0,len(ls1)):
    ans.append(ls1[i])
    i += 1
    ans.append(ls1[i])
    i -= 1
    ans.append(ls2[i])
    i += 1
    ans.append(ls2[i])
    i += 2
               
print("The combined list is",end = " ")
for i in ans:
    print(i,end = " ")
