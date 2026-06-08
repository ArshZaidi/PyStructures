class Stack:

    def __init__(self):
        self.items = []


    #Help function for reference
    def help(self):

        functions = [
            ("push(x)", "Adds element x to the top of the stack."),
            ("pop()", "Removes and returns the top element. Returns None if empty."),
            ("peek()", "Returns the top element without removing it. Returns None if empty."),
            ("isempty()", "Returns True if the stack is empty, False otherwise."),
            ("size()", "Returns the number of elements in the stack."),
            ("clear()", "Removes all elements from the stack."),
            ("merge(x)", "Merges another stack x into this stack."),
    ]
    
        for name, description in functions:
            print(f"{name} : {description}")


    #Add element to the last of stack
    def push(self,x):
        self.items.append(x)
        return self.items

    #Remove the last element
    def pop(self):
        return self.items.pop() if len(self.items) != 0 else None

    #Display the last element of stack
    def peek(self):
        return self.items[-1] if len(self.items) != 0 else None

    #Check if stack is empty
    def isempty(self):
        return True if len(self.items) == 0 else False

    #Length of stack
    def size(self):
        return len(self.items)

    #Clear the whole stack
    def clear(self):
        while len(self.items) != 0:
            self.items.pop()
        return self.items

    #Merge two different stacks
    def merge(self, x):
        self.items.extend(x)
        return self.items