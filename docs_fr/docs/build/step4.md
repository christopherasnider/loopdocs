# Étape 4 : Compatibilité du MGC (CGM)

!!!danger "Temps estimé"

    - 10 minutes pour lire cette page

!!!info "Résumé"

    - Si vous utilisez un système CGM Dexcom G4 Share, G5 ou G6 ... vous êtes déjà prêt à utiliser Loop.
    - Si vous utilisez un capteur Medtronic compatible avec une pompe Medtronic, elle même compatible Loop, vous pouvez utiliser Loop.
    - Si vous avez un Eversense...vous ne pouvez pas utiliser Loop avec ce CGM.
    - Si vous utilisez un FreeStyleLibre...vous devrez utiliser une version modifiée de Loop

!!!warning "FAQs"

    - **"Qu'en est-il des capteurs Libre ?"** Les capteurs Libre ne sont pas conçus pour être des moniteurs de glucose en continu. Toute utilisation de capteurs Libre comme moniteurs de glucose en continu implique l’utilisation d’applications tierces (Xdrip ou Spike) et de lecteurs (BluCon ou Miao Miao). Les développeurs de Loop n'ont pas vu de données démontrant des protections suffisantes de ces lecteurs et applications pour se sentir à l'aise en ajoutant l'intégration dans le code principal de Loop pour ces appareils. Si vous utilisez un capteur Libre, vous devrez utiliser une branche « non-principale » de Loop que quelqu’un (ou vous-même) a modifiée pour permettre une utilisation avec ces capteurs/applications.
    - **"Qu'en est-il d'Eversense?"** L'application d'Eversense ne s'intègre pas avec Apple Santé, et les protocoles de communication pour Eversense n'ont pas été décompilé / analysé par ingénierie inverse non plus. Par conséquent, Eversense n’est pas compatible avec l’utilisation loop actuellement.

Un moniteur de glucose continu (CGM) fournit à Loop des lectures en continu de glycémie. Ces lectures permettent à Loop de prédire quelle est la tendance actuelle de glycémie et de prédire la glycémie future en fonction de l’entrée des glucides et des paramètres que vous avez saisies à Loop. Voici les types de CGMs compatibles avec Loop. Les lectures de CGM sont une partie requise du faire fonctionner Loop. Si votre Loop n’est pas en mesure de récupérer les données de votre capteur, elle ne sera pas en mesure de boucler.

## Les CGM Dexcom G5 et G6 ![G5](img/g5.jpg)

Avec les Dexcom G5 et G6 votre iPhone reçoit les données MGC directement via l'application Dexcom en Bluetooth. Aucun de ces deux systèmes ne nécessite l'utilisation d'un récepteur autonome. Pour que Loop fonctionne, vous aurez besoin de l'application Dexcom en cours d'exécution.

## Le CGM Dexcom G4 avec Share Receiver ![G4 With Receiver](img/g4_receiver.png)

Dexcom G4 Share system transmits CGM data from the transmitter to a Dexcom G4 Share Receiver. The receiver, in turn, connects to the Dexcom Share2 app on your iPhone via Bluetooth. The Share2 app uploads CGM data to the Dexcom servers. For Loop to function, you will need the Dexcom app running.

## Medtronic CGM ![Enlite](img/enlite.png)

The Minimed Enlite CGM, available with the Medtronic 522/722, 523/723, and 554/754, wirelessly sends blood glucose readings to the pump. Loop can read the Medtronic CGM data directly from the pump using the RileyLink.

## Offline Use

Offline use means using Loop when there is no cell data or internet available. Loop does not require any special setup to operate offline. You will not need to do anything special if you go camping or find yourself out in the wilderness. For offline Loop use, the iPhone's Bluetooth still needs to be active; and for Dexcom users, the Share2, G5, or G6 app also still needs to be open (but don't have to be actively "sharing" to the internet). If you put your iPhone into Airplane mode, remember to turn Bluetooth back on to keep your Loop running. If your offline use is failing, chances are you have forgotten to update your transmitter ID in Loop settings when you changed transmitters.

## Dexcom Servers

In some rare instances, the Loop may fail to eavesdrop on the Bluetooth transmissions of the CGM systems.  When that happens, the Loop can pull directly from Dexcom Servers to get the data (assuming you have entered your Share account information in the Loop settings and have Share turned on). When Loop is operating in this mode, you will see a small cloud in the CGM reading in the Loop app. Operating in this mode requires a working internet or cell connection.

## CGMs not natively supported in Loop

Libre (with BluCon or Miao Miao), Eversense, Medtronic Guardian sensors, etc. Yes, there are other CGM systems available out there. Loop does not natively support those CGMs.  If you would like to use one of those alternate CGMs and Loop...you will need to look into third-party integrations to allow Loop to access the blood glucose data.  These docs do not cover the alternate methods of unsupported CGM systems or apps like Spike.

## Next Step: Order a RileyLink

Now you are ready to move onto Step 5 to [Order a RileyLink](step5.md).
