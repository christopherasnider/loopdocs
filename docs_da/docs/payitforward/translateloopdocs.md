# Oversæt Loopdocs

Denne guide vil forklare, hvordan du kan hjælpe med at oversætte Loopdocs.

Kontroller først om dit sprog er på Loopdoc sprogside. Sproget siden kan findes her: [Loopdocs sprogside](https://loopdocs.github.io/loopdocs/)

Hvis dit sprog er opført her, er oversættelsesprojektet allerede opsat, og du kan blive medlem af oversættelsesteamet ved at følge vejledningen nedenfor.

!!!note "Er dit sprog ikke der?"

    Hvis dit sprog ikke er listet og du gerne vil begynde at oversætte Loopdocs til et nyt sprog, opret venligst et 'issue' på github  [her](https://www.github.com/LoopDocs/loopdocs/issues/new?title=New language request&body=Can you please add [ENTER COUNTRY] for translation.).
    
    Oversættelsesteamet vil derefter konfigurere det for dig. Når den er klar til oversættelse, giver vi dig besked i issuet, og så kan du blive en del af Crowdin-teamet.

## Bliv en del af Crowdin-teamet

1. Gå til [Crowdin](https://crowdin.com/project/loopdoctranslation)
2. Log ind (eller tilmeld dig ved at oprette et nyt login eller bruge din github, facebook eller anden konto)
3. Vælg dit sprog
4. Vælg en fil, der skal oversættes.

Og så er du klar til at begynde at oversætte.

Hvis du ikke har brug crowdin før der er en kort introduktion til Crowdin nedenfor.

Hvis du ønsker en mere detaljeret forklaring på, hvordan du bruger Crowdin, kan du [Crowdin - for oversættere](https://support.crowdin.com/online-editor/)

Du kan også deltage i zulip stream [her](https://loop.zulipchat.com/#narrow/stream/270362-documentation/topic/Translation) , som er dedikeret til oversættelse af loopdocs.

## Crowdin introduktion

Når du har valgt dit sprog og en fil, åbnes Crowdin-editoren.

Crowdin-editoren har 5 hovedområder, som er fremhævet nedenfor: ![Crowdin areas](img/crowdinareas.png)

**1. Document to translate** - indeholder alle sætninger i dokumentet. Du oversætter en sætning ad gangen.</0> Du kan klikke på den sætning, du vil oversætte. Når du klikker på en sætning, ændres de fire andre områder.

Sætningerne er farvet i:

- Rød: Sætninger, der skal oversættes.
- Gul: den sætning, du oversætter.
- Grøn: Sætninger, der er blevet oversat.

**2. Sentence you are translating now** - Viser den sætning du har valgt i dokumentet.

**3. Enter translation here** - this is where you enter you translation. After you have entered your translation click the save button. Crowdin will then take you to the next sentence.

!!!important "Save your work!"

    Husk at klikke på gem-knappen ellers din oversættelse vil ikke blive gemt.

**4. Suggested translation of the sentence** - here you will see a list of sentences that Crowdin suggest to use for your translation. You can even see the translation for other languages at the bottom of the list. If you want to use the suggested translation you can just click it and the sentence goes into the "Enter your translation". Then you can edit the sentence and click save. If you just want to use the suggested sentence and not edit it, you can just click "Use and save".

![Suggestion](img/suggestion.png)

**5. Comments** - Here you can enter you comments about the translation that you are doing. Other users can see it and you can have a discussion about the usage of the sentence.

!!!info "All translators read the comments"

    Det er almindelig praksis at bruge kildesproget til kommentarer i dette tilfælde skal du bruge engelsk.

## At oversætte eller ikke at oversætte

### Teksten "!!!"

In most files there is sections the text "!!!note" or "!!!danger" or something other text with "!!!" in front. It is shown like this in Crowdin:

![image](img/admontion.png)

You should NOT translate the text just after the "!!!" in this case "warning", but you should translate "FAQs" in this case. Sometimes there is no text after "!!!warning" you should still NOT translate this. Some of Crowdins translation suggestions would like to translate the "warning" text.

### Teksten "<0>"

There can be strings in a sentence that looks like this "<0>". Just ignore them and do not translate them. They should be untouched.
