# AlDA Blatt 5 Ulrich Prestel und Oskar Weinfurtner
# Aufgabe 2: Taschenrechner

operation = "1+2*4/3"

class Node: 
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Number: 
    def __init__(self, value):
        self.value = value

class Operator: 
    def __init__(self, operator):
        self.operator = operator
        self.left = None
        self.right = None

# Speichere Operator-Präzedenz in Dicitonary:
ops_precedence = {
    '(' : 0,
    ')' : 0,
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

# Funktion zum Umwandeln von infix-Notation in postfix-Notation
def postfixFunktion(infixAusdruck):
    stapel = []
    postfix = [] 

    # Laufe alle Zeichen in der Infix-Notation durch
    for zeichen in infixAusdruck:
        # Zahlen können einfach in die Post-fix-liste gegeben werden
        if zeichen not in ops_precedence:
            postfix.append(zeichen)
        # Operatoren und Klammern extra behandeln
        else:
            if len(stapel) == 0:
                stapel.append(zeichen)
            else:
                # öffende Klammer auf Stapel legen
                if zeichen == "(":
                    stapel.append(zeichen)
                elif zeichen == ")":
                    while stapel[len(stapel) - 1] != "(":
                        postfix.append(stapel.pop())
                    stapel.pop()
                # beachten der Präzedenz der Operatoren
                elif ops_precedence[zeichen] > ops_precedence[stapel[len(stapel) - 1]]:
                    stapel.append(zeichen)
                else:
                    while len(stapel) != 0:
                        if stapel[len(stapel) - 1] == '(':
                            break
                        postfix.append(stapel.pop())
                    stapel.append(zeichen)
     
    while len(stapel) != 0:
        postfix.append(stapel.pop())
    return postfix


# Baum erzeugen aus Infix-Ausdruck s
def parse(s):
    sPostfix = postfixFunktion(s)
 
    stapel = []
 
    for zeichen in sPostfix:
        # Das eingelesene Zeichen ist eine Zahl, kein Operator
        if zeichen not in ops_precedence:
            # Erzeuge ein Blatt und speichere in stapel-liste
            knoten = Number(zeichen)   
            stapel.append(knoten)
        # Das eingelesene Zeichen ist ein Operator
        else:
            # Erzeuge Knoten
            knoten = Operator(zeichen)
            # Die Kinder des Knoten liegen bereits auf dem Stapel
            knoten.right = stapel.pop()
            knoten.left = stapel.pop()
            # lege den Knoten (und damit den gesamten Baum) auf den Stapel
            stapel.append(knoten)
    # gib den Wurzelknoten des Baums zurück
    # das ist automatisch der letzte Knoten auf dem stapel
    return stapel.pop()


# b) Für Skizze siehe Bild in Abgabeordner

# c) Funktion, die den Baum auswertet
def evaluateTree(root):
    # Absichern gegen leeren Knoten
    if root == None:
        return None
    # Falls Knoten Zahl ist, gebe Wert aus
    elif type(root) is Number:
        # cast zu int nötig, weil ziffern als String gespeichert wurden
        return int(root.value)
    # Verschiedene Möglichkeiten für Operationen abprüfen
    elif type(root) is Operator:  
        if root.operator == '*':
            return evaluateTree(root.left)*evaluateTree(root.right)
        elif root.operator == '/':
            return evaluateTree(root.left)/evaluateTree(root.right)
        elif root.operator == '+':
            return evaluateTree(root.left)+evaluateTree(root.right)
        elif root.operator == '-':
            return evaluateTree(root.left)-evaluateTree(root.right)
        else:
            raise Exception("Given Operator in invalid.")
    # Fehler werfen falls kein Fall zutrifft, dann falscher Baum übergeben
    else:
        raise Exception("No valid expression for evaluateTree Function")


# d) Unit Tests

def testCalculator():
    # teste verschiedene Varianten der Operator-Präzedenz und Klammerung
    tree1 = parse("2+5*3")
    tree2 = parse("(1*3)-(2+(2-1))")
    tree3 = parse("3/1*2+5-3")
    tree4 = parse("2+(((3-1)-2)+(2-1))")

    assert(evaluateTree(tree1) == 17)
    assert(evaluateTree(tree2) == 0)
    assert(evaluateTree(tree3) == 8)
    assert(evaluateTree(tree4) == 3)


if __name__ == "__main__":
    testCalculator()

