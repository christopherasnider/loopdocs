# Prévision de la glycémie

La boucle utilise un algorithme pour maintenir la glycémie dans une plage de correction en prédisant les apports de quatre effets individuels (insuline, glucides, correction rétrospective, et dynamisme glycémique) à tout moment *m* pour recommander des corrections de débit de basal temporaire et des bolus.

![équation de base des effets combinés](img/predicted_glucose_equation.png)

Vous pouvez voir les contributions individuelles de ces effets en appuyant sur le graphique de glycémie prédictive sur l'écran d'état de Loop. Loop met à jour cette prédiction de glycémie toutes les cinq minutes quand une nouvelle valeur du MGC a été reçue et que le statut de la pompe a été mis à jour.

Juste une remarque, toute cette section est assez technique. Bien que ce n'est peut-être pas le sujet le plus intéressant pour de nombreux lecteurs, si vous cherchez la vue détaillée de l'algorithme de Loop, cette discussion est assez utile. Si vous voulez une compréhension générale, la vue d'ensemble et les recommandations basales temporaires suffiront probablement.

## Présentation

Avant de nous plonger dans chacun des quatre effets individuels, un aperçu général est probablement un bon début. Il y a quatre effets réunis ensemble pour produire la courbe finale de prédiction glycémique de Loop. Chaque effet individuel, ainsi que leur effet combiné, est illustré dans la figure ci-dessous. L’insuline, des bolus et des basals temporaires, aura un effet décroissant sur la prédiction. Les glucides auront un effet croissant sur la prédiction. L'effet dynamique de la glycémie peut avoir un effet positif ou négatif, selon la comportement de la glycémie dans les dernières valeurs du MGC. Comme le montre l'exemple ci-dessous, la glycémie tend légèrement vers le haut au moment de la prédiction. Par conséquent, la contribution de l’effet d'impulsion de la glycémie tire la prédiction générale des trois autres effets pendant une courte période. La correction rétrospective a un effet décroissant sur la prédiction, indiquant que l’augmentation récente de la glycémie n’était pas aussi grande que cela avait été précédemment prédit par Loop dans un passé récent.

![courbe d’effets combinés](img/combined_effects.png)

Les sections ci-dessous fournissent des renseignements détaillés sur chacune des quatre contributions.

## Effet de l'Insuline

La plupart des utilisateurs de pompes et des fournisseurs de soins traditionnels connaissent déjà le concept de courbe de l'activité d'insuline, où l'effet de l'insuline dans le temps. L'insuline prend un peu de temps pour affecter la glycémie. L'effet d'insuline atteint généralement son pic une heure après avoir donné de l'insuline, puis se dégrade progressivement.

![courbe d’activité de l’insuline](img/insulin_activity_curve.png)

Loop fournit aux utilisateurs deux classes différentes de modèles d'insuline (c'est-à-dire un modèle exponentiel et le modèle Walsh). Tous les modèles exponentiels ont une durée d’activité d’insuline de 6 heures, alors que la durée de l’activité de l’insuline est personnalisable pour le modèle Walsh. Les courbes d'activité de l'insuline rapide et Fiasp sont modélisées comme des courbes exponentielles qui correspondent à la forme des courbes d'activité de l'insuline, et comme observé chez les adultes et les enfants.

![modèle d'insuline](img/insulin_models.png)

La quantité d'effet d'insuline restante ou le pourcentage d'insuline active restante après la délivrance d'un bolus d'insuline, est modélisé mathématiquement dans Loop avec une courbe de décomposition exponentielle.

### Effet de l'insuline restante

![pourcentage d'insuline restant](img/insulin_percent_remaining.png)

Si le facteur de sensibilité à l'insuline (FSI) est de 50 mg/dL par unité d'insuline et que l'utilisateur donne 2 unités d'insuline, on s'attendrait à ce que la glycémie de l'utilisateur baisse de 100 mg/dL dans les 6 heures suivant la distribution d'insuline. Cet effet d'insuline peut être visualisé de différentes manières : l'insuline active attendue, la baisse prévue de la glycémie toutes les 5 minutes après l'injection, et la baisse cumulative prévue de la glycémie. Les chiffres ci-dessous utilisent le modèle d'insuline rapide - adulte en boucle.

### Insuline active

Ce chiffre montre que 2 unités d'insuline sont données initialement, et l'insuline active correspondante (cad, l'insuline active, IOB en anglais) se décompose en fonction de la courbe ci-dessous.

![exemple restant d'insuline](img/insulin_remaining_example.png)

L'insuline active à tout moment est le produit de l'insuline d'origine délivrée et le pourcentage de l'activité d'insuline restante. Connaître l'insuline active attendue dans les 6 prochaines heures et le facteur de sensibilité à l'insuline (50 mg/dL, dans ce cas), Loop peut calculer la baisse prévue de la glycémie à partir de cette dose d'insuline, comme indiqué dans la figure ci-dessous.

![glycémie chute de 2 unités](img/bg_drop.png)

REMARQUE : Le FSI est également une fonction du temps, ce qui signifie que si le FSI de l'utilisateur planifié change pendant le temps d'activité de l'insuline, elle modifiera la baisse prévue de la glycémie en raison de l'effet d'insuline.

### Changement prévu de la glycémie

Pour finir, en prenant la première dérivée (c.-à-d. le taux de changement) de la chute cumulée de la courbe de glycémie donne la variation prévue de la glycémie sur la durée de l'activité d'insuline. Pour chaque dose d’insuline administrée, Loop calcule la baisse prévue de la glycémie pour chaque période de 5 minutes pour la durée de l’activité de l’insuline, comme indiqué ci-dessous.

![taux de changement glycémie](img/derivative.png)

### Effet de l'insuline sur la Glycémie

Pour cet exemple, en supposant que la glycémie d'un utilisateur était de 205 mg/dL au moment de la distribution d'insuline, Loop prédisait une baisse de la glycémie en raison des deux unités livrées à 12 heures, comme le montre le chiffre ci-dessous.

![deux exemples d’unité](img/two_units.png)

### Taux de Basal Planifié

Dans la thérapie traditionnelle de pompe de basal/bolus, les taux basaux sont réglés pour s'adapter à la production endogène de glucose (EGP) de l’utilisateur qui fait augmenter la glycémie. Si les paramètres de basal d'un utilisateur étaient exactement corrects dans la thérapie traditionnelle de la pompe, l'utilisateur aurait un taux de glycémie parfaitement fixe toute la journée, tous les autres facteurs étant égaux.

En réalité, les personnes atteintes de diabète de type 1 et leurs soignants savent que les paramètres basaux ne sont jamais exactement corrects. Chaque jour est un peu différent et une myriade de facteurs qui affectent la glycémie (par exemple, le stress, les hormones, le sommeil, etc.) peuvent affecter les besoins en insuline. Certaines personnes ont des profils basaux différents pour s'adapter à ces variations. Certaines personnes configurent régulièrement et ajustent leur taux de basal et/ou le font lors de leurs visites à la clinique endocrinologique.

Puisque l'algorithme de Loop suppose que les taux de basal définis par l'utilisateur sont corrects, il calcule l'effet de l'insuline par rapport aux taux de basal planifiés. Si les débits de basal ne sont pas entièrement corrects, Loop peut compenser un peu grâce à la correction rétrospective et aux effets de la dynamique de la glycémie décrits plus loin dans cette page.

Le graphique de distribution d'insuline ci-dessous affiche un historique bar-graphique des débits de basal temporaires promulgués par Loop. L'affichage est relatif aux débits de basal programmés entrés dans les paramètres Loop. Un taux affiché dans ce graphique en tant que +0 indiquerait qu'aucun débit de basal temporaire n'a été défini et que le débit de basal fourni était le taux de basal planifié. Des valeurs positives indiquent qu'un taux de basal temporaire a été défini au-dessus du taux de basal planifié (c'est-à-dire plus d'insuline distribuée) et des valeurs négatives indiquent qu'un taux de basal temporaire a été défini en dessous du taux basal planifié (c'est-à-dire moins d'insuline distribuée).

![Graphique basal temporaire de Loop](img/temp_basal_chart.png)

Par exemple, si le débit de basal planifié de l'utilisateur est de 1 U/hr, et que la boucle donne un taux de basal temporaire de 3 U/hr, puis il calculera la chute prévue de la glycémie en raison de +2 U/h d'insuline.

De la même manière si Loop fixe un taux de basal temporaire de 0 U/h pendant 1 heure, alors l'effet d'insuline sera également relatif au taux de basal planifié actuel de 1 U/h, et Loop prédisait que le taux de glycémie de l’utilisateur augmenterait par la quantité de changement de -1 U/h d’insuline. Si la FSI de l’utilisateur est de 50 mg/dL, alors Loop prédit que la glycémie augmentera de 50 mg/dL sur la durée de l’activité de l’insuline (6 heures).

Voici un exemple réel où Loop définit de nombreux débits de basal temporaires au cours de la journée. Les barres orange sont les débits de base temporaires et la ligne orange solide est l'insuline active à tout moment de la journée.

![Graphique basal temporaire de Loop pendant la journée](img/temp_basal_day.png)

### Effet total de l'insuline (combinaison de bolus et taux basal temporaires)

Loop combinera ou empilera l'insuline active de tous les bolus distincts (individuels) et les taux de basal temporaires sur la dernière durée d'activité de l'insuline (6 heures), pour prédire l'insuline active dans les 6 prochaines heures. Comme cela a été démontré ci-dessus, l'utilisation de la prediction d'insuline active de Loop peut prédire la baisse de glycémie au cours des 6 prochaines heures.

Enfin, l'effet combiné du bolus et de l'insuline basale sont visuellement représentés pour l'utilisateur par les graphiques d'insuline de Loop:

![Insuline active et temp Basal dans Loop](img/insulin_delivery_iob.jpg)

L'effet d'insuline peut être exprimé mathématiquement :

![équation de l'effet d'insuline ](img/insulin_effect_equation.png)

où la glycémie est le changement attendu de glycémie avec les unités (mg/dL/5min), Le ISF est le facteur de sensibilité à l'insuline (mg/dL/U) au un instant t, et l'IA est l'activité de l'insuline (U/5min) à l'instant *t*. L'activité de l'insuline peut également être considérée comme une vitesse ou un taux de variation de la glycémie due à l'insuline. L’activité d’insuline explique l’PEG (production endogène de glucose) et toute insuline active des basals et des bolus.

## Effet des glucides

Les glucides augmenteront la glycémie, mais la vitesse et la mesure dans laquelle ils ont un impact sur la glycémie dépendent du type de glucides. Les glucides à indice glycémique élevé (IG) augmenteront rapidement la glycémie sur une période plus courte, tandis que les aliments à faible IG augmenteront la glycémie plus lentement sur une plus longue période. Les aliments comme les bonbons, les jus et les fruits ont tendance à être des aliments riches en IG, tandis que les pizzas, burritos et quesadillas sont généralement des aliments à IG inférieurs. Les problèmes de digestion comme la gastroparésie peuvent également contribuer à des variations dans l’absorption des glucides.

Parce que l’absorption des glucides peut être très variable, Loop a un modèle qui ajuste dynamiquement le temps restant prévu de l’absorption des glucides. Pour commencer, Loop permet à l’utilisateur d’entrer une estimation approximative du temps qu’ils pensent nécessaire pour absorber la nourriture ou la boisson. La conjecture de l’utilisateur est utilisée comme une estimation moyenne, et l’algorithme de Loop va raccourcir ou allonger en fonction du changement observé de glycémie.

Pour toutes les entrées de glucides, Loop suppose que les glucides ne commenceront pas à être absorber pendant 10 minutes, il y a donc une période de 10 minutes de non absorption qui est modélisé avant l’absorption modélisée dans les sections suivantes.

### Absorption linéaire des glucides

Loop adopte une vision prudente de la vitesse à laquelle les glucides restants seront absorberont.  Parce qu'il est plus sûr de sous-fournir de l'insuline pour les repas de longue durée, Loop commence à un taux d'absorption minimum basé sur la prolongation de la durée des glucides entrés de 50%. Dit autrement, le taux minimum d'absorption des glucides est le nombre total de grammes glucose sur 150% de la durée entrée initialement.

En utilisant ce taux d'absorption minimum initial, les glucides restants sont modélisés pour être absorbés linéairement. Par exemple, si l'utilisateur entre dans un repas de 72g de glucides et sélectionne une période d'absorption estimée de 4 heures, alors Loop prévoit un taux d'absorption de 12g/h pour les 6 prochaines heures. Ce taux peut être appelé le taux minimum d’absorption, qui peut être représenté mathématiquement comme :

![équation de l'effet Linéaire des glucides ](img/linear_carb_effect_equation.png)

où MAR est le taux d'absorption minimum (g/h), CA est le nombre glucides (g) et d est la durée prévue (hr) nécessaire à l'absorber les glucides.

### Absorption dynamique de glucides

Le modèle linéaire ci-dessus est modulé par un calcul supplémentaire qui utilise des données de glycémie récemment observées pour estimer la vitesse d’absorption des glucides. La modification prévue de la glycémie en raison des seuls effets d'insuline est comparée aux changements observés du taux de glycémie. Cette différence est appelée l'effet de contre-action de l'insuline (ICE):

![équation dynamique d’effet des glucides ](img/dynamic_carb_effect.png)

où, ICE (mg/dL/5 min) est l'effet de contre-action de l'insuline, OA est l'activité observée (mg/dL/5min) ou le changement observé de glycémie à l'instant <i>t</i>, et IA est l'activité de l'insuline (mg/dL/5min).

Les effets de contre-action de l'insuline sont causés par plus que par de simples glucides, et peuvent inclure de l'exercice, des changements de sensibilité ou des paramètres de distribution d'insuline mal configurés (cad, taux de basal, FSI, etc.). Cependant, comme l'effet des glucides est souvent dominant (après l'insuline), Loop peut encore apporter des ajustements utiles à son modèle de glucides en supposant que la hausse du glycémie est principalement des glucides dans la période suivant les entrées de repas enregistrées.

L'effet de contre-action de l'insuline est converti en une quantité estimée d'absorption de glucides en utilisant le ratio actuel glucide/insuline et le facteur de sensibilité à l'insuline au moment de l'entrée de repas enregistrée.

![équation de l'effet de glucide ice ](img/ice_carb_effect_equation.png)

où l'AC est le nombre glucides (g/5min), ICE est l'effet de contre-action de l'insuline, Le CIR est le ratio glucides / insuline (g/U), et la SI est le facteur de sensibilité à l'insuline (mg/dL/U) à l'instant <i>t</i>.

Si plusieurs entrées de repas sont activées (cad en cours d'absorption), l’absorption estimée est répartie entre chaque entrée de glucides proportionnellement au taux d’absorption minimum de chaque entrée de glucides. Par exemple, si des glucides de 72 g avec un temps d'absorption prévu de 4 heures ont été consommés à 12 heures, et un autre 72 g d'hydrates de carbone avec un temps d'absorption prévu de 2 heures a été consommé à 15 heures, le taux d'absorption minimum (voir l'équation MAR ci-dessus) serait respectivement de 12 g/h et 6 g/h, ou de 1 g/5 min et 0.5 g/5min.

![mar meal 1 equation ](img/mar_12.png)

![mar meal 2 equation ](img/mar_3.png)

Examen de l’effet simple et linéaire des glucides de ces deux repas :

![entrées combinées de repas](img/mixed_meals.png)

Si nous élargissons encore cet exemple, en assumant ce qui suit à 16 h :

* qu’il reste encore des glucides à absorber des deux repas,
* que l'effet de contre-action de l'insuline estimé (ICE) est de +15 ![ICE units](img/ice_units.png), et
* le CIR de l'utilisateur est de 10 g/U et la SI est de 50 mg/dL/U,

alors la quantité estimée de glucides absorbés à 16h serait de 3g :

![entrées combinées de repas](img/at_4.png)

Ces 3 g de glucides seraient alors répartis entre les repas proportionnellement à leurs taux d'absorption minimum:

![entrées combinées de repas](img/meal1.png)

![entrées combinées de repas](img/meal2.png)

ce qui fait que 2g d’absorption étant attribué au repas 1 et 1g attribué au repas 2.

### Taux minimum d’absorption des glucides

Si l’absorption estimée en glucides d’une entrée de repas est inférieure à ce qui aurait été absorbé en utilisant le taux minimum d’absorption, alors le taux minimum d’absorption est utilisé à la place. Il s’agit de s’assurer que les entrées de repas expirent dans un délai raisonnable.

### Modélisation des glucides actifs restants

Après que les glucides absorbés ont été soustraits de chaque entrée de repas, les glucides restants (pour chaque entrée) sont ensuite prévus pour se détériorer ou être absorbés à l’aide du taux d’absorption minimum. Loop utilise cette prévision pour estimer l’effet (glucides actifs ou activité des glucides) des glucides restants. L’effet glucides peut être exprimé mathématiquement en utilisant les termes décrits ci-dessus:

![entrées combinées de repas](img/combined_bgc.png)

## Effet de correction rétrospective

!!!note ""

    L’effet de correction rétrospective permet à l’algorithme Loop de tenir compte des effets qui ne sont pas modélisés avec les effets de l’insuline et des glucides, en comparant les prédictions historiques à la glycémie réelle.

En plus des effets modélisés de l'insuline et des glucides, il existe de nombreux autres facteurs qui affectent la glycemie (exercice, stress, hormones, etc.). Un grand nombre de ces effets sont actifs pendant une certaine période. En observant ses propres erreurs de prévision, Loop peut estimer l'ampleur de ces effets et, en supposant qu'ils continueront pendant une courte période de temps, les incorporent dans les prévisions pour améliorer l'exactitude des prévisions.

Pour ce faire, Loop calcule une prévision rétrospective avec une heure de début de 30 minutes dans le passé, se terminant à l'heure actuelle. Loop compare les prévisions rétrospectives au changement réel observé dans la glycémie, et la différence se résume à une vitesse de glycemie ou à un taux de différence :

![équation de vitesse de glycémie](img/bgvel.png)

où BG*vel* est un terme de vitesse (mg/dL par 5min) qui représente la différence moyenne de glycémie entre la prévision rétrospective (RF) et la glycémie réelle (BG) au cours des 30 dernières minutes. Ce terme est appliqué à la prévision actuelle des effets d'insuline et de glucides avec une décomposition linéaire au cours de l'heure suivante. Par exemple, le premier point de prévision (t=5) est d’environ 100 % de cette vitesse, le point de prévision dans une demi-heure est ajusté de 50 % de la vitesse, et les points d’une heure ou plus dans le futur ne sont pas affectés par ce terme.

L’effet de correction rétrospective peut être exprimé mathématiquement :

![équation rétrospective de la glycémie](img/bgrc.png)

où BG est le changement prévu de la glycémie avec les unités (mg /dL/5min) à la fois *t* sur la plage de temps de 5 à 60 minutes, et l’autre terme donne le pourcentage de BG*vel* qui est appliqué à cet effet.

L’effet de correction rétrospective peut être illustré par un exemple : si le BG*vel* au cours des 30 dernières minutes était de -10 mg/dl par 5 min, alors l’effet de correction rétrospective au cours des 60 prochaines minutes serait le suivant :

| Minutes par rapport à maintenant (*t =0*) | Pourcentage de BG*vel* appliqué à l’effet RC | ![img/delta_bgrc.png](img/delta_bgrc.png) |
| ----------------------------------------- | -------------------------------------------- | ----------------------------------------- |
| 5                                         | 100%                                         | -10                                       |
| 10                                        | 91%                                          | -9.1                                      |
| 15                                        | 82%                                          | -8.2                                      |
| 20                                        | 73%                                          | -7.3                                      |
| 25                                        | 64%                                          | -6.4                                      |
| 30                                        | 55%                                          | -5.5                                      |
| 35                                        | 45%                                          | -4.5                                      |
| 40                                        | 36%                                          | -3.6                                      |
| 45                                        | 27%                                          | -2.7                                      |
| 50                                        | 18%                                          | -1.8                                      |
| 55                                        | 9%                                           | -0.9                                      |
| -0.9                                      | 0%                                           | 0                                         |

Voici un exemple ci-dessous qui montre l'effet de correction rétrospective lorsque le vel*glycémie* au cours des 30 dernières minutes était de -10mg/dL/5min.

![exemple de graphique rétrospectif glycemie](img/bgrc_graphic.png)

## Effet dynamique de la glycémie

!!!note ""

    L'effet de la dynamique de glycémie intègre une composante de prédiction basée sur l'hypothèse que les tendances récentes de glycémie tendent à persister pendant une courte période. En d'autres termes, le meilleur prédicteur de l'avenir est le passé récent.

La partie de la dynamique de la glycémie de l'algorithme donne du poids ou de l'importance à la glycémie récente pour améliorer les prévisions à court terme. Loop calcule la pente des 3 dernières lectures continues du MGC (c’est-à-dire les 15 dernières minutes) à l’aide d’une régression linéaire. L'utilisation de plusieurs points permet de filtrer le bruit dans les données du MGC tout en répondant rapidement aux situations changeantes. Cette pente de dynamique (pente) est le taux approximatif ou moyen de variation au cours des 15 dernières minutes, si elle est normalisée à 5 minutes pour que les unités soient (mg/dL/5min).

La pente de la dynamique est ensuite mélangée dans les 20 prochaines minutes de glycémie prédite des autres effets (i. ., insuline, glucides, et effets de correction rétrospective). Cela rend les 20 prochaines minutes de glycémie plus sensibles aux tendances récentes de glycémie. Le mélange de la pente de tendance récente dans les 20 prochaines minutes est pondéré, de sorte que le premier point de prédiction (5 minutes dans l'avenir) est fortement influencé par la pente, et l'influence de la pente se dégrade progressivement sur la période de 20 minutes. L'effet de la dynamique peut être exprimé mathématiquement comme:

![équation de la dynamique de glycémie](img/momentum_equation.png)

REMARQUE : Le terme ![blood glucose momentum term](img/momentum_term.png) est également appliqué aux effets combinés d'insuline, de glucides et de correction rétrospective pour obtenir la prédiction du delta glycémique.

L'effet de dynamique peut être illustré par un exemple : si les 3 dernières lectures de glycémie étaient 100, 103 et 106 mg/dL, alors la pente serait de 3 mg/dL par 5 minutes (0.6 mg/dL par minute). La quantité de cette tendance ou de cette pente récente appliquée aux 20 prochaines minutes de prédictions (c.-à-d. les 4 prédictions suivantes des autres effets) sont approximativement 100% (3 mg/dL par 5 min) à 5 minutes, 66% (2 mg/dL par 5 min) à 10 minutes, 33% (1 mg/dL par 5 min) à 15 minutes, et 0% (0 mg/dL par 5 min) à 20 minutes.

En outre, si l'effet combiné de l'insuline, des glucides et de la correction rétrospective est supposé être une constante de 6 mg/dL/5min au cours des 20 prochaines minutes alors l’effet global prévu et la glycémie prévue peuvent être calculés comme suit.

| Minutes par rapport à maintenant (*t =0*) | Pourcentage de pente appliquée à l’effet dynamique | Effet dynamique (3mg/dL/5min) | Pourcentage des autres effets appliqués | Autres effets (insuline, glucides et correction rétrospective) | Effet global (mg/dL/5min) | Glycémie prévue (mg/dL) |
| ----------------------------------------- | -------------------------------------------------- | ----------------------------- | --------------------------------------- | -------------------------------------------------------------- | ------------------------- | ----------------------- |
| 5                                         | 100%                                               | 3                             | 0                                       | 6                                                              | 3                         | 109                     |
| 10                                        | 66.6%                                              | 2                             | 33.3%<                                  | 6                                                              | 4                         | 113                     |
| 15                                        | 33.3%                                              | 1                             | 66.6%                                   | 6                                                              | 5                         | 118                     |
| 20                                        | 0%                                                 | 0                             | 100%                                    | 6                                                              | 6                         | 124                     |

Cet exemple est illustré dans la figure ci-dessous.

![graphique de la dynamique de glycémie](img/momentum_graphic.png)

Il convient également de noter que Loop ne calculera pas la dynamique de la glycémie dans les cas où les données MGC ne sont pas continues (c.-à-d. doivent avoir au moins trois lectures continues de CGM pour dessiner la tendance en ligne droite la mieux adaptée). Il ne calculera pas non plus l'élan glycémique lorsque les trois dernières lectures CGM contiennent des points d'étalonnage. car ils ne sont peut-être pas représentatifs des véritables tendances du taux de glycémie.

## Prédiction de la Glycémie

Tel que décrit dans la section effet de la dynamique, l’effet d’impulsion est mélangé avec les effets de correction insuline, glucide, et rétrospective pour prévoir le changement de la glycémie :

![équation de glucides prévues](img/delta_predicted_equation.png)

Enfin, la prévision ou prédiction de la glycémie BG à l'instant *t* est le BG de la glycémie actuel plus la somme de tous les effets de glycémie BG au cours de l’intervalle de temps [t5, t]:

![ajout de tous les deltas](img/sigma_bg_delta.png)

Chaque effet individuel ainsi que les effets combinés sont illustrés dans la figure ci-dessous. Comme nous l'avons montré, le taux de glycémie augmente légèrement au moment de la prédiction. Par conséquent, la contribution de l’effet de la dynamique de la glycémie tire la prédiction générale des trois autres effets pendant une courte période. La correction rétrospective a un effet d'amortissement sur la prédiction, indiquant que la récente augmentation de la glycémie n’était pas aussi importante que ce qui avait été prédit dans le passé récent.

![courbe d’effets combinés](img/combined_effects.png)
