f=open("input.txt",mode='r')
all_input =f.read()
f.close()
commands=all_input.split("\n")
ox_one=list()
ox_zero=list()
co_one=list()
co_zero=list()
count_list_co=list()
total=len(commands)
current_oxygen=commands
current_co=commands

for idx in range(len(commands[0])):
    for command in current_oxygen:
        if(command[idx]=="1"):
            ox_one.append(command)
        else:
            ox_zero.append(command)
    if(len(ox_zero)>len(ox_one)):
        current_oxygen=ox_zero
    else:
        current_oxygen=ox_one
    ox_one=list()
    ox_zero=list()
    if(len(current_co)>1):
        for command in current_co:
            if(command[idx]=="1"):
                co_one.append(command)
            else:
                co_zero.append(command)
        if (len(co_zero) > len(co_one)):
            current_co = co_one
        else:
            current_co = co_zero
        co_zero = list()
        co_one = list()

ox=int(current_oxygen[0],2)
co=int(current_co[0],2)
print(ox*co)
