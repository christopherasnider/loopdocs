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

Oui, vous pouvez... en quelque sorte. Il existe une façon piratée d’installer macOS sur un ordinateur Windows appelé « Virtual Machine ». [Ce lien](https://macosvmware.tech.blog/) peut vous fournir des informations utiles pour ceux qui veulent en savoir plus... mais c'est à vous et à Google si vous rencontrer des embuches. This Virtual Machine method will not work on PCs that have AMD processors either, so double check your computer before to confirm you don't have an old AMD processor. These docs do not provide troubleshooting tips for Virtual Machine installation or use.

## How often do I need to get on the computer for Loop?

The short answer is (1) when you first build and (2) once per year minimum after that. (If you decide to use a free Apple Developer Account, you will need to get on the computer every 7 days.)

The longer answer is that Loop code is updated periodically to include new features and bug fixes. When those updates are released, you'll need access to an Apple computer again to update your Loop app.  In general, probably a few times a year there are updates to Loop released that you'd want to take the time to install. Loop updates are not available through the iPhone's app store...instead you do the app update yourself with [update instructions here](../build/updating.md).

## Will I need to build a new Loop if I switch between Medtronic and Omnipod?

No. Loop will have the option to move between different pump types from within the same Loop app. You'll simply use the "Switch from Omnipods" or "Delete Pump" options to move to the other kind of pump.

## Can I use someone else's Apple Developer account for my Loop build?

Technically, yes...however there are major drawbacks. The person's developer account can only be "linked" to a limited number of build computers. So one person "loaning out" their developer license to a lot of people will quickly exceed the number of allowed computers. In those cases, that person will be told they need to revoke the certificates on some computers (essentially dropping old ones to make room for new ones). When they do that, they may have forgotten about your Loop app on your computer. When they revoke your computer's certificate (and they can do that without you knowing through their developer portal), your Loop app will immediately stop working and not even open.

Your Loop app will also die immediately if their developer account is not renewed or expires. Your Loop updates will also not be able to be built unless that person maintains the developer license agreement updates.

Moral of the story, out of all the ways to save money...borrowing someone's developer account is not a good place to save money. You could find yourself unexpectedly without a Loop app without notice.

## Can I use MY Apple Developer account to build for others?

Technically yes...however, there are reasons this is discouraged. When you build for others, you must be careful to not unintentionally revoke the signing certificate that had been used for other people's apps (see note in FAQ above). You also need to let the people know that the MAXIMUM their app will last is 12 months. It will need to be rebuilt no matter what every 12 months.

But the biggest issue with building for others is that they may be left without a decent method of getting Loop updates. There are a lot of new Loopers on Omnipod system and their apps will likely need updating on a regular basis over the first year. Unless you plan on meeting with that person regularly to update their app, you could leave them on an old app that doesn't work as well as the new versions.

## How can I find a compatible pump? supplies?

There is a [whole page with detailed information about Medtronic pumps](../build/step3.md); how to find them, how to find supplies, and assessing whether your Medtronic pump is compatible. Please check out that page for more info.

With the addition of Omnipod support, you can also now use Omnipod suppliers the way you'd normally source them.

## Can I pay someone else to do this?

NOOOO...you really need to figure this out yourself. This is an automated insulin delivery system and you really need to know how to build and operate this yourself.

## What if I lose my RileyLink?

For Medtronic users, you simply go back to old school pump use until you get a new RileyLink. You can either let your temp basal finish by itself (30 minutes or less) or cancel the temp basal on the pump's menu. For bolusing, you'd go back to using the pump's bolus commands. When you get a RileyLink (either finding your old one or getting your backup RileyLink out) and Loop running again, you'll want to do one thing. Enter in any carbs to Loop that you may have eaten in the recent past that could still be affecting blood glucose. While Loop will read whatever insulin deliveries had happened while the RileyLink was missing, it will not read any carbs you entered into the pump...so make sure to add those to Loop and backdate them to the time they were eaten. That will help make the transition smoother to Looping again.

For Pod users, your Pod will finish any currently running temporary basal rate (maximum of 30 minutes) and then revert back to your scheduled basal rate. Without a RileyLink, you will not be able to affect any Pod use other than normal basals. No temp basals, suspends, or boluses will be possible, similar to if you were to lose your PDM. If you have a backup RileyLink, you can simply connect to the new RileyLink on the same Loop app and it will work with the existing pod session. If you don't have a backup RileyLink, you'll have to remove the pod and start a new pod paired with your PDM until you get a new RileyLink.

## What if I lose or get a new iPhone?

When you get a new iPhone, Loop will need to be built onto that new iPhone in the same way that you built on your old iPhone. Loop will not restore from any iCloud or iTunes backups, so make sure you plan on finding an Apple computer to rebuild on before you plan on Looping with the new iPhone.

## What about other pumps? When will they Loop?

Hey now...let's be grateful for what we have first. The ability to use Loop is the result of tremendous amounts of effort, time, and sacrifice by volunteers. Cracking the pumps for Loop use is a large undertaking. If and when another set of people spend a large amount of time figuring out other pumps, then they could conceivably be added to Loop. But, you don't need to let us know that you'd love to see more pumps compatible with Loop. So would we. There is just an awful lot of work that needs to happen and it is not easy nor quick.

Tandem pumps are not Loop compatible. Animas pumps are not Loop compatible. DASH pods are not Loop compatible. And those all likely won't be compatible anytime in the future.

## Can I have more than one Loop app on a phone?

Yes, technically possible. You can have multiple Loop apps built onto the same iPhone. However, having multiple Loop apps on a single phone may lead to unexpected conflicts that can negatively affect your Loop's ability to stay green (keep looping). Additionally, your Pod will only work on one Loop app at a time anyways. So for smooth looping, just keep one Loop app on any phone for looping use.

## Will I be able to Loop on a plane? Or in the mountains?

Yes. Loop does not require internet or cell coverage to work. So long as the Loop user has Bluetooth turned on on the iPhone (or iPod touch), then the Dexcom and RileyLink will still be able to do their work with Loop and your pump/Pod.
