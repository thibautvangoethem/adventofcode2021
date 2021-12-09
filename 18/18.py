f = open("input.txt", mode="r")
all_input = f.read()
f.close()

lines=all_input.split("\n")
basins=list()
for l_idx,line in enumerate(lines):
    for r_ind,cell in enumerate(line):
        surrounding=list()
        if(l_idx>0):
            surrounding.append(int(lines[l_idx-1][r_ind]))
        if(l_idx<len(lines)-1):
            surrounding.append(int(lines[l_idx + 1][r_ind]))
        if(r_ind>0):
            surrounding.append(int(lines[l_idx][r_ind-1]))
        if(r_ind<len(line)-1):
            surrounding.append(int(lines[l_idx][r_ind + 1]))
        higher=False
        for surr in surrounding:
            if int(cell)>=surr:
                higher=True
        if(not higher):basins.append([(l_idx, r_ind)])
low_points_stack=list()
for i in basins:
    low_points_stack.append(i.copy())
change = True
while change:
    change = False
    for s_idx,stack in enumerate(low_points_stack):
        if(len(stack)>0):
            coordinate=stack[0]
            stack.remove(coordinate)
            change = True
            surrounding = list()
            if (coordinate[0] > 0):
                surrounding.append((coordinate[0] - 1,coordinate[1]))
            if (coordinate[0] < len(lines) - 1):
                surrounding.append((coordinate[0] + 1,coordinate[1]))
            if (coordinate[1] > 0):
                surrounding.append((coordinate[0],coordinate[1]-1))
            if (coordinate[1] < len(lines[0]) - 1):
                surrounding.append((coordinate[0],coordinate[1]+1))
            for candidate in surrounding:
                if candidate not in basins[s_idx]:
                    if(int(lines[candidate[0]][candidate[1]]) !=9):
                        stack.append(candidate)
                        basins[s_idx].append(candidate)
basins.sort(key=len,reverse=True)
print(basins)
print(len(basins[0])*len(basins[1])*len(basins[2]))