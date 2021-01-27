# Étape 6 S'inscrire dans le programme de développement Apple

!!!danger "Temps estimé"
    - 15-20 minutes pour remplir les formulaires d'inscription
    - jusqu'à 2 jours pour attendre l'e-mail de confirmation que l'inscription a été activée

!!!info "Résumé"
    - Si vous avez décidé d'utiliser un compte développeur payant, vous devez vous inscrire dès maintenant. Rendez-vous sur le site [Apple Developer](https://developer.apple.com/programs/enroll/) pour vous inscrire à un compte individuel.
    - Si vous avez décidé d'utiliser un compte développeur gratuit, vous n'avez pas besoin de faire quoi que ce soit maintenant. Nous allons revenir dessus plus tard.

!!!warning "FAQs"
    - **"Puis-je utiliser le compte Apple Developer de quelqu'un d'autre ?"** Bonne question...la réponse est [ici](/faqs/FAQs/#can-i-use-someone-elses-apple-developer-account).
    - **"Est-ce que j'utilise mon identifiant Apple ou l'identifiant Apple de mon enfant pour m'inscrire au programme Apple Developer ?** L'identifiant Apple que vous utilisez pour vous inscrire au programme développeur n'a pas besoin d'être le même ID Apple que l'iPhone qui va utiliser Loop , par exemple, un parent installant Loop sur l'iPhone des enfants. En règle générale, pour l’inscription du développeur, utilisez l’identifiant Apple de la personne qui va construire l’application Loop.
    - **« Combien de temps faut-il pour que mon compte Apple Development soit actif après mon inscription ?** Une fois que vous vous êtes inscrit, assurez-vous de rechercher un e-mail de confirmation. Apple says it can take up to 24-48 hours to confirm and setup a new Apple developer account, however some people have had the process only take minutes. It can vary. One SURE way to make it take longer? Use a different credit card to pay for the Apple Developer account enrollment than is already associated with the Apple ID you'll be enrolling with. When you do that, I've heard Apple makes you send in a xerox copy of your driver's license and a bunch of other hassle.

In order to build your own Loop app, you will need to use an Apple developer account.  You will have two options for an individual account; free or paid.

## Free Developer Account

If you decide to use a **FREE** developer account, here's what you need to know:

1. Loop apps signed with a free developer team will expire after 7 days.  On the 7th day, your Loop app will simply turn white when you open it and then immediately close. To rebuild the Loop app, you will have to find a computer and rebuild the app onto your iPhone again. You cannot rebuild the app on day 5 (when it is convenient, for example)...hoping to reset the 7-day clock.  The app will still expire on the 7th day from when it was first signed and created.</br></br>
2. If you decide to switch to a paid account after trying out the free account, you will need to rebuild your Loop app in order to sign it with the new paid account.</br></br>
3. You will have to do an extra step during the build process to remove Siri and Apple Push capabilities in order to build with free accounts. Because free accounts do not have access to Apple Push notifications, you will also not be able to use remote overrides through Nightscout.</br></br>

## Paid Developer Account

If you decide to use a **PAID** developer account, here's what you need to know:

1. Loop apps signed with a paid developer team will last for a full year.</br></br>
2. The paid developer account is $99 per year and is default set to auto-renew annually. You can change that selection in your developer account settings at any time.</br></br>
3. If your household has multiple Loop users, only one developer account is needed.  That one developer account can be used to sign multiple Loop apps.</br></br>

## Switching from Free to Paid Memberships

In summary: This is no problem trying a free account first before you decide to buy a paid developer account. If you start with a free account, you'll build a Loop app (let's call it FreeLoop). When you switch to a paid account, you'll be building a totally new and separate Loop app onto your phone (let's call it PaidLoop). The two apps will look identical on your phone, but they will be functionally separate from each other...ideally you want to delete the FreeLoop app before using the PaidLoop app.

PaidLoop will know nothing about the settings and information you had stored in FreeLoop, so you will need to re-enter all your settings (basal rates, ISF, carb ratios, etc.) and configurations into the new PaidLoop. It will also not connect or control any pods you are currently using with the old FreeLoop you had installed.

So, when switching from Free to Paid Loop builds...try to remember that you'll have the best luck by (1) timing it at pod change time and (2) take screenshots of your old app's settings so that you can enter them into the new app.

## Enrolling

Paid account enrollment is all through Apple's Developer Program website. Go to the [Apple Developer website](https://developer.apple.com/programs/enroll/) to enroll in an individual paid account. If you instead want the free account, you don't have to do anything on that website. You'll just wait for Step 8 Xcode Preferences and we will get your free account then.

## Next Step: Install Homebrew

Now you are ready to move onto Step 7 to [install Homebrew](step7.md).
