f=open("input.txt",mode="r")
all_input=f.read()
f.close()

test_entries=all_input.split("\n")
split_entries=list()
for i in test_entries:
    left_side,right_side=i.split("|")
    split_entries.append([left_side.strip().split(" "),right_side.strip().split(" ")])
print(split_entries)
sum=0
for i in split_entries:
    for digit in i[1]:
        if len(digit) in [2,3,4,7]: sum+=1
print(sum)