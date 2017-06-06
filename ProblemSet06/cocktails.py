# Alda Blatt 6: Ulrich Prestel und Oskar Weinfurtner
# Aufgabe 2: Cocktail Datenbank

# json importieren für Einlesen
import json



with open('cocktails.json') as json_data:
    # Speichere Rezepte in Dictionary recipes
    recipes = json.load(json_data)
    print(type(recipes))

# Teste ob einlesen funktioniert
#print(recipes["Caipirovka"])

def all_ingredients(recipes):
    ingredients = []
    for cocktail in recipes:
        for ingredient in cocktail["ingredients"]:
            ingredients.append(ingredient)

all_ingredients(recipes)