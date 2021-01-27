# Étape 9 : Préférences d'Xcode

!!!danger "Temps estimé"
    - environ 10-15 minutes pour installer les outils en ligne de commande
    - 5 minutes pour ajouter votre identifiant Apple, en supposant que vous vous rappeliez de votre mot de passe

!!!info "Résumé"
    - Ouvrez les Préférences Xcode et ajoutez votre identifiant Apple sous l'onglet "Comptes" ou "Account".
    - Vérifiez que les outils de ligne de commande ont été correctement installés dans les préférences Xcode sous l’onglet "Emplacements" ou "Locations".

!!!warning "FAQs"
    - **« Je ne vois encore qu’un compte avec `(équipe personnelle ou personal team)` à côté de lui, même si je me suis inscrit au programme de compte développeur payant... que dois-je faire? »** Vous devriez vérifier votre boîte e-mail spam/indésirable au cas où Apple vous ait envoyé un e-mail déplacé dans cette dossier la. Assurez-vous d’avoir attendu les 48 heures qu’Apple dit qu’il peut prendre pour obtenir la validation de votre compte. Si cela fait 48 heures et que vous ne voyez toujours rien dans votre e-mail, contactez le support Apple et demandez-leur le statut de votre inscription. Il peut être retardé par quelque chose de leur côté.

Puisque vous avez travaillé dans l'ordre, Xcode est deja installé sur votre ordinateur depuis l'étape 8. Vous vous êtes également inscrit au programme Apple Developer avec un compte payant, si tel était votre choix, à l’étape 6. Maintenant, nous devons référencer votre compte développeur dans Xcode.

Ouvrez Xcode depuis votre dossier Applications.

## Outils de ligne de commande

Il peut y avoir un court délai la première fois que vous ouvrez Xcode car il installera un paquet d'outils. Ne fermez pas cette fenêtre, laissez-la finir... nous aurons besoin de ces outils de ligne de commande. Conseils utiles : Lorsque l'installation des Outils en ligne de commande est terminée et que la fenêtre pop-up se ferme, vérifiez que vos Outils en ligne de commande sont correctement installés. Make sure that Xcode 12.0.1 (or newer) is selected there. Open Xcode's Preferences by clicking on the word **`Xcode` ** in the top menu bar (just to the right of the Apple icon in the upper-left corner) and selecting `Preferences` in the drop-down menu. The keyboard shortcut to open Xcode Preferences is `command-comma` if that's easier for you. Then select the `Locations` tab of Preferences window and you'll see the dropdown menu for Command Line Tools.

![img/command-line-error-3.png](img/command-line-error-3.png)

## Add Apple ID

Go to the Xcode Preferences window from above, click on the `Accounts` tab and then press the `+` in the lower-left corner to add an Apple ID account.

![img/xcode_account.png](img/xcode_account.png)

If you want to use a free developer account, you will simply enter your Apple ID in this section and Xcode will automatically enroll your Apple ID in the free developer program. If you enrolled in the paid account already and have confirmation that your account is active, enter the Apple ID of the paid developer account. The screenshot below shows the labeling of team names based on whether from free account vs. paid account. Free teams will have `(personal team)` after the name.

![img/apple_id.png](img/apple_id.png)

You are now done setting up Xcode.  Great job!  You will not need to redo the account setup steps on any subsequent builds or updates of your Loop app.  Xcode will remember these settings.

## Next Step: Test Settings

Now you are ready to move onto Step 10 to [Test Your Settings](step10.md).
