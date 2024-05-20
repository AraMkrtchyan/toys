import random

class Toy:
    def __init__(self, toy_id, name, quantity, weight):
        self.toy_id = toy_id
        self.name = name
        self.quantity = quantity
        self.weight = weight

class ToyStore:
    def __init__(self):
        self.toys = []
        self.prize_toys = []

    def add_toy(self, toy):
        self.toys.append(toy)

    def update_weight(self, toy_id, new_weight):
        for toy in self.toys:
            if toy.toy_id == toy_id:
                toy.weight = new_weight
                break

    def draw_prize_toy(self):
        total_weight = sum(toy.weight for toy in self.toys)
        random_value = random.uniform(0, total_weight)
        cumulative_weight = 0

        for toy in self.toys:
            cumulative_weight += toy.weight
            if random_value <= cumulative_weight:
                self.prize_toys.append(toy)
                toy.quantity -= 1
                break

    def save_prize_toys(self, filename):
        with open(filename, 'a') as file:
            for toy in self.prize_toys:
                file.write(f'{toy.toy_id}, {toy.name}\n')

        self.prize_toys = []



store = ToyStore()


toy1 = Toy(1, "Кукла", 5, 20)
toy2 = Toy(2, "Мяч", 10, 30)
toy3 = Toy(3, "Конструктор", 8, 50)

store.add_toy(toy1)
store.add_toy(toy2)
store.add_toy(toy3)


store.update_weight(1, 10)


store.draw_prize_toy()


store.save_prize_toys("prize_toys.txt")