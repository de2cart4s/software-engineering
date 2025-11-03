class LibraryCard:
    def __init__(self, owner, card_number):
        self.owner = owner
        self.__card_number = card_number  # скрытый атрибут

    def show_owner(self):
        print(f"Читатель: {self.owner}")

    def check_card(self, number):
        if number == self.__card_number:
            print("Доступ к библиотечной карте разрешён.")
        else:
            print("Ошибка доступа: неверный номер карты.")


card = LibraryCard("Иван Петров", "B12345")
card.show_owner()
card.check_card("00000")
card.check_card("B12345")
