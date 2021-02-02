# Entwicklungs-Branch FAQs

Diese Seite richtet sich vor allem an diejenigen, die die Loop-App schon einmal zusammengebaut haben und jetzt eine Aktualisierung vornehmen wollen. Im Verlaufe der Aktualisierung wirst du dich gefragt haben, was es mit diesen Entwicklungszweigen/Branches auf sich hat. Was die Unterschiede zwischen den Branches sind und solche Dinge. Also, lass uns starten, diese Fragen so gut wir können zu beantworten.

## Was sind Entwicklungsversionen/-Branches?

Es wird eine Menge über Branches im Zusammenhang mit Loop erzählt, aber das Konzept dahinter ist einfach. Ich nehme eine Analogie zur Hilfe. Im Grunde genommen sind das alles unterschiedliche Versionen der Loop-App, so etwas wie unterschiedliche Ausgaben eines Buches.

Um die wirkliche Bedeutung von Branches zu verstehen, sollten wir vielleicht etwas mehr über den Quellcode der Loop-App sprechen und wie Softwareentwicklung funktioniert.  Du kannst dir [hier](https://www.youtube.com/watch?v=cWqvYs4Azt0&t=4s) ein Video über den Entwicklunsgprozess  ansehen.

Loop-Entwickler haben ein Konto bei GitHub. Dort gibt es ein Projekt, welches [LoopKit](https://github.com/LoopKit) genannt wird.  Within that account, the developers have several "repositories" that support Loop in particular. A repository is like a book...let's think of it like a cookbook for now. Innerhalb des LoopKit-Projektes gibt es verschiedene Ablagen, für die Loop-App selbst, die LoopDocs und einige andere unterstützende Dinge, die der Loop-App beim Zusammenbauen helfen, dass es richtig zusammen passt. For example, Loop's repo has a lot of the info about the app itself; the outward facing things that you interact with. How information is put to you and taken in from you...that's in Loop repository code. But, there's more than just a user interface for Loop. Loop has to do a lot of complex work like Bluetooth communications, algorithm math, pump communications, etc. The Loop app has help from frameworks to do those other parts. The Loop app has help from frameworks to do those other parts. CGMBLEkit for some of the transmitter parts of Loop, RileyLink_ios for the pump managers (talking to the pumps and decoding their information), LoopKit for the algorithm about carbs and insulin curves, etc.

Wenn du Loop-App zusammenbaust, werden diese Hilfswerkzeuge (insgesamt sieben) im Hintergrund von "Carthage" heruntergeladen und hinzugefügt.  Carthage ist so etwas wie ein persönlicher Einkäufer. You give it a shopping list (the cartfile in Loop code is that shopping list) and it goes and fetches that for you during the build process. Manchmal hat dein Rechner aber eine veraltete Einkaufsliste und so etwas kann Fehler beim Zusammenbauen (Build errors) verursachen. Das ist dann der Grund für den sog. "Carthage Update Fix" in der Fehlerliste beim Zusammenbauen der App. Über dieses Kommando aktualisiert du die Einkaufsliste, um für den Zusammenbau die richtigen Versionen der Komponenten zu verwenden.

![../img/commit.png](img/loopkit.png)

Jedenfalls weisst du jetzt über den generellen Aufbau der Loop-App in Github Bescheid. Jetzt können wir etwas näher auf die Loop-App selbst eingehen.

Wir bleiben bei der Vorstellung, die Loop-App wäre ein Kochbuch. Die Entwickler sind die Autoren bzw. Köche der Rezepte (Quellcode) des Kochbuchs. Die Autoren verwenden zahlose Stunden darauf, neue Rezepte zu testen, auszuprobieren und die Dokumentation dazu zu verbessern. Sie übergeben die Entwürfe dem Lektor, der Änderungsvorschläge macht. Es gibt Gramatik-Streitpunkte, kleine Schreibfehler, die Fotos sehen toll aus und die Rezepte sind lecker. Sie veröffentlichen das Buch und du siehst ein großartiges fertiges Produkt im Bücherregal. Das wird ein "Release" genannt und das repräsentiert dann den sog. Master-Branch. Diese Version ist sehr gut getestet und äußerst stabil bei der Anwendung. Jedesmal, wenn du mit diesen Rezepten kochst, weisst du von vorneherein genau was herauskommt und viele Leute vor dir konnten sich davon überzeugen, dass das alles sehr gut schmeckt. Der Master-Branch ist stabil und hinreichend getestet.

Aber dann gehen die Köche/Entwickler auf eine Reise. Sie werden inspiriert von einer neuen Küche und wollen neue Rezepte zum alten Kochbuch hinzufügen (Dinge, wie Unterstützung von Omnipod-Pumpen und Anpassungen sind beispielsweise "neue" Rezepte, die seit dem letzten Release entwickelt wurden). (Things like omnipod support and overrides are new "recipes" that were developed since the last master release, for example.) But, the process for developing a recipe is arduous. Aber der gesamte Prozess des Entwickelns ist sehr anstrengend. Lots of trial and error involved. Haufenweise Korrekturen von Zutaten (Quellcode). Die Lektoren probieren die neuen Rezepte aus und geben Rückmeldung (siehe [Themenliste in GitHub](https://github.com/LoopKit/Loop/issues)). While the recipes are being developed, they have a version of the old cookbook that gets marked up...edited in pencil a lot. Randnotizen und Gekritzel an den Seiten. Überarbeitungen müssen sehr häufig gemacht werden, denn darum geht es beim Testen von Rezepten. Diese Vorab-Versionen von Rezepten werden Entwicklungs-Branch (Dev-Branch) genannt. Short for "development" branch. Wie der Name schon sagt, ist das genau das, womit sich die Entwickler beschäftigen, treffen und neue Rezepte ausprobieren.

Nach all dem Testen und Anpassen treffen die neuen Rezepte vielleicht die Geschmäcker gut   (die Fehler im Sourcecode sind herausgequetscht). Genügend Leute haben Feedback gegeben und die Ergebnisse sorgfältig untersucht. Diese neue Version des Buches geht dann zum Verlag und wird zum nächsten Termin veröffentlicht. Das Kochbuch wird mit einer neuen Versionsnummer veröffentlicht und die neuen Rezept werden hervorgehoben. Wenn dies mit der Loop-App passiert, wird der Master-Branch um die neuen Features, die von den Entwicklern kommen, erweitert ("Der Entwicklungs-Branch wird in den Master-Branch gemergt"). Der Master-Branch bekommt dann eine neue Release-Nummer (du findest [hier](https://github.com/LoopKit/Loop/releases) die Versionshistorie). They stay the same until the Loop developers start working on the next batch of improvements, could be the next hour even or days later, but the process begins again. Die Entwickler werden wieder den Code ändern und die Änderungen im Entwicklungs-Branch löschen, damit die Entwicklung weiter gehen kann.

## Was ist mit dem Omnipod-Test-Branch passiert?

Das Testen der Omnipod Erweiterung für die Loop-App (wir sprechen hier nicht über die aktuellen Anpassungen, die dieser Arbeit vorrausgegangen sind) wurde vor der Bekanntgabe des Releases vor Monaten von einer kleineren Gruppe privater Leute erledigt, bevor der Omnipod-Test-Branch erstellt wurde. Diese kleinere Gruppe von Leuten (ein paar Dutzend) haben aktiv auf ihre Omnipod-Loop-App geachtet und haben Fehler gesammelt und mitgeteilt. Es war eine Menge Arbeit, die die Tester und Pete Schwamb (Loop-App Entwickler) geleistet haben, um den Code stabil und nachvollziehbar zu machen.

Als der Code stabil, sauber und bereit für ein  größeres Publikum war, wurde der Omnipod-Test-Branch öffentlich verfügbar gemacht. Dieser Branch war wirklich gut getestet bevor er der Öffentlichkeit zur Verfügung gestellt wurde, aber noch nicht von Anfang an für jeden perfekt. Es wurde erwartet, dass ein paar Anpassungen auf der Benutzeroberfläche gemacht werden, bevor man ein noch größeres Publikum ansprechen konnte.

Also, omnipod-testing branch was not going to undergo a lot of active revisions to it when it was released. Die Absicht dahinter war, dies als ein wohlbekanntes Produkt zu sehen, dessen Code sich nicht ständig geändert. Daher war es einfacher, den bekannten Code zu korrigieren, wenn Leute einen Fehler berichtet haben.

Der Omnipod-Test-Branch diente als Vorschlag für eine initiale Platform, um Pod-Loooping zu testen. Es wurde offiziell eingestellt und wird nicht weiter benötigt. Die Unterstützung für Omnipod wurde jetzt in den normalen Master- und Entwicklungs-Branch eingearbeitet.  Vielen Dank lieber Omnipod-Branch, du hast uns gut gedient. Einen glücklichen Ruhestand!

## Loop-App 2.0

Am 31. Dezember 2019 wurde die Loop-App Version 2.0 veröffentlicht (genauer gesagt "Der Master-Branch wurde aktualisiert"). Das heisst, dass unser Kochbuch aus dem Entwicklerzweig (Dev-Branch) in den Hauptzweig (Master-Branch) überführt wurde. Am 31.12.2019 waren der Master- und der Entwicklungs-Branch identisch.

Allerdings von diesem Zeitpunkt an, wird am Entwicklungszweig an den neuen Rezepten gearbeitet. Der Entwicklungszweig und der Master-Branch werden auseinander driften mit ungetesteten Änderungen und Weiterentwicklungen im Programmcode. Der Dev-Branch kann anfangs ein paar Fehler und Unzulänglichkeiten aufweisen, was das Ergebnis kommender und gehenden Code-Änderungen ist, die aber ohne größere Ankündigungen oder Diskussionen vonstatten gehen werden.

So, most all users should now start building with master branch again...you will be getting the latest Loop release everytime you build with Loop master branch. Der Zweig bleibt im gleich stabilen Zustand, wie er schon seit einiger Zeit ist. Only use dev branch if you are interested in actively testing new code and have the ability to track/document bugs.

## Was gibt es neues in der Loop-App 2.0?

Diese häufige Frage kommt in mehreren Varianten...

Was ist neu in der Loop-App 2.0? Wo ist der Unterschied zwischen der Loop-App 2.0 und dem Entwicklungs-Branch? Soll ich aktualisieren, wenn ich momentan den Entwicklungszweig verwende?

Zu der Frage über die Unterschiede zwischen der vorhandenen Loop-Version und dem Release kann ich nur antworten, dass ich das nur dann könnte, wenn ich wüsste, auf welcher Version/Branch du momentan bist (UND zu welchem Datum du die gebaut hast, falls du den Entwiklungszweig verwendest). Der Entwicklungszweig ändert sich sehr häufig. Die Version, die jemand im Oktober 2019 benutzt, ist notwendigerweise eine andere, als die, die jemand im November 2019 zum Bauen benutzt.

Ich zeige hier erst einmal einen Rückblick im Vergleich zum letzten Release. Du kannst es dann durchlesen und schauen, ob für dich etwas neues dabei ist, im Vergleich zu der Version, mit der du deine Loop-App gebaut hast. Ich liste sie in fast umgekehrter Reihenfolge auf, wie sie in den Entwicklungszweig eingebaut wurden. Also je höher der Punkt in der Liste steht, desto größer ist die Wahrscheinlichkeit, dass du die Sache noch nie gesehen hast.

### Hochlagen von Glukosewerten nach Nightscout

Die Loop-App 2.0 bietet die Möglichkeit, deine Glukosewerte direkt zu Nightscout hochzuladen. Es gibt einen neuen Schieber für Dexcom Benutzer unterhalb des CGM Einstellungsbereichs. Nachdem du deine CGM Transmitter-ID eingetragen hast, kommst du zurück zur CGM Info. Da siehst du dann den Schieber mit der Beschriftung "Werte hochladen".  Technically, Loop's dev branch had that feature for a hot minute before Loop v2.0 was released...but for almost everyone this will be a brand new feature they haven't had before. Dieses Feature ist nützlich, wenn der Dexcom Share Server wieder mal einen langen Ausfall hat, wie das letzthin der Fall war. Sollte das wieder passieren, kannst du den "Werte hochladen"-Schieber anschalten und deine Glukosewerte sollten dann in Nightscout sein, selbst wenn der Nightscout Share Server nicht ordentlich funktioniert. Good practice would be to temporarily disable your Share bridge in Nightscout while Loop is responsible for CGM uploading so that you don't get duplicate data. Du kannst die "Werte teilen".Funktion in Nightscout ausschalten, indem du dich bei deinem Heroku Konto anmeldest, auf den "Settings"-Reiter wechselst, auf "reveal config vars" klickst und dann das Wort "bridge" aus der "ENABLE" Zeile löschst.

### Eine Lösung für verlorene Einstellungen

IoS 13 brachte uns einen eigenartigen kleinen Fehler, bei dem plötzlich deine Einstellungen von Loop-App weg waren. Allerdings war das nicht auf die Loop-App beschränkt. Manchmal haben auch Dexcom Anwender ihre Einstellungen verloren. Das Problem trat meistens dann auf, wenn das Telefon gerade am Laden war. Allerdings trat es auch zu anderen Zeitpunkten auf. Es gibt in der Loop-App dafür eine Lösung. Grund genug also, um auf die neue Version zu aktualisieren. Solltest du diesen Fehler bereits vor der Aktualisierung auf die neue Version gehabt haben, gibt es auch dafür eine Lösung: Starte einfach die Loop-App neu und deine Einstellungen sollten wieder erscheinen.

### iWatch-Schieber für Bolus

Um einen unabsichtlichen Bolus zu verhindern, solltest du nicht deine Kinder mit der iWatch spielen lassen. Nur Spass, wir haben eine bessere Option hinzugefügt. Es gibt einen neuen Schieber, um den Bolus zu bestätigen, nachdem du den Bolus-Knopf gedrückt hast. Es wird dir dann so etwas wie auf der unteren Grafik angezeigt. Sobald du an der Digital Crown drehst, gehen die zwei Dreiecke inneinander über. Wenn sie dann übereinstimmen, wird der Bolus durch einen kleinen haptischen Hinweis bestätigt und ein weißer Haken erscheint auf der iWatch Anzeige.

![../img/loopdashboard.png](img/spin-to-confirm.png)

### iWatch vorgeschlagene Bolusmenge

Eine häufig vorgenommene Sourcecode-Anpassung wird nun auch nicht mehr benötigt. Viele Leute haben den Sourcecode so verändert, dass die iWatch automatisch 100% der vorgeschlagenen Bolusmenge in das Feld einträgt. Die bisherige Menge war 75%. Die Loop-App trägt nun 100% des vorgeschlagenen Boluses ein, es braucht dafür keine Sourcecode-Anpassungen mehr. Loop now offers the 100% auto-filled recommendation, no code customization needed now.

### Liste mit den letzten Kohlenhydrateinträgen auf der iWatch

Du kannst jetzt die Liste der letzten Kohlenhydrateinträge auf deiner Apple iWatch ansehen. Wische einfach nach links, um zum Blutzuckerverlauf zu kommen. Blättere dann nach unten mit der Digital Crown bis auf den Punkt "Aktive KH" unterhalb der BZ-Verlaufsanzeige und wähle diesen aus. Dann wird dir die Liste der letzten KH-Einträge angezeigt.

### Fehlerbehebung für die Medtronic x15 Nachricht: "Bolus könnte fehlgeschlagen sein"

Viele der Medtronic x15 Anwender bekamen nach jeder Bolusabgabe die Fehlermeldung "Bolus könnte fehlgeschlagen sein". Diese Angelegenheit wurde erledigt und die gepatchte Version der Loop-App wurd nun nicht mehr benötigt. Alles gut!

### Erweiterung der Benachrichtigungspieps

Confirmation beeps have been expanded based on user feedback...we heard parents and school nurses really appreciate hearing a beep for not just boluses, but also for suspend/resume commands and editing basal schedule (so you are sure it saved properly). Also gibt es jetzt Bestätigungspieps bei Bolusabgabe, Anhalten-/Weitermachenkommandos und beim Speichern von Basalratenänderungen.

### Pod-Statuslesen hinzugefügt

Es gibt ein neues Kommando im RileyLink-Menü, um den Pod-Status auszulesen. Das funktioniert analog zum bereits existierenden Kommando für Medtronic Benutzer. You can query your Pod for its current status info using that command.

### Allgemeine Fehlerkorrekturen

Es gibt auch noch eine Menge kleiner niedlicher Fehlerkorrekturen, die in den letzten Wochen umgesetzt wurden. Der Zeitstempel für die temporäre Basalrate bei Medtronic Loops (und auch bei älteren Omnipod Loops) hatte einen Fehler. Wenn die Loop-App wieder zur normalen Basalrate zurückgekehrt ist, sprang die Anzeige der Uhrzeit für die Basalrate im oberen Teil des Displays zurück auf die Uhrzeit, zu der die Loop gestartet wurde und nicht auf die Uhrzeit, zu der die Basalrate gestartet wurde. Es gabe auch noch ein paar Verbeseerungen im Umgang mit bestimmten Bolusen bei Pods. Zusätzlich wurde noch die Anzeige der Markierung für Anhaltenkommandos des Benutzers verbessert, während eine aktive temporäre Basalrate läuft.

### Verbesserungen der Bedienoberfläche

Es wird im oberen Bedienbereich einen gestrichelte Linie anstatt des CGM-Werts angezeigt, falls die Werte älter als 15 MInuten sind. Nur dass du nicht zufällig übersiehst, dass die Kommunikation mit deinem CGM nicht funktioniert. Wenn du versehentlich den führenden Schrägstrich an der URL von Nightscout dran lässt, wird die Loop-App es ignorieren.  The bolus progress row is new to master branch now, although many of you have been accustomed to that visual in dev branch for awhile now. The "Scenarios" screen that would sometimes appear when a phone was shaken is also disabled by default now. The Issue Report has more information about your Loop app's build date and version so that you can more easily track its build history.

### Häufige Build-Fehler wurden aus der Welt geschaffen

One common build error was caused if there was a space in the Loop folder name after downloading. Auch das wurde gefixt und du wirst als nie mehr einen Build-Fehler bekommen, wenn du ein Leerzeichen im Verzeichnisnamen deines Loop-Verzeichnisses hast.  Ahhhhh! Ahh, ich liebe es!

### Nightscout Profil hochladen

Die Loop-App überträgt deine Basalraten, ISFs, KH-Faktoren und Anpassungseinstellungen auf dein Nightscout Profil. Solltest du jemals dein iPhone verlieren und die Loop-App vollständig neu erstellen müssen, findest du jetzt mit Leichtigkeit deine Einstellungen in Nightscout.

### Neue Sprachen

Japanisch, Dänisch, Swedisch, Vietnamesisch, Finnisch, Portugisisch (Brasilien), Polnisch und Rumänisch wurden den regionalen Übersetzungen hinzugefügt. There are definitely some missing strings that will still need touchups...we will get those fixed up in Loop v2.1 if you all [help report those when you see them](https://www.facebook.com/groups/TheLoopedGroup/permalink/2454410898108895/). Danke!

### Nicht-Lineares-Kohlenhydrat-Modell

Da alle Branche (Master und Entwicklung) jetzt ein nicht-lineares Kohlenhydratmodell nutzen, erst einmal ein paar Informationen dazu:

Bisher hatte das Kohlenhydratabsorbtionsmodell eine lineare Absorbtion verwendet mit dynamischen KH Anpassungen. Das bedeutet, dass wir am Anfang der Absorbtion einen etwas erhöhten BZ-Wert sehen, als das lineare Modell vorhersagt. Bisher wurde der Einfluss auf den BZ aber als linear angesehen. Du kannst diesen Effekt im [Insulin Gegenmaßnahmen und Effekt Diagramm](../operation/features/ice.md) sehen, wenn du Kohlenhydrate eingibst. Aber wenn man eine große Anzahl an Datensätzen analysiert, unterstützt durch persönliche, anekdotenhaften Erfahrungen, hat Essen mehr eine nicht-lineare Absorbtionsrate. What this means is that food absorption was modeled as a flat, even effect (like the straight grey graph that you'll see in the [Insulin Counteraction Effects chart](../operation/features/ice.md) after you added a carb entry.

Welche Auswirkungen hatte diese Differenz zwischen der Vorhersage durch das lineare Modell und der eigentlichen Wirkung des Essens?

1. Bolusabgabe: Du hast wahrscheinlich eine etwas niedrigere Insulinabgabe zu Anfang beobachtet, als die, die du erwartet hättest. Das kommt daher, dass vom linearen (und langsameren) Modell vorhergesagt wurde, dass kurz nach der Verabreichung zuviel Insulin zur Reduktion der Kohlenhydrate vorhanden wäre.
2. Früh auftretende Reduktion der temporären Basalrate: Du hast wahrscheinlich einen Hang zur frühen Reduktion auf eine Null- oder sehr niedrige temporäre Basalrate durch die Loop-App innerhalb der ersten 30-60 Minuten nach einem Essensbolus beobachtet, wenn du keine signifikante BZ-Spitze direkt nach dem Eintragen der Kohlenhydrate hattest. Dies wird wahrscheinlich noch offensichtlicher bei denen unter euch gewesen sein, die regelmäßig eine kurze Zeit bis zum Essen nach dem Bolus warten.

Mit einem nicht-linearen Absorbtionsmodell stimmt die Absorbtion der Kohlenhydrate besser mit den Vorhersagen für ein Essen überein. Und wenn die Vorhersage der Absorbtionsrate besser mit den aktuellen Erfahrungen übereinstimmt, wird es die vorhergesagte BZ-Kurve leichter haben, von Anfang an einen höheren Bolus zu verabreichen, der die häufige konservative Reduzierung der temporären Basalraten nach dem Essen verhindert.

**Was kannst du erwarten?** Wie aus der oberen Erläuterung hervorgeht, wirst du wahrscheinlich mehr komplette ausgeführte Bolusempfehlungen beobachten und weniger Reduzierungen der temporären Basalraten nach einem Bolus. Im Hinblick darauf, dass du vielleicht bereits vorher schon Anpassungen an deinen Gewohnheiten und Einstellungen gemacht hast, die ein solches Verhalten verhindern, solltest du diese wieder zurück nehmen. Wwenn du beispielsweise die KH-Absorbtionszeit verkürzt hast, um größere anfängliche Bolusmengen zu ermöglichen, solltest du diese wieder auf ihre normale Zeit zurückdrehen. Behalte das im Auge und passe das Notwendige dann an.

**Was ist, wenn du zum alten Modell zurück möchtest?** Du muss dann eine [Zeile](https://github.com/LoopKit/LoopKit/blob/dev/LoopKit/CarbKit/CarbStore.swift#L207) im LoopKit Sourcecode so anpassen, dass dort `.linear` steht und somit das alte Kohlenhydratmodell verwendet wird. Wenn du näheres über das neue Modell wissen willst, solltest du im [Zulipchat Kanal hier](https://loop.zulipchat.com/#narrow/stream/144111-general/topic/Possible.20Carb.20Model.20Changes) nachlesen. Beachte bitte, dass die Änderungen am Sourcecode für die Modellanpassung am besten durch die Nutzung von [LoopWorkspace](../build/loopworkspace.md) gemacht wird, da diese Änderung einen Framework betrifft, der von Loop verwendet wird (also nicht der Sourcecode der Loop-App selbst).

### Zeitliche Anpassungen (Overrides)

Loop v2.0 marks the first time Loop master branch has overrides included. Additionally, this release moves overrides setup from the configurations area of Loop settings to the workout icon in the Loop toolbar. Es gab im Entwicklungsbranch auch noch Fehler, die die Overrides in der Vergangenheit zum Schweigen gebracht haben. Eine Aktualisierung ist also eine sehr gute Idee, selbst wenn du in deiner aktuellen Version bereits Overrides benutzt hast. Want to learn more about overrides? Solltest du mehr über Overrides wissen wollen, kannst du [hier](../operation/features/workout.md) nachlesen.

### Rückblickende Anpassungen können immer gemacht werden

Die rückblickende Anpassung war immer ein optionaler Schalter im verwendeten Algorithmus. It is now on by default all the time. Dies ist ein sehr wichtiger Aspekt des Algorithmus, da es der Loop-App hilft, indem es den ständigen Vergleich zwischen wirklichem und vorhergesagtem Verlauf bietet.

### Support für Omnipod

Die meisten von euch werden bereits Omnipod in ihrer Loop-App verwenden, aber dies ist das erste Mal, das der Loop-Master-Branch Omnipod unterstützt. Aktualisiere bitte deine Loop-App, wenn du bisher den Omnipod-Test-Branch verwendet hast. Es wird Zeit, dass du alle Fehlerkorrekturen bekommst, die wir in der Loop-App erledigt haben.

### Unterstützung des Dark Mode

iOS 13 brachte den Anwendungsentwicklern den Dark Mode und die Entwickler der Loop-App waren erfüllt davon. Wir haben jetzt einen abgefahrenen, coolen Dark Mode für die unter euch, die den Dark Mode bevorzugen.

### ISF und Leitplanken für den Korrekturbereich und Oberflächenanpassungen

Loop 2.0 verwendet auch erstmalig im Master-Branch die nützlichen Scroll-Rädchen, um die Werte für ISF und den Korrekturbereich anzupassen. Das vereinfach auch die Korrektur eines Fehlers, der die Loop-App abstürtzen ließ, wenn man rückwirkend die Werte des Korrekturbereiches anpasste. Wieder weniger Dicke-Finger-Gefahr bei der Eingabe.

### Pumpen- und CGM-Simulator

Solltest du die passende Ausrüstung für deine Loop noch nicht haben und die Loop-App nur mal testen wollen, kannst du jetzt als Extra eine simulierte Pumpe oder CGM verwenden.

### Unterstützung für die neuen Transmitter von Dexcom

Dexcom hat eine neue Art von Transmittern herausgebracht. Diese Transmitter haben den Loop-Entwicklern einiges abverlangt (Pete! YEAH!) to get them working in offline Looping, but the fix was pushed into all branches shortly thereafter in August 2019. Falls du deine Loop-App seit August 2019 noch nicht aktualisiert hast und du einen Dexcom G6 benutzt, solltest du jetzt aktualsieren.

## Wie kann ich bei den Branches auf dem aktuellen Stand bleiben?

Wie bereits gesagt, ändert sich der Master-Branch nur wenig. Du musst ihn also nicht ständig beobachten.

Aber der Entwicklungs-Branch ist ständig am Umziehen und verändert werden. Wenn du einen Entwicklungs-Branch verwenden willst, musst du dir darüber im Klaren sein, dass Entwickler ständig umstrukturieren, schütteln, anpassen und den Sourcecode häufig und ohne Vorankündigung im herkömmlichen Sinn über die Looped Gruppe oder Instagramm, aber so, dass es die anderen Entwickler mitbekommen, verändern. Es hilft den Entwicklern nicht, wenn Leute sich in den Entwicklungs-Branches herumtreiben und diesen fälschlicherweise für einen stabilen Master-Branch halten, mit jeder Menge Informationen und Dokumentationen. Ein Entwicklungsbranch sollte nur dazu verwendet werden, jemanden bezüglich der Erwartungen an sich selbst und den Umgang mit Informationen und Aktualisierungen von Entwicklern, zu schulen. Leute, die einen Entwicklungszweig benutzen, sollten auch ständigen Zugang zu einem Apple Computer haben, um die Loop-App schnell neu erstellen zu können, sobald ein neuer Fehler oder dessen Korrektur identifiziert ist.

Wenn du einen Entwicklungszweig benutzt, kannst du in einer Vielzahl von Fällen den Entwicklern im Weg herumstehen, das wird aber alles auch deine Arbeit kosten und dich nötigen, dich ständig auf dem Laufenden zu halten. In solchen Situationen solltest du keine tollen, ständig aktualisierten LoopDocs erwarten, die die neuesten Enticklungsneuerungen beinhalten, so funktioniert eine Entwicklungs-Branch nicht!

### Beobachte das Loop Repository und die Themenliste

Erstens solltest du dich bei der Loop-App Reopsitory Themenliste einschreiben ([Loop repo](https://github.com/LoopKit/Loop)). You can choose to watch the repo so that you get emails when new Issues are reported. This is a good way to find out if there's other people reporting odd behavior that you are wondering about. Wenn du einen Entwicklungszweig benutzt und etwas in der Loop-App siehst, dass dir komisch vorkommt, solltest du zuerst die [Themenliste](https://github.com/LoopKit/Loop/issues) anschauen, um zu sehen, ob andere das gleiche beobachten. If so, you can help by capturing information and reporting it. Es ist nicht sonderlich hilfreich, mit einem "habe ich auch" zu antworten. Besser ist es, wenn du Screenshots, Problemberichte aus den Loop-Einstellungen und eine sorgfältige Beschreibung des Problems, welches du entdeckt hast, bereitstellst. Sei Teil der Lösung, indem du gründliche und genaue Informationen bietest, die eine Nachstellen des Problems ermöglichen.

![img/watching.png](img/watching.png)

### Melde dich beim Zulipchat Kanal an

Zweitens, benutze das [Zulipchat](https://loop.zulipchat.com) Forum für Loop. Dieses Forum hat mehrere Unterhaltungs-Streams, abhängig vom Thema. Ich kann dir nur sehr ans Herz legen, dem #github Kanal zu folgen, wenn du Änderungen am Code verfolgen möchtest. Sourcecode-Änderungen werden durch ein Github Commit erledigt. Der #github Kanal hat eine automatische Benachrichtigungsfunktion, sobald ein neuer Commt gemacht wird und wird dir eine kleine und kurze Beschreibung des Commits liefern.

![img/zulipchat.png](img/zulipchat.png)

Du kannst auch direkt zur Commit-Historie jedes Branches gehen, wenn du das willst.

[Loop Entwicklungs-Branch Commit-Historie](https://github.com/LoopKit/Loop/commits/master)

[Loop Master-Branch Commit-Historie](https://github.com/LoopKit/Loop/commits/dev)

Wenn du auf den Commit klickst, kannst du genau sehen, welche Änderungen am Sourcecode gemacht wurden. Dies ist eine interessante Lernerfahrung. Der alte Code ist in rot und der neue Code in grün dargestellt. Als Hilfe hast du auch noch die Zeilennummern und Dateinamen des veränderten Codes.

![img/commit.png](img/commit.png)

Ich glaube nicht, dass viele von euch die genaue Bedeutung der Veränderungen kennen oder verstehen, wie sie genau funktionieren, aber ich komme noch einmal auf den Punkt mit der Commit-History zurück, aus dem du ablesen kannst, wie häufig der Entwicklungszweig verändert wird. Schau dir die Anzahl und Häufigkeit der Commits im Entwicklungs-Branch an. Aus diesem Grund gibt es keine Möglichkeit, eine Dokumentation der Änderungen zu pflegen. Es ist einfach ein zu bewegliches Ziel.

### Schau dir Loop-Gruppen an

Drittens, schau dir andere Loop-Gruppen an. Major concerns/issues are brought up there...so no harm in scrolling through and seeing what's going on there.

### LoopDashboard.org

Außerdem kannst du dir auch das <a href="https://www.loopdashboard.org/">Loop-Dashboard</a> anschauen, wo alle github-Aktivitäten der sieben verschiedenen Repositories der Entwicklungs- und Maaster-Branches zusammengefasst sind. Hier kannst du immer die neusten Informationen und die Historie der Loop-App sehen.

Auf der ersten Seite des Loop-Dashboards kannst du alle Aktivitäten in einer Liste sehen. Du kannst aber auch zu anderen Seiten wechseln und mehr Deatils über Commits, Themen und Pull Requests erfahren. Es gibt auch noch Statistiken darüber, wer welchen Pull Request bearbeitet und wer was comittet. Das Dashboard wird alle zwölf Stunden aktualisiert.

![img/loopdashboard.png](img/loopdashboard.png)

### Mach dich mit deinen Informationsquellen vertraut

Eine andere hilfreiche Sache ist, wenn du einen Entwicklungs-Branch verwendest, der häufig geändert wird, erfährst du sehr viel darüber, wie die Loop-App funktioniert und wo du zusätzliche Informationen über das herbekommst, was dir angezeigt wird. Wenn du z.B. einen IOB-Wert siehst, der dir komisch vorkommt, solltest du wissen, dass die Insulinverabreichungen in der Health-App gespeichert werden. Wenn du weisst, wie man einen Probleminformationsliste zieht, hilft dir sie herauszugeben, wenn du danach gefragt wirst. Zu wissen,  [wie man an die Debug-Logs kommt, wenn der Entwickler danach fragt](https://youtu.be/Ac4MguvUO7M), ist auch noch eine nützliche Fähigkeit.

## Was bringt die Zukunft?

Kurz gesagt für jetzt (31. Dezember 2020):

* Master-Branch: Wir wissen, dass wir die neuen Übersetzungen aufräumen müssen. Es wird eine Menge neuer Begriffe hinzukommen, die in eine Menge neuer Sprachen übersetzt werden müssen. Der Master- und der Entwicklungs-Branch werden mit den Neuerungen bezüglich der Übersetzungen aktualisiert. Sobald diese Änderungen getan sind, gibt es eine Version 2.1.

* Entwicklungs-Branch: Die zukünftigen Weiterentwicklungen des Entwicklungs-Branches können am besten durch Beobachten und Begutachten der [Pull Requests in GitHub](https://github.com/loopkit/loop/pulls) getan werden. Das ist die Stelle, an der initiale Code-Änderungen vorgeschlagen und diskutiert werden.
