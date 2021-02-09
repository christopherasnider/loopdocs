# Loop plante à l'ouverture

Si votre application Loop plante immédiatement à l'ouverture, vous avez un problème qui doit être résolu. Qu'est-ce que je veux dire par "plantage"? Que votre application Loop se tourne immédiatement vers un écran blanc et s'éteint, vous ramenant sur l'écran principal de votre iPhone. Aucune actio ne vous permettra de garder votre application Loop ouverte.

Il n'y a que deux causes possibles à cela:

1. L'application a expiré, ou
2. Une plage de correction a été enregistrée à l'envers.

## Application expirée

Votre application Loop a une date d'expiration. La date d'expiration dépendra du type de compte développeur qui a signé l'application.

* Si vous construisez votre application avec un compte gratuit, elle expirera dans 7 jours.
* Si vous créez votre application avec un compte payant, elle expirera dans 12 mois.

De nombreuses personnes construisent *accidentellement* avec leur ancien compte gratuit même après avoir acheté un compte payant. Comment pouvez-vous savoir avec quel compte vous avez signé? L'equipe de signature gratuite comporte le terme `(Personal Team)` après votre nom.

Si votre application expire, il vous suffit de brancher votre téléphone sur l’ordinateur et d’appuyer à nouveau sur le bouton "Build" de votre projet. Cela va reconstruire l'application. Si vous voulez passer à une équipe de signature payante avant de reconstruire, assurez-vous de vérifier à nouveau quelle équipe de signature est sélectionnée avant de reconstruire.

## Intervalle de correction incorrect

!!!info "Important à savoir"

    Les intervalles de correction dans Loop doivent être saisis dans le format minimu maximum... en d'autres termes, BAS-HAUT. Si vous entrez dans l'intervalle à l'envers, votre application va se planter dès que Loop essayera d'utiliser cette plage de cible inversée... cela peut être immédiatement ou à un moment dans le futur, selon le moment du moment de l'utilisation de cette entrée et le son horaire.

    * Un exemple de plage de correction correctement saisie : 100-120 mg/dL
    * Un exemple de plage de correction incorrecte : 120-100 mg/dL

    S’il vous plaît être prudent lors de l’entrée dans la plage de correction. Suivez les suggestions de texte grisé dans l'interface utilisateur Loop qui disent `min-max`.

Ce problème a été résolu dans la dernière version de Loop.  Si votre application plante à cause d'une plage de correction mal définie, vérifiez que vous exécutez Loop v2.0.

Si vous continuez à connaître des plantages similaires avec Loop v2.0 ou plus tard, générez un [rapport de problème](overview.md#issue-report) et soumettez-le aux développeurs Loop via GitHub.
