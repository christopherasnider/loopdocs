# iOS 13 FAQs

Jedes mal, wenn eine neue Version von iOS herauskommt, gibt es eine Menge Fragen und hektisches Durcheinander. Diese Seite ist dafür da, diese Fragen schnell zu beantworten.

## Soll ich auf iOS 13 updaten?

Das ist eine Frage, die du unabhängig von Loop betrachten solltest. Neue iOS Versionen haben häufig Fehler, also würde ich eine Zeit lang versuchen zu vermeiden, die iOS Version des Handys meiner Tochter zu aktualisieren. Stattdessen aktualisiere ich mein iPhone und probiere die Sachen zuerst aus. Die Dexcom App könnte auch Fehler haben, wer weiss das schon? Ich möchte aber auf jeden Fall erst einmal die ganze Sachen funktionieren sehen (oder es von jemandem hören), bevor ich neue iOS Versionen ausprobiere. Sobald ich sehe, dass die Sache bei mir ohne große Probleme läuft, aktualisiere ich das iOS des iPhones meiner Tochter. Außerdem ist ein Zurück auf die alte Version echt aufwendig und häufig nicht einmal möglich.

Es geht weniger darum, was du in Bezug auf Loop beachten musst, wenn du iOS aktualisierst. Es geht mehr darum, was du vorher bei der nächsten Loop Erstellung brauchst und hinterher in iOS aktualisieren musst.

## Wird meine Loop-App weiter funktionieren, wenn ich nicht auf iOS 13 aktualisiere?

Ja. Deine Loop-App wird ein Jahr lang funktinieren, nachdem du sie gebaut hast (oder solange bis das Entwicklungs-Zertifikat ausläuft, was immer zuerst eintritt). Also, wenn du nicht auf iOS 13 aktualisierst, ist das keine große Sache für die Loop-App.

## Wird meine Loop-App funktionieren, wenn ich auf iOS 13 aktualisiere?

Ja. Wir hatten nicht ein iOS 13 Update, welches die Loop-App gestört hat, das bereits auf dem jeweiligen iPhone installiert war. Soweit ich mich erinnern kann, haben wir mit iOS 9 angefangen und die Loop-App hat über alle Versionen hinweg funktioniert. Loop has worked through all the updates.

## Muss ich die Loop-App aktualisieren, wenn ich auf iOS 13 wechsle?

Nope. Unless you want to try dark mode which is in dev branch and being developed there...that's about the only thing that is iOS 13 specific in Loop.

## Habe ich irgendeinen Vorteil, wenn ich meine Loop-App aktualisieren, wenn ich iOS 13 verwende?

Nein. Außer du willst den Dark Mode ausprobieren, der sich im Entwicklungs-Branch befindet. Das ist das einzige, was iOS 13 spezifisch in der Loop-App ist.

## Warum ist das iOS-Update dann so eine große Sache?

Weil Major-Releases (wie beim Wechsel von iOS 12 auf iOS 13, bei dem sich der erste Teil der Versionsnummer ändert) eine Reihe von Aktualisierungen anderer großer Apple-Angelegenheiten nach sich ziehen. Das ist halt der Kaskadeneffekt.

Wenn man iOS auf eine neue Major-Version bringt, muss Xcode ebenfalls akualisiert werden, da Xcode neue Kommandozeilenwerkzeuge braucht, es Aktualisierungen in der SWIFT-Sprache gibt und die Simulatoren, die zum korrekten Erstellen der Versionen mit dem neuen iOS auf den verschiedenen Geräten notwendig sind, müssen ebenfalls aktualisiert werden. Because Xcode will need the new command tools, Swift language updates, and simulators to be able to properly build for devices that have the new iOS.

Und die Kaskade geht weiter. Das neue Xcode braucht wahrscheinlich ein neues macOS. Und manchmal (was bei der Aktualisierung auf Xcode 10 der Fall war) ist die benötigte Aktualisierung von macOS ebenfalls ein Major Release, was bei manchen Rechnern nicht funktioniert. They were "unsupported" by Apple and were aged-out. Dadurch wurden diese Rechner nicht mehr von Apple unterstützt und waren zu alt. Glücklicherweise hat die Aktualisierung auf Xcode 11 kein Ausmustern von Rechnern zur Folge. Wenn bei dir schon Xcode 10 läuft, kann du auf Xcode 11 ohne Problem aktualisieren.

Also sind iOS-Aktualisierungen eine große Sache für Looper, da sie andere Aktualisierungen zur Folge haben, um beim nächsten Mal weiterhin die Loop-App bauen zu können. Und die Leute vergessen zu aktualisieren. Und dann vergessen sie auch noch die spezielle LoopDoc-Seite, die ihnen beim Aktualisieren helfen soll. Also laden sie blindlings den Code herunter, bauen die App wie beim letzten mal und sind sich nicht bewusst, dass sie zuerst aktualsieren müssen.

Außerdem aktualisiere ich mein iPhone solange nicht, bis ich mein MacOS und Xcode aktualisiert habe. Sobald du dein iOS aktualisiert hast, musst du die Aktualisierungen andere Programme auf dem Mac koordinieren, die dir beim Erstellen der Loop-App helfen.
