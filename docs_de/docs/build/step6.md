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

1. Loop Apps, die mit einem kostenlosen Entwicklerteam signiert sind, laufen nach 7 Tagen ab.  Am 7. Tag wird deine Loop App beim Öffnen einfach weiß und schließt dann sofort. Um die Loop App neu zu erstellen, musst du dann einen Computer haben und die App auf dem iPhone neu erstellen. Du kannst die App z.B. nicht am 5. Tag neu erstellen (wenn es vielleicht gerade gut passt)...in der Hoffnung, den 7-Tage count-down zurückzusetzen.  Die App läuft immer noch am 7. Tag aus, bezogen auf den Tag an dem sie das erste Mal signiert und erstellt wurde.</br></br>
2. Wenn du dich entscheidest, auf ein bezahltes Entwicklerkonto zu wechseln, nachdem du das kostenlose Entwicklerkonto ausgeprobiert hast, musst du die Loop App neu erstellen, um sie mit dem neuen bezahlten Entwicklerkonto zu signieren.</br></br>
3. Du musst während des Erstellungsprozesses der Loop App mit dem kostenlosen Entwicklerkonto einen extra Schritt befolgen, um die Funktionen von Siri und Apple Push-Benachrichtigungen herauszunehmen. Kostenlose Entwicklerkonten haben nämlich keinen Zugriff auf Apple Push-Benachrichtigungen und können auch keine Ferneingriffe mittels Nightscout machen.</br></br>

## Bezahltes Entwicklerkonto

Wenn du dich für die Nutzung eines **BEZAHLTEN** Entwicklerkontos entscheidest, musst folgendes wissen:

1. Loop Apps, die mit einem bezahlten Entwicklerteam signiert wurden, laufen ein ganzes Jahr.</br></br>
2. Das kostenpflichtige Entwicklerkonto kostet 99 USD pro Jahr und hat standardmäßig die Option mit automatischer Verlängerung. You can change that selection in your developer account settings at any time.</br></br>
3. If your household has multiple Loop users, only one developer account is needed.  That one developer account can be used to sign multiple Loop apps.</br></br>

## Switching from Free to Paid Memberships

In summary: This is no problem trying a free account first before you decide to buy a paid developer account. If you start with a free account, you'll build a Loop app (let's call it FreeLoop). When you switch to a paid account, you'll be building a totally new and separate Loop app onto your phone (let's call it PaidLoop). The two apps will look identical on your phone, but they will be functionally separate from each other...ideally you want to delete the FreeLoop app before using the PaidLoop app.

PaidLoop will know nothing about the settings and information you had stored in FreeLoop, so you will need to re-enter all your settings (basal rates, ISF, carb ratios, etc.) and configurations into the new PaidLoop. It will also not connect or control any pods you are currently using with the old FreeLoop you had installed.

So, when switching from Free to Paid Loop builds...try to remember that you'll have the best luck by (1) timing it at pod change time and (2) take screenshots of your old app's settings so that you can enter them into the new app.

## Enrolling

Paid account enrollment is all through Apple's Developer Program website. Go to the [Apple Developer website](https://developer.apple.com/programs/enroll/) to enroll in an individual paid account. If you instead want the free account, you don't have to do anything on that website. You'll just wait for Step 8 Xcode Preferences and we will get your free account then.

## Next Step: Install Homebrew

Now you are ready to move onto Step 7 to [install Homebrew](step7.md).
