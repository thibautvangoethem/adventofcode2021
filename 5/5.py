f=open("input.txt",mode='r')
all_input =f.read()
f.close()
commands=all_input.split("\n")
count_list=list()
total=len(commands)
for _ in range(len(commands[0])):
    count_list.append(0)
for command in commands:
    for idx,bit in enumerate(command):
        if(bit=="1"):
            count_list[idx]+=1

gamma=""
epsilon=""
for number in count_list:
    if(number<total/2):
        gamma+="0"
        epsilon+="1"
    else:
        gamma += "1"
        epsilon += "0"
gamma=int(gamma,2)
epsilon=int(epsilon,2)
print(gamma*epsilon)
