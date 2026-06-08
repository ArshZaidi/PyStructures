class Queue:

    def __init__(self):
        self.items = []


    #Help function for reference
    def help(self):

        functions = [
            ("enqueue(x)", "Adds element x to the rear of the queue."),
            ("dequeue()", "Removes and returns the front element. Returns None if empty."),
            ("front()", "Returns the first element without removing it. Returns None if empty."),
            ("rear()", "Returns the last element without removing it. Returns None if empty."),
            ("isempty()", "Returns True if the queue is empty, False otherwise."),
            ("size()", "Returns the number of elements in the queue."),
            ("clear()", "Removes all elements from the queue."),
            ("merge(x)", "Merges another queue x into this queue."),
    ]
    
    
        for name, description in functions:
            print(f"{name} : {description}")


    #Add element to a queue
    def enqueue(self, x):
        self.items.append(x)
        return self.items

    #Remove the first element of Queue
    def dequeue(self):
        return self.items.pop(0) if len(self.items) != 0 else None

    #Display first element of Queue
    def front(self):
        return self.items[0] if len(self.items) != 0 else None

    #Display last element of Queue
    def rear(self):
        return self.items[-1] if len(self.items) != 0 else None

    #Check if Queue is empty
    def isempty(self):
        return True if len(self.items) == 0 else False

    #Return the length of Queue
    def size(self):
        return len(self.items)

    #Clear the whole Queue
    def clear(self):
        while len(self.items) != 0:
            self.items.pop()
        return self.items

    #Merge two different Queues
    def merge(self, x):
        self.items.extend(x)
        return self.items