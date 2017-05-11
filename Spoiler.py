# -*- coding: utf-8 -*-

import numpy as np


def sharpe_ratio(rp, rf, sdp):
    return (rp - rf) / sdp # Ein einfacher Taschenrechner


def share_dividend_value(rf, div0, g):
    if not g < rf: # Es muss gelten: g < rf 
        return # also returnen wir nichts, wenn es nicht gilt
    else: # Wenn die Bedingung erfüllt ist, dann führe die Formel aus
        return div0 * (1 + g) * (1 / (rf - g))
        

def total_stock_return(p0, p1, D):
    return (p1 - p0 + D) / p0 # Rechenregeln sind wie im Mathematischen


def avg(p): # Dient als Hilfe für standard_deviation1
    temp = 0 # Erschaffe ein Variable, die erstmal 0 ist.
    for x in p: # für jedes Element von p, wir nennen es jeweils x:
        temp += x # rechne das jeweilige x auf temp drauf
    return temp / len(p) # len() gibt die Länge einer Liste zurück

    
def standard_deviation(p):
    mean = avg(p) # Nimmt die Funktion, die wir oben definiert haben, um den
    # Durchschnitt der Elemente unserer Liste zu bestimmen
    result = [] # legt eine leere Liste  mit dem Namen result an
    for i in p: # für jedes Element von p, wir nennen es jeweils i:
        result.append((i - mean) ** 2) # hängen wir die Differenz von i und 
        # dem Durchschnitt an zum Quadrat an unsere leere Liste
    return (avg(result)) ** 0.5 # Und geben die nun die Wurzel des 
    # Durchschnitts der nunmehr nicht mehr leeren Liste zurück

# Jetzt kommen zwei andere Wege wie man es hätte machen können:
# Es gibt aber kein richtig oder Falsch
def standard_deviation2(p):
    n = len(p) # Die Funktion len(Liste) gibt die Länge der List zurück
    mean = sum(p) / n # Die Funktion sum(Liste) gibt die Summe aller Elemente zurück
    result = ((i - mean) ** 2 for i in p) # Jo.. Generator Comprehension... Lernt ihr noch
    return (sum(result) / n) ** 0.5

def standard_deviation3(p):
    return np.array(p).std() # Jemand hat uns natürlich schon die Arbeit abgenommen.

    
if __name__ == "__main__":
    
    assert sharpe_ratio(5, 4, 10) == 0.1, \
            "Your sharpe_ratio(5, 4, 10) should return 0.1"
    assert share_dividend_value(0.05, 10, 0) == 200.0, \
            "Your share_dividend_value(0.05, 10, 0) should return 200"
    assert total_stock_return(100, 110, 10) == 0.2, \
            "Your total_stock_return(100, 110, 10) should return 0.2"
    assert standard_deviation([1, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 8, 7, 9]) == 2.0453835214941964, \
            "Your standard_deviation([1, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 8, 7, 9]) should return 2.0453835214941964"
    
