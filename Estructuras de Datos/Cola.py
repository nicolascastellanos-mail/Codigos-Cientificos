# August Twelfth, 2022. 19:49 (Colombian hour)

class queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def print(self):
        print()
        print("--------------")
        print("**QUEUE INFO**")

        for i in range(0, len(self.queue)):
            print("{0}. {1}".format(i, self.queue[i]))

cart = queue()
print(cart.is_empty)
cart.enqueue("Chicken")
cart.print()
cart.enqueue("Toast")
cart.print()
cart.enqueue("Meat")
cart.print()
cart.dequeue()
cart.print()

# August Twelfth, 2022. 20:10 (Colombian hour)