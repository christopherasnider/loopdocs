#run this locally to update images, css and so 
#this is done instead of having crowdin handle all the image files
robocopy  "../docs" "../docs_da/docs" /S /XF *.md
robocopy  "../docs" "../docs_de/docs" /S /XF *.md
robocopy  "../docs" "../docs_ro/docs" /S /XF *.md