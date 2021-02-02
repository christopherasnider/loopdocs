# Loop plante à l'ouverture

Si votre application Loop plante immédiatement à l'ouverture, vous avez un problème qui doit être résolu. Qu'est-ce que je veux dire par "plantage"? Que votre application Loop se tourne immédiatement vers un écran blanc et s'éteint, vous ramenant sur l'écran principal de votre iPhone. Aucune actio ne vous permettra de garder votre application Loop ouverte.

Il n'y a que deux causes possibles à cela:

1. L'application a expiré, ou
2. A correction range was saved backward.

## Expired app

Your Loop app has an expiration date. The expiration date will depend on the type of developer account that signed the app.

* If you build with a free account, your app will expire after 7 days.
* If you build with a paid account, your app will expire after 12 months.

Many people *accidentally* build with their old free account even after buying a paid account. How can you tell which you're signing with? The free signing team has the `(Personal Team)` listed after your name in the signing team.

If your app expires, you simply need to plug your phone back into the computer and press the play button on your project again. This will rebuild. If you want to change to a paid signing team before rebuilding, please make sure to double-check which signing team is selected before building again.

## Incorrectly entered correction range

!!!info "Important To Know"

    Correction ranges in Loop are to be entered in minimum-maximum...in other words, LOW-HIGH. If you enter the range backward, your app will crash as soon as Loop tries to use that backward target range...that could be immediately or at a time in the future, depending on when the backwards entry is in your schedule.

    * An example of a properly entered correction range: 100-120 mg/dL
    * An example of an improperly entered correction range: 120-100 mg/dL

    Please be careful when entering in the correction range. Follow the greyed out text suggestions in the Loop user interface that say `min-max`.

This issue has been fixed in the latest release of Loop.  If your app crashes because of an improperly set correction range, verify you are running Loop v2.0.

If you continue to experience similar crashes with Loop v2.0 or later, generate an [Issue Report](overview.md#issue-report) and submit it to the Loop developers via GitHub.
