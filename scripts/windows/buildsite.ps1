
$topdirectory=(get-item $PSScriptRoot).parent.FullName
$sitedir="$($topdirectory)\.buildsite"

mkdocs build --config-file $topdirectory\mainsite\mkdocs.yml --site-dir $sitedir

mkdocs build --config-file $topdirectory\mkdocs_en.yml --site-dir $sitedir\en
mkdocs build --config-file $topdirectory\mkdocs_old.yml --site-dir $sitedir\en_old

Get-ChildItem $topdirectory | Where-Object{ $_.Name -like "docs_*" } | ForEach-Object { 

    $lang=$_.Name.Substring(5,2)

    $template=Get-Content -path "$($PSScriptRoot)\template_mkdocs.yml" -Raw
    $nav=Get-Content -path "$topdirectory\$($_.Name)\docs\nav.txt" -Raw
    $newcontent=$template -replace "{replacenavhere}", $nav
    $newcontent=$newcontent -replace "{language}", $lang
    $ymlfilepath="$topdirectory\$($_.Name)\mkdocs.yml"
    $newcontent | Set-Content -Path $ymlfilepath

    mkdocs build --config-file $ymlfilepath --site-dir $sitedir\$lang
} 