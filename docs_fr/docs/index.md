# Bienvenue dans Loop

![img/phones.png](img/phones.png) ![img/phones.png](img/watch.png)

## Introduction

[Loop](https://github.com/LoopKit/Loop) un modèle d’application pour construire un système automatisé d’administration d’insuline. C'est une pierre reposant sur le mur de travail accompli par beaucoup d'autres.  
L'application est construite sur [LoopKit](https://github.com/LoopKit/LoopKit). LoopKit est un ensemble de frameworks qui fournissent le stockage, la récupération et le calcul de données, ainsi que des contrôleurs de vue standard utilisés dans Loop.

!!!warning "Important" Veuillez comprendre que ce projet : - est hautement expérimental - n'est pas approuvé pour la thérapie **Vous assumez l'entière responsabilité de la construction et de l'exécution de ce système et vous le faite à vos propres risques.**

À l’aide du modèle d’application loop open-source, vous pouvez construire un système d’administration d’insuline qui utilise des technologies matérielles et logicielles commerciales et open-source spécifiques pour réunir la pompe à insuline, le moniteur de glucose continu (CGM) et l’algorithme de dosage de l’insuline pour créer un debit basal continu de l’insuline « Loop ».  Ce loop prédit la glycémie future en fonction des horaires de débit de basale, de l'apport en glucides, de l'insuline active dans le corps et des lectures MGC (CGM en anglais) actuelles.  Ces prévisions de glycémie fournissent en boucle les informations nécessaires pour recommander un taux basal temporaire pour atteindre une fourchette de glucose ciblée dans le futur.  Le système peut soit fonctionner comme une « boucle ouverte » en faisant des recommandations à l’utilisateur pour son approbation avant d’adopter soit comme une « boucle fermée » en définissant automatiquement le débit de basal temporaire recommandé. Vous devez entreprendre ce projet par étapes. Par exemple, commencez par la « boucle ouverte » pour vous familiariser avec le fonctionnement de Loop. Étudiez également le code pour vous assurer que vous comprenez ce qu'il recommande et pourquoi. Puis lorsque vous passez à la « boucle fermée », faites-le en toute sécurité en commençant par des limites de sécurité appropriées et en ne progressant vers des limites plus fortes qu'après plusieurs jours hypoglycémie. Veuillez vous poser des questions à ce stade sur la raison pour laquelle Loop fait ses recommandations.  Elles devraient être similaire aux décisions thérapeutiques que vous prendriez vous-même.  Si les recommandations qu’il fait sont différentes de ce que vous feriez, essayez de comprendre pourquoi.

## Historique du développement

Loop a été développé comme un projet open-source et partagé.  Pour une lecture vraiment intéressante sur l’histoire du développement de Loop, consultez ce [Histoire de Loop et LoopKit](https://medium.com/@loudnate/the-history-of-loop-and-loopkit-59b3caf13805) écrit par le développeur Loop Nate Racklyeft.  Le projet continue d’être un travail d’amour par une communauté d’utilisateurs; entretenus et améliorés par des volontaires.

## Comment utiliser ces documents

* Utilisez la barre de navigation en haut pour trouver le lien que vous cherchez.
* Une table des matières pour la page courante est toujours affichée sur le côté gauche de l'écran.
* Vous pouvez chercher dans le Site Loop Docs en cliquant sur l'icône <img src="img/search_icon.png" width="50px" />. ![img/search_example.png](img/search_example.png)

## Restez dans la boucle ! (Loop en anglais)

[Inscrivez-vous à la liste d'annonces des utilisateurs de Loop](https://groups.google.com/forum/#!forum/loop-ios-users) pour rester informé des problèmes critiques qui peuvent survenir. Rejoignez le Zulipchat via [https://loop.zulipchat.com](https://loop.zulipchat.com) Il y a aussi un [groupe Facebook Loop](https://www.facebook.com/groups/TheLoopedGroup/?fref=nf) que vous pourriez souhaiter rejoindre pour obtenir de l'aide.  Lorsque vous demandez à rejoindre le groupe, n'oubliez pas de vérifier votre boîte de messages sur facebook et de répondre au message.

## Contribuer

Veuillez envisager de soumettre toutes les mises à jour et améliorations à la documentation que vous souhaitez partager en soumettant une "Pull Request" au dépôt [loopdocs](https://github.com/LoopKit/loopdocs). Pour plus d'informations sur la façon de contribuer à un projet open-source, ce guide [Comment contribuer à l'Open Source](https://opensource.guide/how-to-contribute/) peut être utile. Aussi, veuillez consulter la [LICENSE](https://github.com/LoopKit/Loop/blob/master/LICENSE.md) Loop et le [CODE_OF_CONDUCT](https://github.com/LoopKit/Loop/blob/master/CODE_OF_CONDUCT.md) de Loop.
