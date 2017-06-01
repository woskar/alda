# Gruppe : Oskar Weinfurtner, Ulrich Prestel

class UniversalContainer:
    def __init__(self):
        self.capacity_ = 1
        self.data_ = [None] * self.capacity_
        self.size_ = 0

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    def push(self, item):
        if self.capacity_ == self.size_:
            # verdopplung der Speichergroesse
            print("doubling memory")
            self.data_ += [None] * self.capacity_
            self.capacity_ *= 2

        self.data_[self.size_] = item
        self.size_ += 1

    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.size_ -= 1
        self.data_ = self.data_[1:]

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.size_ -= 1
        self.data_ = self.data_[:self.size_] + ([None] * (self.capacity_ - self.size_))

    def __getitem__(self, index):
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v):
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        return self.data_[0]

    def last(self):
        return self.data_[self.size_ - 1]

    def __str__(self):
        return str(self.data_)


def testContainer():
    # Die deepcopy- Funktion wird bei meinem Beispiel nicht gebraucht, da ich nur einfache Datentypen verwende

    def testConditions(container):

        # print(container)

        assert (container.size() <= container.capacity())
        if container.size() != 0:
            assert (container.first() == container[0])
            assert (container.last() == container[container.size() - 1])

    def testPushElement(container, element):
        oldsize = container.size()
        olddata = container.data_[:]

        testConditions(container)

        container.push(element)
        assert (container.size() == oldsize + 1)  # i)
        assert (container.last() == element)  # ii)

        if oldsize != 0:
            assert (container.data_[:container.size() - 1] == olddata[:oldsize])  # iii)
        else:
            assert (container.first() == element)  # iv)

    def testSetItem(container, index, element):
        testConditions(container)

        oldsize = container.size()
        olddata1 = container.data_[:index]
        olddata2 = container.data_[index+1:]

        container[index] = element
        assert (oldsize == container.size())
        assert (container[index] == element)
        assert (olddata1 == container.data_[:index])
        assert (olddata2 == (container.data_[index+1:]))

    def testPopLast(container):
        testConditions(container)

        oldsize = container.size()
        olddata = container.data_[:oldsize]
        container.popLast()
        assert (container.size() == oldsize - 1)
        assert (container.data_[:container.size()] == olddata[:-1])

    def testPopFirst(container):
        testConditions(container)

        oldsize = container.size()
        olddata = container.data_[:oldsize]
        container.popFirst()
        assert (container.size() == oldsize - 1)
        assert(container.data_[:container.size()] == olddata[1:])

    # ---------------------

    c = UniversalContainer()
    assert (c.size() == 0)
    testPushElement(c, 1)
    testPushElement(c, "test")

    dataBeforePush = c.data_[:]
    sizeBeforePush = c.size()

    testPushElement(c, (1, 2, 3))
    testPopLast(c)
    assert (c.size() == sizeBeforePush)
    assert (c.data_[:sizeBeforePush] == dataBeforePush[:sizeBeforePush])

    testPushElement(c, 1)
    testPushElement(c, 9)
    testPushElement(c, 5)
    testSetItem(c, 1, 0x0451)
    testPopFirst(c)


if __name__ == "__main__":
    testContainer()
