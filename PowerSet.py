class PowerSet:

    def __init__(self):
        self.slot = []
        # ваша реализация хранилища

    def size(self):
        return len(self.slot)
        # количество элементов в множестве

    def put(self, value):
        if value not in self.slot:
            self.slot.append(value)
        # всегда срабатывает

    def get(self, value):
        if value in self.slot:
            return True
        return False
        # возвращает True если value имеется в множестве,
        # иначе False

    def remove(self, value):
        if value in self.slot:
            self.slot.remove(value)
            return True
        return False
        # возвращает True если value удалено
        # иначе False

    def intersection(self, set2):
        result = PowerSet()
        if self.size() > set2.size():
            for i in set2.slot:
                if self.get(i) is True:
                    result.put(i)
        else:
            for i in set2.slot:
                if set2.get(i) is True:
                    result.put(i)
        # пересечение текущего множества и set2
        return result

    def union(self, set2):
        result = PowerSet()
        for i in self.slot:
            result.put(i)
        for i in set2.slot:
            result.put(i)
        # объединение текущего множества и set2
        return result

    def difference(self, set2):
        result = PowerSet()
        for i in self.slot:
            if set2.get(i) is False:
                result.put(i)
        # разница текущего множества и set2
        return result

    def issubset(self, set2):
        for i in set2.slot:
            if self.get(i) is False:
                return False
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return True

    def print_set(self):
        for i in self.slot:
            print(i)
   
        