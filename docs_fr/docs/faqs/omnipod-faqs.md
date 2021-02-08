# FAQs sur les Omnipod

## Omnipod est-il pris en charge sur Loop ?

OUI !!! WOOHOO!!

## Quelles pods fonctionneront avec Loop ?

Le système Loop décrit dans ces documents (alias DIY Loop) fonctionne avec les pods Eros... ce sont les pods actuels sur le marché en grande majorité. Les nouveaux pods DASH ne sont pas compatibles avec les boucles DIY. Tidepool a commencé un processus pour amener [DIY Loop à travers l'approbation de la FDA](https://tidepool.org/blog/tidepool-delivering-loop) et Insulet a été annoncé comme le [premier partenaire de pompe pour ce projet](https://diatribe.org/omnipod-first-insulin-pump-partner-tidepool-loop). Tidepool Loop utilisera les pods DASH, aucun RileyLink n'est requis.  Si vous souhaitez rester informé des progrès de Tidepool Loop, vous pouvez remplir un formulaire d'intérêt [ici](https://tidepool.org/loop).

Résumé des systèmes éventuels:

* DIY Loop + Eros pods + RileyLink
* Tidepool Loop + DASH pods (sans RileyLink)

## Ai-je encore besoin d’un PDM avec Omnipod Loop ?

Non, les pods sont des petites créatures monogames. Ils s’associeront à un seul appareil à la fois pour des raisons de sécurité... ainsi, un pod est soit jumelé avec un PDM ou sois avec votre application Loop sur votre iPhone. En d'autres termes, votre PDM peut rester dans l'armoire à diabète pendant que vous utiliser Loop. Vous ne pouvez pas utiliser le PDM pour un pod qui a été activé avec Loop. Cela ne veut pas dire que vous devriez vous débarrasser de votre PDM. Au lieu de cela, gardez-le pour les situations de secours si vous perdez votre téléphone. Voir ci-dessous pour savoir quoi faire si vous perdez votre téléphone ou RileyLink.

## Puis-je annuler un ensemble de boucles basales temporaires ? Et pour un bolus ?

Oui, vous pouvez annuler un basal temporaire ou un bolus en cours. Il y a une commande "suspendre la livraison" facile d'accès en tapant sur l'icône d'âge du pod [dans votre zone supérieure droite](../operation/loop-settings/displays.md#pod-age-omnipod-users). Suspendre la distribution d'insuline annulera tout basal ou bolus temporaire en cours d'exécution. La commande suspension s'exécutera indéfiniment. Une notification s'affichera sur l'écran principal de Loop pendant la suspension de la distribution d'insuline.

![img/pump-suspend-banner.png](img/pump-suspend-banner.png)

L’insuline restera suspendue jusqu’à ce que l’utilisateur clique soit sur la commande « Appuyez pour reprendre » à partir de l’écran principal de Loop, soit sur la commande « reprendre la livraison » accessible en appuyant sur l’icône de l’âge du pod. Une fois la distribution d'insuline reprise, les debits de basal planifiés seront réactivés. Si un bolus a été interrompu, le bolus ne reprendra pas. Si vous n'activez pas le mode Boucle Ouverte, dans les 5 minutes suivant la reprise de la distribution d'insuline, votre Boucle devrait reprendre automatiquement les réglages de basal temporaire.

## Puis-je mettre mon propre débit basal temporaire sur Loop ?

Non. Loop does not allow you to pick your own temp basal rate or prime insulin in.

If you find yourself in a situation where you would like to specify an exact temp basal rate of your own, you would need to (1) change your scheduled basal rate for the time(s) that you'd like a temp basal rate to run, and (2) suspend/resume insulin delivery (in order to cancel any currently running temp basal that Loop has running) and then (3) turn the slider so that you are running in "open loop" mode for the duration of the time you want to use that specific basal rate.

## Que se passe-t-il si je perds mon téléphone ou RileyLink ?

Pour les utilisateurs de pod, votre pod finira tout débit de basal temporaire en cours d'exécution et retournera ensuite à votre débit de basal planifié. Cependant, sans téléphone ou RileyLink, vous ne serez pas en mesure d’affecter l’utilisation de votre pod ; aucun changement de basal, suspension, annulation ou bolus. Pour faire autre chose que de laisser le basal continuer, vous devrez prendre des mesures en fonction de la situation.

* RileyLink perdu seulement: Vous pouvez remplacer votre RileyLink manquant par un de secours. Pas de problème pour basculer d'un Rileylink à un autre en plein milieu d'session de pod. Si vous n'avez pas de RileyLink de secours à utiliser, vous devrez alors enlever le pod et en mettre un nouveau en le jumelant avec votre PDM jusqu'à ce que vous puissiez obtenir un nouveau RileyLink.

* IPhone perdu seulement: Vous aurez besoin de supprimer le pod et mettre sur un nouveau pod jumelé avec votre PDM jusqu’à ce que vous puissiez obtenir un nouveau téléphone et installer Loop.

* Perdu à la fois RileyLink et le téléphone: Vous avez une très mauvaise journée. Vous aurez besoin d'un câlin et suivez les mêmes instructions que si vous avez perdu le téléphone comme indiqué dans la puce ci-dessus.

## Y a-t-il une augmentation des défaillances de pod avec Loop ?

Au début du développement, il y en avait. Heureusement par le travail acharné de Pete Schwamb et d’autres, le taux d’échec des pods n'est pas plus élevé que via l’utilisation typique des pod avec un PDM.

## Que faire si un pod ne s'appaire pas ?

La plupart des erreurs de pod sur Loop sera pendant le processus d’appairage. Si vous obtenez un pod qui ne fonctionne pas, veuillez consulter [cette page](../troubleshooting/pod-pairing.md) pour des étapes sur la façon de corriger l'échec et de récupérer avant de perdre définitivement le pod.

## Que faites-vous pour arrêter une pod hurlant ?

Les pods hurlants peuvent être réduites au silence en utilisant un trombone. Il suffit de mettre le trombone dans le petit trou qui est sur le fond (le côté opposé où se trouve la canule) du pod comme indiqué. Poussez le trombone jusqu’à ce que vous entendez un petit clic, ce clic indique que le circuit laissant le pod crier est rompu.

![img/paperclip.jpg](img/paperclip.jpg)
