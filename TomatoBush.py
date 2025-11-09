from Tomato import *

class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]  # protected свойство
    
    def grow_all(self):
        print("Все томаты растут...")
        for tomato in self.tomatoes:
            tomato.grow()
    
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)
    
    def give_away_all(self):
        print("Урожай собран! Куст очищен.")
        self.tomatoes = []

