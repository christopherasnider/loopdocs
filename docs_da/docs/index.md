# Velkommen til Loop

<img src="img/phones.png" width="300" alt="iPhone Screenshot" />
<img src="img/watch.png" alt="Apple Watch Screenshots" />

## Introduktion

[Loop](https://github.com/LoopKit/Loop) er en app-skabelon til opbygning af et automatiseret insulinleveringssystem.

Den app er bygget oven på [LoopKit](https://github.com/LoopKit/LoopKit). LoopKit er et sæt af rammer, der leverer datalagring, hentning og beregning samt standardvisninger, der bruges i Loop.

!!!warning "Vigtigt"

    Forstå venligst, at dette projekt:

    - Er meget eksperimentel
    - Er ikke godkendt til behandling

      **Du tager det fulde ansvar for at bygge og køre dette system og gør det på egen risiko.**

Ved hjælp af open source Loop-appskabelonen kan du opbygge et insulinleveringssystem, der bruger specifikke kommercielle og open source-hardware- og softwareteknologier til at samle insulinpumpen, kontinuerlig glukosemonitor (CGM) og insulindoseringsalgoritmen for at skabe en kontinuerlig levering af insulin.  Dette "Loop" forudsiger fremtidig glukose baseret på basalrater, kulhydratindtag, aktiv insulin, og aktuelle CGM-aflæsninger.  Disse glukose prognoser giver Loop de oplysninger, der er nødvendige for at anbefale en midlertidig basalrate for at opnå det ønskede blodsukkerniveau.  Systemet kan enten fungere som en »åben loop« ved at vise anbefalinger til brugeren som skal godkendes eller som en »lukket loop« ved automatisk at indstille den anbefalede midlertidige basale rate.

Du bør gennemføre dette projekt i etaper. For eksempel, først “open loop” til at gøre dig bekendt med hvordan Loop virker. Også, undersøge koden for at sikre, at du forstår, hvad det anbefaler og hvorfor. Når du går videre til “lukket-loop”, gøre det sikkert ved at starte med passende sikkerhedsgrænser og kun gå videre til højere grænser efter flere dage uden lavt blodsukker. Stil spørgsmål på nuværende tidspunkt om, hvorfor Loop kommer med anbefalingerne.  Det bør svare til de beslutninger du selv ville træffe.  Hvis Loop kommer med anbefalinger, som er anderledes, end du selv ville gøre, så prøv at finde ud af hvorfor.

## Udviklings Historik

Loop er udviklet som et open source, delt projekt.  For en virkelig interessant artikel om historien bag Loop udvikling, Tjek denne [Historie af Loop og LoopKit](https://medium.com/@loudnate/the-history-of-loop-and-loopkit-59b3caf13805) indlæg, skrevet af Loop udvikler Nate Racklyeft.  Projektet fortsætter med at være et arbejde i et fællesskab af brugere; vedligeholdt og forbedret af frivillige.

## Sådan bruges disse dokumenter

* Brug navigationsmenuen øverst på skærmen til at finde de oplysninger, du leder efter.
* En indholdsfortegnelse for den aktuelle side vises altid på venstre side af skærmen.
* Du kan søge på Loop Docs-webstedet ved at klikke på <img src="img/search_icon.png" width="50px" /> ikonet.

    <img src="img/search_example.png" width="400" />

## Hold dig orienteret!

[Sign up for the Loop Users announcement list](https://groups.google.com/forum/#!forum/loop-ios-users) to stay informed of critical issues that may arise.

Join the Zulipchat at [https://loop.zulipchat.com](https://loop.zulipchat.com)

There is also a [Looped Facebook Group](https://www.facebook.com/groups/TheLoopedGroup/?fref=nf) that you might wish to join for support.  When you request to join the group, please remember to check your messages box on facebook and respond to the message.

## Bidrag

Please consider submitting any updates and improvements to the documentation that you want to share by submitting a Pull Request to the [loopdocs repo](https://github.com/LoopKit/loopdocs). For more information on how to contribute to an open-source project, this [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/) guide may be useful. Also, please review the Loop [LICENSE](https://github.com/LoopKit/Loop/blob/master/LICENSE.md) and Loop [CODE_OF_CONDUCT](https://github.com/LoopKit/Loop/blob/master/CODE_OF_CONDUCT.md).
