# Schritt 6: Einschreiben im Apple Developer Program

!!!Gefahr "Geschätzte Zeit"
    - 15-20 Minuten für die Anmeldung
    - bis zu 2 Tage bis das Entwicklerkonto aktiviert ist (du bekommst eine Bestätigungs-E-Mail von Apple)

!!! Info "Zusammenfassung"
    - Wenn du dich für ein kostenpflichtiges Entwicklerkonto entschieden hast, musst du dich jetzt anmelden. Gehe auf die [Apple Developer Website](https://developer.apple.com/programs/enroll/) um dich für ein eigenes Konto anzumelden.
    - Wenn du dich entschieden hast ein kostenloses Entwicklerkonto zu verwenden, musst du jetzt nichts tun, wir erklären es später.

!!!warning "FAQs"
    - **"Kann ich das Apple-Entwicklerkonto von jemand anderes benutzen?"** Gute Frage...Antwort ist [hier](/faqs/FAQs/#can-i-use-someone-elses-apple-developer-account).
    - **"Benutze ich meine Apple-ID oder die Apple-ID meines Kindes, um mich für das Apple Developer Program anzumelden?** Die Apple-ID, mit der du dich für das Developer Program anmeldest, muss nicht die gleiche Apple-ID sein, wie die des Loop-iPhones oder die der Person, die Loop benutzen wird. Du kannst als Elternteil deine Apple-ID benutzen und Loop auf dem iPhone deines Kindes installieren. Es ist sinnvoll die Apple-ID der Person für die Anmeldung beim Developer Program zu benutzen, die die Loop-App-Erstellung durchführen wird.
    - **"Wie lange dauert es, bis mein Apple Entwicklerkonto aktiv ist, nachdem ich mich angemeldet habe?** Achte, nachdem du dich angemeldet hast, auf eine Bestätigungs-E-Mail von Apple. Apple sagt, dass es bis zu 24-48 Stunden dauern kann, um ein neues Apple-Entwicklerkonto einzurichten, es gibt aber Berichte von einigen Leute, dass es nur wenige Minuten gedauert hat. Es variiert einfach. Wie es garantiert länger dauert? Wenn du bei der Anmeldung für das Apple Entwicklerkonto mit einer anderen Kreditkarte bezahlst, als die Kreditkarte, die bereits mit der Apple ID von der Anmeldung verknüpft ist. Ich habe gehört, dass Apple dann zusätzliche Informationen zu deiner Identifikation verlangt.

Um deine eigene Loop App zu erstellen, musst du ein Apple Entwicklerkonto haben.  Du hast hier zwei Optionen; a) kostenlos oder b) bezahlt.

## Kostenloses Entwicklerkonto

Wenn du dich für die Nutzung eines **KOSTENLOSEN** Entwicklerkontos entscheidest, musst folgendes wissen:

1. Loop Apps, die mit einem kostenlosen Entwicklerteam signiert sind, laufen nach 7 Tagen ab.  Am 7. Tag wird deine Loop App beim Öffnen einfach weiß und schließt dann sofort. Um die Loop App neu zu erstellen, musst du dann einen Computer haben und die App auf dem iPhone neu erstellen. Du kannst die App z.B. nicht am 5. Tag neu erstellen (wenn es vielleicht gerade gut passt)...in der Hoffnung, den 7-Tage count-down zurückzusetzen.  Die App läuft immer noch am 7. Tag aus, bezogen auf den Tag an dem sie das erste Mal signiert und erstellt wurde.
2. Wenn du dich entscheidest, auf ein bezahltes Entwicklerkonto zu wechseln, nachdem du das kostenlose Entwicklerkonto ausgeprobiert hast, musst du die Loop App neu erstellen, um sie mit dem neuen bezahlten Entwicklerkonto zu signieren.
3. Du musst während des Erstellungsprozesses der Loop App mit dem kostenlosen Entwicklerkonto einen extra Schritt befolgen, um die Funktionen von Siri und Apple Push-Benachrichtigungen herauszunehmen. Kostenlose Entwicklerkonten haben nämlich keinen Zugriff auf Apple Push-Benachrichtigungen und können auch keine Ferneingriffe mittels Nightscout machen.

## Bezahltes Entwicklerkonto

Wenn du dich für die Nutzung eines **BEZAHLTEN** Entwicklerkontos entscheidest, musst folgendes wissen:

1. Loop Apps, die mit einem bezahlten Entwicklerteam signiert wurden, laufen ein ganzes Jahr.
2. Das kostenpflichtige Entwicklerkonto kostet 99 USD pro Jahr und hat standardmäßig die Option mit automatischer Verlängerung. Du kannst diese Option aber jederzeit in deinen Entwicklerkonto Einstellungen ändern.
3. Auch wenn es in deinem Haushalt mehrere Loop Benutzer gibt, wird nur ein Entwicklerkonto benötigt.  Ein Entwicklerkonto kann verwendet werden, um mehrere Loop Apps zu signieren.

## Wechsel von kostenlosen auf bezahltes Entwicklerkonto

Kurz: Es ist kein Problem, zuerst ein kostenloses Entwicklerkonto auszuprobieren, bevor du dich entscheidest, ein bezahltes Entwicklerkonto abzumachen. Wenn du mit einem kostenlosen Entwicklerkonto beginnest, erstellst du eine Loop App (sagen wir mal LoopKostenlos). Wenn dz auf ein bezahltes Entwicklerkonto wechselst, erstellest du eine völlig neue und separate Loop App auf dem iPhone (diese nennen wir LoopBezahlt). Beide Apps sehen auf deinem iPhone identisch aus, aber sie hängen funktionell nicht zusammen...idealerweise solltest du die LoopKostenlos App löschen, bevor du anfängst die LoopBezahlt App zu benutzen.

LoopBezahlt hat keine Ahnng von den Einstellungen und Informationen, die du in LoopKostenlos gespeichert hast. Du must also alle deine Einstellungen erneut in LoopBezahlt eingeben (Basalraten, Insulinsensitivität, Kohlenhydratverhältnis, usw.). Das neue LoopBezahlt wird auch keine Pods ansteuern oder kontrollieren können, die du derzeit mit dem alten LoopKostenlos verwendest.

Also, wenn du von LoopKostenlos auf LoopBezahlt wechselst...erinnere dich an (1) der optimaler Zeitpunkt ist, wenn auch der Pod getauscht wird und (2) mache Bildschirmfotos der Einstellungen in deiner alten LoopKostenlos App, damit du diese einfach in die neue LoopBezahlt App eintragen kannst.

## Anmeldung

Die kostenpflichtige Anmeldung erfolgt über die Website des Apple's Developer Programms. Gehe dafür auf die [Apple Developer Website](https://developer.apple.com/programs/enroll/) um dich für ein eigenes Entwicklerkonto anzumelden. Wenn du stattdessen das kostenlose Entwicklerkonto möchtest, musst du auf dieser Website nichts machen. Warten einfach bis zu Schritt 8 Xcode Einstellungen und wir erstellen dann dein kostenloses Entwicklerkonto.

## Nächster Schritt: Installation von Homebrew

Jetzt kannst du mit Schritt 7 weitermachen, [Homebrew](step7.md) installieren.
