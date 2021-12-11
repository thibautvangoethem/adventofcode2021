f = open("input.txt", mode="r")
all_input = f.read()
f.close()
open_chars={'(','{','[','<'}
close_chars={')':3,'}': 1197,']':57,'>':25137}
close_to_open_mapping={')':"(",'}':"{",']':'[','>':'<'}
lines=all_input.split("\n")
score=0
for line in lines:
    stack=list()
    for char in line:
        if(char in open_chars):
            stack.append(char)
        if(char in close_chars):
            # get lat char
            prev=stack[len(stack)-1]
            should_be=close_to_open_mapping[char]
            if(prev!=should_be):
                score+=close_chars[char]
                break
            else:
                stack.pop(len(stack)-1)

print(score)