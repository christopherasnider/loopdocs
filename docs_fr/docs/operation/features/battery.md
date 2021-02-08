# Batterie de la pompe

Un des points de confusion courants pour les nouveaux utilisateurs de Loop est la façon d'interpréter le niveau de batterie de leur pompe si il est nécessaire de changer les piles de leur pompe en fonction des éléments d'information.

## Courbes de décharge

Il y a généralement deux types de piles AAA que nous utilisons dans ces pompes Medtronic : les alcaline ou les lithium.

Pour comprendre les niveaux de batterie de la pompe, vous devez d'abord en savoir un peu sur **les courbes de décharge des batteries**.  Ce n’est pas un concept difficile... en gros, comment une batterie meurt au fil du temps car utilisé ou laissé dans un tiroir.  Plus techniquement, une courbe de décharge de la batterie est la mesure des volts qu'une batterie perd au fil du temps.  Les piles commencent à une tension plus élevée et lentement cette sortie de tension se dégrade au fil du temps (ou à l'utiliser) jusqu'à ce que la batterie ne fournisse plus assez de "ummph" pour maintenir le fonctionnement du gadget électronique.  MAIS, les piles alcalines et les piles au lithium ont des courbes de décharge différentes en raison de la chimie qu'elles contiennent, et les courbes peuvent être légèrement différentes en fonction de l'environnement (température) et du fabricant de batteries.

Les piles alcalines ont une baisse de tension relativement régulière au fil du temps, comme indiqué ci-dessous.  Notez que la forme de la courbe a une durée significative dans la plage de 1,3 à 1,2 volts et une baisse relativement douce à environ 1,2 volts.

![img/alkaline.jpg](img/alkaline.jpg)

Les batteries au lithium ont une sortie de tension beaucoup plus stable au fil du temps, comme indiqué ci-dessous.  Notez que la forme de la courbe est relativement plate pour une grande partie de la durée de vie de la batterie avant de s'éteindre soudainement autour de 1,3 volts.

![img/lithium.jpg](img/lithium.jpg)

Que signifie les informations ci-dessus en termes de fonctionnement de Loop ?  Une batterie au lithium à 1.3v est beaucoup plus proche de sa fin de vie qu’une batterie alcaline à 1.3v.  Il ne vous reste peut-être que quelques heures de fonctionnement quand une batterie au lithium est à 1.3v , mais une batterie alcaline à 1.3v pourrait encore durer plusieurs jours.  Donc, lorsque nous parlons de régler les niveaux d'alarme dans l'un ou l'autre système, votre type de batterie est un élément important à prendre en compte.

## Indicateur de niveau de la batterie de la pompe Medtronic

Si vous lisez la documentation de Medtronic, ils vous diront d'utiliser les piles alcalines Energizer dans leurs pompes.  Pourquoi?  Astuce : la réponse ne veut pas dire que les piles Duracell sont intrinsèquement pires que Energizer ou que les piles au lithium ne fonctionneront pas dans les pompes Medtronic.

**La réponse porte sur la précision de l'indicateur de niveau de la pile de leur petite pompe sur l'écran de leur pompe.**  Medtronic a calibré l'indicateur de niveau de la batterie de la pompe à :

* Piles alcalines Energizer
* Utilisations normales (cad pas avec Loop)
* Températures comprises entre 37°F (3°C) et 104°F (40°C).

En d'autres termes, Medtronic a fait des essais pour voir exactement combien de temps une batterie alcaline Energizer durera en utilisation normale de la pompe et a fait sa propre courbe de décharge.  They programmed their pump battery level indicator to change from 4 bars to 3 bars to 2 bars to 1 bar based on that particular discharge curve.

However, Loop users are slightly more demanding on the pump's battery/voltage than simply delivering insulin.  We are also asking for the pump to perform radio communications, in addition to delivering insulin.  Those radio communications needs a slightly higher voltage than the typical "normal" pump use.  So while a non-Looper might be ok running their pump until a voltage of about 1.12 for insulin delivery, radio communications might stop at a voltage output of about 1.17.  If you experiment with your Looping pump, you'll find Loop will turn red from failed pump comms before the pump actually fails at insulin delivery.  This difference between "failure" voltages needs to be considered when determining how much useful battery life is left for a pump battery.

In summary, that little pump battery indicator on the Medtronic pump screen is ONLY useful if you are:

* not using the pump for Looping,
* using Energizer alkaline batteries, and
* in the temperature environment similar to their testing.

!!!info ""

    Loop users should not rely on their Medtronic pump screen's pump battery indicator, and instead use the Loop's pump battery level indicator.

## Loop's Pump Battery Level Indicator

Keeping the information about battery discharge curves in mind, Loop developers tested various battery brands and types to develop discharge curves for Loop users.  These discharge curves form the basis of the pump battery level indicator found in the top right of the Loop's main display screen and the pump battery notifications provided by the Loop app.  The pump battery level indicator will also report in %.

* For x23 and x54 model users, the Loop's pump battery level will move in 25% increments.
* For x15 and x22 model users, the Loop's pump battery level will move in discrete % increments.

Based on the battery type selected and the pump model being used, the Loop's pump battery level notifications are designed to give the user about 8 hours of notice before pump communications are likely to fail.  The Loop user should have some additional time after pump comms fail before actual insulin delivery would stop.

## Nightscout Pump Battery Display

The Nightscout information regarding pump battery levels will depend on pump model being used.

* If you use an x23 or x54 pump and MySentry, the pump levels are reported as a **percent** to NS, because that's how MySentry reports the data to Loop.  The packets use 100%, 75%, 50%, and 25% increments, and the Loop's main display matches the NS pump display.
* If you use an x22 or x15 pump, the pump levels are reported as **voltage** readings to NS because Loop has to specifically request the voltage reading from the pump.  The Loop's main display will show pump battery level as discrete %, not the individual voltage measurement.
* No matter what pump you are using, you can always get the current pump battery's voltage by using the RileyLink's `Read Pump Status` command.
* The extra communications effort for non-MySentry model pumps will mean slightly shorter battery life vs. MySentry model pumps.

## Nightscout Pump Battery Alarms

The Nightscout alarms are based on the Heroku settings that you have input specifically.  If you don't specifically set them, Nightscout will use the default settings for pump battery alerts as shown below:

![img/pump-ns.png](img/pump-ns.png)

Nightscout pump battery levels, if you leave things at default installation, will not trigger alarms.  If however you add a setting of `PUMP_ENABLE_ALERTS` to `true`, you will receive pump battery notifications according to the levels shown in the parenthesis above.  For example, your x23 pump is reporting its levels in percent, therefore you'd receive a yellow warning alarm at 30% and an urgent red alarm at 20%.  Your x22 pump however is reporting its levels at voltage readings, therefore you'd receive a warning yellow alarm at 1.35v and an urgent red alarm at 1.30v.

!!!info ""

    Are the default NS alarm levels going to work for you?  The answer depends on what type of battery level you are using, what model pump you are using, and how much advance notification you want to receive before needing to change a pump battery.  There is a bit of personal preference and experimentation to finding what works for you.

***For x22 or x15 pump users, the NS alert settings that may need to be adjusted are the ones based on voltage.***

Generally speaking, for a x22 or x15 pump using alkaline batteries, the default NS alarm levels will be too early to be useful and lead you to change out your battery too frequently.  Alkaline batteries can go to low 1.2s or high 1.1s before Looping starts to have communication problems.  How much lower than the default voltage 1.35/1.30 alarm levels you want to go will depend on how far in advance you want to be warned about an upcoming battery change.

If however, you are using a x22 or x15 pump with lithium batteries, the default 1.35v/1.30v alarm levels may be completely appropriate.  Remember how the lithium battery curves at the start of this discussion died off quickly around 1.3v?  You won't get hardly any heads-up notice for a lithium battery if you set the alarm below 1.3v.

***For x23 or x54 pump users, the NS alert settings that may need to be adjusted are the ones based on percentage settings.***

Alkaline and lithium batteries should have automatically had their percentage-remaining based on the correct battery type in your Loop settings.  So, generally speaking the default NS alert levels don't generally need adjusting.  However, if you are using lithium batteries, the drop off between 75% to 25% can be quite dramatic and not be easy to anticipate (especially if the drop happens overnight).

As an alternative method of tracking pump battery changes, you could use the insulin age (IAGE) plug-in to anticipate your pump battery changes as well.  For example, after tracking pump battery life on my 723 using energizer batteries lithium batteries for the last several months, I know that we get about 15 days plus a handful of hours.  The amount of hours more beyond 15 days varies depending on how much we've interacted with the pump buttons directly, whether we've looped the full 15-days solid, and if the pump has been in extreme weather (cold weather can sap pump battery life).  By tracking the pump battery changes with NS's careportal "insulin cartridge change", I can see in advance if we are nearing an overnight on a 15 day battery and decide to change batteries before overnight to prevent any middle-of-night battery issues.

!!!info ""

    - Lithium batteries will get a significantly longer life than an alkaline battery.
    - Experiment and track your particular pump model and battery type to understand what NS settings will work best for you.
    - Do not rely on the pump's on-screen pump battery indicator, especially when using lithium batteries.
