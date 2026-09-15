from pathlib import Path
import sys,json,hashlib,concurrent.futures,shutil,os,datetime
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT));W=Path(__file__).parent

def check(item):
 ident,family=item
 from icon_set.model.icons.registry import create
 from icon_set.validation.library_qa import inspect_icon
 icon=create(ident);directory=W/'full-qa'/family/ident
 row=inspect_icon(icon,debug_dir=directory)
 folder={'solo':'solo48','container':'container64','sub':'sub32'}[family]
 assert row.get('svg_sha256')==hashlib.sha256((W/'inputs'/folder/(ident+'.svg')).read_bytes()).hexdigest(),ident
 directory.mkdir(parents=True,exist_ok=True);(directory/'cached-row.json').write_text(json.dumps(row))
 return ident,row['status']

def cached_inspect(icon,debug_dir=None,selected=True):
 source=W/'full-qa'/icon.family/icon.icon_id;row=json.loads((source/'cached-row.json').read_text())
 assert hashlib.sha256(icon.to_svg().encode()).hexdigest()==row['svg_sha256'],icon.icon_id
 if debug_dir is not None:
  debug_dir.mkdir(parents=True,exist_ok=True)
  for p in source.iterdir():
   if p.name!='cached-row.json':
    destination=debug_dir/p.name
    if destination.exists():destination.unlink()
    os.link(p,destination)
 return row

if __name__=='__main__':
 from icon_set.model.icons.registry import factories
 from icon_set.scripts import build as builder
 icons=[(i,f.family) for i,f in factories().items()];completed=0
 with concurrent.futures.ProcessPoolExecutor(max_workers=6) as pool:
  jobs=[pool.submit(check,x) for x in icons]
  for job in concurrent.futures.as_completed(jobs):
   job.result();completed+=1
   if completed%25==0 or completed==len(icons):
    (W/'full-qa-progress.json').write_text(json.dumps({'checked':completed,'total':len(icons)}));print('Full QA',completed,'/',len(icons),flush=True)
 builder.inspect_icon=cached_inspect
 print('Publishing through normal build with all fresh validated rows',flush=True)
 result=builder.build(debug=True,rebuild_all=True,qa_overlays=builder.DEFAULT_QA_OVERLAYS)
 (W/'build-exit.json').write_text(json.dumps({'exit_code':result,'completed_at':datetime.datetime.now().isoformat(),'parallel_qa':True}))
 print('Full build finished, exit:',result,flush=True)
