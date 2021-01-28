# Étape 8 : Télécharger Xcode

!!!danger "Temps estimé"
    - 45 minutes à 2 heures, selon la connexion à Internet...mais vous n'avez pas besoin de surveiller le téléchargement.

!!!info "Résumé"
    - Après s'être assuré que votre macOS est à jour pour iOS de votre iPhone (voir les informations ci-dessous), téléchargez Xcode depuis l'application App Store de votre ordinateur.

!!!warning "FAQs"
    - **« Pourquoi mon Xcode n'est-il pas installé ?** Je ne peux pas voir votre ordinateur pour savoir exactement pourquoi... Les deux raisons les plus courantes sont : (1) le manque de connexion à Internet ou (2) le manque d'espace libre sur le disque dur de l'ordinateur. Xcode est un téléchargement assez costaud... et a besoin d’un peu plus d’espace encore pour bien se décompresser et s’installer. Mieux pour essayer d’avoir environ 20-25 Go d’espace libre sur votre disque dur avant de commencer à se sentir à l'aise sur ce point. Si vous avez peu d'espace libre, j'ai vu des échecs d'installation pour cette raison. Vous pouvez vérifier votre espace libre en cliquant sur `À propos de ce Mac` (comme à l'étape 1) et en cliquant sur l'onglet `Stockage`.

Aujourd'hui, c'est facile, mais c'est probablement la plus longue de toutes les étapes en termes de temps....uniquement parce que le téléchargement prend un certain temps. La bonne nouvelle, c’est que tu n’as pas à surveiller ça. Au lieu de cela, vous pouvez commencer le téléchargement et tout simplement vaquer à d'autres occupations.

Xcode est une application gratuite pour les ordinateurs Apple. Xcode va transformer le code Loop "brut" en une application iOS et l'installer sur votre iPhone/iPod. **Assurez-vous d'avoir mis à jour votre macOS ET vérifiez le bouton `Mises à jour du logiciel` avant de continuer... en d'autres termes, assurez-vous que vous avez fait le travail de l'étape 1.**

Ouvrez votre App Store dans votre ordinateur et recherchez Xcode...vous allez en télécharger un tout neuf ou mettre à jour une installation existante. La version minimale dont vous avez besoin dépendra de l'iOS de votre iPhone. Le numéro de version doit être affiché dans la description « quoi de neuf » comme indiqué dans l’image ci-dessous. Il s'agit d'un gros téléchargement, donc ne vous attendez pas à ce que ce soit rapide.

![../img/xcode.png](img/xcode.png)

!!!warning "Deux choses importantes"

    1. La version minimale de Xcode dont vous avez besoin dépend de la version d'iOS de votre iPhone. Plus la version d’iOS est récente, plus vous aurez besoin d'une version récente d'Xcode. </br></br>La version la plus récente d'iOS (14+) nécessite Xcode 12 et macOS 10.15.4 au minimum</br></br>
    2. La dernière version de Xcode **peut également vous obliger à mettre à jour votre version de macOS**. Si vous avez une ancienne version de macOS, alors l’App Store ne vous montrera pas qu’une nouvelle version de Xcode est disponible. Cela peut créer de la confusion parce que votre iOS pourrait nécessiter un Xcode plus nouveau, mais l’App Store ne le montrera pas comme disponible.

## Comment toutes les versions minimales sont-elles reliées les unes aux autres?

Le plus souvent ce qui se passe, c'est que les gens vont mettre à jour leur iOS sur les iPhones plus souvent qu'ils ne mettent à jour leur macOS ou Xcode.  Vous savez comment ça se passe... vous tapotez un jour sur votre téléphone et il dit qu'il y a une nouvelle version d'iOS disponible pour votre téléphone. Voulez vous le mettre à jour maintenant? Ou vous le rappelez plus tard? Ou peut-être que vous avez même le réglage sur votre téléphone pour installer automatiquement les mises à jour iOS.

Parce que la mise à jour semble si anodine et nous menons tous des vies occupées, nous oublions qu’il pourrait y avoir des conséquences liées aux mises à jour iOS.

!!! danger « Loop et les mises à jour iOS»

    Pour les Loopers (les utilisateurs de Loop)...la conséquence d'une mise à jour d'iOS n'a rien d'immédiate. Votre application Loop ne mourra pas, elle continuera à fredonner. </br></br>MAINTENANT, avant que vous ***<u>mettez à jour ou reconstruisez</u>*** votre application Loop sur ce téléphone, vous devrez probablement mettre à jour vos applications macOS et Xcode à cause de nouveaux iOS.  Et vous devrez faire les mises à jour/vérifications dans un certain ordre :</br></br>
    1er : Vérifiez si votre macOS a des mises à jour</br></br>
    2nd: Vérifiez s'il y a une mise à jour de Xcode.</br></br>

Le graphique ci-dessous est un visuel utile des versions minimales dont vous aurez besoin en fonction de votre iOS.

* macOS : Si vous utilisez un iPhone avec iOS 14, vous devez vous assurer que votre macOS est 10.15.4 au minimum comme première étape. Si vous n'avez pas la version minimale, allez à [l'Étape 1 Compatibilité de l'Ordinateur](step1.md#check-your-macos) et suivez les instructions pour mettre à jour votre macOS.

* Xcode : Maintenant que votre macOS est mis à jour à 10.15.4 minimum, l'App Store sur votre ordinateur indiquera Xcode 12.0.1 (ou une version plus récente) disponible pour le téléchargement/mise à jour.

Si vous avez un oubli et laissez votre macOS à 10.15.2...l'App Store ne vous proposera même pas Xcode version 12 ou plus récente. C’est pourquoi il est important de faire les mises à jour macOS EN PREMIER. Je ne peux pas vous dire combien de personnes postent pour obtenir de l’aide en disant " J’essaie de mettre à jour mon application Loop mais j'ai des messages d'erreurs. » Si je demande quelle version Xcode ils ont et s'ils ont mis à jour, la réponse est "Je n'ai aucune mise à jour Xcode disponible dans l'App Store... donc c'est que je dois utiliser la version la plus récente." Alors qu'en fait ce qui s'est passé, c'est qu'ils ont oublié de vérifier les mises à jour macOS EN PREMIER et donc ne peuvent pas encore voir la mise à jour Xcode nécessaire.

(La source du graphique est [wikipedia](https://en.wikipedia.org/wiki/Xcode))

![img/minimum-related.png](img/minimum-related.png)

## Que se passe-t-il si vous essayez d’utiliser un trop vieux Xcode?

Ce n'est pas un erreur catastrophique si vous essayez de construire avec un Xcode obsolète sans vous en rendre compte. Vous verrez un message d'erreur assez évident pendant votre compilation de Loop qui dit "Impossible de localiser les fichiers de support du périphérique." Ce message vous disent que votre iOS sur le téléphone vous oblige à obtenir une nouvelle version de Xcode pour être en mesure de construire Loop sur ce téléphone.

![../img/device-support-files.jpg](img/device-support-files.jpg)

Donc, si vous voyez ce message d'erreur, vous devrez peut-être mettre à jour votre macOS pour pouvoir voir la dernière version de Xcode dont vous aurez besoin. Assurez-vous de vérifier ce graphique pour voir quelles sont vos versions minimales pour l’iOS que vous utilisez sur votre iPhone.

## Prochaine étape : Préférences d'Xcode

Maintenant vous êtes prêt à passer à l'étape 9 pour [travailler sur les Préférences Xcode](step9.md).
