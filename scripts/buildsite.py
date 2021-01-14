from pathlib import Path
import os
import os.path

def runmkdocs(configfile,sitedir):
    os.system('mkdocs build --config-file ' + configfile + ' --site-dir ' + sitedir)

def right(s, amount):
    return s[-amount:]

scriptdirectory=os.getcwd()
path = Path(scriptdirectory)
topdirectory=path.parent
sitedir=os.path.join(topdirectory,".buildsite") 


runmkdocs(os.path.join(topdirectory, "mainsite", "mkdocs.yml"), sitedir)
runmkdocs(os.path.join(topdirectory,  "mkdocs_en.yml"), os.path.join(sitedir,"en" ))
runmkdocs(os.path.join(topdirectory,  "mkdocs_old.yml"), os.path.join(sitedir,"en_old" ))


templatefile=os.path.join(scriptdirectory,"template_mkdocs.yml")
content=Path(templatefile).read_text()


directory_contents = os.listdir(topdirectory)
for subdir in directory_contents:
    fullpath=os.path.join(topdirectory,subdir)
    if os.path.isdir(fullpath) and "docs_" in subdir:
        lang=right(subdir,2)
        
        navfile=os.path.join(topdirectory,subdir,"docs","nav.txt")
        navcontent=Path(navfile).read_text()

        newymlcontent=content
        newymlcontent= newymlcontent.replace("{replacenavhere}",navcontent)
        newymlcontent= newymlcontent.replace("{language}",lang)

        ymlfilepath=os.path.join(topdirectory,subdir,"mkdocs.yml")

        Path(ymlfilepath).write_text(newymlcontent)

        runmkdocs(ymlfilepath, os.path.join(sitedir,lang))


