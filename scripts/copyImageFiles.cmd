#run this locally to mirror non-md files from "docs" to other folders 
#this is done instead of having crowdin handle all the image files
robocopy  "../docs" "../docs_da/docs" /S /XF *.md /MIR
robocopy  "../docs" "../docs_de/docs" /S /XF *.md /MIR
robocopy  "../docs" "../docs_ro/docs" /S /XF *.md /MIR