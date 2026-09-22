import json,sys,urllib.request
from pathlib import Path
w=Path(__file__).parent
p=json.loads((w/(sys.argv[1]+"-payloads.json")).read_text())
def call(endpoint,data=None):
 r=urllib.request.Request("http://localhost:8000/api/primitives/"+endpoint,data=json.dumps(data).encode() if data else None,headers={"Content-Type":"application/json"})
 with urllib.request.urlopen(r) as f:return json.load(f)
for endpoint,key in [("status","status"),("briefs","brief")]:
 call(endpoint,p[key])
u=p["brief"]["uuid"]
s=call("status")[u];b=call("briefs")[u]
for k in ["status","reason","main_brief","sub_brief"]:assert s[k]==p["status"][k],k
for k in ["family","brief"]:assert b[k]==p["brief"][k],k
(w/(sys.argv[1]+"-verified.json")).write_text(json.dumps({"status":s,"brief":b},indent=2))
print("Verified",u)
