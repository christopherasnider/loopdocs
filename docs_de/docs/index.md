# Willkommen bei Loop

<img src="img/phones.png" width="300" alt="iPhone Screenshot" />
<img src="img/watch.png" alt="Apple Watch Screenshots" />

## Einführung

[Loop](https://github.com/LoopKit/Loop) (englisch für "Schleife") ist eine Programmiervorlage, um eine App zu programmieren, die sich um die automatisierte Insulinzufuhr kümmert. Loop is ein kleiner Stein auf einem riesigen Felsblock, der von vielen anderen entwickelt wurde.

Die App verwendet als Grundlage [LoopKit](https://github.com/LoopKit/LoopKit). LoopKit besteht aus einem Satz von Modulen, die sich um die Belange von Datenspeicherung und -besorgung, Berechnungen und um die standardisierten View Controllers kümmert, die von Loop verwendet werden.

!!!warning "Achtung"

    Dieses Softwareprojekt ist:

    - höchst experimentell
    - nicht für therapeutische Zwecke zugelassen

      **You take full responsibility for building and running this system and do so at your own risk.**

Mit Hilfe der Open-Source Programmiervorlage für Loop kannst du eine App erstellen, die alle möglichen kommerziellen und frei verfügbaren Hard- und Softwaretechnologien verwendet, um deine Insulinpumpe, kontinuierliches Bluzuckermesssystem (CGM) und Algorithmen zur Berechnung von Insulinmengen zu einem System zu vereint, welches sich um die automatisierte Dosierung und Lieferung deines Basalinsulins kümmert.  Diese Loop-App errechnet den zukünftigen Blutzuckerverlauf auf Grundlage deiner zeitlichen Basalraten, Kohlenhydrataufnahme, Restinsulin (IOB) und aktuellen Bluzuckermesswerten.  Diese Bluzuckervorhersagen ermöglichen es der Loop-App temporäre Basalraten vorzuschlagen, um einen bestimmten zukünftigen Blutzuckerzielwert zu erreichen.  Das System kann entweder “open-loop” arbeiten in dem es dir lediglich Vorschläge macht, die auf deine Bestätigung hin auch angewendet werden oder es kann im “closed-loop” Modus arbeiten, in dem es die vorgeschlagenen temporären Basalraten automatisch selbst anwendet.

Du solltest dieses Projekt in einzelnen Etappen angehen. For example, first “open loop” to familiarize yourself with Loop’s operation. Also, investigate the code to ensure you understand what it is recommending and why. Then when you progress to “closed-loop”, do so safely by starting with appropriate safety limits and only progress to higher limits after several days of no lows. Frage dich immer wieder, warum die Loop-App dir welche Vorschläge macht.  It should be similar to the therapy decisions you would make yourself.  If the recommendations it makes are different than you would make, try to figure out why.

## Entwicklungsgeschichte

Loop wurde als open-source und geteiltes Projekt entwickelt.  Ein sehr interessanter Artikel über die Entwicklungsgeschichte von Loop wurde vom Loop-Entwickler Nate Racklyeft geschrieben und befindet sich hier: [History of Loop and LoopKit](https://medium.com/@loudnate/the-history-of-loop-and-loopkit-59b3caf13805).  Das Projekt wird fortgeführt als ein Liebesdienst einer Gemeinschaft von Anwendern, verwaltet und weiterentwickelt von Freiwilligen.


## Verwendung der Dokumentation

* Benutze das Navigationsmenu am oberen Rand um die Information zu finden, nach der du suchst.
* Ein Inhaltsverzeichnis der aktuellen Seite wird immer am linken Rand der Seite angezeigt.
* Du kannst die Loop Docs Seite auch durchsuchen, indem du auf dieses Icon klickst <img src="img/search_icon.png" width="50px" />.

    <img src="img/search_example.png" width="400" />


## Bleib in der Schleife!

[Melde dich für die Loop User-Ankündigungen an](https://groups.google.com/forum/#!forum/loop-ios-users), um über aktuelle kritische Probleme informiert zu sein.

Oder bei Zulipchat unter [https://loop.zulipchat.com](https://loop.zulipchat.com).

Es gibt auch eine Facebook Benutzergruppe [Looped Facebook Group](https://www.facebook.com/groups/TheLoopedGroup/?fref=nf), falls du Hilfe brauchst.  Denk bitte daran, deine Nachrichtenbox in Facebook zu überprüfen, wenn du dich in der Facebook Benutzergruppe anmeldest.

## Mithilfe

Neuerungen und Verbesserungen bezüglich dieser Dokumentation müssen als Pull-Request an das [loopdocs repo](https://github.com/LoopKit/loopdocs) eingereicht werden. Nähere Informationen, wie du bei Open-Source Projekten mithelfen kannst findest du hier [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/). Also, please review the Loop [LICENSE](https://github.com/LoopKit/Loop/blob/master/LICENSE.md) and Loop [CODE_OF_CONDUCT](https://github.com/LoopKit/Loop/blob/master/CODE_OF_CONDUCT.md).
