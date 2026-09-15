from pathlib import Path
import sys,ast,json
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts.create_variant import prepare_variant
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/solo-remaining-repair/before.json'
AUTHOR='gpt-6'
W=Path(__file__).parent
rows=json.loads((W/'before.json').read_text())
existing=json.loads((W/'repairs.json').read_text()) if (W/'repairs.json').exists() else []

def save(n,pairs=(),body=None,reason='Rebalance the cramped opening while preserving the subject.'):
 row=rows[n-1];s=Path(row['file']).read_text()
 for a,b in pairs:
  assert a in s,(n,a)
  s=s.replace(a,b)
 old=next((x for x in existing if x['number']==n),None)
 if old: dest=ROOT/old['file'];newid=old['icon_id'];base=dest.read_text()
 else: dest,newid,base=prepare_variant(row['id'],'solo','Hole and centerline reconstruction')
 t=ast.parse(base);e=ast.parse(s);tc=next(x for x in t.body if isinstance(x,ast.ClassDef));ec=next(x for x in e.body if isinstance(x,ast.ClassDef))
 funcs={x.name:x for x in ec.body if isinstance(x,ast.FunctionDef)}
 if body: funcs['build']=ast.parse('def build(self):\n'+''.join('    '+l+'\n' for l in body.splitlines())).body[0]
 funcs['build'].body.insert(0,ast.Expr(ast.Constant(reason)))
 tc.body=[funcs.get(x.name,x) if isinstance(x,ast.FunctionDef) else x for x in tc.body]
 # Keyshape edits remain explicit source edits.
 for x in tc.body:
  if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='keyshape' for y in x.targets):
   x.value=next(y.value for y in ec.body if isinstance(y,ast.Assign) and any(isinstance(z,ast.Name) and z.id=='keyshape' for z in y.targets))
 meta={z.id:y.value.value for y in t.body if isinstance(y,ast.Assign) and isinstance(y.value,ast.Constant) for z in y.targets if isinstance(z,ast.Name)}
 for x in t.body:
  if isinstance(x,ast.Assign) and any(isinstance(y,ast.Name) and y.id=='AUTHOR' for y in x.targets):x.value=ast.Constant(AUTHOR)
 if not old and meta.get('SOURCE_ICON_ID'): dest=dest.with_name(dest.stem+'_'+meta['SOURCE_ICON_ID'].replace('-','_')+'.py')
 ast.fix_missing_locations(t);dest.write_text(ast.unparse(t)+'\n')
 record=dict(number=n,parent=row['id'],icon_id=newid,file=str(dest.relative_to(ROOT)),reason=reason)
 if old:existing.remove(old)
 existing.append(record);(W/'repairs.json').write_text(json.dumps(sorted(existing,key=lambda r:r['number']),indent=2)+'\n')
 print(n,newid)

if __name__=='__main__':
 save(13,[("(20, 8), (24, 8), radius_x=2, radius_y=2","(19, 9), (25, 9), radius_x=3, radius_y=3"),("(24, 8), (20, 8), radius_x=2, radius_y=2","(25, 9), (19, 9), radius_x=3, radius_y=3"),("(24, 18)","(22, 20)")],reason='Open the filled head with radius 3; place the nearest shoulder at (22,20), exactly 4 ink units below the head. Shared full_body_ref.png proportions.')
 save(26,[("(42,6),(32,38),(31,42)","(42,6),(32,32),(31,42)"),("(26,32),(32,38)","(26,32),(32,32)"),("(32,38),(38,32)","(32,32),(38,32)")],reason='Move the foil attachment to the guard midpoint so the blade does not trap a tiny counter against its right tip.')
 save(52,[("(6, 29)","(6, 25)")],reason='Lift the extended leg to open the space between the two feet and knees.')
 save(58,[("(32,30),(14,6),(8,12),(12,12),(12,18),(18,18),(18,22),(24,22),(22,30)","(32,30),(14,6),(6,14),(10,14),(10,22),(16,22),(16,30)")],reason='Reduce the crowded saw teeth to two broad steps with one clear blade opening.')
 save(65,[("(16,32)","(16,36)"),("(8,32)","(6,36)"),("(24,32)","(26,36)"),("(24,42)","(26,42)"),("(8,42)","(6,42)")],reason='Lower the suspended weight to separate its top edge from the pulley rim.')
 save(68,[("'muzzle',6,20,2","'muzzle',7,20,3"),("'barrel',(8,20)","'barrel',(10,20)")],reason='Open the circular muzzle while preserving its left envelope and the attached barrel.')
 save(74,[("(12, 26), (6, 36), (14, 36)","(6, 26), (6, 36), (14, 36)")],reason='Use an open-top four with a full-width counter instead of a nearly closed triangular wedge.')
 save(95,[("(24,27),(26,32)","(24,27),(30,33)"),("(24,27),(19,31),(22,32)","(24,27),(17,33),(20,34)")],reason='Spread the knees and shorten the inward foot to remove the trapped speck between crossed legs.')
 save(109,[("(24,17),(24,24),(27,24)","(24,17),(24,24)")],reason='Remove the tiny crowded hour hand; the clear clock face and vertical hand retain the station clock.')
 save(118,[("circle('ball',40,31,2)","circle('ball',39,31,3)")],reason='Open the tennis ball to radius 3 and preserve the right envelope.')
 save(119,[("circle('ball',8,34,2)","circle('ball',9,34,3)")],reason='Open the tennis ball to radius 3 while keeping it inside the left envelope.')
 save(127,[("circle('head',37,28,2)","circle('head',37,27,3)"),("(35,40),(42,38)","(35,38),(37,38),(42,40)")],reason='Open the pilot head; nearest body point (37,38) sits exactly 4 ink units below its radius-3 ring.')
 save(191,[("(22, 36)","(22, 40)"),("(13, 44)","(13, 44)"),("9, 8, True","9, 4, True")],reason='Lower and flatten the stand so the meridian no longer pinches its upper shoulder.')
 save(235,[("(21,34),(24,39),(17,44),(25,44)","(19,33),(20,37),(13,44),(25,44)")],reason='Move the forward shin away from the rear leg and retain the kneeling posture.')
 save(249,[("(26, 17), (30, 17), radius_x=2, radius_y=2","(25, 17), (31, 17), radius_x=3, radius_y=3"),("(30, 17), (26, 17), radius_x=2, radius_y=2","(31, 17), (25, 17), radius_x=3, radius_y=3")],reason='Open the punched hole in the front tag.')
 save(270,[("(22, 29)","(22, 25)"),("(18, 21)","(18, 20)")],reason='Raise the hip to open the triangular space above the step.')
 save(272,[("(('left',8),('right',40))","(('left',9),('right',39))"),("self.circle('hand-'+side,x,32,2)","self.circle('hand-'+side,x,32,3)")],reason='Open both repeated hand loops with matching radius 3.')
 save(310,[("(32, 40)","(29, 38)"),("(37, 38)","(39, 36)")],reason='Open the toe and knee recess instead of letting the foot fold back into its own outline.')
 save(340,[("(33, 8), (37, 8), radius_x=2, radius_y=2","(32, 9), (38, 9), radius_x=3, radius_y=3"),("(37, 8), (33, 8), radius_x=2, radius_y=2","(38, 9), (32, 9), radius_x=3, radius_y=3")],reason='Open the head circle; head bottom12 and shoulder20 preserve exactly4 visible ink clearance.')
 save(347,[("(8, 14), (12, 14), radius_x=2, radius_y=2","(9, 13), (15, 13), radius_x=3, radius_y=3"),("(12, 14), (8, 14), radius_x=2, radius_y=2","(15, 13), (9, 13), radius_x=3, radius_y=3")],reason='Open and align the head over the nearest shoulder at (12,24), retaining exactly4 ink clearance.')
 save(359,[("(14,24),(10,20),(44,8),(44,14),(30,24)","(14,24),(6,19),(44,8),(44,14),(30,24)")],reason='Widen the rear breech corner above the wheel.')
 save(366,[("[(24,26),(22,30),(26,32),(24,38)]","[(24,26),(24,30)]")],reason='Reduce the full zigzag crack to a short cleft so the heart has one broad opening.')
 save(371,[("(18,26),(18,32),(6,26)","(18,24),(18,34),(6,28)")],reason='Open the bent paw recess while retaining the raised paw gesture.')
 save(380,[("(34,6),(42,6),(42,14)","(42,6),(42,14)")],reason='Remove the crowded upper barb beside the heart lobe; the remaining open arrowhead preserves direction.')
 save(386,[("pt(14, 30), pt(20, 24), pt(20, 22)","pt(14,30), pt(22,24), pt(22,22)"),("pt(20, 22), pt(18, 16)","pt(22,22), pt(18,16)")],reason='Open both symmetric shoulder notches between the onion domes.')
 save(399,[("(22,24),(44,24),(44,33)","(22,24),(44,20),(44,33)")],reason='Lift the rear deck away from the wheel to open the pinched corner.')
 save(427,[("(18,30),(12,40),(16,42),(24,31)","(16,28),(10,40),(16,42),(24,31)")],reason='Widen the lower tail-fin root and keep the intentional diagonal aircraft silhouette.')
 save(441,[("(34,34),(30,31),(37,26),(44,31),(40,34)","(30,31),(37,25),(44,31)"),("(37,26)","(37,25)")],reason='Remove inward hooked hands that close tiny armpit counters; place the shoulder exactly4 ink units below the radius4 head.')
 save(451,[("rx,ry=20,9","rx,ry=20,6")],reason='Narrow the repeated elliptical orbits together to rebalance all six counters without breaking rotation symmetry.')
 save(474,[("(4, 24),(14, 24),(30, 24)","(4, 20),(14, 20),(30, 20)"),("(14, 16),(14, 24)","(14, 16),(14, 20)")],reason='Raise the cargo bed above the wheel to remove its tiny rear corner pocket.')
 save(480,[("(4,26),(18,26),(34,26),(40,26),(44,30)","(4,22),(18,22),(34,22),(40,22),(44,26)"),("(26,8),(34,26)","(26,8),(34,22)"),("(18,16),(18,26)","(18,14),(18,22)")],reason='Raise the body shoulder above both wheels and move its attached windscreen and roll bar with it.')
