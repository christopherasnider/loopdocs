
#Removes all unused imagefiles in the docs-directory

#Iterate over imagefilenames in the docs directory subdirectories
#for each imagefilename: searches all markdownfiles content
#if no result: remove file by fullname

Get-ChildItem "../docs" -Recurse -include *png,*jpg,*bmp,*jpeg | Where-Object { (Get-ChildItem -recurse -filter *.md | Get-Content | select-string -pattern $_.Name).Count -eq 0} | ForEach-Object { $_.FullName } | Remove-Item