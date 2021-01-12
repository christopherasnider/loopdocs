# Branch FAQs

Denne side er mest for jer som har bygget appen og skal i gang med at opdaterer Loop. I løbet af opdateringen, undrende du dig måske hvad de forskellige branches er osv., ...så lad os prøve at besvare nogle af disse spørgsmål, så godt vi kan.

## Hvad er branches?

Ja, der er en masse "branche" snak i Loop, men konceptet er simpelt.   Grundlæggende set, så er de alle lidt forskellige versioner af Loop - lidt ligesom forskellige versioner af den samme bog.

For virkelig at forstå, hvad branches er, vil vi forklare lidt mere om Loops kode, og hvordan udviklingen fungerer.  Du kan se denne video som vil give en forklaring af processen [her](https://www.youtube.com/watch?v=cWqvYs4Azt0&t=4s).

Loop udviklere har en konto i GitHub kaldet [LoopKit](https://github.com/LoopKit).  Indenfor denne konto har udviklerne har flere "repositories", der i særdeleshed understøtter Loop. Et repository er som en bog - lige nu tænker vi på det som en kogebog. Inden for LoopKit-kontoen er der respositories til Loop selv, LoopDocs, og forskellige andre ting som undersøttende "frameworks", det er 'hjælpe repositores' for at bygge Loop korrekt. For example, Loop's repo has a lot of the info about the app itself; the outward facing things that you interact with. How information is put to you and taken in from you...that's in Loop repository code. Men der er mere end blot en brugergrænseflade til Loop. Loop skal gøre en masse komplekset arbejde som Bluetooth-kommunikation, algoritme matematik, pumpe kommunikation, osv. Loop-appen får hjælp fra frameworks til at gøre de dele af arbejdet. CGMBLEkit for some of the transmitter parts of Loop, RileyLink_ios for the pump managers (talking to the pumps and decoding their information), LoopKit for the algorithm about carbs and insulin curves, etc.

Når du bygger Loop, trækker Loop (i baggrunden) de andre frameworks (7 i alt) ind i byggeprocessen ved hjælp af "Carthage".  Carthage er som en personlig shopper. Du giver det en 'indkøbsliste' (cartfile i Loop kode er indkøbslisten), og det går så ud og henter det for dig under byggeprocessen. Nogle gange har din computer en 'gammel indkøbsliste'... og det kan forårsage byggefejl. Hence the "carthage update" fix in the Build Errors page...that command updates the shopping list to get the right versions of those frameworks.

<p align="center">
<img src="../img/loopkit.png" width="650">
</p>

Så, nu kender du til den generelle struktur i Loop og Loopkit i GitHub. Nu kan vi tage et dybere kig på Loop.

Så lad os forestille os Loop som en kogebog. Udviklerne er forfattere / kokke af opskrifterne (kode) i kogebogen. Forfatterne bruger utallige timer på at teste nye opskrifter, smagsteste og dokumentere forbedringer. De sender et udkast til redaktøren, der kommer med forslag og til sidst er kogebogen færdig. Der er ingen grammatik problemer, ingen slåfejl, billederne er smukke og opskrifterne er lækre. De udgiver bogen, og du ser en flot bog på hylderne. Det kaldes en "release" og det er master branch. Denne bog (kode) er blevet godt testet og er super stabil. Hver gang du laver mad med disse opskrifter, ved du præcis hvad du får og masser af mennesker testet det af for at sikre, at alt smager godt (koden virker). Master branch er stabil og testet.

Men så... går kokkene (udviklerne) ud på en tur. De er inspireret af nye retter og ønsker at tilføje nye opskrifter til den gamle kogebog. (For eksempel ting som omnipod understøttelse og overrides er nye "opskrifter", der blev udviklet siden den sidste master release.) Men processen for at udvikle en opskrift er vanskelig. Masser af forsøg, fejl og test er en del af det. Masser af forskellige ingredienser (kode). Redaktionen afprøver de nye opskrifter og giver feedback (svarende til [Issues List i GitHub](https://github.com/LoopKit/Loop/issues)). Mens opskrifterne er ved at blive udviklet, har de en version af den gamle kogebog, der bliver markeret op ... masser af redigering med 'blyant'.   Rettelser sker ofte, fordi det er det, test af nye opskrifter (kode) handler om. Disse markerede versioner af kogebogen kaldes "dev" branch. Forkortelse for "udvikling" branch. Ligesom navnet siger... er det her udviklingen sker, nye opskrifter og justeringer.

Efter mange test og justeringer, får opskrifterne i sidste ende den rette smag (bugs (fejl) i kode er løst) og flere personer har givet grundigt feedback... og bogen går til forlaget til næste trykning. Kogebogen er genudgivet med et opdateret oplagsnummer og nye opskrifter fremhævet. Når dette sker i Loop, opdateres Loop's master branch med de nye funktioner, der kommer fra Dev (aka, "dev branch koden er flettet ind i master branch"). Når det sker, så får master branch får en anden "release" version (du kan se release historie [her](https://github.com/LoopKit/Loop/releases)) og for én dag ... er dev og master branch nøjagtig de samme. De forbliver de samme, indtil Loop udviklerne begynder at arbejde på den næste pulje af forbedringer, det kunne være en time efter eller dage senere, men processen begynder igen. Udviklerne vil begynde at redigere koden igen og slippe disse redigeringer i dev branch for yderligere udvikling.

## Hvad skete der med Omnipod-test branch?

Omnipod Loop udviklings test (vi taler ikke om det faktiske hacking arbejde, der gik forud for) blev udført af en mindre gruppe af personer i måneder og måneder før offentlig frigivelse af omnipod-test branch. Denne mindre gruppe af personer (flere dusin) var hele tiden opmærksom på deres Omnipod Loops og samlede fejlrapporter sammen. Det var en masse arbejde der blev udført af testere og Pete Schwamb (Loop Developer) for at få koden temmelig stabil og pålidelig.

Da koden kom til en stabil, pålidelig tilstand og var klar til et større publikum, blev omnipod-test branch stillet til rådighed som en "offentlig test" branch. Denne branch var temmelig godt testet før den blev offentlig udgivet, men den ville ikke nødvendigvis være perfekt for alle lige med det samme. There were expectations that some user-interface requests might be asked for after having a wider audience of users.

Also, omnipod-testing branch was not going to undergo a lot of active revisions to it when it was released. The intent was to keep it as a fairly known, unchanged product for people rather than a constantly changing code set...that way if people noted a bug, it would be a more "known" code base to work to debug.

Omnipod-test branch har tjent sit formål som en indledende platform til at teste looping med Omnipod looping. Branchen er officielt blevet pensioneret og er ikke længere nødvendig. Omnipod understøttelsen er nu i den normale master og dev branch.  Tak, omnipod-test branch ... du gjorde det godt. God pension.

## Loop v2.0

Den 31. december 2019, blev Loop v2.0 udgivet (også kendt som "Loop opdateret Master branch"). Det betyder, at kogebogen fra dev branch (for at bruge vores tidligere analogi) blev fusioneret til master branch. Den 31. december var master og dev branch identiske.

Fra denne dato og fremadrettet, vil Dev branch begynde at arbejde på sine nye opskrifter (kode) igen. Dev-branch vil begynde at afvige fra master branch med uprøvede ændringer og udvikling af ny kode. Dev branch kan nu have nogle fejl og tilbageløb som følge af de kode ændringer der bliver fortaget. Det vil ske uden at der bliver givet besked.

Så, de fleste bør begynde at bygge med master branch ... du vil få den nyeste Loop udgivelse, hver gang du bygger med Loop master branch. Master branch vil blive i den samme stabile tilstand, som den har været i et stykke tid. Brug kun udviklings branch, hvis du er interesseret i aktivt at teste ny kode og har mulighed for at spore og dokumenter fejl.

## Hvad er nyt i Loop v2.0?

Dette er absolut et populært spørgsmål og der er flere svar på det spørgsmål...

Hvad er nyt i Loop v2.0? Hvad er forskellen mellem Loop v2.0 og dev branch? Skal jeg opdatere, hvis jeg bruger udviklings branch?

The question about what differences someone will notice between their existing Loop app and the new release...well I can only answer that if I knew which version/branch you are currently using (AND what date you built on if you are using dev branch). Da udviklingsbranchen ændrer sig så ofte, vil den version, som nogen bruger fra oktober 2019, ikke nødvendigvis være den samme som den version, nogen har bygget i november 2019.

So, I'll make a highlights reel compared to the last release and you can check it over to see if any of these seem "new" to you based on the version of Loop you have been using. They are listed roughly in reverse order of when they were merged into dev, so the higher up on the list, the greater the chance is that you haven't seen the feature yet.

### Upload af blodsukker (BS) til Nightscout

Loop v2.0 har mulighed for at uploade dine BS-data direkte til Nightscout. It is a new slider under the CGM configuration section for Dexcom users. After you add your CGM transmitter ID, go back into the CGM info and you'll see a new slider called "Upload Readings."  Technically, Loop's dev branch had that feature for a hot minute before Loop v2.0 was released...but for almost everyone this will be a brand new feature they haven't had before. This feature can help if/when Dexcom's Share servers ever go through another large outage like we had before. If that happens, you can turn on the "Upload Readings" switch and your CGM data will now be in Nightscout even without Share servers working properly. Good practice would be to temporarily disable your Share bridge in Nightscout while Loop is responsible for CGM uploading so that you don't get duplicate data. You can disable Share bridge by logging into your Heroku account, going to the Settings tab, clicking on "reveal config vars" and then deleting the word "bridge" from the ENABLE line.

### A fix for settings loss

iOS 13 brought about a quirky little bug where you could suddenly lose settings in Loop. But, it wasn't just limited to Loop, sometimes people lost Dexcom app settings too. The issue is most common when the phone goes through a power cycle, but it has happened at other times, too. There's a fix for that new bug in Loop now...so that's a good reason to update. (If you encounter that bug before you have a chance to update your Loop app, simply restart the Loop app and your settings should reappear.)

### Spin for Watch Bolus

To prevent an accidental bolus from your Watch app, don't let your kids hold your watch. Just kidding, we've added an even better option. There is a new "spin" to confirm the bolus after you press the bolus button. You'll see a graphic like below on the watch face. As you spin the digital crown, the two triangles will begin to merge. Once they merge, the bolus is confirmed through a little haptic and a white checkmark will appear on the watch screen.

<p align="center">
<img src="../img/spin-to-confirm.png" width="250">
</p>

### Watch recommended bolus

A common code customization is also now no longer needed. Many people used to edit Loop code to have the Watch app provide 100% of the recommended bolus as the auto-filled quantity in the bolus field (default used to be 75%). Loop now offers the 100% auto-filled recommendation, no code customization needed now.

### Recent carbs list on Watch

You can review the recent carb entries on your Apple Watch now. Simply swipe left to see the blood glucose graph screen on your watch. Scroll down with the digital crown to the "active carbs" row beneath the graph, and tap that row. You can see the list of recent carb entries.

### Fix for Medtronic x15 "bolus may have failed" message

A lot of Medtronic x15 users received "bolus may have failed" messages after each bolus. That issue has been fixed and a patched version of Loop is no longer needed. All good!

### Confirmation beeps expanded

Confirmation beeps have been expanded based on user feedback...we heard parents and school nurses really appreciate hearing a beep for not just boluses, but also for suspend/resume commands and editing basal schedule (so you are sure it saved properly). So, confirmation beeps are now for boluses, suspend/resume, and basal schedule edit saves.

### Read Pod Status added

There's a new command in the RileyLink menu for "Read Pod Status" that is analogous to the existing command for Medtronic users. You can query your Pod for its current status info using that command.

### Bug fixes generally

There are a lot of niggly little bug fixes too which were merged in the last couple weeks. The temp basal timestamp for Medtronic Loop (and for older Omnipod Loops, too) had a bug that when Loop reverted to scheduled basals, the timestamp on the HUD's temp basal icon would switch back to the time the Loop was launched (instead of the time the scheduled basal was started again). There are also some new code improvements for handling uncerain boluses for Pod  Also, there are improvements to handle how Loop marks Pod suspend commands that are initiated by users while an active temp basal is in progress.

### User interface improvements

You'll notice dashed lines in the HUD for the CGM value if the CGM data goes older than 15 min (that way you don't accidentally miss the fact that your CGM has failed). The API Secret is hidden after it is saved in Loop Settings now, and if you accidentally leave a trailing slash on the Nightscout URL...Loop will ignore it.  The bolus progress row is new to master branch now, although many of you have been accustomed to that visual in dev branch for awhile now. The "Scenarios" screen that would sometimes appear when a phone was shaken is also disabled by default now. The Issue Report has more information about your Loop app's build date and version so that you can more easily track its build history.

### Common build error squashed

One common build error was caused if there was a space in the Loop folder name after downloading. This problem has been fixed and you will no longer get build errors if you have a space in your Loop folder name.  Ahhhhh! I love it!!!

### Nightscout profile uploading

Loop will upload your basal schedule, ISFs, carb ratios, and override presets from Loop settings to your Nightscout profile. If you ever lose your phone and need to setup Loop brand new...your settings will be easy to find in Nightscout now.

### New languages

Japanese, Danish, Swedish, Vietnamese, Finnish, Portuguese (Brazilian), Polish, and Romanian languages were added to the regional translations for Loop. There are definitely some missing strings that will still need touchups...we will get those fixed up in Loop v2.1 if you all [help report those when you see them](https://www.facebook.com/groups/TheLoopedGroup/permalink/2454410898108895/). Thanks!!

### Non-linear carb model

All branches (master and dev) now use a "non-linear" carb model, so let's give some info about the change.

Previously, the carb model Loop used had a linear absorption predicted with dynamic carbs adjustments. What this means is that food absorption was modeled as a flat, even effect (like the straight grey graph that you'll see in the [Insulin Counteraction Effects chart](../operation/features/ice.md) after you added a carb entry. But looking at large groups of meals' datasets (and supported by personal, anecdotal experiences), food really has a bit more of a non-linear absorption. Meaning, we usually see more of a food impact up-front than the old carb model in Loop predicted.

What did that mismatch mean for us if the model predicts a linear absorption, but the meal actually behaves differently?

1. Bolusing: You've probably seen smaller upfront boluses for meals than you would have preferred. This is because the insulin was predicted to over-power the linear (slower) carb model soon after a bolus is given.
2. Early low temp basals: You've also probably seen a tendency to have early zero basal or low basals set by Loop for the first 30-60 minutes after a meal bolus if you don't have a significant blood glucose spike immediately after the carb entry. This might have been even more obvious for those of you who are regularly waiting to eat after a bolus, too.

With a non-linear absorption model, the carb absorption will more closely match observed blood glucose impacts we've seen after meals. And when the model is more closely matching actual experience, that means the predicted blood glucose curves will do a better job at providing more upfront bolus and not having the tendency to have overly conservative temp basals soon after a meal.

**What should you expect?** Like the description above, you'll likely see more complete bolus recommendations and less low temping after a bolus. With that in mind, if you've made adjustments to your Loop habits or settings to overcome those issues previously, you may want to undo those habits. Like if you shortened carb absorption times to help get larger boluses upfront, you may want to go back to standard times. Keep an eye on things and you should adjust as needed.

**What if you want to go back to the old model?** You will have to edit a line in LoopKit's LoopKit code [here](https://github.com/LoopKit/LoopKit/blob/dev/LoopKit/CarbKit/CarbStore.swift#L207) to use `.linear` if you wanted to go back to the old carb model. If you want to read more about the model, please check out the [Zulipchat thread here](https://loop.zulipchat.com/#narrow/stream/144111-general/topic/Possible.20Carb.20Model.20Changes). But realize that the code edit for changing models would be easiest done using a [LoopWorkspace](../build/loopworkspace.md) because the edit is in one of the frameworks that Loop uses (rather than Loop code itself), so this is one of those instances where you will have to do some work to learn how to use a LoopWorkspace properly.

### Overrides

Loop v2.0 marks the first time Loop master branch has overrides included. Additionally, this release moves overrides setup from the configurations area of Loop settings to the workout icon in the Loop toolbar. There has also been bug squashing in dev branch for overrides over the recent past, so updating is a good idea even if you already have overrides on your current build. Want to learn more about overrides? Read about them [here](../operation/features/workout.md).

### Retrospective Correction always on

Retrospective correction used to be an optional toggle in the algorithm. It is now on by default all the time. It is an important part of the algorithm (helps Loop look at how good/bad its recent prediction curve has been vs reality), and leaving it on made sense anyways.

### Omnipod support

Yes, most of you are already using Omnipod with your Loop...but this is the first time that Loop master branch supports Omnipod users. Please update if you have been using Omnipod-testing branch especially...it's time to get all the bug fixes that we've done in Loop.

### Dark mode support

iOS 13 brought dark mode for application developers, and Loop's developer was all over that. We now have a wickedly cool dark mode Loop for those who prefer the dark side.

### ISF and correction range guardrails and UI change

Loop v2.0 also brings about the first time master branch has the useful scroll wheel to set values of ISF and correction range. This helps mitigate an old bug where backwards entered correction range values would crash Loop app. Also less prone to fat-finger mistakes on entry.

### Simulator pump and CGM

If you don't have compatible gear yet and just want to test Loop app, the new ability to add a simulated pump and/or CGM is a great new feature.

### New style of Dexcom transmitters supported

Dexcom launched a new style of transmitters this summer. The new transmitters took some work by Loop developer (PETE! YEAH!) to get them working in offline Looping, but the fix was pushed into all branches shortly thereafter in August 2019. If you haven't updated your Loop since August 2019 and use a Dexcom G6, you should update now.

## How can I stay current with what's going on in the branches?

Like we said earlier, master branch won't really be changing much. You don't really need to watch that one for changes.

But, dev branch is a constantly shifting, moving place. If you choose to come into a dev branch build...you need to be aware that is what dev does...moves, shakes, changes, and will update code frequently and unannounced in the traditional sense that most users in Looped group or Instagram would see. Developers are not helped by people being in a dev branch if those users are mistakenly thinking of it as a stable master branch with lots of detailed docs to go with it. People should only use a dev branch build if they EDUCATE themselves on the expectations and how to properly manage dev information and updates. People using dev branch should also have regular access to a computer to be able to rebuild quickly if a new bug/fix is identified.

If you choose to use a dev build, you can stay abreast of developments in a number of ways...but they will all require you to do some legwork and keep yourself informed. This is not a situation where you should expect a fancy Loopdocs page updated regularly with current "dev updates"...that's just not the way dev branch works.

### Watch the Loop Repo and Issues list
First, subscribe to the Loop repo's Issues list by "watching" the [Loop repo](https://github.com/LoopKit/Loop). You can choose to watch the repo so that you get emails when new Issues are reported. This is a good way to find out if there's other people reporting odd behavior that you are wondering about. If you use dev and wonder about something you are seeing in Loop, you can check [Issues list](https://github.com/LoopKit/Loop/issues) to see if others are noticing the same. If so, you can help by capturing information and reporting it. Not super helpful to just say "yeah, me too..." but better if you can attach screenshots, Issue Reports from Loop settings, and a thorough description of the problem you are seeing. Be a part of the solution by thoughtfully providing information to help debug.

<p align="center">
<img src="../img/watching.png" width="650">
</p>

### Subscribe to the Zulipchat channels
Second, use [Zulipchat](https://loop.zulipchat.com) forums for Loop. This forum has several "streams" of conversations depending on interest. I highly recommend following the #github channel if you are wanting to watch for code changes. Code changes are called "commits" in GitHub. The #github channel will have an automated post whenever a new commit is made and it will give a brief line description of the commit.

<p align="center">
<img src="../img/zulipchat.png" width="650">
</p>

You can also go directly to the commit history for each of the branches if you'd like.

<a href="https://github.com/LoopKit/Loop/commits/master">Loop master branch commit history</a>

<a href="https://github.com/LoopKit/Loop/commits/dev">Loop dev branch commit history</a>

If you click on the commit, you can see exactly what changes to the code were made. It's an interesting learning experience. In red are the code that is old, in green is the updated code. The line numbers and file names of the edited code are also there to help.

<p align="center">
<img src="../img/commit.png" width="550">
</p>
I don't expect many of you would understand exactly what the edits mean, or how the new code might function...but I bring up the topic of commit history so that you can use that to realize just how often dev is updated. Go ahead and look at the number and frequency of commits in that dev branch...that is why there is no way someone is going to keep a "loopdocs" of dev changes. It's just too much a moving target.

### Keep checking Looped group
Third, keep watching Looped group. Major concerns/issues are brought up there...so no harm in scrolling through and seeing what's going on there.

### LoopDashboard.org
You can always check out the <a href="https://www.loopdashboard.org/">LoopDashboard</a>  which summarize all the github activities in Loops 7 different repositories for dev and master branches. Here you can always see the latest "news" and  the history of Loop.
<br>
On the first page of loopdashboard you can see all the activities in one list, but you can also go to other pages and see more details about commits, issues and pull requests. There are also stats about who is doing the pull requests and commits.<br> The dashboard is updated every 12 hours.
<p align="center">
<img src="../img/loopdashboard.png" width="550">
</p>

### Become familiar with your data sources
Another useful thing if you'll be on dev branches undergoing a lot of active change...know how Loop works and where to look for additional information about what you are seeing. For example, if you see an IOB value that looks odd, you should know to look at the insulin deliveries are stored in Health app. Knowing to pull an Issue Report when you see a problem so you can provide that if asked. Knowing [how to capture debugging logs if the developers ask for that kind of info](https://youtu.be/Ac4MguvUO7M) is also a good skill.

## What is expected in the future?

Roughly speaking...right now (December 31st):

* Master: we know that there will need to be cleanup of the new translations. There were lots of new phrases and development with a lot of new languages, as well. Master (and dev) branch will be updated with fixes for the translations. When those translation fixes are done, there will be a Loop v2.1 released.

* Dev: Dev branch's future development is best tracked by watching and reviewing [pull requests in GitHub](https://github.com/loopkit/loop/pulls). This is the list where code changes are initially proposed and discussed.



