# FAQ générale sur Loop

Bienvenue sur LoopDocs - un endroit pour toutes les choses fréquemment demandé.

## Qu’est-ce que Loop?

Cliquez sur l'image ci-dessous pour regarder une courte [Introduction à Loop en vidéo](https://youtu.be/qw_u1lqboCs).

[![../img/loop_gear.jpg](img/intro-to-loop.png)](https://youtu.be/qw_u1lqboCs)

## De quoi ai-je besoin pour utiliser Loop ?

La boucle a des exigences matérielles et logicielles. En général, pour utiliser Loop, vous devez avoir sept composants.

- Pompe à insuline compatible : [Medtronic ou Omnipod](../build/step3.md)
- [MGC compatible](../build/step4.md)
- [RileyLink](../build/step5.md)
- [IPhone/iPod Touch compatible](../build/step2.md)
- [Ordinateur Apple exécutant Mojave macOS 10.14.3 ou ultérieur](../build/step1.md)
- [Xcode (une application Apple gratuite)](../build/step8.md)
- [Membre de l'Apple Developer](../build/step6.md)

![img/loop_gear.jpg](img/loop_gear.jpg)

## Puis-je télécharger Loop depuis l’App Store ?

Non. Loop n’est pas disponible au téléchargement. Vous devez construire votre propre application Loop. L'application Loop ne sera pas disponible dans l'App Store d'Apple car ce serait considéré comme la distribution d'un appareil médical, et nous ne sommes pas ce type «d'entreprise».  Vous pouvez construire vous-même, mais nous ne sommes pas des distributeurs.

Ne vous inquiétez pas, la construction de votre application Loop est en fait assez facile et c'est de cela qu'il s'agit. La partie la plus difficile sera d'avoir la patience de lire tous les documents avant de commencer. Les nouveaux utilisateurs de la Loop sont tellement excités de commencer qu'ils ne lisent pas toutes les bonnes infos que contiennent ces documentations. Donc, au fur et à mesure que vous commencez la compilation...veuillez prendre le temps de lire les documents qui suivent ce qui se passe APRÈS que vous ayez compilé avec succès votre application Loop.

Si vous avez des questions, ces docs ont une belle fonction de recherche dans la barre de menu bleu foncé qui peut vous aider également à trouver vos réponses assez rapidement.

## Puis-je utiliser un téléphone Android pour Loop ?

Non, c’est uniquement compatible pour iPhone ou iPod touch.

## Dois-je être un "pro de l'informatique" pour construire Loop?

Non. Vous n'avez pas besoin d'expérience dans le code ou les ordinateurs pour construire Loop. Si vous avez déjà possédé un ordinateur Apple et un iPhone, vous avez déjà le niveau d'expérience requis. En plus de cela, il suffit de lire les indications lentement et assidûment ... toutes les informations dont vous aurez besoin sont dans ces documents.

Souvent, les gens non-tech font mieux que les gens de la technologie dans la construction de loop. Pourquoi ? Parce que les non-tech prennent le temps de lire lentement et de regarder les captures d'écran dans les directions. Les gens de la technologie survole et manquent des phrases ... ce qui conduit ensuite à créer des erreurs qui doivent être retracées et corrigées.

## Y a-t-il une feuille de triche à utiliser pour une infirmière scolaire?

Bien sûr, vous pouvez essayer celle-la. [Feuille de triche de l’infirmière scolaire](https://github.com/Kdisimone/images/raw/master/school_nurse.pdf)

## Combien de temps faut-il pour construire Loop ?

La réponse est variée, mais quelques heures du début à la fin, selon l’endroit où vous commencez et comment vous êtes à l’aise avec votre ordinateur.

Si vous préférez decomposer en plusieurs parties votre effort, la section [`Construire son Appli`](../build/step1.md) est divisée en points d'arrêt pratiques avec des estimations de temps pour chaque étape. Vous pouvez faire une ou plusieurs étapes en fonction du type de temps dont vous avez besoin.

## Loop coûte-t-il de l’argent ?

Oui, il y a des coûts, au-delà des coûts évidents de posséder une pompe et un MGC.

Le kit [RileyLink coûte](https://getrileylink.org/) 150 $. C'est un coût unique et beaucoup de gens ont encore leur RileyLinks original après 3 années de fonctionnement. Je recommande fortement l'achat de deux RileyLinks lorsque c'est financièrement réalisable, d'en avoir un en secours en cas de dommages accidentels.

La licence Apple Developer peut être faite gratuitement, cependant, vous devrez reconstruire votre application Loop tous les 7 jours. Ça pourrait devenir très fastidieux. L'inscription annuelle du programme Apple Developer à 99 $ est un excellent investissement.

Il n’y a pas d’autres coûts, periodique ou initiaux, à utiliser Loop.

## Dois-je posséder mon propre ordinateur Apple ?

Vous n'avez pas besoin de posséder votre propre ordinateur Apple, mais vous devez au moins en emprunter un. Il serait vraiment bon d'avoir une capacité à long terme d'emprunter cet ordinateur à nouveau pour [mettre à jour Loop](../build/updating.md#when-to-update) plus tard, lorsque c'est nécessaire.

Si vous empruntez un ordinateur Apple, vous devriez demander à la personne de (1) mettre à jour vers Mojave et (2) [télécharger Xcode gratuitement](https://developer.apple.com/xcode/) avant de vous réunir pour construire votre application Loop. Les mises à jour et le téléchargement de Xcode peuvent prendre quelques heures selon la vitesse Internet de la personne... Alors, mieux vaut faire ces étapes bien avant, pour éviter des problèmes.

## Puis-je utiliser un PC ou un ordinateur Windows pour construire ?

Oui, vous pouvez... en quelque sorte. Il existe une façon piratée d’installer macOS sur un ordinateur Windows appelé « Virtual Machine ». [Ce lien](https://macosvmware.tech.blog/) peut vous fournir des informations utiles pour ceux qui veulent en savoir plus... mais c'est à vous et à Google si vous rencontrer des embuches. Cette méthode de machine virtuelle ne fonctionnera pas non plus sur les PC qui ont des processeurs AMD, alors vérifiez votre ordinateur avant de confirmer que vous n'avez pas d'ancien processeur AMD. Ces docs ne fournissent pas de conseils de dépannage pour l'installation ou l'utilisation d'une machine virtuelle.

## À quelle fréquence dois-je utiliser l’ordinateur pour Loop ?

La réponse courte est (1) lorsque vous construisez et (2) une fois par an minimum après cela. (Si vous décidez d’utiliser un compte de développeur Apple gratuit, vous devrez utiliser l’ordinateur tous les 7 jours.)

La réponse longue est que le code Loop est mis à jour périodiquement pour inclure de nouvelles fonctionnalités et corrections de bogues. Lorsque ces mises à jour sont publiées, vous aurez besoin d’accéder à nouveau à un ordinateur Apple pour mettre à jour votre application Loop.  En général, probablement plusieurs fois par an, il y a des mises à jour de Loop publiées que vous souhaitez prendre le temps d’installer. Loop updates are not available through the iPhone's app store...instead you do the app update yourself with [update instructions here](../build/updating.md).

## Vais-je avoir besoin de construire un nouveau Loop si je passe entre Medtronic et Omnipod?

Non. Loop aura la possibilité de basculer entre différents types de pompes à partir de la même application Loop. Vous utiliserez simplement les options « Basculer vers Omnipods » ou « Supprimer la pompe » pour passer d'une pompe à l'autre.

## Puis-je utiliser le compte Apple Developer de quelqu'un d'autre pour ma version Loop ?

Techniquement, oui... mais il y a des inconvénients majeurs. Le compte développeur de la personne ne peut être « lié » qu'à un nombre limité d'ordinateurs pour construire les applications. Ainsi, une personne « prêtant » sa licence de développeur à un grand nombre de personnes dépassera rapidement le nombre d'ordinateurs autorisés. Dans ces cas, cette personne sera informée qu'elle doit révoquer les certificats sur certains ordinateurs (essentiellement en abandonnant les anciens pour faire de la place pour les nouveaux). Quand ils font cela, ils peuvent avoir oublié votre application Loop sur votre ordinateur. Lorsqu'ils révoquent le certificat de votre ordinateur (et qu'ils peuvent le faire sans que vous le sachiez via leur portail développeur), votre application Loop cessera immédiatement de fonctionner et ne s'ouvrira même plus.

Votre application Loop mourra immédiatement si son compte développeur n'est pas renouvelé ou expiré. Vos mises à jour de Loop ne pourront pas non plus être construites à moins que cette personne ne maintienne les mises à jour du contrat de licence de développeur.

La morale de l'histoire, c'est que pour essayer d'économiser de l'argent... emprunter le compte de développeur de quelqu'un n'est pas forcement une solution si économique. Vous pourriez vous retrouver de façon inattendue et sans préavis préalable avec une application Loop non fonctionnelle.

## Puis-je utiliser MON compte Apple Developer pour créer Loop pour d’autres personnes ?

Oui techniquement...mais il y a des raisons pour lesquelles cela est découragé. Quand vous construisez pour les autres, vous devez veiller à ne pas révoquer involontairement le certificat de signature qui a été utilisé pour les applications d'autres personnes (voir la note dans la FAQ ci-dessus). Vous devez également informer les gens que leur application durera MAXIMUM 12 mois. Il faudra la reconstruire quoi qu’il arrive tous les 12 mois.

Mais le plus gros problème avec la compilation pour les autres est qu'ils peuvent être laissés sans une méthode décente pour obtenir des mises à jour de Loop. Il ya beaucoup de nouveaux utilisateurs de Loop avec le système Omnipod et leurs applications auront probablement besoin d’être mis à jour régulièrement au cours de la première année. À moins que vous ne prévoyiez de rencontrer cette personne régulièrement pour mettre à jour son application, vous pourriez les laisser sur une ancienne application qui ne fonctionne pas aussi bien que les nouvelles versions.

## Comment puis-je trouver une pompe compatible ? les fournitures ?

Il y a une [page entière avec des informations détaillées sur les pompes Medtronic](../build/step3.md); comment les trouver, comment trouver des fournitures, et évaluer si votre pompe Medtronic est compatible. Veuillez consulter cette page pour plus d'informations.

Avec l’ajout de la prise en charge Omnipod, vous pouvez également maintenant utiliser les fournisseurs Omnipod de la meme manière que d'habitude.

## Puis-je payer quelqu'un d'autre pour faire cela?

NOOOON... vous avez vraiment besoin de comprendre cela vous-même. Il s’agit d’un système automatisé d’administration d’insuline et vous avez vraiment besoin de savoir comment le construire et le faire fonctionner.

## Que faire si je perds mon RileyLink ?

Pour les utilisateurs de Medtronic, il vous suffit de revenir à l’utilisation de la pompe comme avant Loop jusqu’à ce que vous obtenez un nouveau RileyLink. Vous pouvez soit laisser votre débit basal temporaire se terminer par lui-même (30 minutes ou moins) ou annuler le basal temporaire dans le menu de la pompe. Pour faire un bolus, vous devriez retourner à l'aide des commandes bolus de la pompe. Quand vous obtenez un RileyLink (soit retrouver votre ancien RileyLink ou récupérer votre RileyLink de secours) et Loop de nouveau vous aurez envie de faire qu'une chose. Entrez tous les glucides dans Loop que vous avez peut-être mangé récemment qui pourraient toujours affecter votre glycémie. Bien que Loop lira les livraisons d'insuline qui se sont produites pendant que le RileyLink était manquant, il ne lira pas les glucides que vous avez entrés dans la pompe... Alors, assurez-vous de les ajouter dans Loop et à la date de leur consommation. Cela aidera à faciliter la transition vers Loop.

Pour les utilisateurs de Pod, votre Pod finira tout débit de basal temporaire en cours d'exécution (maximum de 30 minutes) et retournera ensuite à votre débit basal planifié. Without a RileyLink, you will not be able to affect any Pod use other than normal basals. No temp basals, suspends, or boluses will be possible, similar to if you were to lose your PDM. If you have a backup RileyLink, you can simply connect to the new RileyLink on the same Loop app and it will work with the existing pod session. If you don't have a backup RileyLink, you'll have to remove the pod and start a new pod paired with your PDM until you get a new RileyLink.

## What if I lose or get a new iPhone?

When you get a new iPhone, Loop will need to be built onto that new iPhone in the same way that you built on your old iPhone. Loop will not restore from any iCloud or iTunes backups, so make sure you plan on finding an Apple computer to rebuild on before you plan on Looping with the new iPhone.

## What about other pumps? When will they Loop?

Hey now...let's be grateful for what we have first. The ability to use Loop is the result of tremendous amounts of effort, time, and sacrifice by volunteers. Cracking the pumps for Loop use is a large undertaking. If and when another set of people spend a large amount of time figuring out other pumps, then they could conceivably be added to Loop. But, you don't need to let us know that you'd love to see more pumps compatible with Loop. So would we. There is just an awful lot of work that needs to happen and it is not easy nor quick.

Tandem pumps are not Loop compatible. Animas pumps are not Loop compatible. DASH pods are not Loop compatible. And those all likely won't be compatible anytime in the future.

## Can I have more than one Loop app on a phone?

Yes, technically possible. You can have multiple Loop apps built onto the same iPhone. However, having multiple Loop apps on a single phone may lead to unexpected conflicts that can negatively affect your Loop's ability to stay green (keep looping). Additionally, your Pod will only work on one Loop app at a time anyways. So for smooth looping, just keep one Loop app on any phone for looping use.

## Will I be able to Loop on a plane? Or in the mountains?

Yes. Loop does not require internet or cell coverage to work. So long as the Loop user has Bluetooth turned on on the iPhone (or iPod touch), then the Dexcom and RileyLink will still be able to do their work with Loop and your pump/Pod.
