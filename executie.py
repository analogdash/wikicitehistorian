start = time.time()
while "batchcomplete" not in wikijsondata:
    conti = wikijsondata["continue"]["continue"]
    rvconti = wikijsondata["continue"]["rvcontinue"]
    wikiapidata = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=50&rvprop=ids|timestamp|user|userid|parsedcomment|tags|size|content&pageids="+str(pageid)+"&continue="+conti+"&rvcontinue="+rvconti)
    wikijsondata = json.loads(wikiapidata.content)
    revisiondata.extend(wikijsondata["query"]["pages"][str(pageid)]["revisions"])
    print("Now grabbing "+wikijsondata["query"]["pages"][str(pageid)]["revisions"][0]["timestamp"]+" time elapsed "+str(datetime.timedelta(seconds=time.time()-start)))

endtime = time.time()

print("that whole thing took "+str(datetime.timedelta(seconds=endtime-start))+" for "+str(len(revisiondata))+" revisions.")
