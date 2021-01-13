# Schritt 1: Kompatibler Computer

!!!Gefahr "Geschätzte Zeit"
    - 5 Minuten, wenn du bereits Mojave (10.14) oder Catalina (10.15) auf deinem Apple Computer installiert hast
    - 30-60 Minuten, falls MacOS Aktualisierungen installiert werden müssen

!!! Info "Zusammenfassung"
    - Überprüfe deine MacOS Version, es sollte Mojave oder Catalina sein. **Wenn auf deinem iPhone, auf dem du Loop installieren wirst, die aktuelle iOS Version (14.x) läuft, dann musst du MacOS Catalina auf deinem Apple Computer installiert haben.**
    - Arbeite nicht mit einer Beta MacOS Version. (Du kannst diesen Punkt ignorieren, wenn du nicht weist, was das ist... es bedeutet, dass du kein Beta MacOS auf deinem Apple Computer verwendest.)
    - Solltest du nicht MacOS Mojave oder Catalina verwenden ueberpruefe, ob du auf eines davon aktualisieren kannst.
    - Wenn du deinen Apple Computer nicht auf Mojave oder Catalina aktualieren kannst, bleiben dir die folgenden Optionen. Einen passenden Computer ausleihen, ein "patcher tool" verwenden, oder einen neuen/gebrauchten kompatiblen Apple Computer kaufen.
    - Überprüfe `Software Aktualisierungen`, ob dein Computer auf dem letzten Stand ist. Wenn nicht, führe die Aktualisierungen zuerst durch.

!!!warning "FAQs"
    - **"Kann ich auch einen PC/Windows benutzen? Ich habe keinen Apple Computer."** Ja, es geht schon... Info [this FAQ about using Virtual Machine](/faqs/FAQs/#can-i-use-a-pc-or-windows-computer-to-build). PCs mit einem AMD Prozessor Chip können keinen Apple Computer emulieren. Wenn du das probieren möchtest schaue also zuerst nach, welchen Prozessor Chip du in deinem PC hast.
    - **"What can I do if my computer is too old to be upgraded to Catalina?"** You could take a look at using [Catalina Patcher](http://dosdude1.com/catalina/), but this is totally on your own and not part of these instructions. Just offering the answer to the FAQ...it is up to you to read about the patcher tool and what risks it may involve for you.
    - **"Can I borrow someone else's Apple computer?"** Yes, please see [this FAQ about borrowing a computer](/faqs/FAQs/#do-i-need-to-own-my-own-apple-computer) to learn more.
    - **"How often do I need to use the computer?"** Computer access is only required when you are initially installing the Loop app or updating to a newer Loop release. You do NOT need access to an Apple computer in order to troubleshoot or change Loop settings, such as basal profiles or carb ratios.

## New M1 chip Apple Computers

Yes, the newest Apple computers just released in November 2020 are compatible with Loop building. There is ONE little step to be aware of with the new computers, and that is on the Step 7 Install Homebrew page. I've highlighted in a colored boxes on that page the parts that M1 users will need to do. I promise, it's quick and painless.

And...with that...I'm extremely jealous that you have the new computer. They will make Loop building extremely fast and the time estimates on these docs will be ridiculously slower than you will be experiencing. Lucky duck, I have FOMO.

## Big Sur MacOS

Yes, Big Sur is compatible with Loop building...I'm working on updating this page for that soon. Hang tight.

## Catalina vs Mojave, which do you need?

Do you need Catalina or Mojave? The answer will depend on the iOS of your iPhone you'll install Loop onto.

**If you have iOS 12.4 to 13.2**, you can use macOS 10.14.4 (Mojave) or 10.15.2 or newer (Catalina).

**If you have iOS 13.4 or newer**, you will not be able to use Mojave and will need Catalina at a minimum. In other words, you'll need macOS 10.15.2 at a minimum to build Loop onto an iPhone running iOS 13.4 or newer.

!!!danger "iOS dictates your computer needs"

    Put simply for Loopers...the more up-to-date you keep your iOS, the more up-to-date your computer and macOS will need to be, too. That's not necessarily a bad thing, and you can't avoid iOS updates forever...you just do need to be aware of how they relate to each other if your computer is "getting on the older side".

## Check your macOS

You need an Apple computer that has at least the minimum macOS version as described above; Mojave macOS 10.14.4 (or newer) or Catalina macOS 10.15 (or newer). To find out which version you have installed, click on the little Apple icon in your computer's upper left corner and select the `About this Mac`. It doesn't matter if the computer is a MacBook, iMac, macMini, etc...just so long as it has the minimum you'll need.

If your computer does not have the required minimum version, you'll need to check the `Software Update` button on that screen to see if you can update.

<p align="center">
<img src="img/macosx.png" width="500">
</p>
If your computer does not give you the option to update to the newer macOS (in other words you are stuck on older versions)...it is quite possible that Apple has decided your computer is too old to run the latest and greatest. How old is too old? That will depend on your computer model and year as shown below:

<p align="center">
<img src="img/mojave-minimum.png" width="750">
</p>

## Next Step: Compatible iPhone/iPod touch

Now you are ready to move onto Step 2 to check if you have a [Compatible iPhone/iPod touch](step2.md).
