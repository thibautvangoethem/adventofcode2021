f=open("input.txt",mode='r')
all_input =f.read()
f.close()
numbers=all_input.split("\n")
upcounter=0
prev=1000000
for i in numbers:
    if(int(i)>prev):
        upcounter+=1
    prev=int(i)
print(upcounter)