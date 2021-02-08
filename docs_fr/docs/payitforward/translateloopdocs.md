# Traduire Loopdocs

Ce guide vous expliquera comment vous pouvez aider à traduire Loopdocs.

Vérifiez d’abord si votre langue se trouve dans la page de langue Loopdoc. La page de langue peut être trouvée ici : [Page de langue Loopdocs](https://loopdocs.github.io/loopdocs/)

Si votre langue est listée ici, le projet de traduction est déjà configuré et vous pouvez rejoindre l'équipe de traduction en suivant le guide ci-dessous.

!!!note "Votre langue n'est pas là ?"

    Si votre langue n'est pas listée et que vous voulez commencer à traduire Loopdocs dans une nouvelle langue, veuillez soumettre un problème sur github [here](https://www.github.com/LoopDocs/loopdocs/issues/new?title=New language request&body=Can you please add [ENTER COUNTRY] for translation.).
    
    L’équipe de traduction le mettra en place pour vous. Une fois qu'il sera prêt pour la traduction, nous vous informerons et vous pourrez rejoindre l'équipe Crowdin.

## Rejoignez l'équipe Crowdin

1. Aller dans [Crowdin](https://crowdin.com/project/loopdoctranslation)
2. Connectez-vous (ou inscrivez-vous en créant une nouvelle connexion ou utilisez votre compte github, facebook ou autre compte)
3. Sélectionnez votre langue
4. Sélectionnez un fichier à traduire.

Et vous êtes prêt à traduire.

Si vous n'avez jamais utilisé crowdin avant, il y a une courte introduction à Crowdin ci-dessous.

Si vous voulez une explication plus détaillée sur la façon d'utiliser Crowdin, veuillez visiter [Crowdin - pour les traducteurs](https://support.crowdin.com/online-editor/)

Vous pouvez également rejoindre le flux zulip [ici](https://loop.zulipchat.com/#narrow/stream/270362-documentation/topic/Translation) dédié à la traduction de loopdocs.

## Introduction à Crowdin

Lorsque vous avez sélectionné votre langue et un fichier, l'éditeur Crowdin s'ouvre.

L'éditeur Crowdin a 5 zones principales qui sont surlignées ci-dessous: ![Zones Crowdin](img/crowdinareas.png)

**1. Document à traduire** - contient toutes les phrases dans le document.Vous traduisez une phrase à la fois. Vous pouvez cliquer sur la phrase que vous voulez traduire. Lorsque vous cliquez sur une phrase, les 4 autres zones changent.

Les phrases sont colorées en:

- Rouge : phrases qui doivent être traduites.
- Jaune : la phrase que vous traduisez.
- Vert : phrases qui ont été traduites.

**2. La phrase que vous traduisez maintenant** - Affiche la phrase que vous avez sélectionnée dans le document.

**3. Entrez la traduction ici** - c'est là que vous entrez votre traduction. Après avoir entré votre traduction, cliquez sur le bouton Enregistrer. Crowdin vous emmènera alors à la phrase suivante.

!!!important "Sauvegardez votre travail!"

    N'oubliez pas de cliquer sur le bouton Enregistrer sinon votre traduction ne sera pas enregistrée.

**4. Traduction suggérée de la phrase** - ici vous verrez une liste de phrases que Crowdin suggère d'utiliser pour votre traduction. Vous pouvez même voir la traduction d'autres langues en bas de la liste. Si vous souhaitez utiliser la traduction suggérée, vous pouvez simplement cliquer dessus et la phrase va dans la zone « Entrez votre traduction ». Ensuite, vous pouvez modifier la phrase et cliquer sur Enregistrer. Si vous voulez juste utiliser la phrase suggérée et ne pas la modifier, vous pouvez simplement cliquer sur "Utiliser et enregistrer".

![Suggestion](img/suggestion.png)

**5. Commentaires** - Ici vous pouvez entrer vos commentaires sur la traduction que vous faites. D'autres utilisateurs peuvent le voir et vous pouvez avoir une discussion sur l'utilisation de la phrase.

!!!info "Tous les traducteurs voient les commentaires"

    Il est de pratique courante d'utiliser la langue source pour les commentaires dans ce cas, vous devriez utiliser l'anglais.

## Traduire ou ne pas traduire

### Le texte "!!!"

Dans la plupart des fichiers, il y a des sections le texte "!!!note" ou "!!!danger" ou quelque chose de texte avec "!!!" en premier. Il est affiché comme cela dans Crowdin :

![image](img/admontion.png)

Vous ne devriez PAS traduire le texte juste après le "!!!" dans ce cas "warning", mais vous devez traduire "FAQ" dans ce cas. Parfois, il n'y a pas de texte après "!!!warning" vous ne devriez toujours PAS le traduire . Certaines suggestions de traduction de Crowdins voudraient traduire le texte "warning".

### Le texte "<0>"

Il peut y avoir des chaînes dans une phrase qui ressemble à ceci "<0>". Il suffit de les ignorer et de ne pas les traduire. Ils doivent rester intacts.
