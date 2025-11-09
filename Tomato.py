class Tomato:
    states = {
        0: 'отсутствует',
        1: 'цветение', 
        2: 'зеленый',
        3: 'красный'
    }
    
    def __init__(self, index):
        """
        Инициализация объекта Tomato
        _index - защищенное свойство (protected), содержит индекс томата
        _state - защищенное свойство (protected), содержит текущую стадию созревания
        """
        self._index = index # protected свойство
        self._state = 0 # protected свойство, начальная стадия
    
    def grow(self):
        if self._state < 3:
            self._state += 1
            print(f"Томат {self._index} перешел на стадию: {Tomato.states[self._state]}")
        else:
            print(f"Томат {self._index} уже полностью созрел!")
    
    def is_ripe(self):
        return self._state == 3
    
    def get_state(self):
        return Tomato.states[self._state]
