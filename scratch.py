# -*- encoding: utf-8 -*-
import mwparserfromhell
from wikiciteparser.parser import parse_citation_template
import requests
import json
import datetime

#----------- Grabbing all wikitext
revisiondata = []

pageid = 142721 #MARCOS
pageid = 2280572 #batac

wikiapidata = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=50&rvprop=ids|timestamp|user|userid|comment|tags|size|content&pageids="+str(pageid))
wikijsondata = json.loads(wikiapidata.content)
revisiondata.extend(wikijsondata["query"]["pages"][str(pageid)]["revisions"])

#start = time.time()
while "batchcomplete" not in wikijsondata:
    conti = wikijsondata["continue"]["continue"]
    rvconti = wikijsondata["continue"]["rvcontinue"]
    wikiapidata = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=50&rvprop=ids|timestamp|user|userid|parsedcomment|tags|size|content&pageids="+str(pageid)+"&continue="+conti+"&rvcontinue="+rvconti)
    wikijsondata = json.loads(wikiapidata.content)
    revisiondata.extend(wikijsondata["query"]["pages"][str(pageid)]["revisions"])
    #print("Now grabbing "+wikijsondata["query"]["pages"][str(pageid)]["revisions"][0]["timestamp"]+" time elapsed "+str(datetime.timedelta(seconds=time.time()-start)))

#endtime = time.time()
#print("that whole thing took "+str(datetime.timedelta(seconds=endtime-start))+" for "+str(len(revisiondata))+" revisions.")

for rev in revisiondata






#----------- Grabbing wikitext, choose one

#Retrieves entire wikitext and stores in mwtext
wikiapidata = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&rvprop=ids|flags|timestamp|comment|user|content|tags&titles=Ferdinand_Marcos")
lol=json.loads(wikiapidata.content)
mwtext=lol['query']['pages']['142721']['revisions'][0]['*']

#opens file with wikitext as mwtext
currtext = open("current.wtxt", "r")
mwtext = currtext.read()
currtext.close()

#------------- Given the wikitext of a revision stored in mwtext

#Breaks down mwtext into array refstrings of citations enclosed in <ref> tags
refindex = 0
refendex = 0
lastindex = 0
refstrings = []
cntbrok = 0
cntsmol = 0
cntnorm = 0
norefs = ""

while True:
    refindex = mwtext.find("<ref", refendex)
    if refindex == -1:
        #norefs += mwtext[lastindex:]
        break
    nextref = mwtext.find("<ref", refindex + 1)
    slashref = mwtext.find("/>", refindex)
    refendex = mwtext.find("</ref>",refindex)
    if ((nextref < slashref) | (slashref == -1)) & ((nextref < refendex) | (refendex == -1)) & (nextref != -1):
        reftype = 'broken'
        cntbrok += 1
        refendex = nextref
    elif ((slashref < nextref) | (nextref == -1)) & ((slashref < refendex) | (refendex == -1)) & (slashref != 1):
        reftype = 'small'
        cntsmol += 1
        refendex = slashref + 2
    elif ((refendex < nextref) | (nextref == -1)) & ((refendex < slashref) | (slashref == -1)) & (refendex != -1):
        reftype = 'normal'
        cntnorm += 1
        refendex += 6
    else:
        #lolwtf
        print("Break in the refstring crawling")
        break
    refsnippet = {'type':reftype,'content':mwtext[refindex:refendex]}
    refstrings.append(refsnippet)
    norefs += mwtext[lastindex:refindex]
    lastindex = refendex


#----------- Given reference strings in refstrings list

rcounter = 0
rcountofnone = 0
rcountofref = 0
rcountofurl = 0
rurls = []
rnooners = []
rmeroons = []
rnoonertrack = []
rmeroontrack = []
rsmall = []
parsedReferences = []

for refsnippet in refstrings:
    if refsnippet['type'] == 'broken':
        print("something borked")
    elif refsnippet['type'] == 'small':
        rsmall.append(refsnippet)
    elif refsnippet['type'] == 'normal':
        rcounter += 1
        citationTemplate = mwparserfromhell.parse(refsnippet['content']).filter_templates()
        if len(citationTemplate) == 0:
            rcountofurl += 1
            rurls.append(refsnippet['content'])
        else:
            for tpl in citationTemplate:
                parsed = parse_citation_template(tpl)
                if parsed is None:
                    rcountofnone += 1
                    rnooners.append(tpl)
                    rnoonertrack.append(refsnippet)
                else:
                    rcountofref += 1
                    parsed['count'] = rcounter
                    parsed['countref'] = rcountofref
                    rmeroons.append(tpl)
                    rmeroontrack.append(refsnippet)
                    parsedReferences.append(parsed)


notagnone = 0
notagref = 0
notag = []
for temps in lofles:
    prsed = parse_citation_template(temps)
    if prsed is None:
        notagnone += 1
    else:
        notagref += 1
        notag.append(prsed)










json.dumps(list)
text_file = open("Output.txt", "w")
text_file.write("Purchase Amount: %s" % TotalAmount)
text_file.close()





wikicode = mwparserfromhell.parse(mwtext)
for tpl in wikicode.filter_templates():
   parsed = parse_citation_template(tpl)
   print parsed