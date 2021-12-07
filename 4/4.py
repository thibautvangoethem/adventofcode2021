horizontal_pos=0
depth=0
aim=0
f=open("input.txt",mode='r')
all_input =f.read()
f.close()
commands=all_input.split("\n")
for command in commands:
    splited=command.split(" ")
    type=splited[0]
    magnitude = int(splited[1])
    if(type=="forward"):
        horizontal_pos+=magnitude
        depth+=magnitude*aim
    elif (type == "up"):
        aim-=magnitude
    elif (type == "down"):
        aim += magnitude
print(horizontal_pos*depth)