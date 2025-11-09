from Gardener import *
from TomatoBush import *

if __name__ == "__main__":
    Gardener.knowledge_base()
    
    print("Создаем куст с 3 помидорами...")
    bush = TomatoBush(3)
    print("Наняли садовника Ивана...")
    gardener = Gardener("Иван", bush)
    
    print("\n Первый день ухода ")
    gardener.work()
    
    print("\n Попытка сбора урожая ")
    gardener.harvest()
    
    print("\n Второй день ухода ")
    gardener.work()
    
    print("\n Третий день ухода ")
    gardener.work()
    
    print("\n Финальный сбор урожая ")
    success = gardener.harvest()
    
    if success:
        print("Урожай успешно собран! Программа завершена.")
    else:
        print("Что-то пошло не так...")