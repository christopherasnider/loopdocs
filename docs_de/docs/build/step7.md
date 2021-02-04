# Schritt 7: Installation von Homebrew

!!!danger "Geschätzte Zeit"

    - 10-15 Minuten vorausgesetzt, du kennst das Passwort deines Computers
    - 35 Minuten, wenn du dein Passwort nicht mehr weist und raten musst

!!!info "Zusammenfassung"

    - Installiere Homebrew einfach, indem du einen langen kauderwelsch Text in die Terminalanwendung kopierst und bestätigst.

!!!warning "FAQs"

    - **"Was passiert, wenn ich keine "Installation erfolgreich" Rückmeldung bekomme?"** Wenn du keine erfolgreiche Installationsnachricht siehst, probiere es bitte einfach noch einmal. Wenn du Homebrew nicht installiert hast, wird auch die Erstellung von Loop fehlschlagen. Diesen Schritt kannst du nicht überspringen. Die häufigste Fehlerursache ist das Nichtkopieren der ganzen -Codezeile ... Manchmal gelingt es den Leuten nicht, das letzte `"` am Ende der Zeile zu erwischen. Außerdem musst du ein Benutzerkonto auf dem Computer mit "Admin"-Rechten verwenden, da Homebrew ein Programm ist und auf dem Computer installiert wird.

Tief durchatmen... dieser Schritt sieht aus wie "Programmiercode". Ist es aber nicht. Na ja, ist es doch... aber wir kopieren einfach nur eine Zeile dieser Seltsamkeit, fügen sie ein und fertig. Wir müssen eigentlich nicht viel über Homebrew selbst wissen, oder was die Zeile Code genau bedeutet.

## Der Benutzer muss ein Admin-Konto auf dem Computer habem

Homebrew ist ein Programm, mit dem wir die benötigten Pakete installieren können, um Loop zu erstellen. Before installing Homebrew, we need to double check one thing...that the user account on the computer that you are using to build Loop, that **user account needs to have Administrative rights on the computer**. How can you tell? Go to the computer's System Preferences application, open the Users & Groups section. If your account that you are using doesn't say "Admin" under your name, then you need to click the lock and change that to an Admin account before proceeding. If you are using a work computer, you may not have admin rights on that computer...so be aware that you may have restrictions on company owned computers.

![../img/carthage-done.png](img/admin-user.png)

Side note: If you are a (1) computer-savvy person and (2) already installed Homebrew on a different user account on the computer previously...please go use that user account on the computer to build Loop. Or, delete Homebrew from that User account and install on your account. Homebrew is a bit picky.

## Installing Homebrew

Ok, now that we have the user account confirmed, let's open the Terminal application on your computer. It is located in your Applications folder and then look in the Utilities subfolder...the Terminal application is in there like shown in the screenshot below.

![../img/carthage.jpg](img/terminal.png)

!!!info "New Apple M1 chip users: IMPORTANT STEP"

    If you purchased one of the new Apple computers that have the brand new Apple M1 chip, you will need to do a little step to start with. Homebrew doesn't run natively on the new M1 chips...so we have to open Terminal app using a little "converter" app, in these situations, called Rosetta. It's no big deal...simply find the Terminal app like was described above and instead of opening it by double clicking...I want you to click on the Terminal app's name just once so it is highlighted. Then right-click on the Terminal app's name to bring up some additional choices. Thanks! You will want to select the "Get Info" option.</br></br>
    
    <p align="center">
    <img src="../img/get-info.png" width="550">
    </p>
    
    Now in the informational window that appears...you'll see a checkbox that says "Open using Rosetta".  Check that box...that will allow Terminal app to open in such a way that we can install Homebrew in the next steps. You can close that informational window, after you check the box for "Open using Rosetta", and proceed with the rest of the directions just like normal.
    
    <p align="center">
    <img src="../img/rosetta.png" width="350">
    </p>

Now that you've located where the Terminal app is located in the Utilities folder (and already turned on Rosetta check box, if you are an M1 user)...double-click the Terminal app's name so that the app opens. The Terminal app is very plain looking when you open it. That is normal. Copy and paste the line in the little grey box below into Terminal prompt.

 `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`

Your screen should look like something like this after you copy it in...if it does, then go ahead and press return to continue on with the installation command.

![../img/homebrew-copy-line.png](img/homebrew-copy-line.png)

There will be a prompt asking if you want to continue.  Press return to continue, then it will prompt for your password.  <u>The password is your computer's password.</u>

!!!danger "Don't freak out"

    Don't freak out that you can't see your password while you type. That is normal. The Terminal app doesn't show keystrokes when you enter passwords, but it is still recording your password entry. If you think you messed up because you were confused, press the delete key a bunch of times and then start fresh with the password entry.

Wait while the script does its thing...you’ll see info scroll by and then it will pause for a while. Eventually, it will be done and you’ll see something that says “Installation successful” and you’ll have a ready Terminal prompt again.

![img/carthage.jpg](img/carthage.jpg)

!!!info "If you get an error about homebrew-core being a "shallow clone""

    You will need to follow the instructions given in the error, and update your homebrew installation with the following command:
    
    `git -C "/usr/local/Homebrew/Library/Taps/homebrew/homebrew-core" fetch --unshallow`

## Install Carthage

We are going to finish with one little last installation of something called Carthage. It's a helper that does some of the work during Loop building. Technically, Loop has an automated script that will use Homebrew to install Carthage when you first build Loop.

Now that Homebrew has successfully installed, copy and paste the line in the little grey box below into Terminal prompt (similar to how you did for Homebrew installation line above).

`brew install carthage`

You should see something like below when the command has finished running successfully. Your messages might look slightly different (version number might be newer, for example), but the summary should look similar to seeing a carthage version installed and complete.

![img/carthage-done.png](img/carthage-done.png)

You can close the Terminal application now. You’re done with it. You do not need to do these steps again for any subsequent Loop builds. This is one of those "just do it once" on new computer installations. If you get a new computer though, you will have to repeat this step for the new computer.

## Uninstall Homebrew

If you have something go wrong in Homebrew installation, want to delete it and start fresh, the uninstall command is:

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh)"`

Copy and paste that entire line into Terminal application. Then you can retry the installation of Homebrew using the install command listed earlier in this page.

## Next Step: Download Xcode

Now you are ready to move onto Step 8 to [download Xcode](step8.md).
