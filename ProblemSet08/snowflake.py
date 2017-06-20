# ALDA Blatt 8 Ulrich Prestel und Oskar Weinfurtner
# Aufgabe 1: Snowflake


set term postscript color portrait # aktiviere Postscript-Ausgabe
set out "snowflake.eps"            # Dateiname für Ausgabe setzen
set size square
set xrange [-0.2:1.2]
set yrange [-0.4:1.0]
plot "snowflake.txt" with lines    # Punktliste einlesen und zeichnen
unset out                          # Ausgabedatei schließen


