# Schritt 1: Kompatibler Computer

!!!Gefahr "Geschätzte Zeit"
    - 5 Minuten, wenn du bereits Mojave (10.14) oder Catalina (10.15) auf deinem Apple Computer installiert hast
    - 30-60 Minuten, falls MacOS Aktualisierungen installiert werden müssen

!!! Info "Zusammenfassung"
    - Überprüfe deine MacOS Version, es sollte Mojave oder Catalina sein. **Wenn auf deinem iPhone, auf dem du Loop installieren wirst, die aktuelle iOS Version (14.x) läuft, dann musst du MacOS Catalina auf deinem Apple Computer installiert haben.**
    - Arbeite nicht mit einer Beta MacOS Version. (Du kannst diesen Punkt ignorieren, wenn du nicht weist, was das ist... es bedeutet, dass du kein Beta MacOS auf deinem Apple Computer verwendest.)
    - Solltest du nicht MacOS Mojave oder Catalina verwenden ueberpruefe, ob du auf eines davon aktualisieren kannst.
    - Wenn du deinen Apple Computer nicht auf Mojave oder Catalina aktualieren kannst, bleiben dir die folgenden Optionen. Einen passenden Computer ausleihen, ein "patcher tool" verwenden, oder einen neuen/gebrauchten kompatiblen Apple Computer kaufen.
    - Überprüfe `Software Aktualisierungen`, ob dein Computer auf dem letzten Stand ist. Wenn nicht, führe die Aktualisierungen zuerst durch.

!!!warning "FAQs"
    - **"Kann ich auch einen PC/Windows benutzen? Ich habe keinen Apple Computer."** Ja, es geht schon... Information [this FAQ about using Virtual Machine](/faqs/FAQs/#can-i-use-a-pc-or-windows-computer-to-build). PCs mit einem AMD Prozessor Chip können keinen Apple Computer emulieren. Wenn du das probieren möchtest schaue also zuerst nach, welchen Prozessor Chip du in deinem PC hast.
    - **"Was kann ich tun, wenn mein Computer zu alt ist, um auf Catalina aktualisiert zu werden?"** Du kannst es mit [Catalina Patcher](http://dosdude1.com/catalina/) probieren, allerdings bist du dabei auf dich allein gestellt und es ist nicht Teil dieser Anleitung. Dieses ist nur die Antwort auf eine der FAQs. Es ist an dir, dich über das "patcher tool" zu informieren und zu überlegen, ob du diesen Weg beschreiten moechtest.
    - **"Kann mir von jemandem anderes einen Apple-Computer ausleihen?"** Ja, lies hier [diese FAQ über das Ausleihen eines Computers](/faqs/FAQs/#do-i-need-to-own-my-own-apple-computer), um mehr zu erfahren.
    - **"Wie oft brauche ich den Computer?",** Du brauchst den Computer nur, wenn du die Loop-App installierst oder auf eine neuere Loop-Version aktualisierst. Du brauchst keinen Computer, um die Einstellungen in Loop, wie z. B. Basalprofile oder Kohlenhydratverhältnisse zu ändern oder nach Fehlern zu suchen.

## Neue Apple Computer mit M1-Chip

Auch die im November 2020 vorgestellten Apple Computer mit M1 Chip können für die Installation von Loop verwendet werden. Es gibt EINEN Schritt, den du bei der Verwendung der neuen Computern mit M1 Chip beachten musst, Schritt 7 "Installation von Homebrew". Ich habe auf dieser Seite die Schritte farbig hervorgehoben, die M1-Benutzer beachten müssen. Versprochen, es ist einfach und schnell.

Und...ich bin ein bischen eifersüchtig, dass du den neuen Computer hast. Du Gueckspliz wirst damit die Loop-Installation extrem schnell erledigt haben, die Zeitschätzungen in dieser Anleitung werden gandenlos länger sein als das, was du mit deinem M1 Chip sehen wirst.

## Big Sur MacOS

Ja, Big Sur ist geeigent für die Installation von Loop...ich arbeite daran, diese Seite zu aktualisieren. Habe ein bischen Geduld.

## Catalina oder Mojave, welches davon brauchst du?

Brauchst Du Catalina oder Mojave? Die Antwort hängt von der iOS Version deines iPhones ab, auf dem du Loop installieren möchtest.

**Wenn du iOS 12.4 bis 13.2** hast, kannst du macOS 10.14.4 (Mojave) oder 10.15.2 oder neuer (Catalina) verwenden.

**Wenn du iOS 13.4 oder neuere** hast, kannst du Mojave nicht verwenden und benötigst mindestens Catalina. Mit anderen Worten, du benötigst macOS 10.15.2 oder neuer um Loop auf einem iPhone mit iOS 13.4 oder höher zu installieren.

!!!danger "Die iOS Version bestimmt die MacOS Version auf deinem Computer"

    Etwas vereinfacht könnte man auch sagen...wenn du dein iOS immer auf dem neusten Stand hälst, dann muss du auch deinen Computer und das MacOS aktuell halten. Das ist nichts Schlechtes und du kannst iOS-Updates sowieso nicht für immer vermeiden... du musst nur wissen, wie diese miteinander in Beziehung stehen und wann dein Computer "zu alt" ist.

## Überprüfe deine MacOS Version

Du benötigst einen Apple-Computer, der die Mindestvoraussetzung des MacOS wie oben beschrieben erfüllt; d.h. Mojave MacOS 10.4.4 (oder neuer) oder Catalina MacOS 10.15 (oder neuer). Um herauszufinden, welche Version du installiert hast, klicken auf das kleine Apple-Symbol in der oberen linken Ecke des Computers und wähle `Über diesen Mac` aus. Es spielt dabei keine Rolle, ob der Computer ein MacBook, iMac, Mac mini usw. ist, solange er die Mindestvoraussetzungen erfüllt.

Wenn auf deinem Computer nicht das mindestens erforderliche MacOS installiert ist, musst du mit `Software-Update` überprüfen (siehe das Bild unten), ob du es aktualisieren kannst.

<p align="center">
<img src="../img/macosx.png" width="500">
</p>
Falls dein Computer keine Update auf ein neueres MacOS anbietet, kann es sein, dass Apple entschieden hat, dass dein Computer zu alt dafür ist. Wie alt ist zu alt? Das hängt von deinem Computermodell und Jahr ab (siehe die Bilder unten):

<p align="center">
<img src="../img/mojave-minimum.png" width="750">
</p>

## Nächster Schritt: Kompatible iPhone/iPod touch

Jetzt kannst du mit Schritt 2 weitermachen, um zu überprüfen, ob du ein [kompatibles iPhone/iPod touch](step2.md) hast.
