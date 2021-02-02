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

L'éditeur Crowdin a 5 zones principales qui sont surlignées ci-dessous: ![Crowdin areas](img/crowdinareas.png)

**1. Document à traduire** - contient toutes les phrases dans le document.Vous traduisez une phrase à la fois. Vous pouvez cliquer sur la phrase que vous voulez traduire. When you click a sentence the 4 other areas change.

The sentences are colored in:

- Red: Sentences that needs translating.
- Yellow: the sentence you are translating.
- Green: Sentences that has been translated.

**2. Sentence you are translating now** - Shows the sentence you have selected in the document.

**3. Enter translation here** - this is where you enter you translation. After you have entered your translation click the save button. Crowdin will then take you to the next sentence.

!!!important "Save your work!"

    Remember to click the save button otherwise your translation will not get saved.

**4. Suggested translation of the sentence** - here you will see a list of sentences that Crowdin suggest to use for your translation. You can even see the translation for other languages at the bottom of the list. If you want to use the suggested translation you can just click it and the sentence goes into the "Enter your translation". Then you can edit the sentence and click save. If you just want to use the suggested sentence and not edit it, you can just click "Use and save".

![Suggestion](img/suggestion.png)

**5. Comments** - Here you can enter you comments about the translation that you are doing. Other users can see it and you can have a discussion about the usage of the sentence.

!!!info "All translators read the comments"

    It is standard practice to use the source language for comments in this case you should use english.

## To translate or not to translate

### The "!!!" text

In most files there is sections the text "!!!note" or "!!!danger" or something other text with "!!!" in front. It is shown like this in Crowdin:

![image](img/admontion.png)

You should NOT translate the text just after the "!!!" in this case "warning", but you should translate "FAQs" in this case. Sometimes there is no text after "!!!warning" you should still NOT translate this. Some of Crowdins translation suggestions would like to translate the "warning" text.

### The "<0>" text

There can be strings in a sentence that looks like this "<0>". Just ignore them and do not translate them. They should be untouched.
