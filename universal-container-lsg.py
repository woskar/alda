import copy # nur für Testfälle

class UniversalContainer:
    def __init__(self): # 'Konstruktor'
        self.capacity_ = 1 # Speicher für min ein Item
        self.data_ = [None]*self.capacity_
        self.size_ = 0 # noch kein item drin

    def size(self):
        return self.size_

    def capacity(self):
        return self.capacity_

    # hier haben die meisten von euch einen Fehler gemacht (off-by-one)
    def push(self, item): # push fügt am ende an
        if self.capacity_ == self.size_: # speicher ist voll check
            self.capacity_ *= 2 
            new_data = [None]*self.capacity_ # create new array
            for i in range(self.size_):
                new_data[i] = self.data_[i] # copy old array
            self.data_ = new_data           # "..."
        self.data_[self.size_] = item
        self.size_ += 1

    # und hier auch (s.o.)
    def popFirst(self):
        if self.size_ == 0:
            raise RuntimeError("popFirst() on empty container")
        self.size_ -= 1
        for i in range(self.size_):
            self.data_[i] = self.data_[i+1]

    def popLast(self):
        if self.size_ == 0:
            raise RuntimeError("popLast() on empty container")
        self.size_ -= 1

    def __getitem__(self, index): 
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        return self.data_[index]

    def __setitem__(self, index, v): 
        if index < 0 or index >= self.size_:
            raise RuntimeError("index out of range")
        self.data_[index] = v

    def first(self):
        return self.__getitem__(0)

    def last(self):
        return self.__getitem__(self.size_ - 1)

# alternativ, war aber eigentlich nicht in der Aufgabe gefordert, eignet sich zum Testen
def contEqual(left, right):
    if left.size() != right.size():
        return False
    for i in range(left.size()):
        if left[i] != right[i]:
            return False
    return True

def testContainer():
   #insert tests here!

if __name__ == "__main__":
    testContainer()
