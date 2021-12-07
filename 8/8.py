def boards_to_gameFields(boards):
    bitmasks=list()
    new_boards=list()
    number_to_index_map=dict()
    for board_idx,board_input in enumerate(boards):
        newboard=list()
        newbitmask=list()
        for row_idx,row in enumerate(board_input.split("\n")):
            newrow=list()
            newrowmask=list()
            temp=row.replace("  "," ").strip()
            temp2=temp.split(" ")
            for column_idx,col in enumerate(temp2):
                newrow.append(col)
                newrowmask.append(False)
                if(int(col) not in number_to_index_map):
                    number_to_index_map[int(col)]=list()
                number_to_index_map[int(col)].append([board_idx,row_idx,column_idx])
            newboard.append(newrow)
            newbitmask.append(newrowmask)
        new_boards.append(newboard)
        bitmasks.append(newbitmask)
    return (new_boards,bitmasks,number_to_index_map)


def check_win(board_mask):
    first,second,third,fourth=True,True,True,True
    for i in range(5):
        first=first&board_mask[i][i]
        second = second & board_mask[i][4-i]
        third = third & board_mask[4-i][i]
        fourth = fourth & board_mask[4-i][4-i]
        hor=True
        vert=True
        for j in range(5):
            hor=hor&board_mask[i][j]
            vert = vert & board_mask[j][i]
        if(hor or vert):
            return True
    if(first or second or third or fourth):
        return True
    return False


f=open("input.txt",mode='r')
all_input =f.read()
f.close()
split_input=all_input.split("\n\n")
numbers=list()
boards=list()
for idx,input in enumerate(split_input):
    if(idx==0):
        numbers=input.split(",")
    else:
        boards.append(input)
boards,masks,index_map=boards_to_gameFields(boards)
boards_won=[False]*len(boards)
total_boards=len(boards)
win_idx=-1
final_number=-1
class Found(Exception): pass
try:
    for number in numbers:
        to_flip=index_map[int(number)]
        for flip in to_flip:
            masks[flip[0]][flip[1]][flip[2]]=True
        for mask_idx,mask in enumerate(masks):
            if not boards_won[mask_idx] and check_win(mask):
                boards_won[mask_idx]=True
                total_boards-=1
                win_idx=mask_idx
                final_number=number
                if(total_boards==0):
                    raise Found
except: Found
sum=0
for row_idx,row in enumerate(masks[win_idx]):
    for col_idx, col in enumerate(row):
        if(not col):
            sum+=int(boards[win_idx][row_idx][col_idx])
print(sum*int(final_number))