#open,read, and close the file
poem=open('poem.txt','r')
x_str=poem.read()
poem.close()

#convert the string to the list
poem_list = x_str.split("\n")

#define the funciton
def print_file(lst,line,cursor):
    left='\n'.join(lst[:line])
    mid=lst[line][:cursor]+'^'+lst[line][cursor:]
    right='\n'.join(lst[line+1:])
    print(left+'\n'+mid+'\n'+right)

def cmd_h(lst,line,cursor):
    if cursor>0:
        return line, cursor-1
    #if the cursor is in the beginning of first line then doesn't need to move
    elif line==0 and cursor==0:
        return line , cursor
    #move the cursor to the previous line
    elif line>0 and cursor==0:
        return line-1 , len(lst[line-1])

#print the result
print_file(poem_list,3,1)
line,cursor=cmd_h(poem_list,3,1)
print_file(poem_list,line,cursor)
