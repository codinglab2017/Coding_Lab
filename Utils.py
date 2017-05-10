# -*- coding: utf-8 -*-
"""
Created on Tue May  9 16:00:24 2017

@author: Till Langbein
"""

def sharpe_ratio(rp:float, rf:float, sdp:float)->float:
    """
    rp-rf
    ------
    sdp
    """
    pass

def standart_deviation(p:list)->float:
    """
    1) Nimm den Durchschnitt deiner Liste
    2) Zieh von jedem Punkt den Durchschnitt ab
    3) Quadriere jeden Punkt
    4) Teile die Summe aller solcher Punkte durch die Anzahl der Punkte -1
    5) Zieh nun die Wurzel aus dem Ergebnis

    Hinweise:
        Es gibt auch fertige Funktionen, die genau das machen.
        Du kannst auch Teile der Funktion wieder als eigene Funktion 
        definieren, der Durchschnitt bietet sich zb hierfür an!
    """
    pass












if __name__ == "__main__":
    assert sharpe_ratio(5, 4, 10) == 0.1, "Your sharpe_ratio should return 0.1"
    assert standart_deviation([1, 2, 3, 4, 5, 4, 5, 6, 5, 6, 7, 4, 5, 8, 7, 9])\
            == 5.0625, "Your standart_deviation should return 5.0625"
    

