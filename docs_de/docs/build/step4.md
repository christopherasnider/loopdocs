# Schritt 4: Kompatible CGM

!!!Gefahr "Geschätzte Zeit"

    - 10 Minuten um diese Seite zu lesen

!!! Info "Zusammenfassung"

    - Du verwendest einen Dexcom G4, G5 oder G6 CGM System... damit kannst du Loop benutzen.
    - Du verwendest einen Medtronic-Sensor, der mit einer Loop-kompatiblen Medtronic Insulinpumpe arbeitet...damit kannst du Loop benutzen.
    - Du hast einen Eversense Sensor...dann kannst du Loop leider nicht benutzen.
    - Du verwendest einen Libre Sensor... dieser arbeitet nur mit einer modifizierten Loop App.

!!!warning "FAQs"

    - **"Was ist mit Libre Sensoren?"** Libre Sensoren sind nicht konzipiert, um als kontinuierliche Glukosemonitore zu dienen. Die Verwendung von Libre Sensoren zur kontinuierliche Glukoseüberwachung benötigt zwingend den Einsatz von Anwendungen Dritter (Xdrip oder Spike) und von Lesegeräten (BluCon oder Miao Miao). Bisher haben wir noch nicht genug Daten gesehen, die ausreichende Sicherheitsvorkehrungen von diesen Lesegeräten (und den zugehörigen Apps) demonstrieren, um diese in den Programmcode von Loop zu integrieren. Wenn du einen Libre-Sensor verwendest, musst du einen "nicht Hauptzweig" von Loop verwenden, den jemand (oder du selbst) geändert hat, um die Verwendung mit diesen Sensoren/Apps zu ermöglichen.
    - **"Was ist mit Eversense?"** Die Eversense App integriert sich weder in Apple Health, noch wurden die Kommunikationsprotokolle von Eversense rekonstruiert, daher ist Eversense derzeit nicht mit Loop kompatibel.

Ein kontinuierlich messender Glukosesensor (CGM, engl. für continuous glucose monitor) versorgt Loop mit aktuellen Blutzuckerwerten. Mit Hilfe diese Messwerte kann Loop den aktuellen Glukosetrend vorhersagen und, basierend auf den Kohlenhydrateinträgen und deinen Loop-Einstellungen, auch zukünftige Blutzuckerwerte vorhersagen. Im Folgenden werden die Typen von CGMs, die mit Loop kompatibel sind genannt. CGM-Messungen sind zwingend erforderlicher, damit du Loop benutzen kannst. Wenn deine Loop-App keine BG-Daten abrufen kann, kann Loop auch keinen Glukosetrend oder Blutglukosewerte vorhersagen und wird dann auf die programmierte Basalrate zurückfallen.

## Dexcom G5 und G6 CGM ![G5](img/g5.jpg)

Bei einem Dexcom G5 und G6 Sensor empfängt die Dexcom App auf deinem iPhone die CGM-Daten direkt über Bluetooth. Keines dieser Systeme erfordert die Verwendung des eigenständigen Empfängers (PDM), aber damit Loop funktioniert, musst du die Dexcom-App laufen haben.

## Dexcom G4 CGM mit Empfänger ![G4 With Receiver](img/g4_receiver.png)

Das Dexcom G4 PLATINUM System überträgt CGM Daten vom Sender an einen Dexcom G4 PLATINUM Empfänger. Der Empfänger wiederum kommuniziert mit der Dexcom Share2 App auf deinem iPhone per Bluetooth und die Share2-App übermittelt deine CGM Daten an den Dexcom-Server. Damit also Loop funktioniert, muss die Dexcom-App auf deinem iPhone laufen.

## Medtronic CGM ![Enlite](img/enlite.png)

Der mit der Medtronic 522/722, 523/723 und 554/754 Insulinpumpe erhältlich Minimed Enlite CGM sendet Blutzuckermessungen an die Insulinpump. Loop kann dann die Medtronic CGM-Daten per RileyLink direkt von der Insulinpumpe auslesen.

## Offline Nutzung

Offline Nutzung bedeutet, Loop zu verwenden, wenn keine Mobilfunkdaten oder Internet verfügbar sind. Damit Loop auch offline funktioniert, sind keine spezielle Einrichtungen notwendig. Wenn du also mal campen gehts, oder dich fernab der Zivilisation bewegst, musst du nichts Besonderes tun. Für die offline Nutzung von Loop muss Bluetooth am iPhone weiterhin aktiv sein und für Dexcom-Nutzer muss die Share2-, G5- oder G6-App ebenfalls noch geöffnet sein (müssen aber nicht aktiv mit dem Internet verbunden sein). Wenn du dein iPhone in den Flugmodus schaltest, vergiss nicht Bluetooth wieder zu aktivieren, damit dein Loop weiter funktioniert. Wenn die offline Nutzung nicht funtioniert ist ein haeufiger Fehler, dass du deine Transmitter-ID nicht in den Loop-Einstellungen aktualisiert hast, nachdem du den Transmitter gewechselt hast.

## Dexcom-Server

In seltenen Fällen kann die Loop die Bluetooth-Übertragungen der CGM Systeme nicht empfangen.  Wenn das passiert wird Loop die Daten automatisch von dem Dexcom Server abrufen, vorausgesetzt, du hast dein Dexcom-Benutzerkonto in den Loop Einstellungen eingegeben und Teilen erlaubt. Wenn Loop in diesem Modus arbeitet, wird neben dem Blutzuckerwert in der Loop-App eine kleine Wolke angezeigt. In diesem Modus zu arbeiten erfordert allerdings eine funktionierende Internet- oder Mobilfunkverbindung.

## CGMs die nicht von Loop unterstützt werden

Libre (mit BluCon oder Miao Miao), Eversense, Medtronic Guardian Sensoren, etc.  ja, es gibt noch einige andere CGM-Systeme. Loop unterstützt diese CGMs nicht  und wenn du einen dieser alternativen CGMs mit Loop verwenden möchtst... dann musst du dich mit deren Integrationen mit Hilfe von "Drittanbietern" befassen, damit Loop auf die Blutzuckerdaten zugreifen kann.  Diese Dokumentation deckt nicht die alternativen Methoden zur Integration von nicht unterstützten CGM Systemen oder Apps wie Spike ab.

## Nächster Schritt: Bestellung eines RileyLink

Jetzt kannst du mit Schritt 5 weitermachen, [Bestellung eines RileyLink](step5.md).
