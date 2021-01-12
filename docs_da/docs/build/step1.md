# Trin 1: Kompatibel Computer

!!!danger "Tidsestimat"
    * 5 minutter, hvis der allerede er Mojave eller Catalina macOS
    * 30-60 minutter, hvis det er nødvendigt at installere macOS-opdateringer

!!!info "Resume"
    * Tjek din macOS og sørg for at den er Mojave eller Catalina. **Hvis du har den nyeste iOS-version på iPhonen, der vil bruge Loop... så har du brug for Catalina.**
    * Brug ikke nogen af beta- macOS-versionerne. (Hvis du ikke ved, hvad det betyder, så fortvivl ikke... det betyder, at du ikke bruger ét)
    * Hvis din macOS ikke er Mojave eller Catalina, skal du kontrollere, om du kan opdatere din macOS til en af dem.
    * Hvis du ikke kan opgradere din eksisterende computer til Mojave eller Catalina, skal du låne computer, Patcher værktøj, eller måske en ny / brugt computer kompatibel med Mojave eller Catalina.
    * Tjek `Softwareopdateringen` for at se, om din computer har opdateringer tilgængelige, siden du først installerede den.

!!!warning "FAQs"
    * **"Kan jeg bruge en pc eller Windows-computer? Jeg ejer ikke en Apple-computer."** Ja...sådan da Se venligst [denne FAQ om brug af Virtual Machine](https://loopkit.github.io/loopdocs/faqs/FAQs/#can-i-use-a-pc-or-windows-computer-to-build). Windows-computere med AMD-processorer vil ikke være i stand til at opbygge med succes ved hjælp af Virtual Machine, så sørg for at tjekke din processor type før du indleder Virtual Machine sti.
    * **"Hvad kan jeg gøre, hvis min computer er for gammel til at blive opgraderet til Catalina?** Du kan tage et kig på ved hjælp af [Catalina Patcher](http://dosdude1.com/catalina/), men dette er helt på egen hånd og ikke en del af disse instruktioner. Bare tilbyder svaret på FAQ... det er op til dig at læse om patcher værktøj og hvilke risici det kan indebære for dig.
    * **"Kan jeg låne en andens Apple-computer?"** Ja, se [dette FAQ om at låne en computer](https://loopkit.github.io/loopdocs/faqs/FAQs/#do-i-need-to-own-my-own-apple-computer) for at lære mere.
    * **"Hvor ofte skal jeg bruge computeren?** Computeradgang er kun påkrævet, når du i første omgang installerer Loop app eller opdaterer til en nyere Loop release. Du behøver IKKE adgang til en Apple-computer for at fejlfinde eller ændre Loop indstillinger, såsom basalrater eller kulhydratsforhold.

## Nye M1 chip Apple-computere

Ja, de nyeste Apple-computere, der netop blev udgivet i november 2020, er kompatible med Loop building. Der er ET lille skridt du skal være opmærksom på med de nye computere, og det er på Trin 7 Installer Homebrew side. Jeg har fremhævet i en farvet bokse på denne side de dele, som M1 brugere bliver nødt til at gøre. Jeg lover, det er hurtigt og smertefrit.

Og med det...Jeg er meget jaloux, at du har den nye computer. De vil gøre Loop bygning ekstremt hurtigt, og tidsestimaterne nævnt øverst vil være latterligt langsommere end du vil opleve.

## Big Sur MacOS

Ja, Big Sur er kompatibel med Loop building...Jeg arbejder på at opdatere denne side for det snart. Afvent.

## Catalina vs Mojave, hvilken har du brug for?

Har du brug for Catalina eller Mojave? Svaret vil afhænge af iOS på din iPhone, du vil installere Loop på.

**Hvis du har iOS 12.4 til 13.2**, kan du bruge macOS 10.14.4 (Mojave) eller 10.15.2 eller nyere (Catalina).

**Hvis du har iOS 13.4 eller nyere**, vil du ikke være i stand til at bruge Mojave og vil have brug for Catalina på et minimum. Med andre ord, du har brug for macOS 10.15.2 på et minimum for at bygge Loop på en iPhone, der kører iOS 13.4 eller nyere.

!!!danger "iOS dikterer din computer behov" sagt kort for Loopers ... Jo mere opdateret du holder din iOS, jo mere opdateret skal din computer og macOS også være. Det er ikke nødvendigvis en dårlig ting, og du kan ikke undgå iOS opdateringer for evigt ... du bare nødt til at være opmærksom på, hvordan de relaterer til hinanden, hvis din computer er "at kommet op i årene".

## Tjek din macOS
Du har brug for en Apple-computer, der har mindst den minimale macOS-version som beskrevet ovenfor; Mojave macOS 10. 4.4 (eller nyere) eller Catalina macOS 10.15 (eller nyere). For at finde ud af, hvilken version du har installeret, skal du klikke på det lille Apple-ikon i computerens øverste venstre hjørne og vælge `Om denne Mac`. Det betyder ikke noget, hvis computeren er en MacBook, iMac, macMini, etc ... bare så længe den har det mindste du har brug for.

Hvis computeren ikke har den nødvendige minimumversion, skal du kontrollere knappen `Software Update` på skærmen for at se, om du kan opdatere.

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/macosx.png" width="500">
</p>

Hvis din computer ikke giver dig mulighed for at opdatere til de nyere macOS (med andre ord du sidder fast på ældre versioner) ... det er meget muligt, at Apple har besluttet din computer er for gammel til at køre den nyeste og bedste. Hvor gammel er for gammel? Det vil afhænge af din computer model og år som vist nedenfor:

<p align="center">
<img src="https://loopkit.github.io/loopdocs/build/img/mojave-minimum.png" width="750">
</p>

## Næste trin: Kompatibel iPhone/iPod touch

Nu er du klar til at gå videre til trin 2 for at kontrollere, om du har en [kompatibel iPhone/iPod touch](https://loopkit.github.io/loopdocs/build/step2/).
