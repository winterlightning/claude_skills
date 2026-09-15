from humans import *
# Kayak: a smooth pointed hull and an elongated, full-width cockpit.
for n in (15,16):
 r=next(r for r in records if r['number']==n);t=ast.parse((ROOT/r['file']).read_text());b=next(x for x in ast.walk(t) if isinstance(x,ast.FunctionDef) and x.name=='build');body='\n'.join(ast.unparse(x) for x in b.body[1:]);lines=[]
 for x in b.body[1:]:
  text=ast.unparse(x)
  if "'hull" in text or "'cockpit" in text:continue
  lines.append(text)
 body='\n'.join(lines)+"""
self.add_bezier('hull-rt',(17,8),((25,14),(30,18),(30,24)))
self.add_bezier('hull-rb',(30,24),((30,30),(25,34),(17,40)))
self.add_bezier('hull-lb',(17,40),((9,34),(4,30),(4,24)))
self.add_bezier('hull-lt',(4,24),((4,18),(9,14),(17,8)))
self.add_contour('hull','hull-rt','hull-rb','hull-lb','hull-lt',closed=True)
"""
 if n==15:body+="""self.add_arc('cockpit-r',(17,18),(17,30),radius_x=4,radius_y=6)
self.add_arc('cockpit-l',(17,30),(17,18),radius_x=4,radius_y=6)
self.add_contour('cockpit','cockpit-r','cockpit-l',closed=True)
"""
 save(n,body,r['reason'])
# Preserve the wheelchair rim rather than moving one of its attachment nodes.
specs[142]=('head','person-1',(16,22),(16,22),(16,10),4)
repair_pose(142,specs[142])
# Fix repeated head placement and shared arm elevations in both runners.
r=next(r for r in records if r['number']==263);d=create(r['icon_id']).draw()
pm={(14,23):(14,22),(34,23):(34,22),(6,23):(6,22),(42,18):(42,22)}
save(263,emit(d,{'left-head':(14,10,4),'right-head':(34,10,4)},{},pm),r['reason'].replace('(14, 23)','(14, 22)').replace('(14, 11)','(14, 10)'))
# Split smooth torso from the adjoining leg run at the existing hip node.
for n in specs:
 r=next(r for r in records if r['number']==n);d=create(r['icon_id']).draw();curves={p.element_id for p in d.primitives if isinstance(p,Bezier)}
 split=[c for c in d.contours if len(c.members)>1 and any(m in curves for m in c.members)]
 if not split:continue
 body=emit(d,{},{}).splitlines();body=[l for l in body if not any(l.startswith(f'self.add_contour({c.contour_id!r},') for c in split)]
 for c in split:
  runs=[];run=[]
  for m in c.members:
   if m in curves:
    if run:runs.append(run);run=[]
    runs.append([m])
   else:run.append(m)
  if run:runs.append(run)
  for j,run in enumerate(runs):
   name=c.contour_id if j==0 else c.contour_id+'-section-'+str(j)
   body.append(f'self.add_contour({name!r},*{tuple(run)!r},closed=False)')
  for a,b in zip(c.members,c.members[1:]):body.append(f'self.relate("connect",{a!r},{b!r})')
 # Preserve genuine connections to external branches using authored endpoints.
 ps=d.primitives
 for i,a in enumerate(ps):
  for b in ps[i+1:]:
   if a.start in (b.start,b.end) or a.end in (b.start,b.end):body.append(f'self.relate("connect",{a.element_id!r},{b.element_id!r})')
 save(n,'\n'.join(body),r['reason'])
