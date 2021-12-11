import numpy as np

f = open("input.txt", mode="r")
all_input = f.read()
f.close()
lines = all_input.split("\n")

matrix = np.zeros((len(lines), len(lines[0])))

for idx, i in enumerate(lines):
    for jdx, j in enumerate(i):
        matrix[idx][jdx] = int(j)
print(matrix)
# just an arbitrary low number so it never goes above 9, this is not a permanent fix but works for the task
matrix=np.pad(matrix,1,constant_values=-9999999)
flashes_amount=0
for i in range(100):
    matrix=matrix+1
    increase_set=np.argwhere(matrix>9)
    visited=set()
    flash_stack=list()
    for coords in increase_set:
        visited.add((coords[0],coords[1]))
        flash_stack.append((coords[0],coords[1]))
    while len(flash_stack)!=0:
        coord=flash_stack.pop()
        for first in [-1,0,1]:
            for second in [-1, 0, 1]:
                if(first==0 and second==0):
                    continue
                matrix[coord[0]+first][coord[1]+second]+=1
                if matrix[coord[0]+first][coord[1]+second]>9:
                    to_check=(coord[0]+first,coord[1]+second)
                    if(to_check not in visited):
                        visited.add(to_check)
                        flash_stack.append(to_check)
    to_flash=np.argwhere(matrix > 9)
    flashes_amount+=len(to_flash)
    for idx in to_flash:
        matrix[idx[0]][idx[1]]=0
    # matrix[to_flash]=0
print(flashes_amount)


