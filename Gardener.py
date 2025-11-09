class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    
    def work(self):
        print(f"{self.name} ухаживает за растениями...")
        self._plant.grow_all()
    
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай!")
            self._plant.give_away_all()
            return True
        else:
            print(f"{self.name}: Томаты еще не созрели! Нужно продолжать ухаживать.")
            return False
    
    @staticmethod
    def knowledge_base():
        print("\n СПРАВКА ПО САДОВОДСТВУ ")
        print("1. Помидор проходит 4 стадии созревания:")
        print("   - отсутствует")
        print("   - цветение") 
        print("   - зеленый")
        print("   - красный (созрел)")
        print("2. Садовник должен ухаживать за растениями,")
        print("   пока все томаты не станут красными")
        print("3. Собирать урожай можно только когда все")
        print("   томаты полностью созрели")
        print("\n")