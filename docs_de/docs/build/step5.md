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

Dein RileyLink wird in Einzelteilen geliefert, also Akku getrennt, das kleine Mainboard und das Gehäuse. Du wirst den Akku verbinden und alles in das Gehäuse stecken.

Pass auf, dass die Steckverbindung vom Lipo-Akku gut eingerastet ist. Richte die kleine Nut richtig aus und drücke den Stecker ziemlich fest in die Buchse, um eine sichere Verbindung zu bekommen.  Eine schlechte Akkuverbindung kann dazu führen, dass die Loop-Kommunikation fehlschlägt.  Siehe die Beispielfotos unten an.

!!!info "Typische Benutzerfehler"

    Die häufigsten zwei Fehler neuer RL-Besitzer sind (1) nicht vollständig den Lipo-Akkustecker in die Buchse zu schieben und (2) den RL nicht aufzuladen. Vergleichen dein Lipo-Akku-Kabel mit den Fotos; es braucht ein bisschen Kraft, um den Stecker, wie auf dem Foto unten, vollständig in die Buchse zu schieben. Denke daran, deinen RL jede Nacht aufzuladen.

![../img/rileylink_battery_removal.png](img/battery-cables.jpg)

<figcaption>Lockere Steckverbindung links, richtige Steckverbindung rechts</figcaption>

Schlußendlich passt das kleine Mainboard und der Akku auch nur gerade eben in das kleine Gehäuse.  Klicke auf das Bild unten, um ein hilfreiches [Montagevideo](https://www.youtube.com/watch?v=-GHxxEJMCZc&feature=youtu.be)zu sehen.

[![img/slimcase.png](img/slimcase.png)](https://www.youtube.com/watch?v=-GHxxEJMCZc&feature=youtu.be)

## Zusätzliche Informationen über RileyLink

### Funkkommunikation

The RL communicates with the pump through radio frequency communications.  Numerous factors can influence how well those communications can function...interferences from other devices, temperature, physical blocking, etc.

When your RL and pump are first paired, Loop performs a series of tests that you won't see...they are tuning tests. Basically, RL sends little test messages to the pump and waits for a response. The RL tries this same "ping" to the pump a range of various radio frequencies. The range of radio frequencies it tries is based on the pump you've told RL to expect (Omnipod, Medtronic NA/CA, or Medtronic WW).  RL will then record the radio frequencies that provided the strongest response and use that frequency for future pump communications.

Usually this best frequency is pretty constant for any given pump+RL, but during temperature changes it may be that the best frequency is not the one currently set. In the event that RL has problems communicating with the pump, Loop has code built-in that will automatically tell the RL "Hey, try that tuning pump thing again...maybe there's a better frequency we need to try." This retuning is started automatically if pump communications fail for 14 minutes (in other words, two looping cycles).

### Bluetooth-Kommunikation

RL communicates with your iPhone and Loop app through Bluetooth (BT).

!!!info "Bluetooth Troubleshooting"

    If your iPhone has BT issues, your Loop will have failures.  There have been reports of BT audio devices (such as BT pairings in your car or home audio BT speakers) interfering with the Loop.  If you are finding Loop failures frequently happening at a particular location, you may try to troubleshoot if there are BT problems in the area.

Your BT signal strength can be seen in the Loop settings, under the RL menu, on the `Signal Strength` line. As you move closer and further away from your phone, you can watch that number dynamically change. This line is **not** displaying the signal strength of your pump communications discussed above.

![img/RL_bt.jpg](img/RL_bt.jpg)

### Signallämpchen

RL has several lights that you may notice from time to time. There is no 'power' light. If you suspect that your RL is not being powered, try turning it off and on using the small sliding switch. You should see lights in the middle of the board flash when you do this.  If they flash, that means the board has power.

* Red light: Charging light. The red light will remain on while RL is charging, and it will turn off when charging is complete. You may notice the red light turn on periodically even after charging is complete...it's just "topping off".

* Green light: Bluetooth connection light. The green light will remain on while you have a BT connection with your iPhone.  If that green light fails to stay on, you should troubleshoot your BT connections. Try restarting BT on your iPhone and/or turning the RL off/on by its power switch.

* Blue light: Pump communications.  If you have an older firmware on your RL, some of the blue lights will flash periodically as it communicates with the pump. It's just letting you know that it is busy talking and collecting info. You will also see increased blue flashes if you have "Enabled Diagnostic LEDs" for MDT users that have the RLs with updated firmware (shipping since late August 2018).

A solid blue light that consistently remains lit on the board could mean one of two things:

* A temporary issue that can be resolved by rebooting the RL physically (turning the switch off/on), or

* An electrical short or damage to the board.  Sweat and moisture are most likely culprits, so try to keep case free from those environments. Don't keep RL in sports bras or waistband next to skin, for example, while exercising.

If your blue light remains on despite trying a restart, it is time to pull out your backup RL.

### Aufladen

The battery that comes with RL is not likely charged completely when it is shipped, so feel free to charge it up.  You'll need a [mini-USB cable](https://www.amazon.com/AmazonBasics-USB-2-0-Cable--Male/dp/B00NH13S44) and [0.5A USB charging power supply](https://www.amazon.com/Cellet-Powered-Charger-iPhones-Smartphones-/dp/B00FE8WFCO) like your iPhone power supply.  RL takes about 2 hours to fully charge (the red light will turn off when fully charged, read note above about red light patterns) and should easily last at least a full day of constant Loop use.  Typically, it can go into the 30-hour range without any problems.  Most people charge their RL each night when they are sleeping.  You don't have to worry about leaving the RL plugged in "too long" for charging.  It will automatically stop charging the battery when it is fully charged.

Since the best practice is to charge your RL overnight while you sleep, and the battery lasts safely over 24 hours, there is no battery level indicator for the RL.  The RL's charge level is not viewable on Nightscout, nor within the Loop app.  If you forget to charge your RL overnight, you can recharge it with a portable USB battery in a pinch.  A [short mini-USB cable](https://www.adafruit.com/product/899) could be a good addition to a small gear bag.

### Funkreichweite

The range that your RL will function is **heavily** dependent on the environment that you are in. Most people wear the RL in a pocket or carry a belt holster during the day. The radio frequency communications will have a shorter range than the BT communications, therefore RL will do better closer to the pump rather than the iPhone if you are deciding on options for carrying gear.

Problematic environments will be places like technical conferences, sports arenas, and other places where wireless communications are heavy and plenty.

### Lipo-Batterie

Keep your RL and lipo battery protected from damage.  Lipo batteries are unsafe when damaged or punctured, so the case is an important part of safe Looping. If your battery is damaged in some way, please disconnect it immediately, and dispose of it (they should be recycled). You can order new batteries on the [GetRileyLink website](http://getrileylink.org/)

### Lipo-Batterie herausnehmen

To remove the lipo battery from the RL, please do so slowly and patiently. Work the battery connection side to side slowly to loosen it from the plug. Some people have reported success using small, curved needle-nose pliers such as hemostats. Others have used small flathead screwdrivers as shown in [this video](https://youtu.be/s2qNPLpfwww).

[![img/rileylink_battery_removal.png](img/rileylink_battery_removal.png)](https://youtu.be/s2qNPLpfwww)

## Waiting for RileyLink

Yes, waiting for RL to arrive is extremely difficult if they are backorder.  PLEASE be patient, since Loop CANNOT work without RL.

If you're really dying to do something while RL ships, you can proceed with finishing these build directions all the way through Step 14...but after that you'll have to wait for the RileyLink.  You can't properly enter any settings or pump info in Loop app without the RileyLink.

## Next Step: Enroll in Apple Developer Program

Now you are ready to move onto Step 6 to [enroll in the Apple Developer Program](step6.md).
