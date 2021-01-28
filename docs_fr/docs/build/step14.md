# Étape 14 : Créer l'application Loop

!!!danger "Temps estimé"
    - 60-80 minutes si c'est la première fois
    - 10-15 minutes si c'est une compilation répétée

!!!info "Résumé"
    - Ouvrez le code Loop que vous avez téléchargé dans [l'étape 13](step13.md)
    - Connectez le téléphone à l'ordinateur
    - Réglez le téléphone pour ne pas se verrouiller pendant un certain temps
    - Faire confiance à l'ordinateur (sur le téléphone)
    - Sélectionnez votre téléphone dans la liste des appareils
    - Enregistrer l'appareil
    - Signer les 4 cibles
    - Appuyez sur le bouton build
    - Entrez le mot de passe de l’ordinateur quatre fois pendant la construction (si c’est votre première génération)
    - Regardez avec admiration car vous venez de construire votre propre application Loop

!!!warning "FAQs"
    - **« J'ai une erreur de compilation ! Aïe... que dois-je faire?"** consultez la page [Erreurs de compilation](build_errors.md) pour toutes les solutions dont vous avez besoin.
    - **« La construction semble prendre beaucoup de temps, est-ce normal ? »** Oui, la première version d'un nouveau téléchargement prendra beaucoup de temps. Juste soyez patient... une des étapes de construction pour prendre *beaucoup* de plus que tous les autres. Le processus de compilation se termine toujours par un message de succès ou d'échec, alors attendez qu'il s'affiche jusqu'à ce que vous voyez l'un des messages affichés.

## Ouvrir le projet Loop dans Xcode

Allez dans votre dossier Téléchargements, ouvrez le dossier de code Loop téléchargé et double-cliquez sur Loop.xcodeproj. Si vous avez téléchargé la branche de développement, votre dossier s'appellerait `Loop-dev` et de même pour le téléchargement de `Loop-master`.

![../img/build_button.png](img/loop_code.png)

Un avertissement peut apparaître vous demandant si vous voulez vraiment l'ouvrir, cliquez sur Ouvrir. Xcode va s'organiser, cela peut prendre quelques minutes.

![img/loop_open.jpg](img/loop_open.jpg)

Une fois l'indexation terminée, les différents dossiers et fichiers du projet Loop apparaîtront dans la colonne de gauche. Nous allons maintenant faire trois séries de clics importants:

1. Premier clic : En haut de tous les dossiers et fichiers listés, cliquez sur le "Loop" bleu. Cela va remplir la partie centrale de la fenêtre Xcode avec quelques informations. **Si quelques petites boîtes apparaissent en disant « Le dossier « DerivedWatchAssets.xcassets » n’existe pas. » ... il suffit de cliquer sur les boutons ok et les ignorer. Ils apparaitreront plusieurs fois pendant votre compilation si vous utilisez la branche de développement en ce moment...ne vous inquiétez pas, ne sera pas un problème.**

![img/loop-first-click.png](img/loop-first-click.png)

2. Deuxième (ensemble de clics) : cliquez maintenant sur la case de l'écran du milieu pour révéler la colonne des Projets et Cibles sous cette boîte. Les quatre objectifs que nous allons signer dans les prochaines étapes sont maintenant facilement visibles. Maintenant, cliquez également sur la cible Loop comme indiqué dans la capture d’écran ci-dessous. Il sera surligné en bleu pour vous dire qu'il est sélectionné. Loop, Loop Status Extension, Watch App, and WatchApp Extension sont les cibles qui nous intéressent.

![img/loop-second-click.png](img/loop-second-click.png)

3. Troisième clic : Avec la cible Loop sélectionnée, cliquez sur les "Signing & Capabilities" près du haut de l’écran (dans les onglets). Après avoir cliqué sur cela, vous devriez voir une section « Signing » qui occupe la majeure partie de votre fenêtre centrale. Si vous avez manqué la section "Signing & Capabilities" et que vous n'avez pas trouver ou cliquer pour voir cette partie...cela signifie que vous avez manqué la mise à jour vers Xcode 11 à partir d'une ancienne version de Xcode. Veuillez revenir en arrière et mettre à jour Xcode maintenant. Merci.

![img/loop-third-click.png](img/loop-third-click.png)

## Connectez votre iPhone à l’ordinateur

Connectez votre iPhone par câble à l'ordinateur, sélectionnez votre iPhone en haut de la liste déroulante.  Votre **nom personnel de l’iPhone** devrait être en haut de la liste. Ne sélectionnez pas accidentellement les simulateurs génériques iOS listés sous le nom de votre iPhone.

!!!info "Conseils utiles"

    - Si votre iPhone est verouillé, Xcode ne sera pas en mesure d’installer l’application Loop qu'une fois que votre téléphone est déverrouille pendant la progression de la compilation.  Veuillez désactiver temporairement le verrou jusqu'à ce que vous ayez terminé la construction de l'application Loop.  Allez dans les paramètres de votre iPhone >> Affichage & Luminosité >> Verrouillage automatique et définissez-le sur `Jamais`.  Vous pouvez réactiver votre verrouillage une fois que Loop est installé sur le téléphone. Si vous ne pouvez pas ou ne voulez pas régler le verrouillage automatique à jamais, alors s’il vous plaît n’oubliez pas d’appuyer sur l’écran de votre téléphone périodiquement pendant le processus de construction pour le garder « éveillé ».</br></br>
    - Si c'est la première fois que votre iPhone est branché sur cet ordinateur, vous devrez ouvrir l'iPhone et sélectionner "Faire confiance à cet ordinateur" avant que votre appareil soit utilisable dans la sélection du menu.</br></br>

!!!danger "Erreur la plus courante"

    - L'erreur la plus courante dans cette étape est de ne pas sélectionner votre téléphone comme indiqué dans la deuxième capture d'écran ci-dessous. La liste par défaut n’est qu’un nom de modèles de téléphones généraux rattaché à la partie « simulateurs iOS »... ne vous y trompez pas. Votre téléphone ACTUEL sera au-dessus de la liste des différents modèles de téléphones du simulateur.  Vous devrez peut-être faire défiler vers le haut de la liste afin de le voir.  Assurez-vous de sélectionner votre téléphone actuel, pas seulement un modèle de téléphone de simulateur.

![img/select_device.png](img/select_device.png)

![img/your_device.png](img/your_device.png)

## Signer les 4 cibles (targets)

Une fois que vous avez sélectionné votre appareil (nom de votre iPhone), nous sommes prêts à signer les quatre cibles. Nous commencerons par la cible Loop, la première sur la liste des cibles.  Dans la zone « Signing », assurez-vous d’avoir « All » sélectionnés près du haut, puis sélectionnez le menu défilant où on peut lire actuellement « aucun ». Choisissez votre équipe avec qui vous souhaitez signer. Si vous sélectionnez un nom d’équipe avec (équipe personnelle/personal team), votre application expirera dans 7 jours. Si vous sélectionnez un nom d'équipe sans (équipe personnelle/personal team), votre application durera une année complète.  Si vous ne vous êtes jamais inscrit à un compte de développeur gratuit, vous n’aurez pas d’affichage (équipe personnelle/personal team). Assurez-vous de garder la case "Gérer automatiquement la signature/Automatically manage signing" cochée au-dessus de la zone de sélection de l'équipe.

![img/team.png](img/team.png)

Une fois que vous aurez choisi votre équipe de signature, Xcode générera automatiquement des profils d’approvisionnement et des certificats de signature.  Si c'est la première fois que vous construisez sur cet iPhone avec ce compte développeur, vous pouvez être invité à enregistrer l'appareil.  Il vous suffit de cliquer sur le bouton « Enregistrer l'appareil » pour confirmer.

![img/register_device.png](img/register_device.png)

!!!danger "Utilisateurs du compte développeur gratuits: LISEZ-MOI

    Si vous utilisez un compte développeur gratuit pour signer vos cibles, vous devrez faire une étape supplémentaire. En tant que développeur gratuit, il vous est interdit de construire des applications qui ont des fonctionnalités de notification Siri ou push intégrées. Loop a ces deux capacités... vous devrez donc les désactiver avant de procéder à la signature et à la construction de votre application. La fonction de notification push est utilisée pour définir les remplacements à distance ; la désactivation n'affectera pas les notifications normales (comme celles pour Loop qui n'arrive pas à effectuer sa boucle). Cliquez sur le petit x à côté de Siri et poussez les lignes de notification situées au bas de votre page Signing & Capabilities. Vous devez le faire à la fois dans les parties de l'extension Loop et WatchApp.
    
    <p align="center">
    <img src="../img/siri-errors.png" width="750">
    </p>

Une cible signée avec succès aura un profil d’approvisionnement et un certificat de signature similaire à la capture d’écran ci-dessous.  Cliquez sur chacune des trois cibles restantes, et répétez les étapes de signature en choisissant le même nom d'équipe que vous avez sélectionné dans la première cible.

![img/success.png](img/success.png)

## Personnalisations du code

**Nouveaux utilisateurs de Loop**: Les personnalisations ne sont pas une partie nécessaire pour la construction de Loop. Au fur et à mesure que vous gagnerez de l'expérience dans la façon dont vous utilisez votre application Loop, vous voudrez peut-être personnaliser certaines fonctionnalités. Vous pouvez toujours mettre à jour votre application Loop pour ajouter des personnalisations ultérieurement. En fait, construit dans les normes, l’installation par défaut est très bien.

Si vous souhaitez des configurations personnalisées pour vos applications Loop ou Loop Apple Watch, il est maintenant temps de les réaliser avant de terminer avec la dernière étape de l’installation Loop sur votre iPhone. Suivez les instructions étape par étape sur la page [Personnalisations du Code](code_customization.md). Si vous êtes une personne familière avec la langue Swift d'Apple, n'hésitez pas à faire vos propres personnalisations.

Lorsque vous aurez terminé vos personnalisations, revenez à cette section et continuez avec le reste de la construction.

## Associez votre Apple Watch

**Nouveaux utilisateurs d'Apple Watch**: Si vous avez une montre Apple neuve et que vous voulez l'utiliser avec Loop, il faut deja activer le pairage de la montre avec l'iPhone avant de passer aux étapes suivantes.  Si vous obtenez une nouvelle montre après avoir construit l'application Loop, vous devrez refaire votre version Loop. (Don't worry, it's as easy as pressing play on your saved Loop project.)</br>

**Existing Apple Watch users**: Please update your watchOS prior to building the Loop app.  The current version of Loop requires watchOS 4.1 or newer.

## INTERMISSION

STOP STOP STOP

You guys...this is about safety.

People keep ignoring this advice and I'm frankly a little stumped as to why. So, I'm moving this advice up in the process so that you don't ignore it. ![alt](https://media.giphy.com/media/xT9DPJVjlYHwWsZRxm/source.gif)

!!!warning "DO NOT WING THE SETUP"

    I have warnings all over these instructions to **continue to use these docs to finish setting up your app after it builds. DO NOT IGNORE THAT ADVICE. DO NOT ENTER ONE LOOP APP SETTING WITHOUT HAVING THE DOCS OPEN AND FOLLOWING ALONG AT THE SAME TIME.**

The section in these docs called "Set up App" (See it? Look for it now...at the top of your webpage) needs to be used to input all the settings in your Loop app when it is done building. READ ALONG WITH THE DOCS to enter those settings. There are important safety tips and advice in there. And then after you finish setup, you need to read the "Operate" section...like BEFORE YOU OPERATE LOOP. Don't bolus for a meal, or enter a meal, until you've read through the Operate section.

I'm worried you will fail to heed the advice about using the setup and operate sections. People have ignored it before. They skim read and think that's good enough. DO NOT BE LIKE THAT. Read each section.

BUT, to mitigate the inevitable people who will ignore that advice....here's the two most important safety tips that I feel obliged to present out of order because (damn it), people will ignore my advice still.

!!!warning "TOP TWO SAFETY MISTAKES YOU SHOULD AVOID"
    1. DO NOT ENTER SETTINGS YOU ARE UNSURE OF. If you don't know your settings or know what the terms mean, stop. Read the docs, all the settings entries are explained there. Ask your endo if you don't have established values for those settings. Don't just guess an ISF, carb ratio, basal rate, or maximum delivery limits.</br></br>

    2. DO NOT ENTER ACCIDENTAL DUPLICATE CARB ENTRIES. When you enter a meal in Loop and press the `save` button...those carbs are saved. Let me repeat: THOSE CARBS ARE SAVED...even if you cancel the bolus for them. This is an automated insulin delivery system and if it thinks you have carbs on board, it will try to give you appropriate insulin for those carbs. Most common new user mistake: enters a meal, saves the carbs, has a change of heart or gets confused, and cancels the bolus screen...thinking they've just canceled the entire meal entry. Then they enter in a new carb entry. AND NOW, when you go to bolus...you'll be bolusing for the meal you wanted AND the meal you are mistakenly thinking you had "canceled". You didn't cancel that carb entry though, you had only canceled the bolus...you didn't "unsave" the carbs. If you make a mistake or change your mind on a carb entry after you pressed save, then tap the green carb chart in Loop's main display and edit or delete that entry. **CANCELING A BOLUS DOES NOT CANCEL THE CARB ENTRY THAT GOT YOU THERE. You must delete or edit a saved carb entry if you no longer want Loop to provide insulin for it.**

Ok, so now that I've got your attention, you can continue on with the last step in building you app...but remember, we just pinky swore that you would use the setup and operate sections to finish this all? Don't break my heart, keep your promise.

## Build Loop

Have you signed the four targets? Are you all done with any customizations? Has your Apple watch been paired and updated? Is your iPhone unlocked and plugged into the computer?

Let’s finish the installation of the Loop app onto your iPhone. Double-check to make sure your iPhone's name is still selected and then press the “build” button to start Xcode on its way.

![img/build_button.png](img/build_button.png)

You’ll see the progression of the build in the status window (top middle of Xcode). New builds can take about 40-60 minutes depending on the speed of the computer and the internet.  **Just be patient.**  The progress will get "stuck" on one step/task for a very long time, and then the others will fly by when that one slow step is done. Not every step is equal in duration. Do not give up on the build. <u>**Xcode will ALWAYS tell you eventually that the build either succeeded or failed via a short (self-disappearing) pop-up message on the computer display. If you miss the message, you can look at the top of the Xcode window to see a "Running Loop..." (success) or "Build Failed" (failure) message where the step progress was previously counting down.**</u>

!!!danger "Are you the impatient type?"

    If you just simply can't bear the uncertainty of not seeing that things are progressing, you can take a peek "under the hood" and watch the individual build steps by clicking on the report navigator icon and then the build row at the top of the list. You can watch the slow list of scheme building while you wait.
    
    <p align="center">
    <img src="../img/build-scheme.png" width="650">
    </p></br>

!!!info "First-time builders"

    Be aware though! Sometime during your first ever build on a computer, be ready for a codesign/keychain access prompt that you will see part-way through the build process.</br></br>
    
    <p align="center">
    <img src="../img/keychain-prompt.png" width="350">
    </p></br>
    
    This prompt above, when you see it, requires you to enter your computer password and then select "Always Allow". Normal behavior, this prompt will come up four times in a row even after you enter the correct password. In frustration, people think the prompt must be broken because it keeps reappearing and then people will press deny or cancel. **Don't press deny.** Keep entering your computer password and pressing the "Always Allow" button...as many times as it takes (four times to be exact; one for each target that Xcode is saving the password for). After four times of successful password entry, the build will keep proceeding.

!!!warning "While I have you here..."

    While I have you here, I'm going to give you a piece of Loop troubleshooting advice for once you start looping. This is a little out of order, but too many people miss this super simple **troubleshooting step when their Loop turns red**. Try turning your RileyLink off/on at its physical switch on the side of the case. Carrying a paperclip on the keychain can help you access that recessed switch. The other useful troubleshooting step is to simply close the Loop app (upswipe in iPhone app selector) and reopen it. Wait 5 minutes after each of these steps and see if your issue resolves. It usually will. Don't forget to do these two simple steps to get back to a green loop.  For more red loop troubleshooting, you can check out [this page](../troubleshooting/yellow-red-loop.md).
    
    Also, be aware that there's a **troubleshooting page for Pod pairing** issues, too. If you run into any issues during Pod pairing, PLEASE make sure to read [this page](../troubleshooting/pod-pairing.md) to save yourself from wasting Pods unnecessarily.
    
    Ok, back to the building instructions.

## Build Finished

!!!info "First time building on a new device?"

    If this is the first time you have installed an app on your iPhone using your developer account, you may get a warning like below after a successful build. Don't worry, Loop usually installed just fine on the phone but needs you to do an extra step on the phone before Loop app can open. Just follow the directions shown in the warning for what you need to do on your iPhone. Go to Settings->General->Device Management (or profiles, Profiles & Device Management on newer iOS) and enable trust for your Developer Account. If you are missing the Device Management/Profiles option in your iPhone settings, then head over to [this Build Error section](build_errors.md#device-management-could-not-launch-loop) to find the solution.
    
    <p align="center">
    <img src="../img/trust_device.jpg" width="750">
    </p>

!!!danger "BUILD SUCCEEDED"

    Congrats! If the build is successful, you'll see the message or "Running Loop..." across the top of the Xcode window. Your brand new Loop app will have a screen open immediately on the iPhone asking about allowing Loop notifications and Health App access. `Allow` Loop to send you notifications. In the next screen that follows that, click on the `Turn All Categories On` line and then click `Allow` in the upper right corner.
    
    
    <p align="center">
    <img src="../img/health-start.JPEG" width="450">
    </p></br></br>
    
    **You can unplug your phone from the computer now.** And like we promised earlier, you will use the [Setup App section of this website](../operation/overview.md) to keep proceeding safely.

!!!warning "FAQ: But what about those yellow alerts that remain in Xcode? Should I worry about them?"

    If you see yellow alerts after your build is done...those are not an issue. Whether your build succeeded or failed...the yellow warnings play no role in either outcome. Don't try to resolve them or fret about them. They mean nothing to the successful use of your Loop app.
    
    <p align="center">
    <img src="../img/yellow-warnings.png" width="750">
     </p>

!!!danger "BUILD FAILED"

    Don't despair. Build failures are pretty easily fixed. If you get a message that your build failed and see **RED ERROR** messages, just go to the [Build Errors](build_errors.md) page to find the steps to fix your build error based on the message displayed.
    
    
    <p align="center">
    <img src="../img/general-error.jpg" width="750">
    </p>

## Summary

If your build failed, you need to proceed to the [Build Errors](build_errors.md) page to find the solution. Please head there to find the help you need.

If no build errors, you're done building your Loop app...

![alt](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)

## Next steps

Remember your promise though? You still owe me that you will use the [`Setup App`](../operation/overview.md) section of this website now to keep proceeding safely.
