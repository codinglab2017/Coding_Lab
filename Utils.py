# -*- coding: utf-8 -*-

#############################################################################
# By the way: Zeilen die mit einem Hashtag beginnen und Text zwischen je drei 
# Gänsefüßchen ist ein Kommentar und wird nicht als Programm ausgeführt.
# Er dient nur dazu, mit anderen Programmierern im Code zu kommunizieren und
# ihnen klarzumachen warum man etwas so gemacht hat.
# Je größer die Teams werden, desto wichtiger ist eine umfangreiche 
# Kommentierung.
#############################################################################

def sharpe_ratio(rp, rf, sdp):
    """
    rp : rendite des Portfolios
    rf : risikofreier Zins
    sdp : Volatilität des Portfolios
    
    rp-rf
    geteilt durch:
    sdp
    """
    pass


def share_dividend_value(rf, div0, g):
    """
    Es muss gelten: g < rf
    
    rf : risikofreier Zinssatz
    div0 : Anfängliche Dividende
    g : Dividendenwachstum pro Periode
    
    div0 
    mal
    (1 + g)
    mal
    (rf - g)^-1
    """
    pass


def total_stock_return(p0, p1, D):
    """
    p0 : Einstiegspreis
    p1 : Endpreis
    D : Dividendenzahlungen
    
    (p1 - p0) + D
    geteilt durch
    p0
    """
    pass


def standard_deviation(p):
    """
    p : eine Liste [] von Werten
    
    1) Errechne den Durchschnittswert deiner Liste
    2) Zieh von jedem Element der Liste den Durchschnitt ab
    3) Quadriere jedes Element
    4) Teile die Summe aller solcher Elemente durch die Anzahl der Elemente -1
    5) Zieh nun die Wurzel aus dem Ergebnis

    Hinweise:
        Es gibt auch fertige Funktionen, die genau das machen.
        Du kannst auch Teile der Funktion wieder als eigene Funktion 
        definieren, der Durchschnitt bietet sich zb hierfür an!
    """
    pass

############################################################################
# Bitte fügt weitere Funktionen hinzu, die ihr gerne in einem Börsenspiel
# zur Verfügung hättet!
############################################################################

if __name__ == "__main__":
    # Dieser Teil wird ausgeführt, wenn ihr das Programm ausführt
    # Es wird ein Fehler geworfen, wenn eine Funktion ein 
    # falsches Ergebnis liefert
    assert sharpe_ratio(5, 4, 10) == 0.1, \
            "Your sharpe_ratio(5, 4, 10) should return 0.1"
    assert share_dividend_value(0.05, 10, 0) == 200.0, \
            "Your share_dividend_value(0.05, 10, 0) should return 200"
    assert total_stock_return(100, 110, 10) == 0.2, \
            "Your total_stock_return(100, 110, 10) should return 0.2"
    assert standard_deviation([1, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 8, 7, 9]) == 5.0625, \
            "Your standard_deviation([1, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 8, 7, 9]) should return 5.0625"
    

