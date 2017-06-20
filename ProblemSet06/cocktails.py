# Alda Blatt 6: Ulrich Prestel und Oskar Weinfurtner
# Aufgabe 2: Cocktail Datenbank

# Teilaufgabe a)

# json importieren für Einlesen
import json

# Einlesen der Rezepte in ein Dictionary
with open('cocktails.json') as json_data:
    # Speichere Rezepte in Dictionary recipes
    recipes = json.load(json_data)
    #print(type(recipes))

# Normalisierungsfunktion, soll extra Funktion sein nach Aufgabenstellung
def normalizeString(s):
    # teilt string wenn Klammer erscheint und gibt nur ersten (relevanten) Teil zurück
    # wandelt string in Kleinschreibung um
    return s.split(" (")[0].lower()

# Funktion, die Dictionary mit Rezepten bekommt 
# und Liste mit allen Zutaten zurückgibt
def all_ingredients(recipes):
    ingredients = []

    # durchlaufe alle cocktails
    for cocktail in recipes:
        # durchlaufe die Zutaten jedes Cocktails
        for ingredient in recipes[cocktail]["ingredients"]:
            ingredients.append(normalizeString(ingredient))

    # Liste mit Zuaten zurückgeben
    return list(set(ingredients))

# Prüfe wie viele Zutaten in Rezepten vorkommen: 523
print("Anzahl der Zutaten:", len(all_ingredients(recipes)))


# Teilaufgabe b)

def cocktails_inverse(recipes):
    dictionary = {"":[]}
    # Zutaten in Liste speichern
    ingredients = all_ingredients(recipes)
    # iteriere über alle Zutaten
    for ingredient in ingredients:
        # füge Zutat dem Dictionary hinzu
        dictionary.update({ingredient: []})
        # iteriere über alle Cocktails in Rezepten
        for cocktail in recipes:
            name = cocktail
            # prüfe ob Zutat gebraucht
            if ingredient in " ".join(recipes[cocktail]["ingredients"]).lower():
                # wenn ja, füge Cocktail der Zuatat hinzu
                dictionary[ingredient].append(name)
    return dictionary
    

inverse = cocktails_inverse(recipes)

# exportiere das Dictionary
with open('cokctails_inverse.json', 'w') as file:
    json.dump(inverse, file)


def best_recipes(recipes):
    # cocktails_inverse Funktion benutzen um Zuordnung zu erhalten
    zutaten = cocktails_inverse(recipes)
    # lege zweites dictionary an
    counts = {"": 0}
    # speichere jeweils die Zutat und Anzahl der Cocktails
    for zutat in zutaten:
        counts.update({zutat: len(zutaten[zutat])})
    # gebe 15 häufigsten Zutaten aus sortiert nach den Anzahlen
    print("Zutat", "#Cocktails")
    n = 0    
    for item in sorted(counts, key=counts.get, reverse=True):
        if n < 15:
            print(item, counts[item])
        n += 1    

best_recipes(recipes)

"""
Die 15 häufigsten Zutaten sind:
ei 723
eiswürfel 484
zitrone 350
orange 281
crushed ice 277
zucker 266
zitronensaft 263
rum 260
sirup 252
likör 219
orangensaft 218
sahne 186
met 186
mett 185
wodka 185
"""

