# August Twelfth, 2022. 18:19 (Colombian hour)

class stack:
    objects = []
    indexes = []

    def push(self, object):
        self.objects.append(object)
    
    def pop(self):
        self.objects.pop(-1)

    def is_empty(self):
        if len(self.objecs) == 0:
            return True
        else:
            return False
    
    def print_stack(self):
        print()
        print("--------------")
        print("**STACK INFO**")

        self.indexes = [abs(i - len(self.objects)) for i in range(0, len(self.objects) + 1) if i > 0]
        
        for i in range(0, len(self.indexes)):
            print("{0}. {1}".format(self.indexes[i], self.objects[self.indexes[i]]))

cart = stack()
print(cart.is_empty)
cart.push("Chicken")
cart.print_stack()
cart.push("Toast")
cart.print_stack()
cart.push("Meat")
cart.print_stack()
cart.pop()
cart.print_stack()

# August Twelfth, 2022. 18:38 (Colombian hour)