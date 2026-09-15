from pathlib import Path
import sys,ast,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-remaining-repair/review-decisions.json'
AUTHOR='gpt-6'
rows=json.loads((ROOT/SOURCE_PATH).read_text())
records=json.loads((W/'repairs.json').read_text()) if (W/'repairs.json').exists() else []
helpers='''
def ring(self,name,x,y,r):
    self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
    self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
    self.add_contour(name,name+'-a',name+'-b',closed=True)
def branches(self, branches):
    parts=[]
    for name,points in branches:
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            key=f'{name}-{i}';self.add_line(key,a,b);members.append(key);parts.append((key,a,b))
        if len(members)>1:self.add_contour(name,*members)
    for i,(name,a,b) in enumerate(parts):
        for other,c,d in parts[i+1:]:
            if a in (c,d) or b in (c,d):self.relate('connect',name,other)
'''
def save(n,body,reason,keyshape=None):
 row=rows[n-1];old=next((r for r in records if r['number']==n),None)
 if old:dest=ROOT/old['file'];ident=old['icon_id'];base=dest.read_text()
 else:dest,ident,base=prepare_variant(row['selected'],'solo','Visual reconstruction after full 500-icon audit')
 t=ast.parse(base);cl=next(x for x in t.body if isinstance(x,ast.ClassDef));metadata={z.id:x.value.value for x in t.body if isinstance(x,ast.Assign) and isinstance(x.value,ast.Constant) for z in x.targets if isinstance(z,ast.Name)}
 if not old and metadata.get('SOURCE_ICON_ID'):dest=dest.with_name(dest.stem+'_'+metadata['SOURCE_ICON_ID'].replace('-','_')+'.py')
 cl.body=[x for x in cl.body if not isinstance(x,ast.FunctionDef) or x.name not in ('build','ring','branches')]
 cl.body+=ast.parse(helpers).body+ast.parse('def build(self):\n    '+repr(reason)+'\n'+''.join('    '+l+'\n' for l in body.splitlines())).body
 if keyshape:
  for x in cl.body:
   if isinstance(x,ast.Assign) and any(getattr(y,'id',None)=='keyshape' for y in x.targets):x.value=ast.parse('Keyshape.'+keyshape,mode='eval').body
 for x in t.body:
  if isinstance(x,ast.Assign) and any(getattr(y,'id',None)=='AUTHOR' for y in x.targets):x.value=ast.Constant(AUTHOR)
 t.body[0]=ast.Expr(ast.Constant(reason+'\n\n'+(ast.get_docstring(t) or '')))
 ast.fix_missing_locations(t);dest.write_text(ast.unparse(t)+'\n')
 rec=dict(number=n,parent=row['selected'],icon_id=ident,file=str(dest.relative_to(ROOT)),reason=reason)
 if old:records.remove(old)
 records.append(rec);(W/'repairs.json').write_text(json.dumps(sorted(records,key=lambda r:r['number']),indent=2)+'\n');print(n,ident)

if __name__=='__main__':
 for n in (15,16):
  body="""# Mirrored pointed hull; paddle stored alongside rather than piercing cockpit.
axis=16
self.add_arc('hull-rt',(axis,8),(28,24),radius_x=20)
self.add_arc('hull-rb',(28,24),(axis,40),radius_x=20)
self.add_arc('hull-lb',(axis,40),(4,24),radius_x=20)
self.add_arc('hull-lt',(4,24),(axis,8),radius_x=20)
self.add_contour('hull','hull-rt','hull-rb','hull-lb','hull-lt',closed=True)
for name,top in [('upper',8),('lower',28)]:
    self.add_arc(name+'-top',(36,top+4),(44,top+4),radius_x=4)
    self.add_line(name+'-r',(44,top+4),(44,top+8))
    self.add_arc(name+'-base',(44,top+8),(40,top+12),radius_x=4)
    self.add_arc(name+'-bl',(40,top+12),(36,top+8),radius_x=4)
    self.add_line(name+'-l',(36,top+8),(36,top+4))
    self.add_contour(name,name+'-top',name+'-r',name+'-base',name+'-bl',name+'-l',closed=True)
self.add_line('shaft',(40,20),(40,28))
self.relate('connect','shaft','upper')
self.relate('connect','shaft','lower')
"""
  # Bottom blade top attachment is a point on its top semicircle, split explicitly.
  body=body.replace("self.add_arc(name+'-top',(36,top+4),(44,top+4),radius_x=4)","self.add_arc(name+'-t1',(36,top+4),(40,top),radius_x=4)\n    self.add_arc(name+'-t2',(40,top),(44,top+4),radius_x=4)").replace("name+'-top',name+'-r'","name+'-t1',name+'-t2',name+'-r'")
  if n==15:body+="self.ring('cockpit',16,24,3)\n"
  save(n,body,'Reconstruct the pointed kayak with mirrored hull curves and two matching rounded paddle blades. Paddle moved alongside to preserve both blades and the cockpit counter at SOLO48. Source kayak inspected; Lucide sailboat informs a coherent hull, with deliberate equipment asymmetry.','HRECT_L')
 save(14,"""self.ring('head',24,11,5)
self.add_arc('torso',(24,24),(20,32),radius_x=10)
self.branches([('guard-left',[(24,24),(14,25),(6,21)]),('guard-right',[(24,24),(36,26),(39,17),(42,17)]),('leg-left',[(20,32),(12,35),(6,42)]),('leg-right',[(20,32),(33,34),(38,42)])])
for name in ['guard-left-0','guard-right-0','leg-left-0','leg-right-0']:self.relate('connect','torso',name)
""",'Karate guard: enlarged radius-5 circular head at (24,11), shoulder (24,24), exactly4 painted clearance. Torso arc radius10 starts vertically at shoulder, matching head axis; wide bent knees and raised fist preserve the original fighting stance. Human references full_body_ref.png and approved approaching-ball comparison; Lucide person-standing shared limb joints.')
 save(13,"""self.ring('head',22,11,5)
self.add_arc('torso',(22,24),(26,32),radius_x=10,sweep=False)
self.branches([('arm',[(22,24),(14,28),(6,28)]),('handle',[(6,28),(6,32)]),('leg-down',[(26,32),(23,36)]),('leg-extended',[(26,32),(34,30),(42,30)]),('hull',[(6,32),(14,34),(23,36),(38,39)]),('water',[(6,42),(14,42)])])
for part in ['arm-0','leg-down-0','leg-extended-0']:self.relate('connect','torso',part)
""",'Jet ski: replace the disconnected zigzag with an identifiable shoulder, curved torso, one planted leg and one rearward extended leg. Radius5 head (22,11), shoulder (22,24), exact4 ink gap; upper torso vertical tangent. Original jet-ski pose and full_body_ref.png inspected; coherent Lucide sailboat hull construction supports equipment simplification.')
 save(17,"""self.add_arc('kite-canopy',(26,6),(42,22),radius_x=16)
self.add_polyline('kite-edges',(42,22),(26,22),(26,6))
self.relate('connect','kite-canopy','kite-edges')
self.ring('head',11,15,4)
self.add_arc('torso',(11,27),(15,35),radius_x=10,sweep=False)
self.branches([('arm',[(11,27),(20,27),(26,22)]),('rear-leg',[(15,35),(10,42)]),('front-leg',[(15,35),(23,34),(27,39)]),('ski',[(6,42),(10,42),(26,42),(31,38)])])
for p in ['arm-0','rear-leg-0','front-leg-0']:self.relate('connect','torso',p)
self.relate('connect','arm-1','kite-edges')
""",'Kite skier: distinguish the reaching arm from the curved backward-leaning torso and bend both legs into the skiing action. Radius4 head (11,15), shoulder (11,27), exact4 painted clearance and vertical torso tangent. Original reference and full_body_ref.png inspected. Shared kite corner is the real tether attachment; keep its asymmetry.')
