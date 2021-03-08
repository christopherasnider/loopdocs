# Aktualisierung/Neubau der Loop-App FAQs

SOOOO many questions about updating or rebuilding Loop. The general answer is that people tend to overthink this. Die Aktualisierung deiner Loop App ist im Grunde genommen sehr einfach. Also das Durchlesen dieser Seite sollte die meisten Fragen beantworten.

Zuerst solltest du dir die Zeit nehmen und die Bedeutung der Begriffe vestehen.

"Aktualisieren der Loop-App" ist der Prozess des Herunterladens des Quellcodes und Aktualisierens der Loop-App. Dies ist notwendig, wenn du auf eine andere Version wechseln möchtest. Dies ist auch notwendig, wenn du neue Features oder Fehlerkorrekturen aus dem bereits von dir verwendeten Versionszweig verwenden möchtest. Bei diesem Prozess ist es egal, ob du vom Versionszweig "omnipod-testing" auf "dev" oder "jojo" nach "dev" oder "master" nach "dev oder irgend eine andere Kombination wechselst.

Die Loop-App zu aktualisieren ist im Grunde das gleiche, wie wenn du eine andere App auf deinem iPhone über den App Store aktualisierst. Eine neue Version der Loop App erscheint auf deinem iPhone und ersetzt die alte Version.

## Womit soll ich anfangen, wenn ich meine Loop App aktualisieren möchte?

**Beginne IMMER mit der [Update Loop Seite](../build/updating.md) bevor die irgendwelche Builds startest.** Diese Seite ist sehr wichtig, da sie dir Informationen über die Aktualisierungen liefert, bevor du die App zusammenbaust und sie dir die neuesten Hinweise gibt, die du bei diesem Vorgaang beachten solltest.

Erstelle die App nicht einfach mit der schon Monate alten, bereits heruntergeladen Version. Es ist sehr wahrscheinlich, dass die alte Version nicht mehr aktuell ist. Nimm die neueste Version, die bereits die neuesten und besten Features und Fehlerkorrekturen enthält.

## Wann soll ich aktualisieren oder neu erstellen?

Das absolute Minimum ist: Ein Jahr nach deinem letzten Build (nur beim bezahlten Apple Account, beim unbezahlten Account sieben Tage).

Gut gemeintes Minimum: Wenn du einen Entwicklungszweig (Dev-Branch) verwendest, möglichst oft. Ich habe wertvolle Updates im Entwicklungszweig mindestens einmal pro Woche gefunden. Aber monatlich sollte das Minimum sein. Der Hauptzweig (Master Branch) und der Omnipod-Testing-Zweig haben weniger häufig Aktualisierungen.

Fallspezifisches Minimum: Es kann auch der Fall auftreten, dass du aktualisieren solltest, weil es "Hot-Fixes" für deine Version gibt, die das ganze am Laufen halten sollen. Ein Beispiel war, dass bei den Dexcom Empfänger das Bluetooth-Protokoll geändert wurde. Der Quellcode für die Loop-App wurde so angepasst, dass sie mit dem neuen Protokoll auch im Offline-Fall umgehen kann. Solltest du in so einem Fall nicht aktualisieren, wärst du gezwungen, dass die Loop-App immer eine Internetverbindung hat, um die Loop zu schließen.

## Muss ich meine alte Version der Loop-App löschen?

No. No. No. No. No. No. Do not delete your old Loop. Das wäre eine wirklich keine gute Idee, da du dann die Verbindung zu deinem momentanen Pod und deine ganzen Einstellungen verlierst. Also lösche die alte Version nur in den folgenden beiden Situationen:

1. You broke it: There is a glitch in Loop where if you enter the target correction range backwards, then your Loop app will stop working. Correction range needs to be in minimum-maximum, for example 100-120 mg/dL. If you entered that as 120-100 mg/dL, Loop will not work during the time that backwards correction range is supposed to be active. In this case you would need to delete the app and rebuild.

2. Moving from dev branch back down to jojo branch. The way the new dev branch is coded will require you to delete your dev build prior to going back jojo branch.

## Erstellt eine Aktualisierung eine zweite Loop App?

Yes. So long as you use the same developer team as you originally built the app with before.

Die einzige Ausnahme ist, wenn du beim Erstellen ein anderes Team zum Signieren der App verwendest, als das, welches du bei der vorherigen Version verwendet hast. Die Identität der App wird mit Hilfe des Entwicklungsteams definiert, über das du die App signierst. Jedes Team hat eine eindeutige ID über die Eindeutigkeit deiner App bestimmt wird. Wenn du diese ID änderst, interpretiert dein iPhone auch diese ID als eine neue App, was in zwei Loop Apps auf deinem iPhone mündet. Deswegen, wenn du das Entwicklerkonto änderst, bekommst du eine zweite Loop App und du wirst einen neuen Pod starten müssen. Du musst deine Einstellungen dann von Hand in die neue App übertragen und die alte Version löschen.

## Werden meine Einstellungen bim Aktualisieren gesichert?

Yes. Ja, deswegen sollte die App nicht gelöscht werden. Deine Einstellungen werden gesichert.

## Funktioniert mein Pod noch, wenn ich aktualisiere?

Yes. Nein, solange du das gleiche Entwicklungsteam zum Signieren beim Erstellen der App benutzt, wie das, dass du bei der vorherigen Version verwendet hast.

## Wie kann ich nachschauen, welche Version ich installiert habe?

Die Loop App Version wird oben in der Einstellungsansicht angezeigt. Es geht noch besser: Die Entwicklungszweige haben eine sehr detaillierte Beschreibung über die Version von Loop, der beim Problemreport den oberen Teil der Nachricht einnimmt. Das ist wieder eine tolle Neuerung, beim Suchen nach dem was, wo, wie und wann in deiner Version.

![../img/loop-version.jpg](img/loop-version.jpg)

## Was passiert, wenn ich den Versionszweig wechsle? Spielt das eine Rolle?

Das spielt keine Rolle. Der Wechsel zwischen den Versionszweigen entspricht einer Aktualisierung der App. Es ändert sich nichts an den Einstellungen.

## Was ist, wenn ich mein iPhone wechsle?

Der iPhone-Wechsel unterscheidet sich etwas vom Aktualisieren der App. You will need to change pods in order to move to the new phone's Loop. And you will have to enter all your setting in again. Die Loop-App kann nicht wie andere Apps aus einem Backup wieder hergestellt werden. Du musst die Loop-App also neu erstellen.

## Wie lange dauert das?

Vorausgesetzt das alle Updates auf deinem Mac und Xcode erledigt sind, kann man von ca. 30 Minuten ausgehen.
