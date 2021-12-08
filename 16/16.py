import math

f = open("input.txt", mode="r")
all_input = f.read()
f.close()

test_entries = all_input.split("\n")
split_entries = list()
for i in test_entries:
    left_side, right_side = i.split("|")
    split_entries.append([left_side.strip().split(" "), right_side.strip().split(" ")])
# print(split_entries)
all_possible = ["a", "b", "c", "d", "e", "f", "g"]
segments = ["up", "upl", "upr", "mid", "down", "downl", "downr"]
encoded_numbers = dict()
sum=0
def create_new_dict():
    possibilities_dict = dict()
    for i in segments:
        possibilities_dict[i] = set()
        for j in all_possible:
            possibilities_dict[i].add(j)
    return possibilities_dict


for i in split_entries:
    possibilities_dict = create_new_dict()
    numbers_dict = dict()
    for j in range(10):
        numbers_dict[j] = list()
    for digit in i[0]:
        new_set = set()
        for character in digit:
            new_set.add(character)
        # digit 1
        if len(digit) == 2:
            numbers_dict[1] = [new_set.copy()]
        #  digit 7
        elif len(digit) == 3:
            numbers_dict[7] = [new_set.copy()]
        # digit  4
        elif len(digit) == 4:
            numbers_dict[4] = [new_set.copy()]
        # digit  8
        elif len(digit) == 7:
            numbers_dict[8] = [new_set.copy()]
        # digit 5 or 2 or 3
        elif len(digit) == 5:
            numbers_dict[2].append(new_set.copy())
            numbers_dict[5].append(new_set.copy())
            numbers_dict[3].append(new_set.copy())
        # digit 0 or 9 or 6
        elif len(digit) == 6:
            numbers_dict[0].append(new_set.copy())
            numbers_dict[6].append(new_set.copy())
            numbers_dict[9].append(new_set.copy())
    # This one is know as we have the segments for 1 and 7
    possibilities_dict["up"] = numbers_dict[7][0].difference(numbers_dict[1][0]).pop()
    # We can also find upr and downr by looking at the entry in the 6 length list that does not have both entries, this will be 6
    for entry in numbers_dict[6]:
        if not numbers_dict[1][0].issubset(entry):
            numbers_dict[6]=[entry]
            possibilities_dict["upr"]= numbers_dict[1][0].intersection(entry).pop()
            possibilities_dict["downr"] = numbers_dict[1][0].difference(possibilities_dict["upr"]).pop()
            numbers_dict[0].remove(entry)
            numbers_dict[9].remove(entry)
            break
    #now we can find topl and downl adn mid by looking at the segements of 4 and those of 9/0. There will be 1 where not the entirety of 4 fits into it, this is 0,the section that is missing is mid
    #This can be then used to get downl by looking at the itnersect of 9 and 0 + topl by looking at 0
    for entry in numbers_dict[0]:
        if not numbers_dict[4][0].issubset(entry):
            #this entry is 0
            numbers_dict[0]=[entry]
            numbers_dict[9].remove(entry)
            temp=numbers_dict[4][0].difference(entry)
            possibilities_dict["mid"]= temp.intersection(numbers_dict[4][0]).pop()
            temp=numbers_dict[4][0].copy()
            temp.remove(possibilities_dict["upr"])
            temp.remove(possibilities_dict["downr"])
            temp.remove(possibilities_dict["mid"])
            possibilities_dict["upl"] =temp.pop()
            temp=numbers_dict[0][0].difference(numbers_dict[9][0])
            possibilities_dict["downl"]=temp.pop()
            # now down can be found as it is the remainder
            found_set=set()
            for key in possibilities_dict:
                if not isinstance(possibilities_dict[key],set):
                    found_set.add(possibilities_dict[key])
            possibilities_dict["down"]=possibilities_dict["down"].difference(found_set).pop()
            break
    #now we just have to find the sets for 2 5 and 3, which will be simple as we have segments
    for entry in numbers_dict[5]:
        if possibilities_dict["upl"] in entry:
            numbers_dict[5]=[entry]
            numbers_dict[2].remove(entry)
            numbers_dict[3].remove(entry)

    for entry in numbers_dict[2]:
        if possibilities_dict["downl"] in entry:
            numbers_dict[2] = [entry]
            numbers_dict[3].remove(entry)
    # voila all found now time to calculate the score
    result=0
    for idx,digit in enumerate(i[1]):
        digit_set=set()
        for char in digit:
            digit_set.add(char)
        for number in numbers_dict:
            if numbers_dict[number][0]==digit_set:
                result+=math.pow(10,3-idx)*number
                break
    sum+=int(result)
print(sum)
