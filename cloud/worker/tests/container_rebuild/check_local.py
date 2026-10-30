from pathlib import Path
import sys
from urllib.parse import urlsplit
import urllib.request,urllib.error,http.cookiejar,json,subprocess,hashlib
BASE=sys.argv[1] if len(sys.argv)>1 else 'http://127.0.0.1:8891'
assert urlsplit(BASE).scheme == 'http' and urlsplit(BASE).hostname == '127.0.0.1' and urlsplit(BASE).port, 'Only isolated loopback fixtures are allowed'
COMBINE=Path(__file__).resolve().parents[4]/'icon_set/scripts/templates/combine.js'
op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))
def call(path,body=None):
 req=urllib.request.Request(BASE+path,data=None if body is None else json.dumps(body).encode(),headers={'Content-Type':'application/json'})
 try:
  with op.open(req) as r:return r.status,r.read()
 except urllib.error.HTTPError as e:return e.code,e.read()
def js(path,body=None):
 status,data=call(path,body);return status,json.loads(data)
assert js('/api/auth/login',{'username':'tester','password':'preview-only'})[0]==200
for rid in ['api-regression','plain-control']:
 i=js('/api/combinations?q='+rid)[1]['items'][0]; d=js('/api/combinations/drawings?keys='+','.join(p['icon'] for p in i['parts']))[1]
 script="const C=require(process.argv[2]);const a=JSON.parse(process.argv[1]);console.log(JSON.stringify(C.container(a.main,a.sub,{canvas:64,box:{x:14,y:14,w:36,h:36}})));"
 result=json.loads(subprocess.check_output(['node','-e',script,json.dumps({'main':d[i['parts'][0]['icon']]['svg'],'sub':d[i['parts'][1]['icon']]['svg']}),str(COMBINE)]))
 b={'reference_id':rid,'expected_sha256':i['icon']['svg_sha256'],'svg':result['svg'],'parts':{p['role']:{'icon':p['icon'],'svg_sha256':p['current_sha'],'layout':result['layout'][p['role']]} for p in i['parts']}}
 status,saved=js('/api/combinations/build',{'builds':[b]});assert status==200 and saved['results'][0]['ok'],(status,saved)
 fresh=js('/api/combinations?q='+rid)[1]['items'][0];served=call(fresh['icon']['preview_url'])[1]
 assert hashlib.sha256(served).hexdigest()==fresh['icon']['svg_sha256']==hashlib.sha256(result['svg'].encode()).hexdigest()
 choice=js('/api/icon-artwork?icon='+i['icon']['key'])[1]
 if rid=='api-regression':assert choice['source_mode']=='use_org' and choice['choice']['uploaded']['svg_sha256']==i['icon']['svg_sha256'] and choice['choice']['revision']==3
 status,stale=js('/api/combinations/build',{'builds':[b]});assert status==200 and not stale['results'][0]['ok'],stale
 b['expected_sha256']=fresh['icon']['svg_sha256'];status,repeated=js('/api/combinations/build',{'builds':[b]});assert repeated['results'][0]['ok'],repeated
 print(rid,': selected upload superseded / served hash matches / stale save refused / repeated save succeeds')
print('PASS real local Worker HTTP integration')
