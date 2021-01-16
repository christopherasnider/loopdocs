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

class LoopDocs:

    def __init__(self):
        self.scriptPath=os.path.join(os.getcwd(),"scripts")
        self.loopDocsPath=Path(self.scriptPath).parent
        self.buildsitePath=os.path.join(self.loopDocsPath,".buildsite") 

        self.xliffFactory=XliffFactory(self)
        self.mkdocsFactory=MkDocsFactory(self)
        self.staticSiteFactory=StaticSiteFactory()

        self.sites=[]
        directory_contents = os.listdir(self.loopDocsPath)
        for subdir in directory_contents:
            fullpath=os.path.join(self.loopDocsPath,subdir)
            if os.path.isdir(fullpath) and "docs_" in subdir:
                lang=subdir[-2:] 
                self.sites.append(LoopDocLanguageSite(lang,self))
    
    def buildSites(self):
        sitedir=self.buildsitePath
        topdirectory=self.loopDocsPath

        self.staticSiteFactory.runBuilder(os.path.join(topdirectory, "mainsite", "mkdocs.yml"), sitedir)
        self.staticSiteFactory.runBuilder(os.path.join(topdirectory,  "mkdocs_en.yml"), os.path.join(sitedir,"en" ))
        self.staticSiteFactory.runBuilder(os.path.join(topdirectory,  "mkdocs_old.yml"), os.path.join(sitedir,"en_old" ))   

        for site in self.sites:
            site.buildSite()

class StaticSiteFactory:

    def runBuilder(self,configfile,sitedir):
        os.system('mkdocs build --config-file ' + configfile + ' --site-dir ' + sitedir)

class XliffFactory:
    def __init__(self,LoopDocs):
        self.menuFilename="navMenu.xliff"
        self.xliffDirectoryPath=os.path.join(LoopDocs.loopDocsPath,"xliff")
        self.xliffBaseDirectoryPath=os.path.join(self.xliffDirectoryPath,"basexliff")
        self.xliffBaseMenuPath=os.path.join(self.xliffBaseDirectoryPath, self.menuFilename)
        self.loopdocs=LoopDocs
        self.baseValues=[]

    def createBaseXliffFile(self):
        self.createXliffFile(self.loopdocs.mkdocsFactory.generalMkdocsYmlFile,self.xliffBaseMenuPath)


    def  createXliffFile(self,templatePath,savePath):
        yamlcontent=self.loopdocs.mkdocsFactory.getYamlContent(templatePath)
        nav=yamlcontent['nav']
        navtest=deep_keys(nav)
        xliff="""<?xml version="1.0" encoding="utf-8"?>
<xliff xmlns:xlf="urn:oasis:names:tc:xliff:document:1.2" version="1.2">
<file datatype="plaintext" original="source.txt" source-language="en">
<body>"""
        i=0
        for name in navtest:
            i+=1
            count=f"00000{i}"
            xliffItem=f"""<trans-unit id="{count[-4:]}">
<source>""" + name + """</source>
</trans-unit>"""
            xliff = xliff + "\n" + xliffItem
        xliff=xliff + """\n</body>
</file>
</xliff>"""

        Path(savePath).write_text(xliff)

    def replaceContentFromXliffFile(self,xliffPath, content):

        tree = ET.parse(xliffPath)
        root=tree.getroot()
        iter=tree.iter('trans-unit')
        wordDic =[]
        for elem in iter:
            listvalues=list(elem.iter())
            menu=TranslateMenu()
            if listvalues.__len__()==4:

              wordDic[listvalues[1].text].a=end(listvalues[2].text)  
                
            if listvalues.__len__()==3:
                wordDic[listvalues[1].text].append(listvalues[1].text)

        
        self.replace_nested(content['nav'],wordDic)
        return newContent

class TranslateMenu:
     def __init__(self,source,target):
         self.source=source
         self.target=target



    def replace_nested(self,dct,wordDic):
        if isinstance(dct, list):
            for item in dct:
                if isinstance(item,dict):
                    for key in item.keys():
                        translated=wordDic[key]
                        if translated:
                            item[translated]=item.pop(key)
                            return
                        else:
                            if isinstance(item[key],list):
                                self.replace_nested(item[key],wordDic)

class MkDocsFactory:
    def __init__(self,LoopDocs):
        self.generalMkdocsYmlFile=os.path.join(LoopDocs.scriptPath,"mkdocs_template.yml")
        self.generalMkdocsYmlFileContent=self.getYamlContent(self.generalMkdocsYmlFile) 

    def getYamlContent(self,path):
        with open(self.generalMkdocsYmlFile, 'r') as stream:
            return yaml.safe_load(stream)

class LoopDocLanguageSite:
    def __init__(self,language,LoopDocs):
        self.language=language
        self.loopdocs=LoopDocs
        self.ymlFilename="mkdocs.yml"
        self.languageDirectory=os.path.join(self.loopdocs.loopDocsPath,"docs_" + self.language)
        self.langyamlpath=os.path.join( self.languageDirectory,self.ymlFilename)
        self.buildpath=buildpath=os.path.join(self.loopdocs.buildsitePath,self.language)

    def createYamlFile(self):
        
        
        content=self.loopdocs.mkdocsFactory.generalMkdocsYmlFileContent
        langPath=os.path.join(self.loopdocs.xliffFactory.xliffDirectoryPath,"xliff_" + self.language)
        xliffPath=os.path.join(langPath,self.loopdocs.xliffFactory.menuFilename)

        newcontent=self.loopdocs.xliffFactory.replaceContentFromXliffFile(xliffPath,content)

        newcontent['theme']['language']=self.language
        with open(self.langyamlpath, 'w') as outfile:
            yaml.safe_dump(newcontent,outfile,  default_flow_style=False)

    def buildSite(self):
        self.createYamlFile()
        self.loopdocs.staticSiteFactory.runBuilder(self.langyamlpath,self.buildpath)