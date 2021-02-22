Dieses Programm verfügt über die Funktion MERGE, die eine Liste von Listen entgegennimmt, die Intervalle enthalten,
 und alle sich überschneidenden Intervalle zu einem zusammenführt und alle zusammengeführten Intervalle in eine Ausgabedatei namens output.txt zurückgibt.

## How to Use ##
Geben Sie eine Liste der Intervalle `[x,y]`, die Sie zusammenführen möchten, in einer Datei "input.txt" im selben Verzeichnis an und verwenden Sie ';' als Trennzeichen.

Starten Sie das Programm mit dem Befehl `make run`

## Laufzeit ##
Die Laufzeit für das Programm ist in O(n) es werden hauptsächlich einfache for-schleifen verwendet. 
In den Zeilen 45 & 47 haben wir eine geschachtelte for-schleife. Zeile 45 läuft über alle Zeilen der Input Datei (im einfachen Fall nur eine Zeile mit n Elementen). 
Das sorting geschieht über effeziente built in Algorithmen.
Auch bei großen Eingaben, läuft das Programm effizient und nahezu in linearer Zeit.

## Robustheit ##
Das Programm ist auf die richtige Formattierung der Intervalle in der input.txt-Datei angewiesen, sowie der richtigen Namensgebung dieser Datei.
Ebenso liest das Programm lediglich aus einem Dateityp Daten aus. befinden sich die Intervalle in einer Datei in anderem Format muss, das Programm angepasst werden.

## Speicher ##
Der Speicherverbrauch ist angemessen auch für große Dateneingaben. Es werden lediglich zwei "große" variablen angelegt, welche sind `intervals` und `nowMerged`, wobei `nowMerged` meist sehr viel kleiner als `intervals` ist, da diese alle merged Intervalle enthält und `intervals` alle regulären Intervalle als integer Liste.

@author Leander van Diepen
@license MIT
@version 1.0
@date 2/22/2021

Bearbeitungszeit: 3-4 Stunden
