# Allgemeine Loop FAQs

Willkommen bei den LoopDocs - ein Platz für alle häufigen Fragen (FAQs).

## Was ist Loop?

Klicke auf das untere Bild, um eine kurze [Einführung in Loop (englisch)](https://youtu.be/qw_u1lqboCs) zu sehen.

<a href="https://youtu.be/qw_u1lqboCs" target="_blank"><img src="../img/intro-to-loop.png"  title="Einführung in Loop (englisch)" /></a>

## Was benötige ich, um zu loopen?

Loop hat sowohl Hard-, als auch Software-Anforderungen. Allgemein brauchst du sieben Komponenten:

- Compatible insulin pump: [Medtronic or Omnipod](../build/step3.md)
- [Compatible CGM](../build/step4.md)
- [RileyLink](../build/step5.md)
- [Ein \[kompatibles iPhone und/oder iPod Touch\](https://loopkit.github.io/loopdocs/build/step2/)](../build/step2.md)
- [Einen \[Apple Computer mit Mojave macOS 10.14.3 oder neuer\](https://loopkit.github.io/loopdocs/build/step1/).](../build/step1.md)
- [Xcode (a free Apple application)](../build/step8.md)
- [Apple Developer Membership](../build/step6.md)

<p align="center">
<img src="../img/loop_gear.jpg" width="500">
</p>

## Kann ich Loop einfach aus dem App Store herunterladen und installieren?

Nein. Loop ist nicht zum Download verfügbar. Du musst dir die App selbst bauen. Wenn Loop im App Store zum Download verfügbar wäre, würde dies der Verteilung eines medizinischem Gerätes gleich kommen und wir bewegen uns halt nicht in diesem Bereich ;-).  Du kannst es dir selbst zusammenbauen, aber wir sind nicht der Verteiler.

Keine Angst, das Übersetzen und Zusammenbauen der App ist eigentlich ganz einfach und genau darum dreht es in dieser Dokumentation ja gerade. Der schwierigere Teil für dich ist allerdings, die Geduld aufzubringen, die gesamte Dokumentation durchzulesen, bevor du mit dem Übersetzen und Zusammenbau startest. Neue Loop Benutzer sind so aufgeregt, dass sie die ganzen wichtigen Informationen beim Durchlesen dieser Dokumentation verpassen. Also, starte mit dem Zusammenbau, aber plane die Zeit für das Durcharbeiten der Dokumentation ein, nachdem du erfolgreich die Loop App zusammengebaut hast.

Falls du irgendwelche Fragen hast, findest du eine nette kleine Suchfunktionalität am oberen Rand der Seite, die dir die Antwort auf deine Frage schnell geben kann.

## Kann ich ein Android Handy für Loop benutzen?

Nein, Loop funktioniert nur auf einem iPhone und iPod touch.

## Muss ich technisch affin sein, um Loop zusammenzubauen?

Nein, nein und nochmals nein! Nein, du brauchst keinerlei Erfahrungen im Programmieren oder Umgang mit deinem Computer, um die Loop-App zu erstellen. If you have already owned an Apple computer and iPhone, you already have the required level of experience. Beyond that, simply read the directions slowly and diligently...all the information you will need are in these documents.

Often times the non-tech people do better than the tech people in building Loop. Why? Because the non-tech people take the time to read slowly and look at the screenshots in the directions. Die Techniker überfliegen häufig die Texte nur und überlesen ganze Sätze, was oftmals zu sog. Build-Fehlern führt, die erst zurückverfolgt und dann korrigiert werden müssen.

## Gibt es einen Spickzettel für diabetische Hilfskräfte und Diabetologen?

Sicher. Schau dir das mal an [PDF Download für diabetische Hilfskräfte und Profis](https://github.com/Kdisimone/images/raw/master/school_nurse.pdf)

## Wie lange dauert es, die Loop-App zu bauen?

Die Antwort variert, aber es dauert schon ein paar Stunden, um das Ganze von Anfang bis zum Ende durchzuarbeiten, je nachdem wie vertraut du mit deinem Rechner bist.

If you'd rather break it up into several shorter bits of effort, the [`Build App`](../build/step1.md) section is divided into convenient stopping points with Time Estimates for each step. Du kannst dann einen oder mehrere Schriite abarbeiten, je nachdem wieviel Zeit du aufbringen kannst.

## Kostet die Loop-App Geld?

Ja, da sind ein paar Kosten, abgesehen von den offensichtlichen Kosten einer Pumpe und eines CGMs.

Der [RileyLink](https://getrileylink.org/) kostet ca. 130€ (150$). Dies sind einmalige Kosten. Einige von euch werden auch noch den originalen RileyLink am Laufen haben, der seit rund drei Jahren einen guten Dienst tut. Ich rate dringend, gleich zwei RileyLinks zu kaufen, insofern das bezüglich der Kosten machbar ist. So hat man immer einen in der Hinterhand, falls der andere in irgendeiner Form Schaden nimmt.

Die Entwicklerlizenz von Apple gibt es zwar auch kostenlos, das heisst dann aber automatisch, dass du die App alle sieben Tage neu zusammenbauen musst, was ziemlich ermüdent ist. That could get very tedious. Die jährliche Investition von rund 85€ (99$) in eine kokstenpflichtige Apple Entwicklerlizenz ist durchaus sinnvoll.

Ansonsten gibt es keine weiteren Kosten, weder laufende, noch einmalige.

## Brauche ich meinen eigenen Apple Computer?

Du brauchst keinen eigenen. Du kannst dir entweder einen leihen oder dir einen virtuellen Apple Rechner auf deinen Windows Computer zaubern (https://macosvmware.tech.blog/). It would be really good to have longer term ability to borrow that computer again for [updating Loop](../build/updating.md#when-to-update) later, when needed.

Wenn du dir einen Apple leihst, solltest du die Person bitten, erstens mindestens auf Mojave zu aktualisieren und zweitens [XCode](https://developer.apple.com/xcode/) zu installieren, bevor du ans Zusammenbauen der Loop-App gehst. The updates and download of Xcode can take a couple hours depending on the person's internet speed...so best to do those steps well ahead of time to save trouble.

## Kann ich mit einem PC oder Windows Computer die Loop-App zusammenbauen?

Ja, du kannst. Es gibt einen "Hacker-Weg" ein MacOs als virtuelle Maschine auf einem Windows Computer zu betreiben. [Dieser Link](https://macosvmware.tech.blog/) gibt dir ein paar hilfreiche Informationen zu diesem Thema, aber es obliegt dir und Google falls du an Grenzen stößt. Diese virtuelle Maschine läuft aber nicht auf Rechnern mit AMD Prozessoren, also überprüfe es vorher genau, dass  kein AMD Prozessor in deinem PC steckt. Diese Dokumentation beinhaltet keine Fehlerbehebungen oder Tipps für Virtual-Maschinen-Installationen oder deren Benutzung.

## Wie oft muss ich an den Rechner für die Loop-App?

Die kurze Antwort ist: Einmal wenn du die App installierst und danach einmal pro Jahr. Falls du dich für ein kostenloses Apple Entwickler Account entschieden hast, musst du einmal pro Woche an den Rechner.

Die lange Antwort ist: Der Progarmmcode für die Loop-App wird immer wieder aktualisiert und verbessert, um neue Features ein- und Bugs auszubauen. When those updates are released, you'll need access to an Apple computer again to update your Loop app.  Im Allgemeinen gibt es mehrmals pro Jahr ein Update, für das du dir vielleicht Zeit zum Installieren nehmen möchtest. Loop updates are not available through the iPhone's app store...instead you do the app update yourself with [update instructions here](../build/updating.md).

## Muss ich die Loop-App neu erstellen, wenn ich zwischen der Medtronic und Omnipod Pumpe wechseln will?

Nein. Die Loop-App bietet die Möglichkeit über die Einstellungen zwischen den verschiedenen Pumpen zu wechseln. Über die "Wechsle von Onmipod" oder "Pumpe löschen" Funktion kann du von einer Pumpe zur anderen wechseln.

## Kann ich das Apple Entwickler Konto einer anderen Person benutzen, um die Loop-App zu erstellen?

Technisch gesehen ja, aber da sind ein paar wichtige Beeinträchtigungen. Das Entwicklerkonto einer bestimmten Person kann nur mit einer beschränkten Anzahl von Entwicklungsrechnern verknüpft werden. Wenn also eine Person sein Entwicklerkonto an mehrere Leute "verleiht", ist die begrenzte Anzahl an Entwicklerechnern schnell erreicht. In einem solchen Fall wird der Entwickler dazu aufgefordert, die Zertifikate, die zur Erstellung der App benötigt werden, von einigen Rechnern zu widerrufen (im Grunde genommen alte Zertifikate löschen, um Platz für neue zu schaffen). Wenn er dies tut, kann es sein, dass er übersieht, dass ein Zertifikat für deine Loop-App verwendet wird (kann im Entwicklerkonto nicht gesehen werden). Deine Loop-App wird dann sofort geschlossen und kann nicht mehr benutzt werden.

Deine Loop-App wird auch sofort sterben, wenn das Entwicklerkonto nicht erneuert wird oder ausläuft. Deine Loop-App Updates werden auch nicht erstellt werden können, solange der Entwickler den Lizenz Vereinbarungen nicht zustimmt.

Die Moral von der Geschichte ist, die Entlehnung einer Entwickler Lizenz von einer anderen Person ist "Sparen am falschen Platz". Du könntest unerwartet ohne Loop-App dastehen, ohne vorher informiert zu werden.

## Kann ich mein Apple Entwickler Konto benutzen, um Loop-App für andere zu erstellen?

Technisch gesehen ja, aber es gibt Gründe die dagegen sprechen. Wenn du die Loop-App für andere erstellst, musst du darauf achten, dass du das Zertifikat, mit dem die App des anderen signiert ist, nicht unbeabsichtigt löschst oder ungültig machst (siehe vorherige Frage). Du musst die Personen, für die du die Loop-App erstellst, auch informieren, dass ihre Loop-App MAXIMAL zwölf Monate benutzt werden kann. Wie auch immer muss die App alle zwölf Monate neu erstellt werden.

Aber das größte Problem ist sicherlich, dass die Leute, für die du die Loop-App erstellst, keine akzeptable Möglichkeit haben, an Neuerungen und Fehlerkorrekturen zu gelangen. Eine Menge neuer Looper mit einer Omnipod Pumpe brauchen ein regelmäßiges Update ihrer App innerhalb des ersten Jahres. Solange du vorhast, dich mit diesen Personen häufig zu treffen, kannst du sie gern mit einer alten Version der Loop-App alleine lassen, die nicht so gut funktioniert, wie die neue Version.

## Wie kann ich eine kompatible Pumpe finden? Gibt es Nachschub?

There is a [whole page with detailed information about Medtronic pumps](../build/step3.md); how to find them, how to find supplies, and assessing whether your Medtronic pump is compatible. Schau dir diese Seite an, falls du diesbezüglich Fragen hast.

Zusätzlich kannst du auch den Omniport Support auf die gleiche Weise befragen, wie du es normalerweise gwohnt bist.

## Kann ich jemanden Geld bezahlen, dass alles für mich zu erledigen?

NOOOO...you really need to figure this out yourself. Du musst wirklich selbst lernen, wie das alles funktioniert. Die Loop-App ist ein System zur automatisierten Insulinabgabe und du musst wirklich selbst wissen, wie es erstellt, funktioniert und benutzt wird.

## Was ist, wenn ich meinen RileyLink verliere?

Medtronic Benutzer gehen einfach zurück auf die alte Art ihre Pumpe zu benutzen und warten, bis der neue RileyLink ankommt. Du kannst entweder abwarten, bis die temporäre Basalrate von alleine durch ist (typischerweise 30 Minuten oder schneller) oder du stoppst die temporäre Basalrate über das Menü der Pumpe. Für den normmalen Bolus verwendest du die normale Bolusfunktion deiner Pumpe. Wenn du wieder einen RileyLink hast (entweder du findest den alten oder entdeckst den Ersatz-RileyLink wieder) und die Loop App wieder starten willst, solltest du eine Sache auf jeden Fall beachten: Gib alle Kohlenhydrate ein, die du in der nahen Vergangenheit gegessen hast, die auf deinen aktuellen Blutzucker Einfluss gehabt haben könnten. Auch wenn die Loop-App bei einer Metronik-Pumpe jede Insulinabgabe ermittelt, die während der Abwesenheit des RileyLinks vorgenommen wurde, kann sie nicht die dazugehörigen Kohlenhydrate ermitteln, auch die nicht, die du in der Pumpe angegeben hast. Also stelle sicher, dass du diese Werte eingibst und auf die richtige Uhrzeit datierst, zu der sie gegessen wurden. Das hilft, den Übergang zum Loopen glatt laufen zu lassen.

Für Pod Benutzer gilt, dass dein Pod alle momentan laufenden temporären Basalraten auslaufen lässt (das dauert maximal 30 Minuten) und dann wieder zur normalen voreingestellten Basalrate zurückkehrt. Without a RileyLink, you will not be able to affect any Pod use other than normal basals. Es wird nicht möglich sein, temporäre Basalraten zu verabreichen oder die Basalrate auszusetzen. Genauso, als wenn du deinen PDM verlierst. If you have a backup RileyLink, you can simply connect to the new RileyLink on the same Loop app and it will work with the existing pod session. Falls du keinen Ersatz hast, kannst du nur noch den momentanen Pod durch einen neuen ersetzen, den du mit deinem PDM aktivierst, so lange, bis du einen neuen RileyLink hast.

## Was ist, wenn ich mein iPhone verliere oder ein neues habe?

Wenn du ein neues iPhone hast, musst du die Loop-App auf die gleiche Art und Weise installieren, wie du es bei deinem alten iPhone getan hast. Die Loop-App kann nicht aus der iCloud oder aus Backups wiederhergestellt werden. Beachte also, dass du rechtzeitig einen Apple Computer zur Hand hast, mit dem du die Loop-App für dein neues iPhone wieder erstellen kannst.

## Wie sieht es mit anderen Pumpen aus? Kann ich mit denen loopen?

ok, lass uns zuerst einmal dankbar sein für das, was wir bereits haben. The Möglichkeit die Loop-App zu nutzen ist das Ergebnis der enormen Anstrengung, Zeit und Opfer von Freiwilligen. Das Hacken und Reengineeren der Verbindungen zu den Pumpen ist eine sehr große Anstrengung. Wenn eine neue Gruppe von Programmierern sich dran macht, die enorme Zeit aufzuwenden neue Pumpen anzubinden, wäre es sich denkbar, diese neuen Pumpen in Loop-App zu integrieren. Du brauchst uns nicht zu sagen, dass du gerne andere Pumpen in Loop integriert hättest. Das wollen wir auch. Es ist einfach eine furchtbare Menge Zeit, die es braucht, um das geschehen zu lassen und es geht weder einfach, noch schnell.

Tandem Pumpen sind nicht mit der Loop-App kompatibel. Animas Pumpen sind nicht mit der Loop-App kompatibel. DASH Pods sind nicht mit der Loop-App kompatibel. All diese Pumpen werden wahrscheinlich auch in Zukunft nicht kompatibel sein.

## Kann ich mehr als eine Loop-App auf meinem iPhone haben?

Technisch gesehen ja. Du kannst mehrere Loop-Apps auf deinem iPhone haben. Allerdings können mehrere Loop-Apps auf deinem iPhone zu unerwarteten Konflikten führen, die negative Auswirkungen für die Loop-App haben, die dir einen grünen Ring anzuzeigen und demzufolge dich am Loopen zu halten. Außerdem wird dein Pod nur mit einer Loop-App zusammenarbeiten. Für ein glattes Loopen solltest du also nur eine Loop-App zur Zeit auf deinem Telefon haben.

## Kann ich auch im Flugzeug loopen? Oder in den Bergen?

Ja. Die Loop-App benötigt keine Internet- oder Telefonverbindung, um zu funktionieren. Solange der Benutzer Bluetooth angeschaltet lässt, können der Dexcom und der RileyLink ihre Loop-Arbeit erledigen.

