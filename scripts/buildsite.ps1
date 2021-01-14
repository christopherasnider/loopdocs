$sitedir=".buildsite"


mkdocs build --config-file ../mainsite/mkdocs.yml --site-dir ../$sitedir

mkdocs build --config-file ../mkdocs_en.yml --site-dir $sitedir/en
mkdocs build --config-file ../mkdocs_old.yml --site-dir $sitedir/en_old

Get-ChildItem "../" | Where-Object{ $_.Name -like "docs_*" } | ForEach-Object { 

    $lang=$_.Name.Substring(5,2)

    $template=Get-Content -path "template_mkdocs.yml" -Raw
    $nav=Get-Content -path "../$($_.Name)/docs/nav.yml" -Raw
    $newcontent=$template -replace "{replacenavhere}", $nav
    $newcontent=$newcontent -replace "{language}", $lang
    $newcontent | Set-Content -Path "../$($_.Name)/mkdocs.yml"

    mkdocs build --config-file ../docs_$lang/mkdocs.yml --site-dir ../$sitedir/$lang
} 