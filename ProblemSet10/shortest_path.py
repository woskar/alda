# ALDA Blatt 10: Ulrich Prestel und Oskar Weinfurtner
# Aufgabe 2: Kürzeste Wege mit Dijkstra

import json # zum Einlesen der Städte json Datei
import heapq # heapq implementiert die Funktionen für Heaps
import math
import time


# Teilaufgabe a) Funktion implementieren

def createGraph(distanceDict):
    """
    returns from dictionary distanceDict:
    graph: Adjazenzliste des Graphen (Jede Stadt als Nummer kodiert)
    names: property map die jeder Knotennummer den Städtenamen zuordnet
    weights: property map der Kantengewichte weights[(i,j)]
    """

    # Initialisiere Rückgaben
    graph = []
    names = {}
    weights = {}

    # Städte/Knoten in Nummern umwandeln
    n = 0
    for stadt in distanceDict:
        # speichere Nummer der Stadt mit Namen in names ab
        names[n] = stadt
        n += 1

    # Invertieren von names
    # numbers["Stadtname"] soll Zahl des Knotens zurückgeben
    numbers = {}
    for number in names:
        numbers[names[number]] = number


    # Iteriere über Einträge in json file
    for stadt in distanceDict:
        # Leere Liste, die Nachbarknoten enthalten wird
        nachbarstädte = []
        # Speichern der Nachbarstädte in Adjazenzliste 
        for nachbar in distanceDict[stadt]['Nachbarn'].keys():
            nachbarstädte.append(numbers[nachbar])
        graph.append(nachbarstädte)
    
    # Weights mit "Unendlich" Initialisieren
    for i in range(len(names)):
        for j in range(len(names)):
            weights[(i,j)] = 10000000000000

    # Iteriere über Einträge in json file und speichere Distanzen in weights
    for stadt in distanceDict:
        for nachbar in distanceDict[stadt]['Nachbarn']:
            #print((numbers[stadt], numbers[nachbar]), distanceDict[stadt]['Nachbarn'][nachbar])
            weights[(numbers[stadt], numbers[nachbar])] = distanceDict[stadt]['Nachbarn'][nachbar]


    # Teilaufgabe c) Luftlinie:
    air_distance = {}

    # ermittle alle Luftlinien zwischen den Städten
    for i in range(len(names)):
        for j in range(len(names)):
            #print(distanceDict[names[i]], distanceDict[names[j]])
            air_distance[(i,j)] = entfernung(distanceDict[names[i]], distanceDict[names[j]])

    # Test um zu überprüfen dass Luftlinie stets kürzer als Weglänge
    for i in range(len(names)):
        for j in range(len(names)):
            assert(air_distance[(i,j)] < weights[(i,j)])

    return graph, names, weights, numbers, air_distance




# Teilaufgabe b) Dijkstras Algorithmus implementieren

   
def dijkstra(graph, weights, startnode, destination):
    parents = [None]*len(graph)       # registriere für jeden Knoten den Vaterknoten im Pfadbaum
 
    q = []                            # Array q wird als Heap verwendet
    heapq.heappush(q, (0.0, startnode, startnode))  # Startknoten in Heap einfügen
    n = 0
    while len(q) > 0:                 # solange es noch Knoten im Heap gibt:
        n += 1 # Zähle besuchte knoten
        length, node, predecessor = heapq.heappop(q)   # Knoten aus dem Heap nehmen
        if parents[node] is not None: # parent ist schon gesetzt => es gab einen anderen, kürzeren Weg
            continue                  #   => wir können diesen Weg ignorieren
        parents[node] = predecessor   # parent setzen
        if node == destination:       # Zielknoten erreicht
            break                     #   => Suche beenden
        for neighbor in graph[node]:  # die Nachbarn von node besuchen,
            if parents[neighbor] is None:   # aber nur, wenn ihr kürzester Weg noch nicht bekannt ist
                newLength = length + weights[(node,neighbor)]   # berechne Pfadlänge zu neighbor              
                heapq.heappush(q, (newLength, neighbor, node))  # und füge neighbor in den Heap ein
 
    if parents[destination] is None:  # Suche wurde beendet ohne den Zielknoten zu besuchen
        return None, None             # => kein Pfad gefunden (unzusammenhängender Graph)
 
    # Pfad durch die parents-Kette zurückverfolgen und speichern
    path = [destination]
    while path[-1] != startnode:
        path.append(parents[path[-1]])
    path.reverse()                    # Reihenfolge umdrehen (Ziel => Start wird zu Start => Ziel)
    print('Dijkstra:', names[startnode], 'nach', names[destination], ':', n, 'Knoten besucht.')
    return path, length               # gefundenen Pfad und dessen Länge zurückgeben


# Definiere Funktion, die den Weg formatiert ausgibt
def pfadDarstellung(graph, weights, numbers, start, ziel):

    path, length = dijkstra(graph, weights, numbers[start], numbers[ziel])
    print(start, 'nach', ziel, ':', length, 'km')
    for i in range(len(path)):
        print(names[path[i]], end=' ')
        if i < len(path)-1:
            print('=>', end=' ')
            print(weights[path[i], path[i+1]], 'km', end=' ')
            print('=>', end=' ')
    print('(insgesamt:', length, 'km)', '\n')


# Teilaufgabe c) 


# Funktion um Luftlinie zu berechnen
def entfernung(stadt1, stadt2):
    
    a1, b1 = stadt1['Koordinaten']['Breite'].split('N')
    B1 = (float(a1) + (float(b1) / 60)) / 180 * math.pi

    c1, d1 = stadt1['Koordinaten']['Länge'].split('E')
    L1 = (float(c1) + (float(d1) / 60)) / 180 * math.pi

    a2, b2 = stadt2['Koordinaten']['Breite'].split('N')
    B2 = (float(a2) + (float(b2) / 60)) / 180 * math.pi

    c2, d2 = stadt2['Koordinaten']['Länge'].split('E')
    L2 = (float(c2) + (float(d2) / 60)) / 180 * math.pi

    a = math.sin(B1)*math.sin(B2)
    b = math.cos(B1)*math.cos(B2)*math.cos(L2-L1)

    # in acht fällen wird die Summe wegen rundungsfehlern minimal zu groß
    # daher manuelle korrektur um math error zu verhindern
    if (a + b) > 1:
        c = 1
    else:
        c = a + b

    return 6378.137 * math.acos(c)


# Luftlinien-Test ist in createGraph-Funktion enthalten

# A* Algorithmus

def a_star(graph, weights, air_distance, startnode, destination):
    parents = [None]*len(graph)       # registriere für jeden Knoten den Vaterknoten im Pfadbaum
 
    q = []                            # Array q wird als Heap verwendet
    heapq.heappush(q, (0.0, 0.0, startnode, startnode))  # Startknoten in Heap einfügen
    n = 0
    while len(q) > 0:                 # solange es noch Knoten im Heap gibt:
        n += 1 # Zähle besuchte Knoten
        priority, length, node, predecessor = heapq.heappop(q)   # Knoten aus dem Heap nehmen
        if parents[node] is not None: # parent ist schon gesetzt => es gab einen anderen, kürzeren Weg
            continue                  #   => wir können diesen Weg ignorieren
        parents[node] = predecessor   # parent setzen
        if node == destination:       # Zielknoten erreicht
            break                     #   => Suche beenden
        for neighbor in graph[node]:  # die Nachbarn von node besuchen,
            if parents[neighbor] is None:   # aber nur, wenn ihr kürzester Weg noch nicht bekannt ist
                newLength = length + weights[(node,neighbor)]   # berechne Pfadlänge zu neighbor              
                newPriority = newLength + air_distance[(neighbor, destination)] ## Priority als neues Maß
                heapq.heappush(q, (newPriority, newLength, neighbor, node))  # und füge neighbor in den Heap ein
 
    if parents[destination] is None:  # Suche wurde beendet ohne den Zielknoten zu besuchen
        return None, None             # => kein Pfad gefunden (unzusammenhängender Graph)
 
    # Pfad durch die parents-Kette zurückverfolgen und speichern
    path = [destination]
    while path[-1] != startnode:
        path.append(parents[path[-1]])
    path.reverse()                    # Reihenfolge umdrehen (Ziel => Start wird zu Start => Ziel)
    print('A-Star:  ',names[startnode], 'nach', names[destination], ':', n, 'Knoten besucht.')
    return path, length               # gefundenen Pfad und dessen Länge zurückgeben


# Definiere Funktion, die den Weg formatiert ausgibt
def pfadDarstellung_star(graph, weights, air_distance, numbers, start, ziel):

    path, length = a_star(graph, weights, air_distance, numbers[start], numbers[ziel])
    print(start, 'nach', ziel, ':', length, 'km')
    for i in range(len(path)):
        print(names[path[i]], end=' ')
        if i < len(path)-1:
            print('=>', end=' ')
            print(weights[path[i], path[i+1]], 'km', end=' ')
            print('=>', end=' ')
    print('(insgesamt:', length, 'km)', '\n')



# zu a): json einlesen
with open('entfernungen.json', encoding="utf-8") as f:
    entfernungen = json.load(f)

graph, names, weights, numbers, air_distance = createGraph(entfernungen)

"""
# zu b): Entfernungen ausgeben
pfadDarstellung(graph, weights, numbers, 'Aachen', 'Passau')
pfadDarstellung(graph, weights, numbers, 'Saarbrücken', 'Leipzig')
pfadDarstellung(graph, weights, numbers, 'München', 'Greifswald')
pfadDarstellung(graph, weights, numbers, 'Konstanz', 'Kassel')
"""

# zu c): 
#pfadDarstellung_star(graph, weights, air_distance, numbers, 'Aachen', 'Passau')


# Zeitmessung um zu bestimmen welcher Algorithmus schneller ist

# Zeitmessung
t_start = time.time()
weg1, länge1 = dijkstra(graph, weights, numbers['Aachen'], numbers['Passau'])
t_end = time.time()
zeit1 = t_end-t_start

t_start = time.time()
weg2, länge2 = a_star(graph, weights, air_distance, numbers['Aachen'], numbers['Passau'])
t_end = time.time()
zeit2 = t_end-t_start

# Ausgabe:
print('Algorithmus', 'Zeit', 'Weg', 'Länge')
print('Dijkstra:', zeit1, weg1, länge1)
print('A-Star:  ',zeit2, weg2, länge2)

"""
Algorithmus Zeit Weg Länge
Dijkstra: 0.0004661083221435547 [0, 32, 39, 103, 78, 41, 60, 152, 37, 118, 111] 708.0
A-Star:   0.00020003318786621094 [0, 32, 39, 103, 78, 41, 60, 152, 37, 118, 111] 708.0

Wir sehen, dass die Wege und Distanzen von beiden Algorithmen gleich gefunden wurden.
Die Zeit bei A_star ist weniger als halb so lang wie bei Dijkstra, 
demnach ist der verbesserte Algorithmus tatsächlich schneller :D
"""

# Überprüfe, dass Wege für alle vier Routen gleich gefunden werden
weg1d, länge1d = dijkstra(graph, weights, numbers['Aachen'], numbers['Passau'])
weg1a, länge1a = a_star(graph, weights, air_distance, numbers['Aachen'], numbers['Passau'])
assert(weg1d == weg1a)

weg2d, länge2d = dijkstra(graph, weights, numbers['Saarbrücken'], numbers['Leipzig'])
weg2a, länge2a = a_star(graph, weights, air_distance, numbers['Saarbrücken'], numbers['Leipzig'])
assert(weg2d == weg2a)

weg3d, länge3d = dijkstra(graph, weights, numbers['München'], numbers['Greifswald'])
weg3a, länge3a = a_star(graph, weights, air_distance, numbers['München'], numbers['Greifswald'])
assert(weg3d == weg3a)

weg4d, länge4d = dijkstra(graph, weights, numbers['Konstanz'], numbers['Kassel'])
weg4a, länge4a = a_star(graph, weights, air_distance, numbers['Konstanz'], numbers['Kassel'])
assert(weg4d == weg4a)


# Prüfen wie viele Knoten besucht wurden
# durch zusätzliche Ausgabe/print statements in den Algorithmen

"""
Dijkstra: Aachen nach Passau : 367 Knoten besucht.
A-Star:   Aachen nach Passau : 138 Knoten besucht.
Dijkstra: Saarbrücken nach Leipzig : 309 Knoten besucht.
A-Star:   Saarbrücken nach Leipzig : 51 Knoten besucht.
Dijkstra: München nach Greifswald : 350 Knoten besucht.
A-Star:   München nach Greifswald : 53 Knoten besucht.
Dijkstra: Konstanz nach Kassel : 152 Knoten besucht.
A-Star:   Konstanz nach Kassel : 60 Knoten besucht.

wir sehen, dass A-Star in allen Fällen weniger Knoten besuchen muss als Dijkstra.
"""
