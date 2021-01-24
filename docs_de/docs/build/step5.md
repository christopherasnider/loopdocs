# Schritt 5: Bestellung eines RileyLink

!!!Gefahr "Geschätzte Zeit"
    - 15 Minuten um einen RileyLink zu bestellen
    - 15-20 Minuten, um den RileyLink zusammenzusetzen, sobald du ihn mit der Post bekommen hast
    - 15-20 Minuten um über den RileyLink zu lesen

!!! Info "Zusammenfassung"
    - Bestellen deinen [Omnipod RileyLink](https://getrileylink.org/product/rileylink433) oder [Medtronic RileyLink](https://getrileylink.org/product/rileylink916).
    - Baue den RileyLink zusammen, nachdem du den Postboten freudig verabschiedet hast
    - Lies die "Extradetails" um mehr über die RileyLink Signallämpchen, das Aufladen, die Empfangsreichweite usw. zu erfahren.

!!!warning "FAQs"
    - **"Brauche ich einen RileyLink?"** Ja. Loop funktioniert nicht ohne RileyLink und Omnipod Benutzer können ohne RileyLink auch keinen Bolus geben.
    - **"Was passiert, wenn ich meinen RileyLink verliere oder mich davon entferne?"** Gute Frage...hier [beantwortet](/faqs/rileylink-faqs/#what-happens-if-i-walk-away-from-my-rileylink).
    - **"Kann ich einen Omnipod RileyLink mit einer Medtronic-Pumpe verwenden? oder umgekehrt?"** Gute Frage... [hier beantwortet](/faqs/rileylink-faqs/#what-will-happen-if-you-use-a-916mhz-antenna-rileylink-with-an-omnipod-or-vice-versa).
    - **"Kann ich RileyLinks jederzeit tauschen?"** Ja, das ist möglich. RileyLinks können ganz einfach ersetzt werden, ohne dass du einen neuen Pod starten oder die Loop App neu erstellen musst. In den Loop-Einstellungen findest du leicht den Namen des neuen RileyLink und aktivierst die Bluetooth-Verbindung, um ihn zu verwenden.
    - **"Wie nah muss mir der RileyLink bei mir sein? Muss ich ihn bei mir tragen?"** Gute Fragen...beantwortete [hier](/faqs/rileylink-faqs/#do-i-have-to-carry-the-rileylink-everywhere).
    - **"Warum heißt es eigentlich RileyLink?"** Riley ist der Name von Pete Schwamb's Tochter und er hat den RileyLink entwickelt.
    - **"Kann ich einen RileyLink komplett selbst bauen?"** Theoretisch ja, aber das ist kein einfaches Projekt. Du brauchst dafür spezielles Werkzeuge und eine gute Portion Geduld. Wenn du das näher erforschen möchtest empfehle dir [Zulipchat](https://loop.zulipchat.com/#narrow/stream/148542-RileyLink) von anderen Leuten anzusehen, die in den letzten Jahren erfolgreich ihre eigenen RileyLinks gebaut haben. Allerdings haben bisher nur 3 Personen ihre eigenen RileyLinks gebaut...aber ich denke, das bedeutet technisch ist es möglich. Die PCB-Dateien und -Software mit Anweisungen, wie du dein eigenes Hardware-Modul baust, findest du im [RileyLink Github repo](https://github.com/ps2/rileylink).

## Was ist ein RileyLink

Der RileyLink (RL) ist ein Open-Source-Hardware-Gerät, das die Kommunikation zwischen niedrigenergie Bluetooth (BLE, Bluethooth Low Energie) und 916MHz oder 433MHz drahtlosem Funk überbrücken kann. Was bedeutet das für dich? Es bedeutet, RileyLink ist das Bindeglied zwischen deiner Insulinpumpe, CGM und iPhone.</br></br>

Loop funktioniert nicht ohne RileyLink.</b></br></br>

![../img/RL_bt.jpg](img/rl_diag.png)

## RileyLink bestellen

Das ist ein einfacher Schritt, du musst einen RileyLink auf der [GetRiley Webseite](https://getrileylink.org) bestellen.

Es gibt zwei Typen des RileyLinks: [einen für Omnipod](https://getrileylink.org/product/rileylink433) Benutzer und [einen für Medtronic](https://getrileylink.org/product/rileylink916) Benutzer. Bestelle den RileyLink genau für die Insulinpumpe, mit der du Loop benutzen wirst.

## RileyLink zusammenbauen

Dein RileyLink wird in Einzelteilen geliefert, also Akku getrennt, die kleine Platine und das Gehäuse. Du wirst den Akku verbinden und alles in das Gehäuse stecken.

Pass auf, dass die Steckverbindung vom Lipo-Akku gut eingerastet ist. Richte die kleine Nut richtig aus und drücke den Stecker ziemlich fest in die Buchse, um eine sichere Verbindung zu bekommen.  Eine schlechte Akkuverbindung kann dazu führen, dass die Loop-Kommunikation fehlschlägt.  Siehe die Beispielfotos unten an.

!!!info "Typische Benutzerfehler"

    Die häufigsten zwei Fehler neuer RL-Besitzer sind (1) nicht vollständig den Lipo-Akkustecker in die Buchse zu schieben und (2) den RL nicht aufzuladen. Vergleichen dein Lipo-Akku-Kabel mit den Fotos; es braucht ein bisschen Kraft, um den Stecker, wie auf dem Foto unten, vollständig in die Buchse zu schieben. Denke daran, deinen RL jede Nacht aufzuladen.

![../img/rileylink_battery_removal.png](img/battery-cables.jpg)

<figcaption>Lockere Steckverbindung links, richtige Steckverbindung rechts</figcaption>

Schlußendlich passt die kleine Platine und der Akku auch nur gerade eben in das kleine Gehäuse.  Klicke auf das Bild unten, um ein hilfreiches [Montagevideo](https://www.youtube.com/watch?v=-GHxxEJMCZc&feature=youtu.be) zu sehen.

[![img/slimcase.png](img/slimcase.png)](https://www.youtube.com/watch?v=-GHxxEJMCZc&feature=youtu.be)

## Zusätzliche Informationen über RileyLink

### Funkkommunikation

Der RL kommuniziert mit der Insulinpumpe über Funk.  Zahlreiche Faktoren beeinflussen, wie gut diese Kommunikation funktionieren kann... Störungen von anderen Geräten, Temperatur, physikalische Abschirmung usw.

Wenn dein RL und Insulinpumpe zum ersten Mal gekoppelt werden, führt Loop eine Reihe von Tests durch, die du nicht sehen kannst... dieses dienen der Feinabstimmung der Kommunikation. Dabei sendet der RL kleine Testmeldungen an die Insulinpumpe und wartet auf die Antwort. Dein RL versendet das gleiche "ping" an die Insulinpumpe in verschiedenen Funkfrequenzen. Dabei ist der Bereich der getesteten Funkfrequenzen abhängig von deiner Insulinpumpe, die du dem RL über die Loop-Einstellungen mitgeteilt hast (Omnipod, Medtronic WW oder Medtronic NA/CA).  Dein RL merkt sich dann die Funkfrequenzen, die die stärkste Antwortsignale geliefert haben und nutzt diese Frequenzen dann für die zukünftige Kommunikationen mit deiner Insulinpumpe.

Normalerweise ist die beste Funkfrequenz für jede gegebene Pumpe+RL ziemlich konstant, aber bei Temperaturänderungen kann es sein, dass die beste Frequenz nicht die ist, die derzeit eingestellt ist. Für den Falls, dass der RL mal Probleme mit der Kommunikation mit deiner Insulinpumpe hat, hat Loop hat Code eingebaut. Dieser Code ("Hey RL, versuche die Feinabstimmung mit der Pumpe noch einmal... vielleicht gibt es eine bessere Frequenz.") wiederholt automatisch die Suche nach der besten Funkfrequenz. Diese Neuabstimmung findet automatisch statt, wenn die Kommunikation mit der Insulinpumpe 14 Minuten lang ausfällt (d. h. zwei Loop-Zyklen).

### Bluetooth-Kommunikation

Der RL kommuniziert mit deinem iPhone und Loop-App über Bluetooth (BT).

!!!info "Bluetooth Fehlerbehebung"

    Wenn dein iPhone BT Probleme hat, funtioniert Loop nicht.  Es gab Berichte über BT-Audiogeräte (wie BT-Verbindungsversuche im Auto oder BT-Heimlautsprecher), die die Loop stören.  Wenn an einem bestimmten Ort häufig Fehler auftreten, solltest du untersuchen, ob es dort Probleme mit BT gibt und diese beheben.

Die BT-Signalstärke kannst du in den Loop-Einstellungen im RL-Menü unter `Signalstärke` anschauen.  Wenn du dich immer weiter von deinem Telefon entfernst, kannst du beobachten, wie sich diese Nummer dynamisch ändert. Diese Anzeige **zeigt nicht** die Signalstärke der Kommunikation mit deiner Insulinpumpe an.

![img/RL_bt.jpg](img/RL_bt.jpg)

### Signallämpchen

Der RL hat mehrere Signallämpchen, die du manchmal bemerken wirst. Es gibt kein spezielles Signallämpchen, welches anzeigt, dasss der Rl auch eingeschaltet ist. Wenn du vermutest, dass dein RL nicht eingeschaltet ist, versuchen ihn mit dem kleinen Schieberegler aus- und wieder einzuschalten. Wenn du das tust, solltest du Signallämpchen auf der Boardmitte aufblinken sehen.  Wenn sie aufblinken bedeutet es, dass die Platine über Strom verfügt.

* Rotes Signallämpchen: Ladelicht. Das rote Signallämpchen leuchtet während der Akku des RL geladen wird und es geht wieder aus, wenn die Ladung abgeschlossen ist. Du wirst sehen, dass das rote Signallämpchen periodisch aufleuchtet, auch wenn das Laden abgeschlossen ist... der Akku wird einfach "voll gehalten".

* Grünes Signallämpchen: Bluetooth-Verbindungslicht. Die grüne Signallämpchen leucht konstant, solange du eine BT-Verbindung mit deinem iPhone hast.  Wenn dieses grüne Signallämpchen nicht leuchtet, musst du eine Fehlersuche der BT-Verbindungen machen. Versuchen BT auf deinem iPhone neu zu starten und/oder den RL aus- und wieder einzuschalten.

* Blaues Signallämpchen: Insulinpumpenkommunikation.  Wenn du eine ältere Firmware auf deinme RL hast, werden einige der blauen Signallämpchen regelmäßig blinken, während der RL mit der Insulinpumpe kommuniziert. Es zeigt nur an, dass es gearde aktiv ist und Informationen austauscht. Du wirst auch häufiger blaues Blinken sehen, wenn du als MDT-Benutzer "DiagnoseLEDs eingeschaltet" hast, die einen RLs mit aktualisierter Firmware hast (Versand seit Ende August 2018).

Ein permanet leuchtendes blaues Signallämpchen, kann eines von zwei Dingen bedeuten:

* Ein temporäres Problem, das durch einen Neustart des RL behoben werden kann (aus- und wieder einschalten) oder

* Ein elektrischer Kurzschluss oder ein Schaden an der Platine.  Schweiß und Feuchtigkeit sind dafür am ehesten der Grund, also versuchen am besten das Gehäuse davon fern zu halten. Stecke deshalb den RL z. B. beim Training nicht in einen Sport-BH oder ein Taillenband direkt an der Haut.

Wenn das blaue Signallämpchen trotz eines Neustarts des RL weiter leuchtet, ist es an der Zeit, deinen Backup-RL fertig zu machen.

### Aufladen

Der mit dem RL gelieferte Akku wird wahrscheinlich nicht vollständig geladen sein, also zöge nicht ihn aufzuladen.  Dafür benötigst du ein [Mini-USB-Kabel](https://www.amazon.com/AmazonBasics-USB-2-0-Cable--Male/dp/B00NH13S44) und [0.5A USB-Ladesgerät](https://www.amazon.com/Cellet-Powered-Charger-iPhones-Smartphones-/dp/B00FE8WFCO) wie dein iPhone-Ladegerät.  Es dauert ca. 2 Stunden den RL voll zu laden (das rote Signallämpchen schaltet sich ab, wenn er voll geladen ist, lies oben die Hinweise zum roten Signallämpchen) und sollte locker ausreichen, um einen vollen Tag mit Loop zu funktionieren.  Es sollte sogar für ca. 30-Stunden Benutzung ausreichen.  Die meisten laden ihren RL jede Nacht, wenn sie schlafen.  Du musst dir keine Sorgen machen, den RL "zu lang" am Ladegrät angeschlossen zu haben,  sobald der Akku voll ist, hört der Ladevorgang automatisch auf.

Da es am besten ist deinen RL über Nacht zu laden, während du schläfts, und der Akuu danach sicher für 24 Stunden hält, gibt es am RL keine Batterieanzeige.  Der Ladezustand des RL ist weder bei Nightscout, noch in der Loop App sichtbar.  Falls du einmal vergessen hast deinen RL über Nacht aufzuladen, kannst du ihn auch am nächsten Tag mit einem tragbaren USB-Akku aufladen.  Ein [kurzes Mini-USB-Kabel](https://www.adafruit.com/product/899) ist deshalb eine gute Ergänzung für deine Notfall/Diabetikertasche.

### Funkreichweite

Der Funkreichweite deines RL ist **stark** von der Umgebung abhängig, in der du dich befindest. Die meisten tragen ihren RL am Tag in der Hosentasche oder an einen Gürtelholster. Die Kommunikation über Funk hat eine kürzere Reichweite, als die BT-Kommunikation. Wenn du also überlegst, wie du den RL am besten trägst, ist es besser den RL dichter an der Insulinpumpe zu haben, als am iPhone.

Problematische Umgebungen sind Orte wie z.B. technische Konferenzen, Sportarenen und andere Plätze, wo andere drahtlose Kommunikation über Funkfrequenzen stark und zahlreich ist.

### Lithium-Polymer Akku

Schütze deinen RL und den Lithium-Polymer (Lipo) Akku vor Beschädigungen.  Lipo-Akkus sind gefährlich, wenn sie beschädigt oder durchstochen werden, deshalb ist die Hülle des RL ein wichtiger Teil, um sicher Loop zu benutzen. Wenn dein Lipo-Akku in irgendeiner Weise beschädigt wurde, trennen ihn bitte sofort vom RL und entsorge ihn fachgerecht (du solltest ihn zum Recycling bringen). Einen neuen Akku kannst du auf der [GetRileyLink-Website bestellen](http://getrileylink.org/)

### Lipo-Batterie herausnehmen

Nimm dir Zeit und arbeite sorfältig, wenn du den Lipo-Akku aus dem RL herausnimmst. Schiebe den Verbindungsstecker mit einem kleinen Werkzeug langsam und Stück für Stück aus der Buchse, bis du ihn mit den Fingern ganz herausziehen kannst. Some people have reported success using small, curved needle-nose pliers such as hemostats. Others have used small flathead screwdrivers as shown in [this video](https://youtu.be/s2qNPLpfwww).

[![img/rileylink_battery_removal.png](img/rileylink_battery_removal.png)](https://youtu.be/s2qNPLpfwww)

## Waiting for RileyLink

Yes, waiting for RL to arrive is extremely difficult if they are backorder.  PLEASE be patient, since Loop CANNOT work without RL.

If you're really dying to do something while RL ships, you can proceed with finishing these build directions all the way through Step 14...but after that you'll have to wait for the RileyLink.  You can't properly enter any settings or pump info in Loop app without the RileyLink.

## Next Step: Enroll in Apple Developer Program

Now you are ready to move onto Step 6 to [enroll in the Apple Developer Program](step6.md).
