# 1. Reverse 1st 3 elements of a queue:

def reverse_first_three(queue):
    temp = []
    for _ in range(3):
        if queue:
            temp.append(queue.pop(0))
    
    temp.reverse()
    
    queue = temp + queue

    return queue

# usage
queue = [1, 2, 3, 4, 5]
print(f"Input queue: {queue}")
result = reverse_first_three(queue)
print(f"Output queue: {result}")

# 2. Rolling queue (keep only last 5 numbers)

def manage_queue():
    queue = []
    
    while True:
        user_input = input("Enter a number (or press Enter to stop): ").strip()
        
        if user_input == "":
            break
        
        try:
            num = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        queue.append(num)
        
        if len(queue) > 5:
            queue.pop(0)
    
    print(f"Queue at the end: {queue}")

manage_queue()

# 3. Round Robin-time Processing

def process_tasks(tasks):
    queue = tasks 
    finished = []

    while queue:
        name, time_needed = queue.pop(0)

        time_needed -= 2

        if time_needed > 0:
            queue.append((name, time_needed))
        else:
            finished.append(name)

    return finished

# usage:
tasks = [("A", 3), ("B", 6), ("C", 1)]
completion_order = process_tasks(tasks)
print(f"Completion order: {completion_order}")


