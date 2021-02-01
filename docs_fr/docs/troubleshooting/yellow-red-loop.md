# Boucles rouges

Divisons cette page en deux parties. La première partie traite des boucles rouges individuelles. Comme si cela vient de se produire et que vous voulez le résoudre. La deuxième partie traitera des situations où vous avez à plusieurs reprises et « plus souvent » des boucles rouges et que vous pensez que cela arrive «trop souvent » (les deux bien sûr sont des termes subjectifs).

## Résoudre une boucle rouge

Vous êtes donc là pour retrouver votre boucle verte ? C’est rouge et ça ne marche pas ? Vous vous demandez ce qui se passe? Vous pouvez cliquer sur l’icône de la boucle rouge pour lire un message d’erreur que vous pouvez ou ne pouvez pas comprendre. Si vous le comprenez, super... qui devrait vous aider à résoudre le problème. Si vous ne le comprenez pas, alors il y a deux options pour corriger la boucle rouge ; la première est rapide et facile, la seconde est plus en profondeur. Examinons les deux.

Un petit mot : Ne pas rapidement décider de retirer un omnipod qui ne répond pas et qui a une boucle rouge. Habituellement, le problème est que le RileyLink a besoin d’une réinitialisation comme décrit ci-dessous dans l’option 1, plutôt que le pod devant être changé. Si vous ne corrigez pas le problème du RileyLink en premier, Le problème sera probablement present à la nouvelle tentative d'appairage de pod et vous aurez un tas de problèmes d'appairage du nouveau pod parce que le RileyLink ne fonctionne toujours pas. Alors, s'il vous plaît essayer de faire fonctionner le RileyLink correctement avant de décider d'abandonner une pod à cause d'une boucle rouge.

### Option 1 : Étapes faciles

!!!danger ""

    Vous ne vous souciez guère de l’origine du problème, vous voulez juste passer à autre chose aussi rapidement que possible? Ok, très bien, alors procédez comme suit:

    * Éteignez votre RileyLink à son interrupteur d'alimentation physique situé sur le côté du RileyLink. Utilisez un petit objet pointu pour déplacer soigneusement le curseur du port de chargement, puis remonter vers le port de chargement. Un trombone sur le porte-clés peut fournir l’aide dont vous avez besoin pour atteindre l’interrupteur dans le boîtier encastré, et a un double usage comme un outil [anti cri pour les pod](../../faqs/omnipod-faqs/#what-do-you-do-to-stop-a-screaming-pod).
    * Fermez votre application Loop (en la faisant glisser vers le haut dans le sélecteur d'applications de l'iPhone) et rouvrez-la.


    ![../img/riley-switch.png](img/riley-switch.png) </br>

    C'est à peu près tout ce que vous avez à faire pour l'option 1 pour restaurer une boucle verte en 5 minutes, 99% du temps. Vous pouvez confirmer que les choses sont de retour au boulot en revoyant une boucle verte et/ou en émettant une "commande de test" ou "presser des boutons" avec succès dans le menu RileyLink.

### Option 2 : Chercher la cause

!!!info ""

    Donc, si l’option 1 n’a pas fonctionné pour résoudre votre problème ... ensuite, vous aurez besoin de regarder un peu plus profondément. Il peut y avoir une variété de raisons pour lesquelles l'option 1 n'a pas fonctionné pour restaurer la fonction de votre boucle, pour que vous ayez besoin de remonter à l'origine du problème. Il y a quelques catégories de base :

    1. RileyLink est cassé
    2. Les valeurs MGC ne sont pas récupérées par Loop
    3. La pompe ne répond pas

## RileyLink est cassé

Comment pouvez-vous savoir si votre RileyLink a un problème? La réponse est principalement dans les lumières LED qui s'affichent sur le carte.

**Voyant rouge**: s'allume pendant la charge et s'éteindre/s'allumera périodiquement, alors qu'il est toujours branché, une fois la charge terminée.

**Voyant vert**: indique une connexion BT active avec le téléphone. Vous voulez que la lumière vert reste allumée tout le temps sur le RileyLink. Si le voyant vert n'est pas allumé, assurez-vous que le Bluetooth de votre iPhone est toujours activé.

**Lumière bleue**: La lumière bleue clignotera périodiquement lorsque le RileyLink et la pompe communiquent activement. Elle ne devrait PAS être allumée en continue. Si votre lumière bleue est bloquée, c'est une indication d'un problème sur la carte. Essayez de chercher des signes de dommages ou de débris qui peuvent causer un court circuit sur la carte. Nettoyez la planche avec de l’alcool [(débranchez d’abord la batterie](https://youtu.be/s2qNPLpfwww)). Si vous ne pouvez toujours pas éteindre la lumière bleue, contactez GetRileyLink pour obtenir un nouveau RileyLink.

## Les valeurs MGC ne sont pas récupérées par Loop

### Nouveau transmetteur

Si vous avez récemment modifié un émetteur, vous devez également mettre à jour les paramètres de votre Loop pour refléter le nouvel iD de l’émetteur. Allez à la section MGC des paramètres de Loop et `Supprimer le MGC` (c'est un bouton au bas de cette page). Puis, utilisez le `Ajouter le MGC` dans les paramètres de boucle pour inclure le nouvel identifiant du transmetteur.

### Émetteur de style Firefly

Si vous n'avez pas mis à jour votre application Loop depuis fin Juillet 2019 et que vous utilisez Dexcom G6, vous devrez mettre à jour votre application Loop pour pouvoir continuer à boucler sans connexion internet. En juillet 2019, nous avons commencé à voir sur le marché un nouveau style d'émetteurs Dexcom G6. Ces nouveaux émetteurs ont besoin d'un remaniement de certains codes de Loop pour continuer à « espionner » l'émetteur. Sans la mise à jour, votre Loop n'obtiendra pas de données MGC à moins qu'elle n'utilise celles des serveurs Share (ce qui n'est pas un mode de fonctionnement recommandé). Donc, mettez à jour votre application Loop si vous avez un nouveau type d'émetteur et que vous n'avez pas mis à jour depuis juillet 2019.

### Supprimer le compte Share

En fait, nous voyons beaucoup d'erreurs signalées parce que les gens ont des problèmes avec leurs informations de serveur de partage dans l'application Loop. **Veuillez supprimer les informations de votre compte de partage dans les paramètres de Loop.** En d'autres termes, la partie d'identification des informations du compte de partage, comme indiqué dans la capture d'écran ci-dessous, devrait dire `Appuyer pour définir` et ne pas avoir les informations de votre compte. Il est inutile de remplir cette portion car la recuperation en local et non via Internet d'un émetteur est de toute façon la source de MGC préférée. In fact, by leaving this information out, it will help you remember to change your transmitter ID when you change transmitters because CGM data won't appear in Loop. By not including Share account in Loop, you will prevent yourself from accidentally becoming internet dependent.

![../img/no-share.jpg](img/no-share.jpg)

## Pump is not responding

The obvious fix is to make sure the RileyLink is not so far away from the pump or Pod that they cannot communicate. Assuming you've addressed this, then you can move on to other steps. For Pod Loopers, Option 1 almost always fixes this issue. For Medtronic Loopers, you will see some times where the pump is not responding and you may see "decoding" errors or various other messages about pump responses. For Medtronic users, try the following:

1. Change pump battery. Low pump battery will cause radio communications to fail.
2. Use the `Change Time` command in the RileyLink menu to update the pump's clock. If you've accidentally changed the pump's time in the pump itself, this will get the Loop app and pump back in sync.
3. If using a x23 or x54 pump, try deleting all the IDs under the "Other Devices" submenu in the pump's "Connect Devices" menu.  Then go to the RileyLink menu and use the MySentry pairing command to get a fresh ID issued. Follow the directions listed in the MySentry pairing command's screen to scan for devices. A fresh ID can help prevent recurring red loops for x23 and x54 users, particularly if they started to occur after a recent Loop update.
4. Make sure the following are checked in the pump:
    * Your pump cannot be suspended.  Resume insulin deliveries.
    * Temp basal type must be set to unit/hour, not percent, in pump's Basal menu.

## Resolving Frequent Red Loops

Here's some things to check if you have frequent red loops:

* Have you [cleaned your mLab database in Nightscout](../nightscout/mlab_cleanup/) recently? If your database gets backlogged (or Nightscout otherwise isn't working properly), Loop can get clogged up with a bunch of unfinished Nightscout uploads. This clogged condition can cause red loops. So, make sure you are periodically checking your mLab and cleaning it. Try deleting your Nightscout account from Loop settings and see if your Loop stops having red loops. If it does, then you'll need to assess what's going wrong in your Nightscout site and fix it. Most of the time that is your mLab database cleanup needing to be done.

* Is your [RileyLink battery plugged in all the way](../build/step5.md#assemble-rileylink) on the board?

* Has your RL been fully charged? Try charging your RL for an hour or two, make sure the red light comes on while charging. Try a new charger.

* Oddly, some people have found that turning off Siri integrations for Loop and Dexcom apps in your iPhone settings has helped. I don't know if this is coincidental or an actual help yet, but I'll mention it here.

* Check for sources of wireless interference. If you have a certain environment that seems to have more drops than others, it is likely that there is a source of wireless communication interfering with your Loop. Lots of Medtronic Loopers in a room together will often interfere with each other and get "cross-talk" red loop error messages. If it is a bedroom at night causing problems, try moving other wireless devices such as routers or baby monitors farther away from where you and your RileyLink are.

## Posting for Help

Before you post on Looped group for help with a red loop, please make sure you've tried Option 1 and have restarted your RileyLink and Loop app.

Before you post for help, please also check your mLab and Nightscout status. This step is often overlooked and yet solves a lot of problems.

When posting for help, include two screenshots of Loop's main screen; one with the red loop's error message and the other just the plain Loop main screen. Include a detailed description of what you have tried doing from the troubleshooting list above. For example, state if you've double checked the transmitter ID, deleted the Share account info from Loop settings, and updated your Loop app since July 19, 2019 so that we can rule out some of the causes of CGM issues.
