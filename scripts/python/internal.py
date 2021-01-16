from loopbuilder import LoopDocs

loopdocs=LoopDocs()
#loopdocs.buildSite()


for site in loopdocs.sites:
    if site.language=="da":
        site.buildSite()


