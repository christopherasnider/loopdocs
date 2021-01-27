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

    Pour les Loopers (les utilisateurs de Loop)...la conséquence d'une mise à jour d'iOS n'a rien d'immédiate. Your Loop app won't die, it will keep humming along. </br></br>BUT, before you ***<u>update or rebuild</u>*** your Loop app on that phone, you will likely need to update your macOS and Xcode applications because of the newer iOS.  And you will need to do the updates/checks in a certain order:</br></br>
    1st: Check if your macOS has updates</br></br>
    2nd: Check for an Xcode update.</br></br>

The chart below is a helpful visual of the minimum versions you'll need based on your iOS.

* macOS: If you are running an iPhone with iOS 14, you need to make sure your macOS is 10.15.4 at a minimum as the first step. If you don't have the minimum version, go to [Step 1 Compatible Computer](step1.md#check-your-macos) and follow directions for updating your macOS.

* Xcode: Now that your macOS is updated to 10.15.4 minimum, the App Store in your computer will have Xcode 12.0.1 (or newer) available for you to download/update.

If you have a brainfart and leave your macOS back at 10.15.2...the App Store won't even tell you Xcode version 12 or newer exists. That's why it is important to do the macOS updates FIRST. I can't tell you how many people post for help saying "I'm trying to update my Loop app but am getting errors." If I ask what Xcode version they have and if they've updated, the response is "I don't have any Xcode updates available in the App Store...so I must be running the most current version." When actually what's happened is they have forgotten to check for macOS updates FIRST and therefore cannot see the needed Xcode update yet.

(Source for the chart is [wikipedia](https://en.wikipedia.org/wiki/Xcode))

![img/minimum-related.png](img/minimum-related.png)

## What happens if you try using too old of Xcode?

It isn't some catastrophic failure if you try to build with an outdated Xcode without realizing it. You'll see a pretty obvious error message during your Loop build that says "Could not locate device support files." That messages is telling you that your iOS on the phone requires you to get a newer version of Xcode to be able to build Loop onto that phone.

![../img/device-support-files.jpg](img/device-support-files.jpg)

So, if you see that error message realize you may have to update your macOS to be able to see the newest Xcode version that you will need. Make sure to check that chart to see what your minimum versions are for the iOS you are running on your iPhone.

## Next Step: Xcode Preferences

Now you are ready to move onto Step 9 to [work on Xcode Preferences](step9.md).
