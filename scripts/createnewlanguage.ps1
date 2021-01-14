$lang="se"

$docdictoryname="docs"
$directory="../$($docdictoryname)_$($lang)"
$langdocsdirectory="$($directory)/$($docdictoryname)"
$ymlfile="$($directory)/mkdocs.yml"


New-Item -Name $directory -ItemType directory #-Path "../"
New-Item -Name $langdocsdirectory -ItemType directory #-Path "../"

Copy-Item "../mkdocs_en_new.yml" -Destination $ymlfile
(Get-Content -path $ymlfile -Raw) | ForEach-Object {
  $newcontent= $_ -replace "custom_dir: overrides","custom_dir: ../overrides"
  $newcontent=$newcontent -replace "language: en","language: $($lang)"
  $newcontent=$newcontent -replace "repo_url: https://github.com/LoopKit/loopdocs",""
}  
$newcontent | Set-Content -Path $ymlfile

robocopy "../$($docdictoryname)" $docsdirectory /S /XF *.md /MIR
