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

La plage de correction est la plage de glycémie vers laquelle vous voudriez que Loop vous corrige. La plage de correction n’est pas nécessairement la même plage "cible" de glycémie discutée avec votre endocrinologue ; en règle générale, la plage du médecin est beaucoup plus large. For example, you may keep a correction target of 100-110 for Loop to aim to, but use a desired BG target range of 80-180 when discussing things with your endo about "time in range".

![img/premeal_entry.jpg](img/premeal_entry.jpg)

Click the + in the upper right corner to add correction BG range(s). You can have multiple ranges based on time of day, but the first setting of the day needs to begin at midnight.

Correction ranges can be a single number, such as 100-100 mg/dL, or a range such as 100-120 mg/dL. Generally speaking, if you choose to use a range, keeping the range between about 10-30 mg/dL between the lowest and highest value is a good starting place.

### Override Ranges

Below the Correction Range entry is a section called "Overrides" with a Pre-Meal setting. While active, the pre-meal targets will replace the usual correction range for Loop's temp basal recommendations. If a pre-meal range is not entered in this section, the icon will remain grey and unusable on the main screen's toolbar.

The pre-meal override target can be used to as an easy way to get a small amount of insulin delivered before a meal in order to help control post-meal blood glucose spikes.

If your normal target is 100-110 mg/dL and pre-meal target is 80-80 mg/dL, for example, Loop will give you an extra push to get you to the lower target number before the meal. This early insulin brings you into the meal with a mini-prebolus. The pre-meal target, when activated by pressing on the icon, will stay active for one hour, until carbs are entered, or until it is manually cancelled...whichever comes first.

Loop will adjust any insulin bolus as needed based on the extra insulin provided during this pre-meal time.

## Suspend Threshold

The suspend threshold must be set up for successful configuration of Loop. **Your Loop will not turn green without setting this value.** This value affects both bolus and basal recommendations by Loop.

### Bolus

* If you are trying to bolus a meal while any part of the predicted BG curve is below this suspend threshold value, Loop will not recommend a bolus.  Instead, you will need to wait until your prediction curve is above the suspend threshold value in order to bolus.

### Basal

* If your current or any point on your predicted BG curve is below the suspend threshold, Loop will always recommend a temporary basal rate of 0 U/hr.

Reasonable settings for suspend threshold will depend on user preference, but recommended not set lower than 65 mg/dL.

## Basal Rates

!!!danger ""

    **Note: You cannot enter basal rates until you first add a pump in Loop settings.** Your basal rates will be initially populated when you walk through the `Add Pump` part of the setup at the beginning of this setup guide.

Only one basal schedule may be set in each Loop app. The basal increments are available according to the increments of the particular pump/pod you are using. Not all pumps provide the same increments for basal deliveries. Basal schedule must start at midnight and cannot contain rates of 0 U/hr.

To edit a line in your basal schedule, tap the line and adjust the time and/or amount.  To remove a line, select Edit in the top right and delete it.  If tapping the line doesn't work, try closing and re-opening the app.  When finished editing, click on the `Save to Pump...` or `Sync With Pod` button, depending on which pump you are using.

!!!info ""

    If you make any basal edits and use the `Cancel` button to go back to the menu without successfully saving/syncing to pump/pod, the changes you made will not be saved. Loop makes saving/syncing to pump a mandatory step to successfully editing basal rates. If you get an error message while trying to save/sync the edited basal rates, please retry until successful.

## Delivery Limits

The maximum basal rate and maximum bolus settings are collectively referred to as Delivery Limits. This section will have been initially populated when you finished the `Add Pump` part of the setup previously. For safety, similar to basal schedule, you must keep these values the same on both the Loop app and within the pump/pod settings. If you edit these settings in Loop app, always use the `Save to Pump...` or `Sync With Pod` button, depending on which pump you are using.

### Maximum Basal Rate

Maximum basal rate will cap the the maximum temporary basal rate that the Loop is allowed to enact to meet your correction range. Typically, Loop users set their maximum basal rate around 3-4 times their highest scheduled basal rate. When you are first beginning to use Loop, it is wise to start conservative (low) in setting your maximum basal rate. If your settings are incorrect in other areas (basal rates, insulin sensitivity, carb ratio, etc), you may need time to identify where settings need to be adjusted. This process is easier if Loop is given less latitude to set high basal rates. Gradually increase your maximum basal rate as your comfort and confidence in Loop increases. If you need help with your settings adjustment, head over to LoopTips for some [initial settings help](https://kdisimone.github.io/looptips/settings/settings/)

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
