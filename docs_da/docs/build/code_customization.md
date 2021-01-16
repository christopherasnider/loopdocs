# Code Customizations

Baseret på Loop-brugernes oplevelse er der nogle tilpasninger, som du måske vil indarbejde forud for opbygningen af din Loop-app og Apple Watch-appen.  Disse tilpasninger skal ske, før du bygger Loop-appen på din iPhone, de kan ikke foretages inde fra selve appen.

!!!info "Line numbers may change"

    Every effort will be made to update the line numbers as the code is updated, but there may be times where the screenshots and line numbers are slightly different than the current version of Loop code.  These instructions have been updated for Loop v2.0 master branch. If you can't find the same exact line on that line number listed, then look nearby and you'll likely find it just a couple lines away.

## Disable Authentication for Bolusing

Afhængigt af dine iPhone-præferencer og -model, kan du have Face ID eller Touch ID aktiveret.  Disse sikkerhedsfunktioner vil også blive brugt til at godkende bolus levering i Loop.  Du kan vælge at deaktivere godkendelse (dvs. ikke kræver Face ID, Touch ID eller adgangskode til bolus) gennem følgende kode tilpasning:

 Ændre linje 201 i Loop>>Se controllere>>BolusViewController.swift.  Tilføj `false &&` som vist på skærmbilledet nedenfor:

![img/custom-id.png](img/custom-id.png)

## Default Carb Absorption Times

![img/carb_screen.png](img/carb_screen.png)

Loops standard carb absorptionstider er baseret på det høje, medium, og lave glykæmiske indeks absorptionskurver præsenteret i <i>Think Like A Pancreas</i> af Gary Scheiner.  I øjeblikket slikkepind (hurtig) ikon er indstillet til 2 timer, taco (medium) ikon for 3 timer, og pizza (langsom) ikon for 4 timer.

Hvis du vil ændre disse standarder, kan du gøre det i Loop Core>>LoopSettings.swift Linje 16.

![img/carb_times.png](img/carb_times.png)

For eksempel, hvis du ønskede at gøre slikkepind en 30 minutters absorption og pizza en 5 timers absorption, vil redigeringen se ud nedenfor:

![img/carb_times_example.png](img/carb_times_example.png)

## Exponential Insulin Curve

De eksponentielle insulinkurve modeller (Rapid-Acting Adult, Rapid-Acting Barn, og Fiasp) standard til en insulinvarighed på 360 minutter. .men de forskellige kurvers maksimale aktivitet er forskellig som følger:

* Hurtigtvirkende voksenkurve topper ved 75 minutter
* Hurtigtvirkende barnekurve topper efter 65 minutter
* Fiasp kurven topper ved 55 minutter

Hvis du vil tilpasse disse værdier, kan du justere dem på linje 34-38 i LoopCore>>Insulin>>ExponentialInsulinModelPreset.swift.

![img/exponential.png](img/exponential.png)

## Loop Logo

Hvis du vil have et andet applogo end standardgrøn cirkel til din Loop-app, kan du nemt tilpasse dette.  For at gøre det nemt at generere de korrekte størrelser af ikoner, kan du bruge et websted som [appicon.build](http://www.appicon.build/) eller [appicon.co](https://appicon.co/) og bare trække og slippe dit kildebillede. Kildebilledet skal være 1024 pixel x 1024 pixel.  Sitet vil e-maile dig en zip-fil eller automatisk downloade et sæt af filer.  Fremhæv og kopiér indholdet af det Appicon.appiconset, du har sendt, herunder filen Contents.json

Naviger nu til den tilsvarende loop-mappe (DefaultAssessts.xcassets, Appicon.appiconset) som vist nedenfor.

![img/appicon1.png](img/appicon1.png)

Erstat indholdet af Appicon.appiconset med dine kopierede billeder og Contents.json-filen.

![img/appicon2.png](img/appicon2.png)

Du kan bekræfte den vellykkede ændring ved at kigge i Xcode under Loop -> DefaultAssets.xcassets -> Appicon.  Du bør se dit brugerdefinerede logo i Appicon-sættet nu.  Du får muligvis også vist en gul advarsel om, at der er "unassigned children", afhængigt af de billeder, som appikongeneratorværktøjet har produceret. Advarslen om "unassigned children" forhindrer ikke din app i at bygge, det er simpelthen fordi der er flere størrelser af billeder, end Loop-appen bruger.  Du kan bare lade de "unassigned children" være.

![img/appicon3.png](img/appicon3.png)

Og nu vil du være den stolte nye ejer af et brugerdefineret Loop-ikon.

![img/unicorn-logo.jpeg](img/unicorn-logo.jpeg)

## Adjust the sensitivity of Watch's digital crown for carb and bolus entry

Hastigheden af ændringen af carb og bolus indtastning, når du bruger den digitale krone kan ændres. Du skal redigere to linjer i filer i WatchApp Extension>>Controllers mappe.  I BolusInterfaceController.swift redigere linje 191, og i AddCarbsInterfaceController.swift redigere linje 249. Værdien 1/24 er forholdet mellem rotationer af kronen og mængden af ændring i værdien. Ændring til 1/12 ville betyde, at dobbelt så mange drej ville være nødvendigt for den samme mængde af carb eller bolus.

![img/sensitivity1.png](img/sensitivity1.png)

![img/sensitivity2.png](img/sensitivity2.png)
