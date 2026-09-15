exec(open(__file__.replace('finish_shapes.py','repair.py')).read().split('edit(3,')[0])
def refine(i,changes,note):
 p=Path(P[i]['target_file']);b=W/'stage-two'/p.name;b.parent.mkdir(exist_ok=True)
 if not b.exists():b.write_bytes(p.read_bytes())
 s=b.read_text()
 for a,z in changes:
  assert a in s,(i,a);s=s.replace(a,z)
 p.write_text('# Refinement: '+note+'\n'+s);CHANGED[i]=note
refine(4,[('(16,6)','(12,6)')],'Widen the back palm between its outer edge and the front thumb.')
refine(7,[('(9, 13)','(9, 14)'),('(9, 19)','(9, 20)')],'Separate the circular discus from the circular head by more than eight units.')
refine(11,[('(16, 15)','(16, 17)'),('(28, 15)','(28, 17)')],'Lower the forehead edge inside the full headdress arch.')
refine(19,[('(30, 20)','(30, 22)')],'Open the thumb bend without crowding the right cuff.')
refine(24,[('(6,36)','(6,38)')],'Put the rear skate wheels below the angled pushing foot.')
refine(30,[("('A',18,18,True,(6,24))", "('L',(14,42)),('A',8,8,True,(6,34)),('L',(6,24))")],'Use a smaller lower-left enclosure corner so the LM baseline has full clearance.')
refine(39,[('(25, 42)','(27, 42)')],'Move the rear foot clear of the full rounded mop head.')
refine(40,[('(20, 29)','(20, 31)')],'Lengthen the falling body so the outstretched leg clears the upper arm.')
refine(57,[('(40, 18)','(41, 18)')],'Add the final unit of clearance above the central hand.')
refine(60,[('(14, 32)','(14, 33)'),('(20, 32)','(20, 33)'),('(28, 32)','(28, 33)'),('(34, 32)','(34, 33)'),('(20, 40)','(20, 41)'),('(28, 40)','(28, 41)')],'Lower the squat hips and belt together to open both shoulder-to-belly gaps.')
refine(62,[('(15,19)','(15,22)')],'Level the upper arm below the head instead of letting it encroach on the exact neck gap.')
refine(69,[(", 24)",", 22)"),("(4, 32)","(4, 31)"),("(44, 32)","(44, 31)"),("(x, 32), (x + 10, 32)","(x, 31), (x + 10, 31)")],'Make the cake taller to fit shallow icing with eight units to both outer edges.')
H='from ._symmetry_curves import path, ellipse, line, poly, contacts\n'
redraw(61,H+'''
ellipse(self,'head',17,10,4)
poly(self,'arms',(6,22),(17,22),(27,23))
path(self,'torso',(17,22),('C',(17,25),(14,26),(13,28)))
line(self,'leg',(13,28),(20,34))
poly(self,'board',(6,34),(20,34),(29,34))
path(self,'wave',(32,6),('A',8,14,True,(40,20)),('L',(40,34)),('A',2,8,False,(42,42)))
line(self,'water',(6,42),(42,42))
contacts(self)
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
''','Give the surfer a real bent leg above a level board, with the breaking wave and water below.')
redraw(67,H+'''
ellipse(self,'head',15,12,4)
path(self,'torso',(15,24),('C',(15,27),(14,29),(14,32)))
poly(self,'leg',(14,32),(22,32),(24,40))
poly(self,'arms',(6,27),(15,24),(30,24),(44,21))
path(self,'ski',(4,40),('L',(24,40)),('L',(36,40)),('A',8,8,False,(44,32)))
contacts(self)
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
''','Use one clearly visible profile ski with an upturned tip; fit the bent leg between ski and tow arm with full clearance.')
redraw(70,H+'''
from ._hand_geometry import heart
''','placeholder') if False else None
# Keep the existing heart helper and source metadata while reconstructing the vehicle.
redraw(70,'''
from ._symmetry_curves import path, ellipse, line, poly, contacts
# Two circular lobes define the tethered heart balloon.
path(self,'balloon',(14,10),('A',4,4,False,(6,10)),('L',(14,20)),('L',(22,10)),('A',4,4,False,(14,10)),closed=True)
path(self,'tether',(14,20),('A',10,10,False,(12,28)))
path(self,'body',(12,36),('L',(12,28)),('L',(16,28)),('L',(23,24)),('L',(31,24)),('L',(34,28)),('L',(38,28)),('L',(42,32)),('L',(36,36)))
ellipse(self,'rear-wheel',12,39,3)
ellipse(self,'front-wheel',36,39,3)
line(self,'sill',(15,39),(33,39))
contacts(self)
''','Attach the open car body at the tops of two equal circular wheels and retain the heart balloon on a curved tether.')
# Equivalent two-half-circle encoding lets the existing exact circle/hull checker prove the mandated head gap.
for g in P.values():
 p=Path(g['target_file']);s=p.read_text();t=ast.parse(s);lines=s.splitlines();repls=[]
 for node in ast.walk(t):
  if not isinstance(node,ast.Call) or not isinstance(node.func,ast.Name) or node.func.id!='ellipse' or len(node.args)!=5:continue
  try:n=ast.literal_eval(node.args[1]);cx,cy,r=[ast.literal_eval(z) for z in node.args[2:]]
  except (ValueError,TypeError):continue
  if n!='head':continue
  code=f"path(self,'head',({cx-r},{cy}),('A',{r},{r},True,({cx+r},{cy})),('A',{r},{r},True,({cx-r},{cy})),closed=True)"
  repls.append((node.lineno-1,' '*node.col_offset+code))
 for i,line_ in reversed(repls):lines[i]=line_
 if repls:p.write_text('\n'.join(lines)+'\n')
(W/'finish-changes.json').write_text(json.dumps(CHANGED,indent=2))
