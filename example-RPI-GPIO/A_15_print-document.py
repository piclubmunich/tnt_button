#in diesem Programm lernen wir eine dokument zu drucken mit deinem tnt-button

# installiere cubs
# § sudo apt-get install cups
# § sudo usermod -a -G lpadmin username
# oeffne Chromium und tippe http://1 27.0.0.1 :631 ein
# gebe dein username und dein root-password kano ein
# clicke auf add printer
# suche deinen printer und fuege in hinzu
# installiere python cubs
# § sudo apt-get install python-cups

# $ sudo apt-get install abiword
# $ sudo apt-get install libreoffice
# oder gehe in den kano app store und lade die beide Programme herunter
# bei meinem ersten Test konnte ich libre office nicht installieren, ich vermute aber es liegt daran, dass meine SD Karte bereits voll ist
# 


#schreibe ein Programm mit dem du eine datei mit deinem TNT-Button ausdruckst
#achtung das Porgramm geht noch nicht!!!

import cubs
conn = cups.Connection ()
printers = conn.getPrinters ()
for printer in printers:
  print printer, printers[printer]["device-uri"]
