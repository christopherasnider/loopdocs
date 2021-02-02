from pathlib import Path
import os
import os.path
import json
import yaml
from extract import deep_keys
import sys
from collections import OrderedDict
from xml.dom import minidom
import xml.etree.ElementTree as ET
import subprocess
import codecs

class LoopDocs:

    def __init__(self):
        self.scriptPath=os.path.join(os.getcwd(),"scripts")
        self.loopDocsPath=Path(self.scriptPath).parent
        self.buildsitePath=os.path.join(self.loopDocsPath,".buildsite") 
        self.menuXliffFilename="navMenu.xliff"
        self.xliffDirectoryPath=os.path.join(self.loopDocsPath,"xliff")
        self.xliffBaseDirectoryPath=os.path.join(self.xliffDirectoryPath,"basexliff")
        self.xliffBaseMenuPath=os.path.join(self.xliffBaseDirectoryPath, self.menuXliffFilename)

        self.sites=[]
        directory_contents = os.listdir(self.loopDocsPath)
        for subdir in directory_contents:
            fullpath=os.path.join(self.loopDocsPath,subdir)
            if os.path.isdir(fullpath) and "docs_" in subdir:
                splitted=subdir.split("_")
                lang=splitted[1] #subdir[-2:] 
                self.sites.append(LoopDocLanguageSite(lang,self))
    
    def buildSites(self):
        sitedir=self.buildsitePath
        topdirectory=self.loopDocsPath

       # self.runBuilder(os.path.join(topdirectory, "mainsite", "mkdocs.yml"), sitedir)
       # self.runBuilder(os.path.join(topdirectory,  "mkdocs_en.yml"), os.path.join(sitedir,"en" ))
       # self.runBuilder(os.path.join(topdirectory,  "mkdocs_old.yml"), os.path.join(sitedir,"en_old" ))   

        for site in self.sites:
            site.buildSite()

    def runBuilder(self,configfile,sitedir):
        os.system('mkdocs build --config-file ' + configfile + ' --site-dir ' + sitedir)



class TranslateMenus:
    def __init__(self,xliffPath, templatePath, savePath):
        self.xliffpath=xliffPath
        self.templatepath=templatePath
        self.savepath=savePath
        self.menus=[]

    
    def readXliff(self):
        tree = ET.parse(self.xliffpath)
        root=tree.getroot()
        iter=tree.iter('trans-unit')
        for elem in iter:
            m=TranslateMenu(elem)
            self.menus.append(m)

    def replaceValues(self):

        
        template = open(self.templatepath, "r")
        templatedata = template.read()
        template.close()

        for menu in self.menus:
            templatedata = templatedata.replace(menu.findmenu(), menu.replacemenu())

        newfile = open(self.savepath, "w",encoding="utf-8")
        newfile.write(templatedata)
        newfile.close()

    def TranslateYmlMenu(self):
        self.readXliff()
        self.replaceValues()

class TranslateMenu:
    def __init__(self,elem):
        listvalues=list(elem)
        self.source=listvalues[0].text
        self.target=listvalues[1].text
        self.note=listvalues[2].text
           
    
    def findmenu(self):
        if self.note:
            return f"- \"{self.source}\" : \"{self.note}\""
        else:
            return f"- \"{self.source}\" :"

    def replacemenu(self):
        if self.note:
            return f"- \"{self.target}\" : \"{self.note}\""
        else:
            return f"- \"{self.target}\" :"

class LoopDocLanguageSite:
    def __init__(self,language,LoopDocs):
        self.language=language
        self.loopdocs=LoopDocs
        self.ymlFilename="mkdocs.yml"
        self.languageDirectory=os.path.join(self.loopdocs.loopDocsPath,"docs_" + self.language)
        self.langyamlpath=os.path.join( self.languageDirectory,self.ymlFilename)
        self.buildpath=buildpath=os.path.join(self.loopdocs.buildsitePath,self.language)
        self.generalMkdocsYmlFile=os.path.join(LoopDocs.scriptPath,"mkdocs_template.yml")
        self.langxliffDirectory=os.path.join(self.loopdocs.xliffDirectoryPath,"xliff_" + self.language)
        self.xliffPath=os.path.join(self.langxliffDirectory,self.loopdocs.menuXliffFilename)



    def createYamlFile(self):
        
        menus=TranslateMenus(self.xliffPath,self.generalMkdocsYmlFile,self.langyamlpath)
        menus.TranslateYmlMenu()

        with open(self.langyamlpath,'r',encoding="utf-8") as file:
            data=file.read()
            data=data.replace("language: en",f"language: {self.language}")
            if self.language=="ach":
                data=data.replace("custom_dir: ../overrides","custom_dir: ../overrides_ach")
                data=data.replace("use_directory_urls: true","use_directory_urls: false")
                
            # content=yaml.load(file)
            # content['theme']['language']=self.language
        newfile = open(self.langyamlpath, "w",encoding="utf-8")
        newfile.write(data)
        newfile.close()

                # yaml.safe_dump(content,outfile,  default_flow_style=False)

    def buildSite(self):
        self.createYamlFile()
        self.loopdocs.runBuilder(self.langyamlpath,self.buildpath)