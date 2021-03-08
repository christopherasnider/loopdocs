# Apport de Glucides

![img/toolbar.png](img/toolbar.png)

De nouvelles entrées de glucides peuvent être faites en utilisant l'outil Glucides vert dans la barre d'outils en bas de l'écran d'état.  N'utilisez pas l'assistant de bolus de votre pompe ou l'entrée de glucides de votre pompe pour enregistrer des glucides dans l'application Loop.  Vous ne devriez pas non plus utiliser le portail de soins de Nightscout pour entrer dans les glucides, car Loop ne lit pas à distance les entrées de glucides.

## Nouveaux Glucides

Pour commencer une nouvelle entrée de repas, entrez simplement le nombre de glucides à consommer dans la ligne de ` la quantité consommée`.  Par défaut, le temps d'absorption des glucides pour une nouvelle entrée de glucides correspond à l'icône de tacos.  Si vous n'avez pas fait de personnalisation aux icônes de sucettes, tacos ou pizza pendant votre compilation de Loop, alors le temps d'absorption par défaut des glucides s'affichera sous la forme de 3 heures.  L’entrée de temps par défaut est pour l’heure et la date actuelles.  Une fois que vous appuyez sur `Enregistrer` sur l'écran d'entrée de glucides, l'outil bolus de Loop s'ouvrira pour fournir un bolus recommandé.

![img/carb_entry.png](img/carb_entry.png)

## Éviter les entrées doubles de glucides

!!!info "Soyez attentif"

    Lorsque vous appuyez sur « Enregistrer » pour une entrée de glucides, Loop considérera l’entrée de glucides enregistré et l’utilisera pour le calcul des basals temp et bolus recommandés.  Be cautious about repeated attempts to enter the same meal...Loop will continue to save the carb entries UNLESS you push cancel on the carb entry screen.
    
    **Simply canceling a bolus does not cancel the carb entry.**
    
    If you have accidentally made multiple entries for the same carbs, click on the Carbs Chart in the main Loop display and you can delete the redundant carb entries by swiping left on the entries.

## Durée d’absorption des Glucides

![img/food_icons_times.png](img/food_icons_times.png)

Pour sélectionner la durée d'absorption de votre entrée de glucides, vous pouvez soit cliquer sur les émojis alimentaires par défaut ou entrer manuellement le temps d'absorption des glucides en sélectionnant la ligne `temps d'absorption` dans l'outil d'entrée des glucides.

Appuyer sur la ligne `type de nourriture` peut également être utilisé si vous n'êtes pas sûr d'un nouvel aliment.  Il existe d’autres emojis alimentaires regroupés en aliments à absorption rapide, moyenne et lente.  Cela peut être particulièrement utile pour les adolescents qui essaient d'apprendre de nouveaux aliments ou repas.  De plus, vous pouvez ajouter du texte à votre `type de nourriture` en sélectionnant le bouton `abc` dans le coin inférieur gauche de l'écran.

![img/plate.png](img/plate.png)

![img/ns-plate.png](img/ns-plate.png)

Les temps d'absorption des glucides par défaut dans l'application Loop sont des représentations moyennes pour les aliments à indice glycémique élevé, moyen et faible.  Depuis la version 1.4.0, l'algorithme intègre l'absorption dynamique des glucides.  Les versions précédentes de loop étaient basées sur une courbe qui supposait que le taux d’absorption des glucides commencerait lentement, augmenterait à un point médian, puis diminuerait.  Cependant, dans le monde réel, l’absorption des glucides est assez variable.  Le modèle d'absorption dynamique des glucides est en mesure de modéliser une partie de cette variabilité et de permettre à Loop de répondre plus raisonnablement lorsque l'absorption réelle des glucides ne correspond pas bien à l'heure d'absorption des glucides sélectionnée pour un repas.  Pour faire court, bien que l'entrée dans une période d'absorption de glucides fasse toujours partie de l'enregistrement des repas dans Loop, il est beaucoup moins critique de le faire correctement.  Maintenant, votre entrée sert de guide plutôt que de règle pour modéliser l'absorption des glucides.  Pour une explication plus détaillée du nouveau modèle dynamique d’absorption des glucides, veuillez lire à ce sujet [ici](https://github.com/LoopKit/Loop/pull/507).

Pour aider Loop à ajuster les glucides qui peuvent digérer plus lentement que votre estimation initiale, Loop appliquera d’abord un multiplicateur de 1,5 x à votre temps d’absorption des glucides entrés.  Ainsi, un repas entré à l'aide de l'icône tacos sera traité initialement comme un repas d'absorption de 4,5 heures.  Comme Loop observe les impacts de glycémie du repas, Loop raccourcira le temps d’absorption du repas si les glycémies montrent des impacts plus rapides que prévu, ainsi que d’ajuster les injections d’insuline (par exemple, augmenter les basals temporaires).  Vous pouvez observer la progression des observations de Loop sur votre repas en cliquant sur le graphique des glucides et en observant les effets de la contre-action de l'insuline.

## Mixer les glucides d'un repas

Vous n’avez pas à entrer tous les glucides pour un repas au même temps d’absorption ou de consommation.  Si vous voulez entrer certains glucides du repas avec une vitesse d'absorption rapide, et certains plus lents, vous pouvez enregistrer le repas en décomposant en plusieurs entrées de glucides.  Par exemple, pour les repas qui contiennent des glucides sucrés ainsi que des glucides à action lente (nourriture chinoise), vous pouvez faire une partie des glucides avec le logo sucette et une partie des glucides avec celui de la pizza.

En appuyant sur le bouton `Enregistrer` dans le coin supérieur droit pour enregistrer les glucides dans l’application Loop et de faire apparaitre l’outil bolus.  Lorsque vous entrez plusieurs durées d’absorption des glucides pour un seul repas, appuyez sur enregistrer sur l’entrée de glucides, puis appuyez sur annuler sur l’outil bolus quand il apparaît.  Lorsque vous avez entré votre dernière entrée de glucides pour le repas, utilisez l'outil bolus pour fournir le bolus pour le repas entier.  Loop fournira une recommandation basée sur le total des glucides enregistrés et leurs durées d’absorption respectives.

## Prebolus

Vous pouvez indiquer à Loop que vous pré annoncer un bolus d'un repas en ajustant l'heure de l'entrée de glucides sur la ligne « date » de l'entrée de glucides.  Si vous avez un prébolus de 20 minutes, ajoutez simplement 20 minutes à l'heure d'entrée des glucides.

## Modifier les Glucides

En cliquant sur le graphique des glucides dans l'écran principal de Loop, vous ouvrirez l'historique de l'entrée de glucides et les entrées précédentes pourront être modifiées ou supprimées à travers cet écran.  Si vous avez besoin de changer l'heure du prébolus, ajouter/soustraire les glucides, ajuster les temps d'absorption des glucides (même au milieu du repas), entrez simplement dans cet écran d'édition et appuyez sur l'entrée de glucides que vous souhaitez modifier, ou glissez vers la gauche pour supprimer complètement l'entrée.  Cela peut être un outil particulièrement utile lorsque :

* Vous n'avez pas terminé un repas entier pour lequel vous avez deja déclaré un bolus,
* Vous n'avez pas mangé de repas au moment initialement prévu,
* Vous avez mangé plus de quantité que ce qui était entré prévu initialement, ou
* Vous soupçonnez que votre nombre de glucides était erroné parce que la glycemie augmente plus/moins que prévu.

![img/carb_edit.png](img/carb_edit.png)

## Applications tierces

Si vous utilisez une application tierce, telle que My Fitness Pal, pour entrer et suivre les glucides et cette application stocke également les valeurs de glucides dans Santé, Loop lira ces valeurs depuis Apple Santé et les affichera et les utilisera dans le calcul des débits de basal temporaires. Les entrées des applications tierces ne peuvent pas être retirées à partir de Loop.  Vous devrez les modifier dans l'application tierce ou depuis l'application Santé. En raison de ce risque de confusion, il est recommandé de désactiver la capacité de Loop à lire les données sur les glucides des autres applications de Santé. On vous demande si vous voulez activer cette option lorsque Loop est installé pour la première fois. Après l'installation, vous pouvez également aller dans l'application Paramètres -> Confidentialité -> Santé -> Loop et désactiver `Lire les données pour les glucides`.
