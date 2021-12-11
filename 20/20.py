f = open("input.txt", mode="r")
all_input = f.read()
f.close()
open_chars={'(','{','[','<'}
close_chars={')':1,'}': 3,']':2,'>':4}
close_to_open_mapping={')':"(",'}':"{",']':'[','>':'<'}
open_to_close_mapping = {v: k for k, v in close_to_open_mapping.items()}
lines=all_input.split("\n")
scores=list()
for line in lines:
    corrupt=False
    stack=list()
    for char in line:
        if(char in open_chars):
            stack.append(char)
        if(char in close_chars):
            # get lat char
            prev=stack[len(stack)-1]
            should_be=close_to_open_mapping[char]
            if(prev!=should_be):
                corrupt=True
                break
            else:
                stack.pop(len(stack)-1)
    if(not corrupt):
        score=0
        stack.reverse()
        for stack_char in stack:
            to_add=open_to_close_mapping[stack_char]
            score*=5
            score+=close_chars[to_add]
        scores.append(score)


scores.sort()
print(scores)
print(scores[len(scores)//2])