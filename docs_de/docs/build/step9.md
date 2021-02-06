# Schritt 9: Xcode Einstellungen

!!!danger "Geschätzte Zeit"
    - etwa 10-15 Minuten für die Installation der Kommandozeilen-Programme
    - 5 Minuten, um deine Apple-ID hinzuzufügen, vorausgesetzt, du erinnerst dich an dein Passwort

!!!info "Zusammenfassung"
    - Öffnen Sie Xcode Einstellungen und füge deine Apple-ID unter dem Accounts Tab hinzu.
    - Überprüfe, dass die Kommandozeilen-Programme in den Xcode Einstellungen und dort in der Registerkarte "Locations" korrekt installiert wurden.

!!!warning "FAQs"
    - **"Ich sehe immer noch nur ein Konto mit `(personal team)`, obwohl ich mich für das bezahlte Entwicklerkonto eingeschrieben habe...was soll ich machen? "** Bitte überprüfe deine Spam-Mailbox für den Fall, dass die E-Mail von Apple dort gelandet ist. Stellen Sie sicher, dass du die 48 Stunden gewartet hast, die Apple sagt, dass es dauern kann, um dein Konto zu aktivieren. Wenn bereits 48 Stunden vergangen sind und du noch keine E-Mail bekommen hast, kontaktiere den Apple Support und fragen nach dem Status deiner Anmeldung. Vielleicht steckt es bei Apple fest und ihr könnt es zusammen klären.

Da du alles der Reihe nach gemacht hast, hast du Xcode in Schritt 8 auf deinem Computer installiert. Du hast dich auch in Schritt 6, wenn dies deine Wahl war, für das Apple Developer-Programm mit einem kostenpflichtigen Konto registriert. Now we need to tell Xcode about your Developer Account.

Open Xcode from your Applications folder.

## Command Line Tools

There may be a short delay the very first time you open Xcode because it will install a package of tools. Don't close that window out, let it finish...we will need those Command Line Tools. Helpful tip: When the Command Line Tools installation is done and the pop-up window closes, check that your Command Line Tools installed correctly. Make sure that Xcode 12.0.1 (or newer) is selected there. Open Xcode's Preferences by clicking on the word **`Xcode` ** in the top menu bar (just to the right of the Apple icon in the upper-left corner) and selecting `Preferences` in the drop-down menu. The keyboard shortcut to open Xcode Preferences is `command-comma` if that's easier for you. Then select the `Locations` tab of Preferences window and you'll see the dropdown menu for Command Line Tools.

![img/command-line-error-3.png](img/command-line-error-3.png)

## Add Apple ID

Go to the Xcode Preferences window from above, click on the `Accounts` tab and then press the `+` in the lower-left corner to add an Apple ID account.

![img/xcode_account.png](img/xcode_account.png)

If you want to use a free developer account, you will simply enter your Apple ID in this section and Xcode will automatically enroll your Apple ID in the free developer program. If you enrolled in the paid account already and have confirmation that your account is active, enter the Apple ID of the paid developer account. The screenshot below shows the labeling of team names based on whether from free account vs. paid account. Free teams will have `(personal team)` after the name.

![img/apple_id.png](img/apple_id.png)

You are now done setting up Xcode.  Great job!  You will not need to redo the account setup steps on any subsequent builds or updates of your Loop app.  Xcode will remember these settings.

## Next Step: Test Settings

Now you are ready to move onto Step 10 to [Test Your Settings](step10.md).
