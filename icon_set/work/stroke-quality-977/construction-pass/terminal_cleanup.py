import sys,json,re
from pathlib import Path
from dataclasses import replace
H=Path(__file__).resolve().parent;ROOT=H.parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.validation.library_qa import inspect_icon
from normalize import code
rows={r['id']:r for r in json.loads((H/'baseline.json').read_text())};out=[]
for id,pid in [('read','e2'),('rh','e6'),('shadow-tech-logo','e1')]:
 icon=create(id);prims=[]
 for p in icon.primitives:
  if p.element_id==pid:
   segs=list(p.segments);a,b,old=segs[-2];end=p.end.as_tuple();delta=tuple(end[k]-old[k] for k in range(2));segs[-2]=(a,tuple(b[k]+delta[k] for k in range(2)),end);segs.pop();p=replace(p,segments=tuple(segs))
  prims.append(p)
 icon.primitives=prims;q=inspect_icon(icon);assert q['status']=='pass' and not q['warnings'],(id,q['errors'],q['warnings'])
 p=ROOT/rows[id]['source'];s=p.read_text();s=s[:s.index('    def build(')];s=re.sub(r'REVIEW_ACTION = .*',"REVIEW_ACTION = 'geometry-reconstructed'",s)
 s+='    def build(self):\n        # Plan: absorb the microscopic terminal detour into the preceding smooth cubic.\n        # Reference: original curve and its exact final attachment.\n'+code(icon);p.write_text(s)
 out.append(dict(id=id,source=rows[id]['source'],plan='Absorb the microscopic final curve fragment into its preceding cubic, preserving the exact attachment endpoint.',reference='Original subject; terminal control points and endpoint inspection.'))
(H/'terminal-cleanup.json').write_text(json.dumps(out,indent=2));print('Cleaned terminal fragments:',len(out))
