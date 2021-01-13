## Tilpasning af kode
Baseret på Loop-brugernes oplevelse er der nogle tilpasninger, som du måske vil indarbejde forud for opbygningen af din Loop-app og Apple Watch-appen.  Disse tilpasninger skal ske, før du bygger Loop-appen på din iPhone, de kan ikke foretages inde fra selve appen.

!!!info "Line numbers may change"

    Every effort will be made to update the line numbers as the code is updated, but there may be times where the screenshots and line numbers are slightly different than the current version of Loop code.  These instructions have been updated for Loop v2.0 master branch. If you can't find the same exact line on that line number listed, then look nearby and you'll likely find it just a couple lines away.

### Deaktivér godkendelse til bolus

Afhængigt af dine iPhone-præferencer og -model, kan du have Face ID eller Touch ID aktiveret.  Disse sikkerhedsfunktioner vil også blive brugt til at godkende bolus levering i Loop.  Du kan vælge at deaktivere godkendelse (dvs. ikke kræver Face ID, Touch ID eller adgangskode til bolus) gennem følgende kode tilpasning:

 Ændre linje 201 i Loop>>Se controllere>>BolusViewController.swift.  Tilføj `false &&` som vist på skærmbilledet nedenfor:

<p align="center">
<img src="../img/custom-id.png" width="750">
</p>

### Standard kulhydrate absorbering tider

<img style="float: right;" width="200" src="../img/carb_screen.png" />

Loops standard carb absorptionstider er baseret på det høje, medium, og lave glykæmiske indeks absorptionskurver præsenteret i <i>Think Like A Pancreas</i> af Gary Scheiner.  I øjeblikket slikkepind (hurtig) ikon er indstillet til 2 timer, taco (medium) ikon for 3 timer, og pizza (langsom) ikon for 4 timer.

Hvis du vil ændre disse standarder, kan du gøre det i Loop Core>>LoopSettings.swift Linje 16.

<p align="center">
<img src="../img/carb_times.png" width="750">
</p>

For eksempel, hvis du ønskede at gøre slikkepind en 30 minutters absorption og pizza en 5 timers absorption, vil redigeringen se ud nedenfor:

<p align="center">
<img src="../img/carb_times_example.png" width="750">
</p>

### Eksponentiel insulinkurve
De eksponentielle insulinkurve modeller (Rapid-Acting Adult, Rapid-Acting Barn, og Fiasp) standard til en insulinvarighed på 360 minutter. .men de forskellige kurvers maksimale aktivitet er forskellig som følger:

* Hurtigtvirkende voksenkurve topper ved 75 minutter
* Hurtigtvirkende barnekurve topper efter 65 minutter
* Fiasp kurven topper ved 55 minutter

Hvis du vil tilpasse disse værdier, kan du justere dem på linje 34-38 i LoopCore>>Insulin>>ExponentialInsulinModelPreset.swift.

<p align="center">
<img src="../img/exponential.png" width="750">
</p>

### Loop Logo
Hvis du vil have et andet applogo end standardgrøn cirkel til din Loop-app, kan du nemt tilpasse dette.  For at gøre det nemt at generere de korrekte størrelser af ikoner, kan du bruge et websted som [appicon.build](http://www.appicon.build/) eller [appicon.co](https://appicon.co/) og bare trække og slippe dit kildebillede. Kildebilledet skal være 1024 pixel x 1024 pixel.  Sitet vil e-maile dig en zip-fil eller automatisk downloade et sæt af filer.  Fremhæv og kopiér indholdet af det Appicon.appiconset, du har sendt, herunder filen Contents.json

Naviger nu til den tilsvarende loop-mappe (DefaultAssessts.xcassets, Appicon.appiconset) som vist nedenfor.  

<p align="center">
<img src="../img/appicon1.png" width="650">
</p>

Erstat indholdet af Appicon.appiconset med dine kopierede billeder og Contents.json-filen.

<p align="center">
<img src="../img/appicon2.png" width="650">
</p>

Du kan bekræfte den vellykkede ændring ved at kigge i Xcode under Loop -> DefaultAssets.xcassets -> Appicon.  Du bør se dit brugerdefinerede logo i Appicon-sættet nu.  Du får muligvis også vist en gul advarsel om, at der er "unassigned children", afhængigt af de billeder, som appikongeneratorværktøjet har produceret. Advarslen om "unassigned children" forhindrer ikke din app i at bygge, det er simpelthen fordi der er flere størrelser af billeder, end Loop-appen bruger.  Du kan bare lade de "unassigned children" være.

<p align="center">
<img src="../img/appicon3.png" width="650">
</p>

Og nu vil du være den stolte nye ejer af et brugerdefineret Loop-ikon.

<p align="center">
<img src="../img/unicorn-logo.jpeg" width="350">
</p>

### Juster følsomheden af Watch's digitale krone for carb og bolus indtastning
Hastigheden af ændringen af carb og bolus indtastning, når du bruger den digitale krone kan ændres. Du skal redigere to linjer i filer i WatchApp Extension>>Controllers mappe.  I BolusInterfaceController.swift redigere linje 191, og i AddCarbsInterfaceController.swift redigere linje 249. Værdien 1/24 er forholdet mellem rotationer af kronen og mængden af ændring i værdien. Ændring til 1/12 ville betyde, at dobbelt så mange drej ville være nødvendigt for den samme mængde af carb eller bolus.

<p align="center">
<img src="../img/sensitivity1.png" width="800">
</p>

<p align="center">
<img src="../img/sensitivity2.png" width="800">
</p>


