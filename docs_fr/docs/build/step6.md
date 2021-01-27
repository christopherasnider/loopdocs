# Étape 6 S'inscrire dans le programme de développement Apple

!!!danger "Temps estimé"
    - 15-20 minutes pour remplir les formulaires d'inscription
    - jusqu'à 2 jours pour attendre l'e-mail de confirmation que l'inscription a été activée

!!!info "Résumé"
    - Si vous avez décidé d'utiliser un compte développeur payant, vous devez vous inscrire dès maintenant. Rendez-vous sur le site [Apple Developer](https://developer.apple.com/programs/enroll/) pour vous inscrire à un compte individuel.
    - Si vous avez décidé d'utiliser un compte développeur gratuit, vous n'avez pas besoin de faire quoi que ce soit maintenant. Nous allons revenir dessus plus tard.

!!!warning "FAQs"
    - **"Puis-je utiliser le compte Apple Developer de quelqu'un d'autre ?"** Bonne question...la réponse est [ici](/faqs/FAQs/#can-i-use-someone-elses-apple-developer-account).
    - **"Est-ce que j'utilise mon identifiant Apple ou l'identifiant Apple de mon enfant pour m'inscrire au programme Apple Developer ?** L'identifiant Apple que vous utilisez pour vous inscrire au programme développeur n'a pas besoin d'être le même ID Apple que l'iPhone qui va utiliser Loop , par exemple, un parent installant Loop sur l'iPhone des enfants. En règle générale, pour l’inscription du développeur, utilisez l’identifiant Apple de la personne qui va construire l’application Loop.
    - **« Combien de temps faut-il pour que mon compte Apple Development soit actif après mon inscription ?** Une fois que vous vous êtes inscrit, assurez-vous de rechercher un e-mail de confirmation. Apple dit que cela peut prendre jusqu'à 24-48 heures pour confirmer et configurer un nouveau compte développeur Apple, Cependant, certaines personnes ont vu la procedure ne prendre que quelques minutes. Cela peut varier. Une manière sure to rallonger la procedure ? C'est d'utiliser une carte de crédit différente pour payer l'inscription au compte Apple Developer que celle déjà associée à l'identifiant Apple avec lequel vous vous inscrirez. Quand vous faites ça, j'ai entendu dire qu'Apple vous demande d'envoyer une copie de votre permis de conduire et un tas d'autres tracas.

Afin de construire votre propre application Loop, vous devrez utiliser un compte développeur Apple.  Vous aurez deux options pour un compte individuel; gratuit ou payant.

## Compte développeur gratuit

Si vous décidez d'utiliser un compte développeur **GRATUIT** , voici ce que vous devez savoir :

1. Les applications Loop signées avec des comptes de développeurs gratuite expireront au bout de 7 jours.  Le 7ème jour, votre application Loop deviendra simplement vide lorsque vous l'ouvrirez puis se refermera immédiatement. Pour reconstruire l'application Loop, vous devrez trouver un ordinateur et reconstruire l'application sur votre iPhone à nouveau. Vous ne pouvez pas reconstruire l'application le jour 5 (quand c'est pratique, par exemple)... en espérant réinitialiser l'horloge de 7 jours.  L’application expirera toujours le 7ème jour à partir du moment où elle a été signée et créée pour la première fois.</br></br>
2. Si vous décidez de passer à un compte payant après avoir essayé le compte gratuit, vous devrez reconstruire votre application Loop pour la signer avec le nouveau compte payant.</br></br>
3. Vous devrez effectuer une étape supplémentaire pendant le processus de construction pour supprimer les fonctionnalités Siri et Apple Push pour de construire Loop avec des comptes gratuits. Parce que les comptes gratuits n'ont pas accès aux notifications Push d'Apple, vous ne pourrez pas non plus utiliser les substitutions à distance via Nightscout.</br></br>

## Compte développeur payant

Si vous décidez d’utiliser compte développeur **PAYANT** , voici ce que vous devez savoir :

1. Les applications Loop signées avec un compte/équipe de développeurs payants dureront une année complète.</br></br>
2. Le compte de développeur payant est de 99 € (ou 99 $) par année et est par défaut configuré pour le renouvellement automatique annuel. Vous pouvez modifier ce choix dans les paramètres de votre compte développeur à tout moment.</br></br>
3. Si votre foyer a plusieurs utilisateurs de Loop, un seul compte développeur est nécessaire.  Ce seul compte développeur peut être utilisé pour signer plusieurs applications Loop.</br></br>

## Passage d'un abonnement gratuit à un payant

En résumé: Ce n’est pas un problème d’essayer un compte gratuit d’abord avant de décider d’acheter un compte développeur payant. Si vous commencez avec un compte gratuit, vous allez construire une application Loop (appelons-la FreeLoop). Lorsque vous passez à un compte payant, vous construirez une application Loop totalement nouvelle et distincte sur votre téléphone (appelons-la PaidLoop). Les deux applications seront identiques sur votre téléphone, mais elles seront fonctionnellement séparées l'une de l'autre... Idéalement vous voulez supprimer l'application FreeLoop avant d'utiliser l'application PaidLoop.

La version PaidLoop ne saura rien sur les paramètres et les informations que vous avez stockés dans FreeLoop, vous devrez donc saisir à nouveau tous vos paramètres (débits de basal, ISF, ratios de glucides, etc.) et configurations dans le nouveau PaidLoop. Il ne connectera pas ou ne contrôlera pas non plus les pods que vous utilisez actuellement avec l’ancien FreeLoop que vous aviez installé.

Donc, lorsque vous passez de Free à PaidLoop... Rappelez-vous que vous aurez la meilleure chance en (1) choisissant le moment du changement de pod et (2) en prenant des captures d'écran des paramètres de votre ancienne application afin que vous puissiez les saisir dans la nouvelle application.

## Inscription

L’inscription à un compte payant se fait sur le site Web du Programme des développeurs d’Apple. Rendez-vous sur le site [Apple Developer](https://developer.apple.com/programs/enroll/) pour vous inscrire à un compte individuel payant. Si vous voulez plutôt le compte gratuit, vous n’avez rien à faire sur ce site. Vous allez juste attendre l'étape 8 Les Préférences d'Xcode et nous utiliserons alors votre compte gratuit.

## Prochaine étape : Installer Homebrew

Maintenant vous êtes prêt à passer à l'étape 7 pour [installer Homebrew](step7.md).
