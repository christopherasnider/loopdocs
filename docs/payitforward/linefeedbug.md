This a document to show the problem.

Bug: Crowdin removes a linefeed and spacing from the next line and puts the two lines on one line.
Expected behaviour: Crowdin should not remove linefeeds and then indent (in line 12)

This in source file:

12
23

45
	67
89

01


Becomes this in the translated file:

12 23

45 67 89

01


