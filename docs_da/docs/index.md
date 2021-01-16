# Velkommen til Loop

![img/phones.png](img/phones.png) ![img/phones.png](img/watch.png)

## Introduktion

[Loop](https://github.com/LoopKit/Loop) er en app-skabelon til opbygning af et automatiseret insulinleveringssystem.   LoopKit er et sæt af rammer, der leverer datalagring, hentning og beregning samt standardvisninger, der bruges i Loop. !!!warning "Vigtigt" Forstå venligst: dette projekt: - Er yderst eksperimentel - Er ikke godkendt til terapi **Du tager det fulde ansvar for at opbygge og køre dette system og gør det på egen risiko.**

Ved hjælp af open source Loop-appskabelonen kan du opbygge et insulinleveringssystem, der bruger specifikke kommercielle og open source-hardware- og softwareteknologier til at samle insulinpumpen, kontinuerlig glukosemonitor (CGM) og insulindoseringsalgoritmen for at skabe en kontinuerlig levering af insulin.  Dette "Loop" forudsiger fremtidig glukose baseret på basalrater, kulhydratindtag, aktiv insulin, og aktuelle CGM-aflæsninger.  Disse glukose prognoser giver Loop de oplysninger, der er nødvendige for at anbefale en midlertidig basalrate for at opnå det ønskede blodsukkerniveau.  Systemet kan enten fungere som en »åben loop« ved at vise anbefalinger til brugeren som skal godkendes eller som en »lukket loop« ved automatisk at indstille den anbefalede midlertidige basale rate. Du bør gennemføre dette projekt i etaper. For eksempel, først “open loop” til at gøre dig bekendt med hvordan Loop virker. Også, undersøge koden for at sikre, at du forstår, hvad det anbefaler og hvorfor. Når du går videre til “lukket-loop”, gøre det sikkert ved at starte med passende sikkerhedsgrænser og kun gå videre til højere grænser efter flere dage uden lavt blodsukker. Stil spørgsmål på nuværende tidspunkt om, hvorfor Loop kommer med anbefalingerne.  Det bør svare til de beslutninger du selv ville træffe.  Hvis Loop kommer med anbefalinger, som er anderledes, end du selv ville gøre, så prøv at finde ud af hvorfor.

## Udviklings Historik

Loop has been developed as an open-source, shared project.  For a really interesting read about the history of Loop development, check out this [History of Loop and LoopKit](https://medium.com/@loudnate/the-history-of-loop-and-loopkit-59b3caf13805) post, written by Loop developer Nate Racklyeft.  The project continues to be a labor-of-love by a community of users; maintained and improved by volunteers.

## Sådan bruges disse dokumenter

* Er meget eksperimentel
* A Table of Contents for the current page is always displayed on the left side of the screen.
* You can search the Loop Docs site by clicking the ![img/search_icon.png](img/search_icon.png) icon. ![img/search_example.png](img/search_example.png)

## Hold dig orienteret!

[Sign up for the Loop Users announcement list](https://groups.google.com/forum/#!forum/loop-ios-users) to stay informed of critical issues that may arise. Join the Zulipchat at [https://loop.zulipchat.com](https://loop.zulipchat.com) There is also a [Looped Facebook Group](https://www.facebook.com/groups/TheLoopedGroup/?fref=nf) that you might wish to join for support.  When you request to join the group, please remember to check your messages box on facebook and respond to the message.

## Bidrag

Please consider submitting any updates and improvements to the documentation that you want to share by submitting a Pull Request to the [loopdocs repo](https://github.com/LoopKit/loopdocs). For more information on how to contribute to an open-source project, this [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/) guide may be useful. Also, please review the Loop [LICENSE](https://github.com/LoopKit/Loop/blob/master/LICENSE.md) and Loop [CODE_OF_CONDUCT](https://github.com/LoopKit/Loop/blob/master/CODE_OF_CONDUCT.md).
