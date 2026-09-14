"""Propose bounded whole-symbol spacing edits; original Python files are untouched."""
SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/work/spacing-remaining/targets.json'
AUTHOR = 'gpt-6'
import sys,json,re,copy,itertools,pathlib,math
from dataclasses import replace
ROOT=pathlib.Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.model.icons.registry import create
from icon_set.model.primitives import Line,Arc,Bezier,Point,Relationship,primitive_to_dict
W=pathlib.Path(__file__).parent

def groups(i):
 cs={c.contour_id:set(c.members) for c in i.contours};owned=set().union(*cs.values()) if cs else set()
 cs.update({p.element_id:{p.element_id} for p in i.primitives if p.element_id not in owned})
 ends={p.element_id:{p.start.as_tuple(),p.end.as_tuple()} for p in i.primitives}
 namedends={n:set().union(*(ends[p] for p in ps)) for n,ps in cs.items()}
 # Only genuine shared authored endpoints qualify as automatic contact repairs.
 for a,b in itertools.combinations(cs,2):
  if namedends[a]&namedends[b] and not any(a in r.members and b in r.members for r in i.relationships):i.relationships.append(Relationship('connect',(a,b)))
 parent={n:n for n in cs}
 def find(x):
  while parent[x]!=x:x=parent[x]
  return x
 def owner(x):return next((k for k,v in cs.items() if x==k or x in v),None)
 for r in i.relationships:
  if r.kind!='connect':continue
  ns=[owner(x) for x in r.members];ns=[n for n in ns if n]
  for n in ns[1:]:parent[find(n)]=find(ns[0])
 gs={}
 for k,v in cs.items():gs.setdefault(find(k),set()).update(v)
 return list(gs.values())

def score(i):
 try:r=i.validate_icon()
 except Exception:return 1e6,None
 if r.status=='valid':return 0,r
 cost=0
 for e in list(r.errors)+list(r.warnings):
  if 'mic [' in e:
   m=re.search(r'are ([\d.]+) apart',e);gap=float(m.group(1)) if m else 0;cost+=1+max(0,8-gap)
  else:cost+=100
 return cost,r

def trans(p,scale,cx,cy,dx,dy):
 def xy(x,y):return (round(cx+(x-cx)*scale)+dx,round(cy+(y-cy)*scale)+dy)
 st=Point(*xy(p.start.x,p.start.y));en=Point(*xy(p.end.x,p.end.y))
 if isinstance(p,Line):return replace(p,start=st,end=en)
 if isinstance(p,Arc):return replace(p,start=st,end=en,radius_x=max(1,round(p.radius_x*scale)),radius_y=max(1,round(p.radius_y*scale)))
 def cp(q):return (cx+(q[0]-cx)*scale+dx,cy+(q[1]-cy)*scale+dy)
 return replace(p,start=st,end=en,segments=tuple((cp(a),cp(b),xy(*c)) for a,b,c in p.segments))

def propose(n):
 original=create(n);i=copy.deepcopy(original);gs=groups(i);start,_=score(original);cost,r=score(i);steps=[]
 for iteration in range(4):
  if cost==0:break
  names=set()
  for e in list(r.errors)+list(r.warnings):
   m=re.search(r'mic \[([^]]+)\]: (\S+) and (\S+) are ',e)
   if m:names.update(m.groups())
  primnames=set(names)
  for c in i.contours:
   if c.contour_id in names:primnames.update(c.members)
  active=[g for g in gs if g&primnames]
  best=None;bestcost=cost
  for g in sorted(active,key=len):
   ps=[p for p in i.primitives if p.element_id in g];xs=[v for p in ps for v in (p.start.x,p.end.x)];ys=[v for p in ps for v in (p.start.y,p.end.y)]
   if len(g)==len(i.primitives):continue
   owncx=round((min(xs)+max(xs))/2);owncy=round((min(ys)+max(ys))/2)
   ops=[(1,0,0,dx,dy) for dx,dy in ((0,-1),(0,1),(-1,0),(1,0),(-1,-1),(1,-1),(-1,1),(1,1),(0,-2),(0,2),(-2,0),(2,0))]
   ops += [(s,cx,cy,0,0) for s in (.94,.88,.82) for cx,cy in ((owncx,owncy),(24,24))]
   for op in ops:
    trial=copy.deepcopy(i);trial.primitives=[trans(p,*op) if p.element_id in g else p for p in i.primitives];tc,tr=score(trial)
    if tc<bestcost-0.0001:best=(trial,tr,sorted(g),op);bestcost=tc
    if tc==0:break
   if bestcost==0:break
  if best is None:break
  i,r,g,op=best;steps.append({'members':g,'operation':op});cost=bestcost
 return {'id':n,'initial_score':start,'score':cost,'report':r.describe() if r else '', 'steps':steps,'primitives':[primitive_to_dict(p) for p in i.primitives], 'contours':[{'id':c.contour_id,'members':c.members,'closed':c.closed} for c in i.contours],'relationships':[{'kind':r.kind,'members':r.members} for r in i.relationships]}
if __name__=='__main__':
 start=int(sys.argv[1]);end=int(sys.argv[2]);rs=json.load(open(W/'targets.json'));out=W/f'candidates-{start:03}-{end:03}.json';results=[]
 for row in rs[start:end]:
  q=propose(row['id']);results.append(q);out.write_text(json.dumps(results,indent=2));print(q['id'],q['score'],len(q['steps']),flush=True)
