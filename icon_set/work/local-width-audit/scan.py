from pathlib import Path
import sys,json,hashlib,inspect,time,traceback,os
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import get_context
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from detector import analyze,PARAMETERS
from icon_set.model.icons.registry import factories
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/model/icons/solo/'
AUTHOR='gpt-6'
REGISTRY={}
def inspect_one(entry):
 ident,filename,digest=entry
 try:
  obj=REGISTRY[ident]();svg=obj.to_svg();current_hash=hashlib.sha256(svg.encode()).hexdigest()
  baseline_path=ROOT/'icon_set/dist/qa/solo'/ident/'metrics.json'
  baseline=json.loads(baseline_path.read_text()) if baseline_path.exists() else {}
  matching=baseline.get('svg_sha256')==current_hash
  result=analyze(obj)
  lengths=[f['sustained_length'] for f in result['findings']]
  result.update(id=ident,file=filename,source_sha256=digest,source_unchanged=hashlib.sha256(Path(filename).read_bytes()).hexdigest()==digest,
   baseline_status=baseline.get('status') if matching else 'unmatched',baseline_internal_review=baseline.get('needs_review',False) if matching else None,
   narrow_run_max=max(lengths,default=0),variant_of=getattr(obj,'variant_of',None))
  result.pop('parameters',None)
  return result
 except Exception as e:return {'id':ident,'file':filename,'status':'error','error':str(e),'traceback':traceback.format_exc(limit=2)}

if __name__=='__main__':
 REGISTRY=factories();entries=[]
 for ident,cls in sorted(REGISTRY.items()):
  if cls.family!='solo':continue
  p=Path(inspect.getsourcefile(cls));entries.append((ident,str(p),hashlib.sha256(p.read_bytes()).hexdigest()))
 (W/'inventory.json').write_text(json.dumps(entries,indent=2));start=time.time();results=[]
 print('Auditing',len(entries),'solo icons',flush=True)
 with ProcessPoolExecutor(max_workers=4,mp_context=get_context('fork')) as pool:
  for i,row in enumerate(pool.map(inspect_one,entries,chunksize=8),1):
   results.append(row)
   if i%250==0:print(i,'/',len(entries),'elapsed',round(time.time()-start),'seconds',flush=True)
   if i%500==0:(W/'partial.json').write_text(json.dumps(results))
 (W/'results.json').write_text(json.dumps(results))
 summary={'total':len(entries),'analyzed':sum(r['status']!='error' for r in results),'errors':sum(r['status']=='error' for r in results),
  'parameters':PARAMETERS,'elapsed_seconds':round(time.time()-start,2),'source_changed':sum(r.get('source_unchanged')==False for r in results),
  'baseline_unmatched':sum(r.get('baseline_status')=='unmatched' for r in results),'thresholds':{}}
 for threshold in [2,4,6]:
  flagged=[r for r in results if r.get('narrow_run_max',0)>=threshold]
  summary['thresholds'][str(threshold)]={'flagged':len(flagged),'currently_pass':sum(r.get('baseline_status')=='pass' for r in flagged),
   'currently_fail':sum(r.get('baseline_status')=='fail' for r in flagged),'other_baseline':sum(r.get('baseline_status') not in ['pass','fail'] for r in flagged),
   'already_internal_review':sum(r.get('baseline_internal_review')==True for r in flagged),
   'missed_by_old_internal_checker':sum(r.get('baseline_internal_review')==False for r in flagged)}
 (W/'summary.json').write_text(json.dumps(summary,indent=2));print(json.dumps(summary,indent=2),flush=True)
