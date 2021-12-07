f=open("input.txt",mode="r")
all_input=f.read()
f.close()
text_lines=all_input.split("\n")
lines=list()
for i in text_lines:
    coords=i.split(" -> ")
    first=coords[0].split(",")
    second=coords[1].split(",")
    lines.append(((int(first[0]),int(first[1])),(int(second[0]),int(second[1]))))
map=dict()
for line in lines:
    if(line[0][0]==line[1][0]):
        it=line[0][1]-line[1][1]
        first=None
        second=None
        if(it>0):
            first=line[1]
            second=line[0]
        elif(it<0):
            first = line[0]
            second = line[1]
            it=abs(it)
        it+=1
        for i in range(it):
            point=(first[0],first[1]+i)
            if point not in map:
                map[point]=0
            map[point]+=1
    elif(line[0][1]==line[1][1]):
        it=line[0][0]-line[1][0]
        first=None
        second=None
        if(it>0):
            first=line[1]
            second=line[0]
        elif(it<0):
            first = line[0]
            second = line[1]
            it=abs(it)
        it+=1
        for i in range(it):
            point=(first[0]+i,first[1])
            if point not in map:
                map[point]=0
            map[point]+=1
    else:
        hor = line[0][0] - line[1][0]
        vert = line[0][1]-line[1][1]
        first = line[0]
        second = line[1]
        for i in range(abs(hor)+1):
            co1=None
            co2=None
            if(hor>0):
                co1=first[0]-i
            else:
                co1 = first[0] + i
            if(vert>0):
                co2=first[1]-i
            else:
                co2 = first[1] + i
            point = (co1,co2)
            if point not in map:
                map[point] = 0
            map[point] += 1
sum=0
for i in map:
    if map[i]>1:
        sum+=1
print(sum)

from PIL import Image
img  = Image.new( mode = "RGB", size = (1000, 1000) )

pixels = img.load()
for i in map:

    pixels[i[0],i[1]]=(255, 0, 0)
img.show()