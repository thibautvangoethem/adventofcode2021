import numpy as np

f = open("input.txt", mode="r")
all_input = f.read()
f.close()
lines = all_input.split("\n")
risk_dict = dict()
visited_dict = dict()
for idx, i in enumerate(lines):
    for jdx, j in enumerate(i):
        risk_dict[(idx, jdx)] = int(j)
        visited_dict[(idx, jdx)] = None
size=100
new_risk_dict=dict()
for i in range(5):
    for j in range(5):
        for item in risk_dict:
            co=(item[0]+size*i,item[1]+size*j)
            new_risk_dict[co]=(risk_dict[item]+i+j)
            if new_risk_dict[co]>9:
                new_risk_dict[co]=new_risk_dict[co]-9

            visited_dict[co] = None
risk_dict=new_risk_dict
# matrix only for visualization in pycharm
# mt=np.zeros(shape=(50,50))
# for i in risk_dict:
#     mt[i]=risk_dict[i]
size=size*5
def get_surrounding_coords(coord):
    result = list()
    if (coord[0] > 0):
        result.append((coord[0] - 1, coord[1]))
    if (coord[0] < size-1):
        result.append((coord[0] + 1, coord[1]))
    if (coord[1] > 0):
        result.append((coord[0], coord[1] - 1))
    if (coord[1] < size-1):
        result.append((coord[0], coord[1] + 1))
    return result

end=(size-1,size-1)
tovisit=list()
tovisit.append((0,0))
visited_dict[(0,0)]=0

while len(tovisit)>0:
    visiting=tovisit.pop()
    # if visiting==end:
    #     break
    to_check=get_surrounding_coords(visiting)
    for i in to_check:
        if(visited_dict[i]==None or visited_dict[visiting]+risk_dict[i]<visited_dict[i]):
            visited_dict[i]=visited_dict[visiting]+risk_dict[i]
            tovisit.append(i)
    tovisit.sort(reverse=True, key=visited_dict.get)

print(visited_dict[end])

