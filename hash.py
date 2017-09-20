'''Kapitel 10: Hashing und Hashtabellen'''

class HashNode:
     def __init__(self,key,data,next):
         self.key = key
         self.data = data
         self.next = next    # Verkettung!


class HashTable:
    def __init__(self):
        self.capacity = ... # Geeignete Werte siehe unten
        self.size = 0       # Anzahl der Werte, die zur Zeit tatsächlich gespeichert sind
        self.array = [None]*self.capacity

    def __setitem__(self, key, value):
        index = hash(key) % self.capacity  # hash(...) ist in Python eine vordefinierte Funktion
        node  = self.array[index]          # finde die zu 'key' gehörende Liste
        while node is not None:            # sequentielle Suche nach 'key' in dieser Liste
            if node.key == key:
                # Element 'key' ist schon in der Tabelle
                # => überschreibe die Daten mit dem neuen Wert
                node.data = value
                return
            # andernfalls: Kollision des Hashwerts, probiere nächsten 'key' aus
            node = node.next
        # kein Element hatte den richtigen Schlüssel.
        # => es gibt diesen Schlüssel noch nicht
        #    füge also ein neues Element in die Hashtabelle ein
        self.array[index] = HashNode(key, value, self.array[index]) # der alte Anfang der Liste wird zum
                                                                    # Nachfolger des neu eingefügten ersten Elements
        self.size += 1
        ... # eventuell muss jetzt noch die Kapazität optimiert werden

    def __getitem__(self, key):
        index = hash(key) % self.capacity
        node = self.array[index]     # finde die zu 'key' gehörende Liste
        while node is not None:      # sequentielle Suche nach 'key' in dieser Liste
             if node.key == key:     # gefunden!
                 return node.data    # => Daten zurückgeben
             node = node.next        # nächsten Schlüssel probieren
        raise KeyError(key)          # Schlüssel nicht gefunden => Fehler
