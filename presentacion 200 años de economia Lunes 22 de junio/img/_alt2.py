import json,urllib.request,urllib.parse
UA={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read()
def is_img(b): return b[:3]==b'\xff\xd8\xff' or b[:8]==b'\x89PNG\r\n\x1a\n'
def fetch(q,prefix,want=3):
    api="https://api.openverse.org/v1/images/?"+urllib.parse.urlencode({"q":q,"page_size":25,"license_type":"all"})
    data=json.loads(get(api)); n=0
    for r in data.get("results",[]):
        u=r.get("url")
        if not u: continue
        try: b=get(u)
        except Exception: continue
        if is_img(b) and len(b)>35000:
            n+=1; fn=f"{prefix}_{n}.jpg"; open(fn,"wb").write(b)
            print(fn, len(b)//1024,"KB","|",r.get("title","")[:42])
            if n>=want: break
fetch("warehouse boxes logistics","cand08",4)
