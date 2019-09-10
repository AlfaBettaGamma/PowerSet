from PowerSet import PowerSet

class My_test:
    def test1(self):
        test1 = PowerSet()
        for i in range(100):
            test1.put(i)
        test1.print_set()
        test1.put(7)
        test1.put(222)
        test1.print_set()

    def test2(self):
        test1 = PowerSet()
        for i in range(100):
            test1.put(i)
        test1.print_set()
        test1.put(222)
        test1.remove(55)
        test1.print_set()

    def test3(self):
        test1 = PowerSet()
        for i in range(31):
            test1.put(i)
        test1.print_set()
        test1.put(222)
        test2 = PowerSet()
        for i in range(20,40):
            test2.put(i)
        test2.print_set()
        print('__________________')
        res = test1.intersection(test2)
        res.print_set()
        print(type(res))

    def test4(self):
        test1 = PowerSet()
        for i in range(10):
            test1.put(i)
        test1.print_set()
        test1.put(222)
        test2 = PowerSet()
        for i in range(30,40):
            test2.put(i)
        test2.print_set()
        print('__________________')
        res = test1.intersection(test2)
        res.print_set()
        print(type(res))

    def test5(self):
        test1 = PowerSet()
        for i in range(10):
            test1.put(i)
        test1.print_set()
        test2 = PowerSet()
        for i in range(100,105):
            test2.put(i)
        test2.print_set()
        print('__________________')
        res = test1.union(test2)
        res.print_set()

    def test6(self):
        test1 = PowerSet()
        for i in range(10):
            test1.put(i)
        test1.print_set()
        test2 = PowerSet()
        print('__________________')
        res = test1.union(test2)
        res.print_set()

    def test7(self):
        test1 = PowerSet()
        for i in range(10):
            test1.put(i)
        test2 = PowerSet()
        for i in range(5,15):
            test2.put(i)
        res = test2.difference(test1)
        res.print_set()
        print('______________0')
        res = test1.difference(test2)
        res.print_set()

    def test8(self):
        test1 = PowerSet()
        for i in range(10):
            test1.put(i)
        test2 = PowerSet()
        for i in range(10):
            test2.put(i)
        res = test2.difference(test1)
        res.print_set()
        print('______________0')
        res = test1.difference(test2)
        res.print_set()

    def test9(self):
        test1 = PowerSet()
        for i in range(30):
            test1.put(i)
        test2 = PowerSet()
        for i in range(10):
            test2.put(i)
        print(test1.issubset(test2))

    def test10(self):
        test1 = PowerSet()
        for i in range(9,30):
            test1.put(i)
        test2 = PowerSet()
        for i in range(10):
            test2.put(i)
        print(test1.issubset(test2))

test = My_test()
test.test3()
print('************************')
test.test4()
