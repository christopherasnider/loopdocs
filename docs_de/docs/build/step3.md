# Schritt 3: Kompatible Pumpen

!!!Gefahr "Geschätzte Zeit"
    - Omnipod Benutzer: 3 Sekunden, um sich zu erinnern, welchen PDM du verwendest hast.
    - Medtronic-Benutzer: 10 Minuten um eine Batterie einzulegen und Modell und Firmware anzuschauen
    - Benutzer anderer Pumpen: 5 Tage, um eine E-Mail an Freunde zu senden und sie zu bitten, ihre Schränke nach alten Medtronic-Pumpe zu durchforsten oder um deine Versicherung anzurufen und mit der Autorisierung für Omnipod zu beginnen

!!! Info "Zusammenfassung"
    - Wenn du einen großen klobigen PDM mit eingebautem BG-Meter hast... du kannst deine Pods für Loop verwenden.
    - Wenn du einen schlanken Touchscreen Android-artigen PDM hast... du kannst deine Pods NICHT für Loop verwenden.
    - Wenn du eine Medtronic Insulinpumpe hast, überprüfen die Liste mit den kompatiblen Modellen/Firmware.

!!!warning "FAQs"
    - **"Wie kann ich eine kompatible Medtronic-Pumpe finden?"** Diese Frage wird im Abschnitt Zusätzliche Informationen zu Medtronic weiter unten beantwortet.
    - **"Was sind die Unterschiede zwischen den verschiedenen Medtronic Insulinpumpen?"** Diese Frage wird auch im Abschnitt Zusätzliche Informationen zu Medtronic weiter unten beantwortet.
    - **"Was ist mit den anderen Insulinpumpen?"** Diese sind leider nicht kompatibel,... es sei denn, es ist eine DanaRS, DanaR, Accu-Chek Insight, oder Accu-Chek Combo. Wenn du eine dieser Pumpen hast, kannst du eventuell [AndroidAPS](https://androidaps.readthedocs.io/en/latest/index.html) anstelle von Loop benutzen. Falls du eine Medtronic 512 oder 712 hast kannst du [OpenAPS](https://openaps.readthedocs.io/en/latest/) evaluieren. Dieses unterstützt, neben den anderen Loop-kompatiblen Medtronic Insulinpumpen, auch die Modelle 512 und 712. Keines dieser Systeme (AndroidAPS oder OpenAPS) unterstützt derzeit Omnipod für Looping.
    - **"Kann ich die Firmware meiner Medtronic-Pumpe ändern?** Arbeitest du bei Medtronic und hast Zugriff auf die internen Tools und Firmware-Versionen, mit denen das gehen würde? Du würdest wohl deinen Job verlieren, aber ich wetten, damit könnten es gehen. Wir können es leider nicht.

## Überprüfe das Insulinpumpenmodell

Dies ist ein einfacher Schritt... überprüfe, ob du eine kompatible Pumpe hast, um Loop zu verwenden:

* Medtronic 515 oder 715 (beliebige Firmware)
* Medtronic 522 oder 722 (beliebige Firmware)
* Medtronic 523 oder 723 (Firmware 2.4 oder niedriger)
* Medtronic Worldwide Veo 554 oder 754 (Firmware 2.6A oder niedriger)
* Medtronic Kanada/Australien Veo 554 oder 754 (Firmware 2.7A oder niedriger)
* Omnipod "Eros" Pods

Wenn du eine der oben aufgeführten Pumpen hast, kannst du Loop verwenden! Glückwunsch!

## Zusätzliche Informationen zu Medtronic

![Insulinpumpe](img/pump.png)

Es gibt eine Reihe von Medtronic-Insulinpumpen, die zwischen 2006 bis 2012 hergestellt werden und Loop-kompatibel sind.  Kompatibilität setzt zwei Dinge voraus: (1) Insulinpumpenmodell und (2) Firmware.

### Medtronic Insulinpumpenmodell

Um dein Insulinpumpenmodell zu bestimmen, schauen auf der Rückseite deiner Pumpe nach.  Auf der Unterseite der Pumpe sollte ein Aufkleber stehen.  Auf der rechten Seite des Aufklebers steht REF MMT-XXXXXX

![Pumpe](img/pump_model.jpg)

!!!note ""

    - MMT ---> Pump Manufacturer Model (MiniMed Medtronic)
    - 722 ---> Pump Model Number
    - NA ---> Pump Region (NA=North America, CA=Canada/Australia, WW=Worldwide)
    - S ---> Pump Color (S=Smoke, L=Clear/Lucite, B=Blue, P=Pink/Purple)

Einige Pumpen können vor der Pumpenregion noch ein „L“ oder „S“ oder „R“ haben, z.B. eine Modellnummer wie MMT-722LNAS.  Dieses hat keinen Einfluss auf die Kompatibilität mit Loop.

### Medtronic Insulinpumpenfirmware

Die Firmware einer Insulinpumpe ist die interne Software, die deren grundlegenden Funktionen steuert.  Ältere Medtronic-Firmware erlaubt es Loop als „Fernbedienung“ zu fungieren, um Temp-Basalraten zu setzen und Pumpendaten zu empfangen.  Neuere Firmware deaktiviert den "Fernbedienungszugriff" und kann deshlab nicht mit diesen DIY-Geschlossenen-Loop-Systemen verwendet werden.  Derzeit ist es nicht möglich, die Firmware einer Pumpe herunterzustufen oder durch ältere Firmware zu ersetzen.  Bevor du eine gebrauchte Pumpe kaufst, prüfe unbedingt, dass diese eine kompatible Firmware hat.

!!!note ""

    The firmware on all 515/715 and 522/722 model Medtronic pumps are all compatible with Loop. You will only need to check the firmware version for 523/723 and 554/754 model Medtronic pumps.

    + Medtronic 515 or 715 --> any firmware
    + Medtronic 522 or 722  --> any firmware
    + Medtronic 523 or 723 --> firmware 2.4 or lower
    + Medtronic Worldwide Veo 554 or 754 --> firmware 2.6A or lower
    + Medtronic Canadian/Australian Veo 554 or 754 --> firmware 2.7A or lower

Um die Firmware deiner Insulinpumpe nachzuschauen, musst du sie einschalten. Falls die Pumpe längere Zeit ausgeschaltet war (d.h. einige Zeit ohne Batterie herumlag), wird sie zuerst durch eine Startprozedur gehen und die Firmware-Version wird dann unten rechts auf dem Bildschirm der Insulinpumpe angezeigt.  Du musst gut aufpassen, die Firmeware-Version wird nur kurz angezeigt, bevor der Bildschirm andere Informationen zeigt.

Wenn die Pumpe noch vor kurzem benutzt wurde oder gerade eine Ampulle eingelegt ist, führe die folgenden Schritte aus:

1. Drücke die ![img/esc.png](img/esc.png) Taste auf deiner Pumpe.

2. Benutze die Taste ![img/light_button.png](img/light_button.png) um in der Statusanzeige nach unten zu gehen.

3. Schaue auf die letzte Zeile des Bildschirms.

![Firmware](img/pump_firmware.png)

### Unterschiede der Medtronic Insulinpumpen

Wenn du die Wahl hast und zwischen verschiedenen Insulinpumpen aussuchen kannst, dann gibt es ein paar kleine Unterschiede zwischen den Loop-kompatiblen Medtronic-Insulinpumpen.

**500 vs 700**: Der Unterschied zwischen den Medtronic 500 und 700 Insulinpumpen ist die Größe des Insulinampulle.  The 500 series pumps use a 180 unit reservoir, and the 700 series pumps use a 300 unit reservoir (or smaller 180 unit reservoir, if you want).

<font color ="orange">x15/x22 vs x23/x54</font>:  The difference between the x15 and x22 pumps versus the x23 and x54 series pumps has only a few notable mentions:

* The x23/x54 pumps will allow for smaller insulin deliveries in certain situations, if the smaller scroll rate is selected in the Bolus>Setup>Scroll Rate menu.  **Loop will have the insulin delivery automatically rounded by the pump to the units available in the pump model, and any smaller adjustments (to make up for the rounding) will be made through Loop’s use of temp basals.  If you want the smaller increments of basal rates, you can still enter those values in Loop app's settings and Loop will use those values for the purposes of insulin delivery calculations.**

| Pump Model                  | Basal increments       | Bolus increments         | Range                                                                              |
| --------------------------- | ---------------------- | ------------------------ | ---------------------------------------------------------------------------------- |
| 515/715</br>and</br>522/722 | 0.05</br>0.1           | 0.1</br>0.1              | deliveries of less than 10 units</br>greater than 10 units                         |
| 523/723</br>and</br>554/754 | 0.025</br>0.05</br>0.1 | 0.025 </br>0.05 </br>0.1 | between 0.025 to 0.975 units</br>between 1 to 9.95 units</br>greater than 10 units |

* Additionally, because of the way Loop fetches information from the pump, the x23/x54 series of pumps are slightly better at conserving battery life through the use of the MySentry packets to collect information from the pump.  x22 pumps do not use MySentry.

* The x23/x54 series pumps are also faster at delivering boluses greater than 10 units.  On an x23 pump, a 13-unit bolus takes 5:00 minutes to complete.  On an x22 pump, a 13-unit bolus takes 8:40 minutes to complete.

### Finding a Medtronic pump

Finding a compatible Medtronic pump is probably the most difficult part for most new Loopers.  Our suggestion:

* Talk to friends in the diabetic community.

* Ask your endocrinologist.

* Ask at a local JDRF chapter meeting if someone has an old backup pump they'd be willing to donate to you.

* Join diabetic supply groups on Facebook; both for-trade and for-sale groups.

* Check Craigslist often and be willing to expand your search area to include larger cities.

* Check out the **HelpAround, NextDoor, OfferUp, and/or LetGo** apps for pumps.

* Search [Medwow](http://medwow.com) for used Medtronic pumps.

Medwow has been fairly frustrating for most people; poor response rate and high prices.  The most success appears to come from either one-on-one discussions with fellow diabetics/doctors or using apps (Craigslist, NextDoor, LetGo, HelpAround).  If you are using Craigslist, you may wish to use an app on your iPhone to make the searching easier.  There are apps to search multiple cities at once for your keywords and set up alerts.

![Craigslist](img/craigslist.png)

### Safe Purchasing

If you choose to purchase from a remote or unknown seller, here are some tips for safe purchasing:

* Use PayPal and purchase using the "Goods and Services" payment option. This costs nothing for the buyer, but the seller will lose 2.95% of the sale to PayPal fees. PayPal offers some protection for both buyer and seller in the event of fraud.

* Ask for photos of the pump. Check to make sure the serial number of the pump on the backside matches the serial number of the pump showing in the display menu. Ask for a short video of the pump, or at least a photo of the pump turned on, so that you can see the pump's firmware and model number. Cracks and some wear on these pumps are expected. These pumps are not usually free of marks. Many people are successfully looping on pumps that have cracks and rub marks, but you may want to ask if you are concerned about any you see in photos.

* Beware if the bottom of the reservoir/motor sleeve has the drive support cap pushed out, as shown [here](/troubleshooting/pump-errors/#motor-error). Those pumps will generally not work (or only work intermittently), however some people have successfully repaired those pumps as shown in that link. Just be aware that it should be checked in advance.

* Repairs to cracks or missing bits of plastic on battery cap area and reservoir caps are possible and not very difficult in most situations. You can read more about how to repair those [here](/troubleshooting/pump-errors/#crackmissing-piece-repairs).

* Ask for shipping that includes a tracking number. USPS Priority Mail's smallest box is a great option.  It's only $7.20 domestically in the US and includes tracking. Ask the seller to add a small bit of packing protection such as bubble wrap around the pump to keep it safe during shipping. Make sure you get a tracking number within a reasonable period of time after you have paid.

Red flags that may indicate a scam:

* Asking for payment through "friends and family" on PayPal, especially if you don't know the person or have any solid references for them. Paying in that way offers you no buyer protection. It's just like giving the seller cash, so you had better trust the seller.

* Offering an "almost new" pump is a big red flag. These pumps should be at least 5-years-old by now. Do you really think a 5 year old pump should be unused and sitting in shrink wrap at this point? This seems highly suspicious. There are some out there, but they are very infrequent.

* Not able to provide new pictures of the pump when requested. Sure they posted some pictures with the ad, but what if they just downloaded them from other people's ads? The seller should be able to furnish a couple of "new" photos at your request. A good one to ask for is the battery and reservoir tops so you can see the condition of those.

### Pump Supplies

Medtronic will not typically sell pump supplies directly to customers who have not previously purchased a registered Medtronic pump. Ask your insurance about purchasing pump supplies through a durable medical equipment (DME) provider. Typically, the DME provider will coordinate with your insurance and doctor's office to get the necessary insurance approval and prescriptions for the supplies. If you are brand new to Medtronic infusion sites, you may want to ask for help from friends to try a variety of infusion sets before purchasing a full 90-day supply of any type in particular.

## Zusätzliche Informationen zu Omnipods

!!!warnung "Hinweis und Haftungsausschluss"

    Through the work of the DIY community, Insulet's Omnipod (Eros) system is now Loop compatible. Using Eros pods with Loop is not supported by Insulet. Do not call Insulet asking for help with your Loop build, setup, or operation. This project is not FDA-approved and you are using this project under your own responsibility and risk. Please read these documents and familiarize yourself with Loop before using.

### Eros

Eros Pods wurden 2013 in den Markt eingeführt und werden auch weiterhin von Insulet verkauft. Soweit uns bekannt ist, wurden keine Pläne oder ein Datum für die Einstellung der Eros Pods an bestehende Kunden kommuniziert. Insulet bezeichnet diese nicht mehr als "Eros", sondern verwendet den Begriff "Omnipod-System". Zum Nachschauen [Insulet's webpage](https://www.myomnipod.com/about):

Das Eros System benutzt den charakteristischen PDM, denn wir alle aus den letzten Jahren kennen.

![../img/dash.png](img/eros.png)

### DASH

Insulet hat das DASH-System als möglichen Ersatz und Nachfolger für Eros/Omnipod-System vorgestellt und vertreibt es nun in parallel.   Das DASH System erkennst du an seinem neueren, schlankeren Android PDM und der Kommunikation per Bluetooth. Loop ist nicht mit dem DASH-System kompatibel.

![img/dash.png](img/dash.png)

## Nächster Schritt: Kompatible CGM

Jetzt kannst du mit Schritt 4 weitermachen, um zu überprüfen, ob du einen [Kompatiblen CGM-](step4.md)hast.
