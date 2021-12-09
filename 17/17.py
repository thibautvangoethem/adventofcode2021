f = open("input.txt", mode="r")
all_input = f.read()
f.close()

lines=all_input.split("\n")
low_points=list()
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
        if(not higher):low_points.append(int(cell))
sum=0
for i in low_points:
    sum+=i+1
print(sum)