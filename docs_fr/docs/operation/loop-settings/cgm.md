# Ajouter un Lecteur de Glycémie (MGC ou CGM)

Maintenant, nous devons ajouter une Moniteur de glycémie continue (MGC ou CGM en anglais) pour que Loop ait des données Glycémie. À partir de l'écran des paramètres de Loop, sélectionnez `Ajouter un CGM`.

![img/add-cgm.png](img/add-cgm.png)

La sélection standard des choix disponibles est :

* Dexcom G6
* Dexcom G5
* Dexcom G4
* Dexcom Share

!!!info ""

    Si vous avez ajouté une pompe Medtronic plus tôt dans le processus d'installation, alors vous verrez aussi une option pour le capteur Medtronic compatible qui fonctionne avec cette même pompe. Si vous utilisez un capteur MDT compatible, sélectionnez cette option et les données CGM seront téléchargées sur Loop lorsque l’état de la pompe sera mis à jour.

## A propos des identifiants Dexcom Share

!!!danger ""

    Notez que vous n'avez **PAS** besoin des informations de votre compte de partage répertoriées dans les paramètres de Loop si vous utilisez un système G4, G5 ou G6. L'identifiant de l'émetteur est suffisant. En fait, Je vous recommande de laisser votre compte de partage vide afin que vous ne deveniez pas accidentellement dépendants d'Internet pour les données MGC lorsque vous oubliez de mettre à jour votre identifiant de transmetteur lorsque vous démarrez un nouveau transmetteur. Il suffit de laisser les informations d’identification share vides.

Pour toutes les sélections, les identifiants Dexcom Share (en d'autres mots, identifiant du compte) est le même que ce que vous avez utilisé pour vous connecter à l'application Dexcom active sur votre iPhone. **Le compte Dexcom Share n'est pas toujours les mêmes informations de connexion que votre compte Dexcom Clarity .** Pour les utilisateurs G4, le compte Partage se trouve dans l'onglet Compte de l'application. Pour les utilisateurs de G5/G6, malheureusement, il n'y a aucune information dans l'application qui affiche le nom de votre compte. Les informations sont saisies lorsque vous vous connectez pour la première fois à l'application et ne sont plus jamais affichées, ni visibles sur les écrans d'informations. Si vous avez oublié vos informations de compte G5/G6, vous pouvez supprimer l'application Dexcom et la télécharger à nouveau pour essayer de vous connecter. Cela ne provoquera pas de redémarrage des sessions de capteurs en cours.

Si vous ne saisissez pas correctement vos identifiants Share, vous obtiendrez une erreur lorsque Loop tentera d'accéder à votre compte de partage pour récupérer les données du CGM. Ce message d'erreur ressemblera à l'image ci-dessous. Si vous voyez ce message, supprimez votre compte Partage des paramètres de Loop et réessayez... ou laissez-le comme ça et utiliser votre identifiant de transmetteur.

![img/shareclient.jpg](img/shareclient.jpg)

## Dexcom G5 and G6

The Dexcom G5 and G6 options only require the addition of the active transmitter ID, and the matching Dexcom app to be running on the Loop iPhone. You do not have to add your Dexcom Share account credentials, but if you do, make sure they match what you originally entered into your Dexcom app.

When you change transmitters, you will need to select the `Delete CGM` button at the very bottom of the CGM info page in Loop. Then you will select your Dexcom system again and add the new transmitter ID. You cannot just tap on your old transmitter ID to update it.

If you don't update your transmitter ID when you change active transmitters, your Loop will be forced to go to your Dexcom Share server to get your CGM data and will not work without cell or wifi connection. When Loop is using data from Dexcom Share servers, a small cloud will appear above the BG reading in Loop and should tip you off that maybe you forgot to update your transmitter ID.

## Dexcom G4

Dexcom G4 users will need the Dexcom G4 Share2 app active on their iPhone and paired to their Dexcom G4 Share receiver.

## Dexcom Share

The Dexcom Share selection is primarily for people who wish to test Loop function without a local CGM source and who are not running the Dexcom app on their Loop iPhone. This selection will require login access to a Dexcom Share account with live data and active internet connection in order to work.

## Spike Users

Users who are using Spike app to access other CGM types (or to avoid using the Dexcom app), you will need to follow the directions contained within the Spike app in order to build/modify Loop with Spike. Loop does not natively support Spike app and does not currently plan to. You are responsible for modifying or adapting Loop in order to use Spike so that it is an available option as a CGM source.

## Next Step: Configuration

Now that you have added your CGM source, we need to complete the configuration and settings in your Loop. Please head over to the [Configuration page](configurations.md) for guidance with this important part of Loop's setup.
