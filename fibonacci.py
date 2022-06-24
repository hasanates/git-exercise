number = int(input("enter number"))
my_list=[]
last_list=[]

for i in range(1,number+1):
    answer = False
    for a in range(2,(i//2 + 1)):
        if (i%a != 0):
            answer = True
            break
    if (answer == True ):
        last_list.append(i)
print(last_list)