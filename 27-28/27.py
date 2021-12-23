import copy
f = open("input.txt", mode="r")
all_input = f.read()
f.close()
lines = all_input.split("\n")
rules=dict()
pairs_and_count_empty=dict()
pairs_and_count=dict()
the_string=None
for idx,line in enumerate(lines):
    if(idx==0):
        the_string=line
    elif(idx==1):
        continue
    else:
        splited=line.split(" -> ")
        rules[splited[0]]=(splited[0][0]+splited[1],splited[1]+splited[0][1])
        for i in rules[splited[0]]:
            pairs_and_count[i]=0
            pairs_and_count_empty[i] = 0
for i in range(len(the_string)-1):
    pair=the_string[i]+the_string[i+1]
    if pair not in pairs_and_count_empty:
        pairs_and_count_empty[pair]=0
        pairs_and_count[pair]=0
    pairs_and_count[pair] += 1

print(pairs_and_count)
for i in range(40):
    new_pairs=copy.copy(pairs_and_count_empty)
    for item in pairs_and_count:
        new_for_this_rule=rules[item]
        new_pairs[new_for_this_rule[0]]+=pairs_and_count[item]
        new_pairs[new_for_this_rule[1]] += pairs_and_count[item]
    pairs_and_count=new_pairs

count_dict=dict()
difference_dict=dict()
for item in pairs_and_count:
    first=item[0]
    second=item[1]
    if first not in count_dict:
        count_dict[first]=0
        difference_dict[first]=0
    if second not in count_dict:
        count_dict[second]=0
        difference_dict[second] = 0
    count_dict[first]+=pairs_and_count[item]
    difference_dict[first] += pairs_and_count[item]
    difference_dict[second]-=pairs_and_count[item]
for i in difference_dict:
    count_dict[i]-=difference_dict[i]

largest=0
smallest=False
for i in count_dict:
    if count_dict[i]>largest:
        largest=count_dict[i]
    if smallest==False or count_dict[i]<smallest:
        smallest=count_dict[i]
print("counts: ",count_dict)
print("differences: ",difference_dict)
print(largest-smallest)
