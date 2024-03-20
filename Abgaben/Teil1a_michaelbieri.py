import numpy as np
liste = [12,23,234,543,583,984,132,431] #fuer alle Funktionensbeispiele

### Arithmetrischs Mittel = mean
def mean(values):
    total = sum(values)
    number = len(values)
    return total/number

# Beispiel
#liste = [4,234,1235,46345,123,234,234]
print(mean(liste))

### Geometrisches Mittel = zentralen Wert Wurzel(x1*x2*x3)
#Verwendung fuer Wachtums- oder Zuwachsdaten.
def geometrisches_mittel(values):
    produkt = 1
    n = len(values)
    for value in values:
        produkt *= values
    return produkt ** (1/n) #** heisst wurzel, es wird von innen gestartet

# Beispiel
#liste = [12,23,234,543,583,984,132,431]
Beispiel_geomittel = geometrisches_mittel(liste)
print("Das geometrische mittel fuer die liste ist:", Beispiel_geomittel)

### Harmonisches Mittel
def harmonisches_mittel(values):
    return len(values) / sum(1/value for value in values)
    
# Beispiel
#liste = [135,123,345,234]
Beispiel_harmmittel = harmonisches_mittel(liste)
print("Das harmonische mittel der liste ist:", Beispiel_harmmittel)

### Median mit sorted funktion oder sort/copy
# Wenn Datenanzahl ungerade: zuerst Daten sortieren und dann die mitte der Werte
# Wenn gerade: Durchschnitt der beiden mittleren Werte
def median(values):
    if values % 2 == 1: # Wenn ungerade
        sorted_values = sorted(values) # Sortieren
        n = len(sorted_values) # Anzahl der Werte
        return n // 2 # Die Mitte dieser Werte ist der Median
    else: # Wenn gerade
        sorted_values = sorted(values)
        length = len(sorted_values)
        middle_index = length // 2 # Mittlere Zahl als index
        wert1 = sorted_values[middle_index] # mittlere Wert
        wert2 = sorted_values[middle_index - 1] # untere Wert
        return wert1 / wert2

# Beispiel
Beispiel_median = median(liste)
print("Der Median der liste ist:", Beispiel_median)

### Modus
def modus(values):
    

### Varianz

### Standardabweichung

### Variationskoeffizient