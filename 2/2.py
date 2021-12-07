f=open("input.txt",mode='r')
all_input =f.read()
f.close()
numbers=all_input.split("\n")
upcounter=0
prev=1000000
for idx in range(len(numbers)):
    if idx<len(numbers)-2:
        sum=int(numbers[idx])+int(numbers[idx+1])+int(numbers[idx+2])
        if(sum>prev):
            upcounter+=1
        prev=sum

print(upcounter)