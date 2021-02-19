# Bolus Empfehlungen

Die Loop-App wird eine Bolus-Empfehlungen vorschlagen für den eventuellen Fall, dass der Blutzucker höher ist als der Zielwert und das aktive Insulin plus eine noch ausstehende 30 minütige Basalrate nicht ausreichen, um den vorhergesagten zu hohen Verlauf auszugleichen. Diese Empfehlungen werden nicht proaktiv an den Benutzer der Loop-App durch Mitteilungen oder Banner mitgeteilt. Die Empfehlung ist nur dann sichtbar, wenn der Benutzer auf das Bolus-Werkzeug tippt. Note that Loop never issues a bolus command automatically; all boluses are initiated by the user.

Die Berechnung der Bolusmenge stimmt mit der Formel zur Berechnung der Basalmengen-Empfehlung überein mit der folgenden Ausnahme:

* der Anteil an der momantan laufenden temporären Basalrate, die durch die Loop-App eingestellt wurde, wird vom von der empfohlenen Boulsmenge abgezogen und
* die Differenz wird zum oberen und nicht zum mittleren Wert des Korrekturbereiches berechnet

Bei erst kürzlich eingegeben Kohlenhydraten, bei denen die vorhergesagte Absorbtion länger dauert, als die Insulinwirkdauer (z.B. bei sehr langsam absorbierenden Mahlzeiten, wie Pizza oder Pasta) wird der Loop-Algorithmus von sich aus den initialen Essensbolus herabsetzen, um den häufig auftretenden Fall von Unterzuckerung bei solchen Mahlzeiten zu verhindern, indem er nur so viel Bolus vorschlägt, dass der Blutzucker nicht unter den Korrekturbeich gerät. Wie oben beschrieben schlägt der Algorithmus nur so viel Insulin vor, dass der vorhergesagte Blutzuckerverlauf nicht unter den Korrekturbereich fällt. Das kann zu einem vorhergesagten Bluzuckerwert führen, der über dem Korrekturbereich liegt, verhindert dadurch aber eine Unterzuckerung kurz nach der Mahlzeit, so wie es manchmal bei Menschen mit einer normalen Pumpentherapie vorkommt, die einen "Pizza-Bolus" eingeben. Die Loop-App wird dann zu einem späteren Zeitpunkt Korrekturen mit Hilfe von höheren temporären Basalraten verabreichen. In Wirklichkeit miemt der Algorithmus den erweiterten oder Dual Wave Modus bei der normalen Insulinpumpentherapie nach, mit dem Vorteil von zusätzlichen Informationen über die aktuelle Kohlenhydratabsorbtionseffekte, sobald alles vorbei ist.

Letztendlich überprüft die Loop-App noch, ob das Ergebnis der Berechnung über der maximalen Bolusmenge liegt, die der Benutzer in seinen Einstellungen festgelegt hat. Sollte der berechnete Boluswert kleiner sein als die maximal erlaubte Bolusmengeneinstellung, wird er dann im Bolus-Werkzeug der Loop-App angezeigt.

!!!info "Bolus-Sicherheits Feature"

    Sollte der aktuelle Bluzuckerwert oder irgendein Wert der Vorhersage unterhalb des Abschaltwertes liegen, wird die Loop-App keine Empfehlung für einen Bolus anzeigen. Wenn der kleinste Vorhersagewert oberhalb des Abschaltwertes liegt, wird eine Empfehlung angezeigt.
