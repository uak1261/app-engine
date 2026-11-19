import os,json,sys,urllib.request
U="https://mcp.appkittie.com"
def call(method,params=None,i=1):
    req=urllib.request.Request(U,data=json.dumps({"jsonrpc":"2.0","id":i,"method":method,"params":params or {}}).encode(),
      headers={"Authorization":"Bearer "+os.environ.get("APPKITTIE_API_KEY",""),"Content-Type":"application/json","Accept":"application/json, text/event-stream"})
    t=urllib.request.urlopen(req,timeout=120).read().decode()
    if t.lstrip().startswith("event") or "data:" in t[:20]:
        t=[l[5:] for l in t.splitlines() if l.startswith("data:")][0]
    return json.loads(t)
if __name__=="__main__":
    m=sys.argv[1]
    if m=="list":
        d=call("tools/list")
        for t in d["result"]["tools"]:
            if t["name"]=="search_apps": print(json.dumps(t["inputSchema"]["properties"].get("categories")))
    else:
        args=json.loads(sys.argv[2]); out=sys.argv[3]
        d=call("tools/call",{"name":m,"arguments":args})
        txt=d["result"]["content"][0]["text"]
        open(out,"w").write(txt)
        print(("ERROR " if d["result"].get("isError") else "ok ")+out, len(txt))
