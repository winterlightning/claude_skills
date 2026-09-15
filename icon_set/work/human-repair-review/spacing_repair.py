"""Second geometry pass over the existing repair variants."""
from repair import *
variants=json.loads((OUT/'variants.json').read_text())
repairs=json.loads((OUT/'repairs.json').read_text())
vs={r['parent']:r for r in variants}
def current(r):
 v=vs[r['icon_id']];name=v['path'][:-3].replace('/','.');baseline=OUT/'spacing-before'/Path(v['path']).name
 if baseline.exists():
  ns={'__name__':name,'__package__':'icon_set.model.icons.solo'};exec(compile(baseline.read_text(),str(baseline),'exec'),ns);classes=ns.values()
 else:classes=vars(importlib.import_module(name)).values()
 return next(c for c in classes if inspect.isclass(c) and issubclass(c,Icon) and getattr(c,'icon_id',None)==v['icon_id'])()
def drop(i,*ids):
 ids=set(ids);i.primitives=[p for p in i.primitives if p.element_id not in ids]
 i.contours=[replace(c,members=tuple(m for m in c.members if m not in ids)) for c in i.contours if any(m not in ids for m in c.members)]
 existing={p.element_id for p in i.primitives}|{c.contour_id for c in i.contours}
 i.relationships=[r for r in i.relationships if all(m in existing for m in r.members)]
def patch(i,name,**kw):i.primitives=[replace(p,**kw) if p.element_id==name else p for p in i.primitives]
def change(i,n):
 if n==66:i.human_construction='bust'
 if n==1:move_joint(i,(24,31),(26,28))
 if n==26:move_joint(i,(28,24),(31,22))
 if n==27:move_joint(i,(8,30),(8,27));move_joint(i,(20,30),(20,27))
 if n==34:
  move_joint(i,(24,34),(18,34));move_joint(i,(23,26),(28,22))
 if n==42:move_joint(i,(28,28),(29,24))
 if n in {90,168,169}:drop(i,'rear-hair')
 if n in {168,169}:
  # Split the circular face at the actual fringe and hair junctions.
  patch(i,'front-head-a',start=Point(6,16),end=Point(26,16))
  patch(i,'front-head-b',start=Point(26,16),end=Point(6,16))
  if n==168:move_joint(i,(16,13),(16,14))
 if n==96:
  move_joint(i,(18,36),(20,34));move_joint(i,(16,42),(20,42));move_joint(i,(26,40),(30,42));move_joint(i,(28,24),(26,22));move_joint(i,(28,27),(26,24));move_joint(i,(20,26),(18,24))
 if n==100:
  move_joint(i,(16,29),(16,30));move_joint(i,(26,28),(26,30));move_joint(i,(6,27),(6,22));move_joint(i,(20,36),(20,38));move_joint(i,(30,36),(30,38))
 if n==101:
  move_head(i, next(r for r in repairs if r['number']==101)['after_figures'][0], 2, 0)
  move_joint(i,(18,22),(20,22));move_joint(i,(24,32),(28,32));move_joint(i,(16,24),(14,26));move_joint(i,(6,24),(6,26));move_joint(i,(16,32),(14,34));move_joint(i,(6,32),(6,34))
 if n==104:move_joint(i,(38,42),(42,42))
 if n==133:move_joint(i,(10,32),(10,36));move_joint(i,(20,36),(20,38))
 if n==139:move_joint(i,(19,10),(18,7));move_joint(i,(12,6),(10,6));move_joint(i,(15,16),(12,16))
 if n==180:move_joint(i,(31,34),(35,34));move_joint(i,(31,28),(35,28))
 return i
if __name__=='__main__':
 for r in repairs:
  if len(sys.argv)>1 and str(r['number']) not in sys.argv[1:]:continue
  i=change(current(r),r['number']);q=record_report(i)
  (OUT/'after'/f'{r["icon_id"]}.svg').write_text(i.to_svg())
  print(r['number'],q['status'],q['errors'],q['warnings'],flush=True)
