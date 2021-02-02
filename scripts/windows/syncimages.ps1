#Copies all files, except markdownfiles, to the language-sites

Push-Location $PSScriptRoot
Get-ChildItem "../../" | Where-Object{ $_.Name -like "docs_*" } | ForEach-Object { 
    robocopy "../../docs" "$($_.FullName)\docs" /S /XF *.md /MIR
} 

#robocopy "../docs" "../mainsite/docs/img" /S /XF *.md /MIR