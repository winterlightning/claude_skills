"""Batch-local resilient intake: an unavailable history is excluded, never assumed eligible."""
from pathlib import Path
import sys,json
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts import primitive_fix as p,work_queue as w
root=Path(__file__).parent
w.TIMEOUT=60
original_call=w.call
claims=[]
def logged_call(base_url,method,path,body=None,query=None):
 result=original_call(base_url,method,path,body,query)
 if path=='/api/work/claim':
  claims.append(result);(root/'remaining-claim-responses.json').write_text(json.dumps(claims,indent=2));print('Claimed',body['icon'],flush=True)
 return result
w.call=logged_call
def resilient_next(base_url,worker,family=None,category=None,icon_type=None,*,limit=1,offset=0,reason=None,max_disapprovals=None):
 assert family=='solo' and max_disapprovals==1 and offset==0 and limit==6
 matches=[];skipped=[];page_offset=0
 def verify(item):
  try:
   history=w.call(base_url,'GET','/api/work/history',query={'icon':item['key']})
   count=w.disapproval_count(history)
   return item,count,None
  except w.ApiError as exc:return item,None,{'status':exc.status,'payload':exc.payload}
 while len(matches)<limit+w.CLAIM_ATTEMPTS:
  page=w.call(base_url,'GET','/api/work/queue',query={'family':family,'limit':w.MAX_PAGE,'offset':page_offset,'max_disapprovals':1})
  with ThreadPoolExecutor(max_workers=6) as pool:
   for first in range(0,len(page['items']),24):
    batch=page['items'][first:first+24]
    for item,count,error in pool.map(verify,batch):
     if error is not None:
      skipped.append({'key':item['key'],'reason':'history unavailable; eligibility unknown','error':error});print('Excluded unverifiable history',item['key'],flush=True)
     elif count<=max_disapprovals:
      item['disapprovals']=count;matches.append(item)
     else:skipped.append({'key':item['key'],'disapprovals':count})
    print('Verified candidates',len(matches),'excluded',len(skipped),flush=True)
    if len(matches)>=limit+w.CLAIM_ATTEMPTS:break
  if len(matches)>=limit+w.CLAIM_ATTEMPTS or page.get('next_offset') is None:break
  page_offset=page['next_offset']
 (root/'remaining-eligibility.json').write_text(json.dumps({'matching':matches,'excluded':skipped},indent=2))
 claimed,last=w._claim(base_url,worker,matches,limit)
 return claimed,{'items':matches},last
w.take_next=resilient_next
raise SystemExit(p.main(['start','--worker','thuan-mac','--limit','6','--max-disapprovals','1','--family','solo','--offset','0']))
