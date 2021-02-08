# Notifications de Loop

Loop fournit des notifications sur l’iPhone et la Watch qui apparaîtront sur l’écran (verrouillé) et vibreront, en fonction de vos paramètres de notification de Loop.

## Omnipod

<font color ="orange">**Omnipod**</font>  
La plupart des alarmes sonores sont désactivées pour une utilisation beaucoup plus discrète de l'omnipod. Seuls les accusés ou alarmes audibles suivants sont actuellement utilisés :

- Reconnaissance du pod activé lors du remplissage du pod avec suffisamment d’insuline lors de l’appariement d’un nouveau Pod.
- Alerte d'expiration du pod à 72 heures/3 jours (que vous pouvez désactiver dans les [paramètres de statut du pod](../loop-settings/omnipod-pump.md#status))
- Réservoir vide du Pod (que vous pouvez couper en silence dans les paramètres de statut du pod [](../loop-settings/omnipod-pump/#status))
- Reconnaissance de désactivation du Pod
- Alarme de panne de pod (également appelé hurleur) lorsque vous atteignez la vie maximale du Pod : 80 heures (3 jours + 8 heures) ou si une défaillance/occlusion se produit. (que vous pouvez réduire au silence en utilisant la commande [remplacer le pod](../loop-settings/omnipod-pump.md#pod-commands)) dans la page des paramètres du pod)

## Paramètres des notifications

Vous pouvez personnaliser le comportement des notifications de Loop dans l'application Réglages de l'iPhone :

![img/iphone-settings-notifications.png](img/iphone-settings-notifications.png)

Paramètres de Loop:

![img/iphone-notifications-loop.png](img/iphone-notifications-loop.png)

## Défaillance de Loop

À 20, 40, 60 et 120 minutes, il y a une notification de défaillance de Loop. Cela se produit principalement lorsque la connexion est perdue pendant une longue période entre le MGC ou le Rileylink et Loop.

![img/loop-failure.png](img/loop-failure.png)

## Échec de Bolus

Si Loop détecte qu’un bolus n’a pas pu être livré, il fournira une notification.  Les défaillances de Bolus sont généralement dues à des données de pompe périmées.  Essayez d’obtenir l’historique récent du menu RileyLink pour mettre à jour les données de la pompe.  Loop notifiera également les injections partielles de bolus.

![img/loop-bolus-failure.png](img/loop-bolus-failure.png)

## Niveau réservoir bas
<font color ="orange">**Medtronique**</font>  
À 20% et 10% de volume restant, il y a une notification de réservoir faible.
<font color ="orange">**Omnipod**</font>  
À <30U, <20U, <10U

![img/pod-reservoir-10U.png](img/pod-reservoir-10U.png)

## Réservoir vide

Loop avisera lorsque le réservoir est vide. Loop vous avertira chaque minute avec cette notification.
<font color ="orange">**Omnipod**</font>  
Normalement, vous aurez 5-30 minutes pour remplacer la nacelle, mais vous savez que la nacelle peut [crier](https://soundcloud.com/eelke-jager/1f-nibble-f) à tout moment à partir de ce point.

![img/loop-reservoir-empty.png](img/loop-reservoir-empty.png)

## Expiration du Pod (Omnipod)

Vous pouvez personnaliser l'heure de notification quand vous remplacez votre pod à tout moment de 1 heure à 71 heures (3 jours - 1 heure) [après avoir lancé un nouveau pod](../loop-settings/omnipod-pump.md#expiration-reminder) ou changer l'heure plus tard dans les [paramètres de configuration du pod]. /loop-settings/omnipod-pump.md#configuration). L'alarme d'expiration sonnera toujours lorsque le pod atteint un total de 3 jours (72 heures) que vous pouvez faire taire [dans les paramètres d'état du pod](../loop-settings/omnipod-pump.md#status).

![img/pod-expiration-notice.png](img/pod-expiration-notice.png)

## Batterie Faible (Medtronic)

Loop avisera quand il reste environ 8-10 heures d’autonomie de batterie.

## Notifications distantes

Loop n’a pas de notification à distance vers d’autres appareils.  Si vous êtes un parent demandeur de surveillance à distance, vous voudrez lire [ici](../../nightscout/pushover.md#pushover) sur la mise en place d'alertes à l'aide de votre site Nightscout si vous voulez des notifications proactives liées à Loop.
