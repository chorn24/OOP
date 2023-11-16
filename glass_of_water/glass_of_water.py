class Glass:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount):
        self.amount += amount
        if self.amount > self.capacity:
            self.amount = self.capacity

        
        # amount += WaterIn
        # if glass.current_amount > glass.capacity:
        #     glass.current_amount = glass.capacity

    def pour_out(self, amount):
        self.amount -= amount
        if self.amount < 0:
            self.amount = 0
    