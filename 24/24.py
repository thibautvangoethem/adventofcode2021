import numpy as np
from collections import deque
import copy

f = open("input.txt", mode="r")
all_input = f.read()
f.close()
lines = all_input.split("\n")

class node:
    def __init__(self,name):
        self.name=name
        self.is_start=name=="start"
        self.is_end=name=="end"
        self.is_small=(name==name.lower()) and not (self.is_start or self.is_end)
        self.connections=list()

graph=dict()
for i in lines:
    left=i.split("-")[0]
    right = i.split("-")[1]
    if left not in graph:
        graph[left]=node(left)
    if right not in graph:
        graph[right] = node(right)
    graph[left].connections.append(right)
    graph[right].connections.append(left)

def add_node(stack,source:node):
    stack.append(("walkback",source.name))
    for i in source.connections:
        stack.append(("goto",i))
# this variable is more for debugging but also for checking the visiting of small caves
current_path=list()
unique_paths=0
stack=deque()
stack.append("stop")
# current_node=
all_visited=list()
add_node(stack,graph["start"])
current_path.append("start")
small_visited_twice=False
test=stack.__getitem__(len(stack)-1)
while(stack.__getitem__(len(stack)-1) != "stop"):
    action=stack.pop()
    if(action[0]=="goto"):
        togonode=graph[action[1]]
        if(togonode.is_end):
            unique_paths+=1
            all_visited.append(copy.copy(current_path))
            continue
        elif(togonode.is_start):
            continue
        elif (not togonode.is_small or (togonode.is_small and togonode.name not in current_path)):
            add_node(stack,togonode)
            current_path.append(togonode.name)
        elif(togonode.is_small and current_path.count(togonode.name) ==1 and not small_visited_twice):
            add_node(stack, togonode)
            current_path.append(togonode.name)
            small_visited_twice=True
        else:
            continue
    elif(action[0]=="walkback"):
        current_node=graph[current_path[len(current_path)-1]]
        if(current_node.is_small and current_path.count(current_node.name) ==2):
            small_visited_twice=False
        current_path.pop()
print(unique_paths)