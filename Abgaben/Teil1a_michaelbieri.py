import numpy as np
liste = [12,23,234,543,583,984,132,431] #fuer alle Funktionensbeispiele

### Arithmetrischs Mittel = mean
def mean(values):
    total = sum(values)
    number = len(values)
    return total/number

# Beispiel
#Beispiel_arithm = mean(liste)
#print("Das arithmetrische mittel fuer die liste ist:", Beispiel_arithm)

### Geometrisches Mittel = zentralen Wert Wurzel(x1*x2*x3)
#Verwendung fuer Wachtums- oder Zuwachsdaten.
def geometrisches_mittel(values):
    produkt = 1
    n = len(values)
    for value in values:
        produkt *= value
    return produkt ** (1 / n) #** heisst wurzel, es wird von innen gestartet

# Beispiel
#Beispiel_geomittel = geometrisches_mittel(liste)
#print("Das geometrische mittel fuer die liste ist:", Beispiel_geomittel)

### Harmonisches Mittel
def harmonisches_mittel(values):
    return len(values) / sum(1/value for value in values)
    
# Beispiel
#Beispiel_harmmittel = harmonisches_mittel(liste)
#print("Das harmonische mittel der liste ist:", Beispiel_harmmittel)

### Median mit sorted funktion oder sort/copy
# Wenn Datenanzahl ungerade: zuerst Daten sortieren und dann die mitte der Werte
# Wenn gerade: Durchschnitt der beiden mittleren Werte
def median(values):
    sorted_values = sorted(values)  # Sortiere die Werte
    length = len(sorted_values)  # Anzahl der Werte
    middle_index = length // 2  # Mittlerer Index

    if length % 2 == 1:  # Wenn die Anzahl der Werte ungerade ist
        return sorted_values[middle_index]  # Der Wert in der Mitte ist der Median
    else:  # Wenn die Anzahl der Werte gerade ist
        lower_value = sorted_values[middle_index - 1]  # Wert unter der Mitte
        upper_value = sorted_values[middle_index]  # Wert über der Mitte
        return (lower_value + upper_value) / 2  # Mittelwert der beiden mittleren Werte

# Beispiel
#Beispiel_median = median(liste)
#print("Der Median der liste ist:", Beispiel_median)

### Modus
# Wert der am hauefigsten vorkommt
def modus(values):
    counter_liste = {} #Leere Liste um die Anzahl jedes Wertes darin abzuspeichern
    for value in values: #Fuer alle Werte in values
        if value in counter_liste: #Wenn ein Wert bereits in der counter_liste ist
            counter_liste[value] += 1 #Wenn drin dann um 1 erhoehen
        else:
            counter_liste[value] = 1 #Wenn nicht dann einfuegen
            
    max_value = max(counter_liste.values())
    mode = [key for key, count in counter_liste.items() if count == max_value] #Key ist der Wert und count Anzahl der Vorkommen, es wird geprueft ob die Anzahl der Vorkommen gleich der max. Anzahl der Vorkommen ist. Ist die max value erreicht, wird es auf mode aufgenommen.
            
# Beispiel
#Beispiel_modus = modus(liste)
#print("Der modus der liste ist:", Beispiel_modus)

### Varianz
def varianz(values):
    n = len(values)
    durchschnitt = sum(values)/n
    klammersumme = (sum(x-durchschnitt) ** 2 for x in values) # Fuer alle Werte x
    return klammersumme/2

# Beispiel
#Beispiel_varianz = varianz(liste)
#print("Die Varianz der liste:", Beispiel_varianz)

### Standardabweichung
# Wie varianz aber mit Wurzel ueber allem
def standardabweichung(values):
    varianzwert = varianz(values)
    return varianzwert ** 0.5 #Verwendung Funktion varianz

# Beispiel
#Beispiel_standardabweichung = standardabweichung(liste)
#print("Die Standardabweichung der liste ist:", Beispiel_standardabweichung)

### Variationskoeffizient
#Mass fuer die relative streuung im verhaeltnis zum mittelwert, Standardabweichung durch mittelwert und multiplizieren mit 100 fuer prozent
def variationskoeffizient(values):
    mittelwert = sum(values)/len(values)
    variationskoeffizient_wert = (standardabweichung(values)/mittelwert) * 100
    return variationskoeffizient_wert

#Beispiel
Beispiel_variationskoeffizient = variationskoeffizient(liste)
print("Der variationskoeffizient der liste ist:", Beispiel_variationskoeffizient)