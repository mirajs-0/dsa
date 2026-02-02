# 1. Find the minimum value in a stack

def find_min(stack):
    if stack:
        return min(stack)
    else:
        return "Stack is empty" 

# usage:
stack = [5, 2, 9, 1, 7]
print(f"The minimum value in the stack is: {find_min(stack)}")

# 2. Undo last N actions

def undo_actions(stack, n):
    undone = []
    
    for _ in range(n):
        if stack: 
            undone.append(stack.pop())
        else:
            break 

    return undone, stack

# usage:
actions = ["open", "edit", "save", "close"]
n = 2

undone, remaining_stack = undo_actions(actions, n)

print(f"Undone: {undone}")
print(f"Left in stack: {remaining_stack}")

# 3. Simplify a file path using a stack

def simplify_path(path):
    parts = path.split("/")
    
    stack = []
    
    for part in parts:
        if part == "" or part == ".":  
            continue
        elif part == "..": 
            if stack:
                stack.pop()
        else: 
            stack.append(part)
    
        return "/" + "/".join(stack)

# usage:
path = "/home//user/.././docs"
simplified_path = simplify_path(path)
print(f"Simplified Path: {simplified_path}")
