#Copies all files, except markdownfiles, to the language-sites

Get-ChildItem "../" | Where-Object{ $_.Name -like "docs_*" } | ForEach-Object { 
    robocopy "../docs" "$($_.FullName)\docs" /S /XF *.md /MIR
} 
