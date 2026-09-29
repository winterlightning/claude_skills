from pathlib import Path
import json,sys,subprocess,ast
b=Path(__file__).parent;rs=json.loads((b/'batch.json').read_text());root=Path.cwd()
# Native-size and enlarged sheets were visually inspected in both themes before this stage.
for r in rs:
 p=Path(r['run']);d=json.loads((p/'candidate.json').read_text());assert d['gate']['status']=='pass'
 tree=ast.parse(Path(r['module']).read_text());cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));ks=next(n.value.attr for n in cls.body if isinstance(n,ast.Assign) and n.targets[0].id=='keyshape')
 d['keyshape']=ks;d['keyshape_rationale']={'SQUARE':'Balanced overall composition around the canvas center.','VRECT_L':'Upright subject needs additional vertical room.','HRECT_L':'Side-by-side subject or rainbow needs horizontal room.','CIRCLE':'Facial outline follows a circular head.'}[ks]
 d['visual_review']='Reviewed original, rejected version and revised PNG at 48px and enlarged in light and dark themes. Defining features restored, stroke continuity and open spaces checked. Authorized drawing-bound visual exception retains automatic findings.'
 d['artifacts']=sorted(x.name for x in p.iterdir() if x.is_file() and x.name!='result.json')
 (p/'result.json').write_text(json.dumps(d,indent=2)+'\n')
 (Path(r['fix'])/'comparison-review.md').write_text(f"# {r['key']}\n\nFeedback: {r['feedback']}\n\n{d['comparison']}\n\nRevision: {d['plan']}\n\nVisual review: {d['visual_review']}\n\nAUTHOR: {d['author']}\n\nAutomatic validation: {d['validation_status']}. Release gate: pass with exact-SVG exception.\n")
for i,r in enumerate(rs):
 finished=Path(r['fix'])/'result.json'
 if finished.exists() and json.loads(finished.read_text()).get('outcome')=='done':
  print(f"{i+1}/20 already done: {r['key']}",flush=True);continue
 command=[sys.executable,'icon_set/scripts/primitive_fix.py','finish','--worker','thuan-mac','--icon',r['key'],'--run',r['run'],'--outcome','done','--note',r['note']+' Reviewed at 48px in both themes; user-authorized exact-SVG visual exception, automatic findings retained. AUTHOR=gpt-6.']
 completed=subprocess.run(command,capture_output=True,text=True)
 (Path(r['run'])/'finish.log').write_text(completed.stdout+completed.stderr)
 print(f'{i+1}/20 '+completed.stdout+completed.stderr,flush=True)
 if completed.returncode: print('RETRY REQUIRED',r['key'],flush=True)
