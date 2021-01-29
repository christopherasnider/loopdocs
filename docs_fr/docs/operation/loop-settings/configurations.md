# Configuration

Cette page couvrira deux parties générales des paramètres de Loop, encerclées en rouge dans la capture d'écran ci-dessous. Les rubriques correspondent à l'ordre d'affichage sur l’écran, de haut en bas.

* La première section encerclée couvre l’état de boucle fermée/ouverte de votre Loop et le rapport de problème de la boucle.

* La deuxième section entourée est la zone de configuration. Cette section contient beaucoup de paramètres vraiment importants qui contrôlent la façon dont votre boucle va calculer votre courbe de glycémie prévue. Compte tenu de l'importance de votre courbe de glycémie prévue pour les actions de Loop, Assurez-vous de lire attentivement cette page pour savoir comment naviguer dans les sélections et les entrées.

![img/configurations.jpg](img/configurations.jpg)

## Boucle fermée/ouverte

Le commutateur de Boucle Fermée contrôle si la Boucle active automatiquement les réglages de basal temporaire recommandés (mode Boucle Fermée) ou si vous devez appuyer manuellement pour activer les recommandations (mode Boucle Ouverte). En plus de l'indicateur visuel de ce commutateur discuté ci-dessous, l'icône d'état de la boucle [sur l'écran principal](displays.md#loop-status) apparaîtra également différemment en fonction du mode sélectionné. Le mode Boucle Ouverte aura un cercle incomplet pour l'icône de statut de la Boucle.

### Mode Boucle Ouverte

![img/open_loop.png](img/open_loop.png)

Lorsque l'interrupteur Boucle Fermée est dans la position (Off&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   ), la Boucle N'INJECTERA PAS automatiquement les Basals temporaires recommandées. Au lieu de cela, la boucle affichera les Basales temporaires recommandées sur l'affichage de l'état principal, juste au-dessus du graphique de glycémie. Ceci est appelé **boucle ouverte**, et est une bonne façon de comprendre comment la boucle va fonctionner, et quel type de recommandations il ferait. Si vous cliquez sur la ligne basale temporaire recommandée en mode boucle ouverte, Loop exécute l'ordre préconisé de le basal temporaire.

### Mode Boucle Fermée

![img/closed_loop.png](img/closed_loop.png)

Lorsque l'interrupteur Boucle Fermée est en position (&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   On ) La boucle INJECTERA AUTOMATIQUEMENT les Basals temporaires recommandés via la pompe à insuline configurée. C’est ce qu’on appelle **la boucle fermée**. En règle générale, Loop affichera le basal temporaire recommandé juste au-dessus du graphique de glycémie avant de l’adopter automatiquement. Il peut prendre une minute ou deux pour que la Boucle promulgue le basal recommandé. Une fois que le basal temporaire a été activé avec succès sur la pompe, le basal temporaire recommandé disparaîtra de l'écran et le nouveau taux de basal temporaire sera représenté dans les graphiques de distribution d'insuline.

## Rapport de problèmes

Si vous rencontrez des problèmes ou des erreurs avec votre Loop, un rapport de problèmes peut être utilisé pour aider à identifier où le problème se produit. Le rapport de problème est généré automatiquement et vous pouvez le partager par e-mail. Souvent, si vous cherchez de l’aide pour un problème technique, un rapport de problème fournira un aperçu pour les développeurs et les dépannages. Veuillez vous envoyer un rapport de problème à chaque fois que vous vous interrogez des comportements ou des affichages de Loop. Vous pouvez ensuite utiliser ce rapport de problèmes plus tard pour aider à déboguer le problème.

!!!info "Avant de continuer plus loin, un mot sur les unités Glycémie"

    Les entrées dans la section de configuration seront disponibles en mg/dL ou mmol/L automatiquement, en fonction de la façon dont vos valeurs de glycémie sont reçues. Par défaut, ils sont définis à mg/dL, cependant une fois que les valeurs CGM arrivent en mmol/L, ces paramètres Loop peuvent être saisis en mmol/L. **Si vous prévoyez d’utiliser du mmol/L, assurez-vous d’attendre de définir vos entrées jusqu’à ce que vous avez commencé à recevoir des valeurs CGM en boucle.** Si vous les faites dans le mauvais ordre, vos graphiques et entrées peuvent avoir des unités incorrectes.

## Plage de Correction

La plage de correction est la plage de glycémie vers laquelle vous voudriez que Loop vous corrige. La plage de correction n’est pas nécessairement la même plage "cible" de glycémie discutée avec votre endocrinologue ; en règle générale, la plage du médecin est beaucoup plus large. Par exemple, vous pouvez garder un objectif de correction de 100-110 que Loop s'efforcera de viser, mais utilisez une plage cible de glycémie souhaitée entre 80-180 lorsque vous en discutez avec votre endo sur « la zone dans la cible ».

![img/premeal_entry.jpg](img/premeal_entry.jpg)

Cliquez sur le + dans le coin supérieur droit pour ajouter des plages de correction de glycémie. Vous pouvez avoir plusieurs plages basées sur l'heure de la journée, mais le premier réglage de la journée doit commencer à minuit.

Les plages de correction peuvent être un nombre unique, comme 100-100 mg/dL, ou une plage telle que 100-120 mg/dL. En général, si vous choisissez d'utiliser une gamme, garder la plage entre 10 et 30 mg/dL entre la valeur la plus basse et la plus élevée est un bon point de départ.

### Plage de substitution

Au-dessous de la zone de correction se trouve une section appelée « Substitution » avec un paramètre Pré-Repas. Pendant son activation, les cibles pré repas remplaceront la plage de correction habituelle pour les recommandations de Basal temporaire de Loop. Si une plage de pré-repas n'est pas entrée dans cette section, l'icône restera grise et inutilisable sur la barre d'outils de l'écran principal.

La cible de substitution avant repas (ou pré-repas) peut être utilisée comme moyen facile d'obtenir une petite quantité d'insuline avant un repas afin d'aider à contrôler les pics de glycémie post-repas.

Si votre cible normale est de 100-110 mg/dL et que la cible avant le repas est de 80-80 mg/dL, par exemple, Loop vous donnera un petit coup supplémentaire pour vous amener au nombre cible inférieur avant le repas. Cette dose d'insuline vous prépare à un repas avec un mini-prébolus. La cible du pré-repas, lorsqu'elle est activée en appuyant sur l'icône, restera active pendant une heure, jusqu'à ce que les glucides soient saisis, ou jusqu'à ce qu'ils soient annulés manuellement... quelle que soit l'action qui a été faite en premier.

La boucle ajustera tous les bolus d'insuline selon les besoins en fonction de l'insuline supplémentaire fournie pendant cette période pré-repas.

## Seuil de suspension

Le seuil de suspension doit être mis en place pour la configuration réussie de Loop. **votre boucle ne deviendra pas verte sans définir cette valeur.** cette valeur affecte à la fois bolus et recommandations basales par Loop.

### Bolus

* Si vous essayez d'injecter un bolus pour un repas alors que n’importe quelle partie de la courbe prévisionnelle de glycémie est en dessous de cette valeur seuil de suspension, Loop ne recommandera pas un bolus.  Au lieu de cela, vous devrez attendre que votre courbe de prédiction soit supérieure à la valeur de seuil de suspension afin de pouvoir faire un bolus.

### Basal

* Si votre point actuel ou n'importe quel point de votre courbe de glycémie prévue est inférieur au seuil de suspension, La boucle recommandera toujours un débit basal temporaire de 0 U/h.

Les paramètres raisonnables pour le seuil de suspension dépendront de la préférence de l'utilisateur, mais il n'est pas recommandé de définir une valeur inférieure à 65 mg/dL.

## Débit Basaux

!!!danger ""

    **Remarque : Vous ne pouvez pas entrer de débits basaux tant que vous n'avez pas ajouté une pompe dans les paramètres de Loop. * Vos débits de basal seront initialement remplis lorsque vous compléterez la partie `Ajouter une pompe` de la configuration au début de ce guide d'installation.

Un seul planning de basal peut être défini dans chaque application Loop. Les incréments de basal sont disponibles en fonction de la precision incrémentale de la pompe/pod que vous utilisez. Toutes les pompes ne fournissent pas les mêmes incréments pour les injections de basal. L'horaire de basal doit commencer à minuit et ne peut pas contenir des taux de 0 U/h.

Pour modifier une ligne dans votre planning de basale, appuyez sur la ligne et ajustez l'heure et/ou le montant.  Pour supprimer une ligne, sélectionnez Modifier en haut à droite et supprimez-la.  Si en appuyant sur la ligne, cela ne fonctionne pas, essayez de fermer et de rouvrir l'application.  Lorsque l'édition est terminée, cliquez sur le bouton `Enregistrer dans la pompe...` ou `Synchroniser avec le Pod` en fonction de la pompe que vous utilisez.

!!!info ""

    Si vous faites des modifications de basal et utilisez le bouton `Annuler` pour retourner au menu sans enregistrer / synchroniser avec succès vers la pompe/pod, les modifications que vous avez apportées ne seront pas enregistrées. La boucle fait de l'enregistrement/synchronisation vers la pomper une étape obligatoire pour éditer correctement les débits de basal. Si vous obtenez un message d'erreur en essayant de sauvegarder/synchroniser les taux de basal modifiés, veuillez réessayer jusqu'à succès.

## Limites d'Administration

Le taux de basal maximum et les paramètres de bolus maximum sont collectivement désignés sous le nom de limites de livraison. Cette section aura d’abord été peuplée lorsque vous avez terminé la `ajouter la Pompe` partie de la configuration vu précédemment. Pour plus de sécurité, similaire à l’horaire basal, vous devez conserver ces valeurs de la même façon à la fois sur l’application Loop et dans les paramètres de la pompe/pod. Si vous modifiez ces paramètres dans l'application Loop, utilisez toujours le bonton `Enregistrer dans la pompe...` ou `Synchroniser avec le bouton Pod` selon la pompe que vous utilisez.

### Débit Basal Maximum

Le débit basal maximal limitera le débit de base temporaire maximal autorisé par Loop pour atteindre votre plage de correction. Typically, Loop users set their maximum basal rate around 3-4 times their highest scheduled basal rate. When you are first beginning to use Loop, it is wise to start conservative (low) in setting your maximum basal rate. If your settings are incorrect in other areas (basal rates, insulin sensitivity, carb ratio, etc), you may need time to identify where settings need to be adjusted. This process is easier if Loop is given less latitude to set high basal rates. Gradually increase your maximum basal rate as your comfort and confidence in Loop increases. If you need help with your settings adjustment, head over to LoopTips for some [initial settings help](https://kdisimone.github.io/looptips/settings/settings/)

#### **Maximum Bolus**

Enter your desired single bolus maximum here. For safety, don't set a maximum bolus limit any higher than your typical large meal bolus.

## Insulin Model

There are four insulin models to choose from; Walsh, Rapid-Acting Adults, Rapid-Acting Children, and Fiasp. If you want to read the nitty-gritty discussion that went into the development of the Rapid-Acting and Fiasp curves (collectively called "exponential insulin models"), you can see that in GitHub [here](https://github.com/LoopKit/Loop/issues/388#issuecomment-317938473).

**We highly recommend selecting one of the exponential insulin models (in other words, not the Walsh model).**

A common new Loop user error is to select Walsh model in order to easily shorten their insulin duration (DIA) to one like they used prior to Looping. This almost invariably leads to insulin stacking. If you would like to read more about why the duration of insulin action is important in Loop vs how you've traditionally used it, please click [here](https://seemycgm.com/2017/08/09/why-dia-matters/) to read a blog post about the subject. In summary, choosing Walsh curve just to shorten your DIA will lead to insulin stacking and less than desired bolusing recommendations.

You can click on each model and see what each model's insulin activity curve looks like, active one selected in blue.

![img/models.jpg](img/models.jpg)

The differences between the three exponential models (two Rapid-Acting and Fiasp) models has to do with the timing of the peak insulin activity timing. Not surprising, since Fiasp is marketed as the "faster acting" insulin. Currently all the exponential models are defaulted to an insulin duration of 6 hours, but the peak activity of the curves differs:

* Rapid-acting adult curve peaks at 75 minutes
* Rapid-acting child curve peaks at 65 minutes
* Fiasp peaks curve peaks at 55 minutes

## Carb Ratios

Click the + in the upper right to add carb ratios for various times of day. Loop works best if you have [tested and optimized](https://kdisimone.github.io/looptips/settings/settings/) your carb ratio settings for accuracy.

!!!info "Beware of other apps writing carbs to Health app"

    If you are using a third-party app (such as Spike or MyFitness) that can write carbohydrates to the phone's Health app, you will need to edit the permissions to make sure Loop doesn't double carb entries.  You should disable the third-party app's permissions in Health so that they can only `read` and not `write`.  See [Carb Entries with Third Party apps](../features/carbs.md#third-party-apps) for more information about this setting.

## Insulin Sensitivities

Insulin Sensitivity Factor (ISF) is the same term as Correction Factor used in some clinics and endocrinology offices. ISF represents the drop in blood glucose levels expected from one unit of insulin. Click the + in the upper right to add insulin sensitivities for various times of day. Loop works best if you have [tested and optimized](https://kdisimone.github.io/looptips/settings/settings/) your ISF settings for accuracy. Insulin sensitivities can change for many reasons including waiting too long to change your infusion set. Loop will not auto-detect changes in ISF.

Incorrectly set ISF is the most common cause of roller coaster BGs for new Loop users. You will need to raise (increase) your ISF value/number to help smooth a roller coaster BG trend. You can read about that topic more over in LoopTips [here](https://kdisimone.github.io/looptips/settings/settings/#3rd-insulin-sensitivity-factor).

## Next Step: Loop Services

You have completed the required configurations and settings in your Loop app. If you have a Nightscout site you'd like to connect Loop to, please continue on to the [Loop Services page](services.md).

If you are not integrating with a Nightscout site and don't want any optional logging services connected, then please proceed to the [Loop's displays page](displays.md). Understanding the Loop displays can be a valuable tool to understanding your Loop's actions, and also for troubleshooting, if you are having issues.
