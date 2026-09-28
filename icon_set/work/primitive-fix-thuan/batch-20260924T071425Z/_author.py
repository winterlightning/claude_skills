from pathlib import Path
import json,textwrap
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ROWS=json.loads((ROOT/'inputs.json').read_text())
SOURCE_ICON_ID={r['icon_id']:r['source_uuid'] for r in ROWS}
SOURCE_PATH={r['icon_id']:r['reference_path'] for r in ROWS}
HELPERS='''
    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            n=f'{name}-{i}'
            if kind=='L': self.add_line(n,start,end)
            elif kind=='A': self.add_arc(n,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(n,start,(args[0],args[1],end))
            members.append(n);start=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def mirror(self,n,start,commands,closed=True):
        axis=24
        m=lambda p:(2*axis-p[0],p[1])
        nodes=[start]+[c[1] for c in commands]
        rev=[]
        for i,c in reversed(list(enumerate(commands))):
            k,end,*args=c
            if k=='C':rev.append((k,m(nodes[i]),m(args[1]),m(args[0])))
            elif k=='A':rev.append((k,m(nodes[i]),*args))
            else:rev.append((k,m(nodes[i])))
        self.path(n,start,commands+rev,closed)
'''
D={}
def design(i,key,plan,body,ref='No useful exact Lucide match.',omit='None.'):
 D[i]=(key,plan,body,ref,omit)
design(14,'SQUARE','Three repeated smoke strokes above a curved bowl on mirrored splayed legs; lengthen wisps and make bowl curvature continuous.', '''
p('bowl',(6,23),[('L',(42,23)),('C',(32,32),(42,27),(37,31)),('C',(24,34),(29,34),(27,34)),('C',(16,32),(21,34),(19,34)),('C',(6,23),(11,31),(6,27))],True)
line('left-leg',(16,32),(11,42));line('right-leg',(32,32),(37,42))
join('left-leg','bowl');join('right-leg','bowl')
for i,x in enumerate((14,24,34)):
 p(f'smoke-{i}',(x,6),[('C',(x,15),(x-4,9),(x+4,12))])
''','Lucide soup: coherent bowl and repeated curved steam.','Lower leg crossbar omitted to avoid a narrow band under the bowl.')
design(15,'HRECT_M','Mirror the tapered crown about x=24, using tangent cubic shoulders; a broad curved brim reaches (4,38)-(44,38).', '''
p('crown',(14,28),[('C',(24,10),(18,15),(18,10)),('C',(34,28),(30,10),(30,15))])
p('brim',(4,28),[('L',(14,28)),('L',(34,28)),('L',(44,28)),('A',(34,38),10,10,True),('L',(14,38)),('A',(4,28),10,10,True)],True)
join('crown','brim')
''','Lucide soup: tangent rounded lower enclosure, adapted to a wide brim.')
design(18,'VRECT_L','Open shackle with a true semicircle and smooth rounded lower lock body; shared node at shackle attachment.', '''
p('body',(8,24),[('L',(14,24)),('L',(40,24)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(8,24))],True)
p('shackle',(14,24),[('L',(14,14)),('A',(34,14),10,10,True)])
join('shackle','body')
''','Lucide lock-open: semicircular open shackle and rounded rectangular body.')
design(0,'VRECT_L','Sloped upper panel, round control and softened body corners, symmetric about x=24; seam attachment nodes explicitly shared.', '''
p('body',(8,21),[('L',(12,7)),('C',(16,4),(13,4),(14,4)),('L',(32,4)),('C',(36,7),(34,4),(35,4)),('L',(40,21)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(8,21))],True)
line('seam',(8,21),(40,21));join('seam','body')
line('vent',(21,13),(27,13))
oval('control',24,32,3,3)
''','Lucide air-vent: simple slat and coherent rounded housing.','Flattened the top vent to a single open slat so its small hole cannot fill in.')
design(2,'SQUARE','Bengal cat face with tall rounded ears, soft cheeks and tapered chin; mirror one side to avoid uneven jaws.', '''
self.mirror('head',(24,16),[('C',(31,17),(27,16),(29,16)),('C',(39,6),(35,12),(37,6)),('C',(42,10),(41,6),(42,7)),('C',(39,25),(42,15),(40,21)),('C',(34,35),(42,30),(39,33)),('C',(24,42),(31,39),(29,42))])
p('mouth',(21,30),[('L',(24,27)),('L',(27,30))])
line('nose',(24,25),(24,27));join('nose','mouth')
''','Lucide cat: coherent mirrored ear/cheek outline.','No added eyes; reference has only the small nose/mouth mark.')
design(5,'SQUARE','Seven broad gear teeth on a rotationally balanced polygon; use one authored vertex series instead of uneven mirrored six-tooth zigzags.', '''
# Seven teeth: common angular spacing, rounded integer vertices.
import math
vertices=[]
for tooth in range(7):
 for angle_offset,radius in ((-8,19),(8,19),(15,14),(36,14)):
  angle=math.radians(-90+tooth*360/7+angle_offset)
  vertices.append((24+round(18*radius/19*math.cos(angle)),24+round(radius*math.sin(angle))))
vertices[0]=(vertices[0][0],6);vertices[1]=(vertices[1][0],6)
poly('gear',*vertices,closed=True)
''','Lucide settings: repeated tooth/valley rhythm.','Omit the nearly invisible source center speck; preserve the solid gear silhouette.')
design(11,'SQUARE','Six rounded lobes with smooth alternating convex and concave shoulders; mirror both axes using one upper-right definition.', '''
q=[('C',(32,14),(28,6),(28,14)),('C',(42,16),(36,14),(42,10)),('C',(37,24),(42,20),(37,21)),('C',(42,32),(37,27),(42,28)),('C',(32,34),(42,38),(36,34)),('C',(24,42),(28,34),(28,42))]
self.mirror('gear',(24,6),q)
line('center-mark',(24,23),(24,25))
''','Lucide settings: tangent alternating convex and concave lobes.')
design(12,*D[11])
design(13,'SQUARE','Smooth mirrored torso sides, a curved upper garment edge and lower waistband around the navel; preserve cropped anatomy without a detached head.', '''
for side in (-1,1):
 m=lambda x,y:(24+side*x,y)
 p('upper-'+str(side),m(17,6),[('C',m(12,18),m(18,14),m(17,18))])
 p('waist-'+str(side),m(12,18),[('C',m(13,35),m(8,25),m(9,30)),('C',m(18,42),m(16,38),m(18,40))])
 join('upper-'+str(side),'waist-'+str(side))
p('top-edge',(12,18),[('C',(24,17),(16,19),(20,17)),('C',(36,18),(28,17),(32,19))])
p('waistband',(11,35),[('C',(24,37),(15,34),(19,37)),('C',(37,35),(29,37),(33,34))])
for side in (-1,1):
 join('top-edge','upper-'+str(side));join('top-edge','waist-'+str(side));join('waistband','waist-'+str(side))
dot('navel',(24,28))
''','Human full_body_ref.png and user.svg: coherent anatomy curves; cropped torso has no detached head.','Omit the small upper cleavage mark to give the garment breathing room.')
design(19,'HRECT_M','Low classic convertible with equal wheels and a single rounded hood; wheel joins occur at explicit cardinal nodes instead of cutting across tires.', '''
for n,x in [('rear',12),('front',36)]:oval(n,x,32,6,6)
p('body',(6,32),[('L',(4,32)),('L',(4,25)),('A',(9,20),5,5,True),('L',(25,20)),('L',(33,20)),('C',(44,32),(39,20),(44,25)),('L',(42,32))])
line('chassis',(18,32),(30,32))
for n in ('rear','front'):join('body',n);join('chassis',n)
p('windscreen',(25,20),[('L',(19,10)),('L',(16,10))]);join('windscreen','body')
''','Lucide car: equal circular wheels, split body edges, coherent curved hood.')
# Remaining compositions authored below.

def write(indices=None):
 for i,(key,plan,body,ref,omit) in D.items():
  if indices is not None and i not in indices:continue
  r=ROWS[i]
  code=f'"""{plan}\nConstruction: {ref}\nOmissions: {omit}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {r["source_uuid"]!r}\nSOURCE_PATH = {r["reference_path"]!r}\nAUTHOR = {AUTHOR!r}\n\nclass Drawing(Solo48):\n    icon_id = {r["icon_id"]!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = {tuple(r["concept"].split())!r}\n\n    def build(self):\n        # Symbol plan: {plan}\n        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot\n        join=lambda a,b:self.relate("connect",a,b)\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'+HELPERS
  Path(r['module']).write_text(code)
  (Path(r['run'])/'design.json').write_text(json.dumps({'keyshape':key,'plan':plan,'construction_reference':ref,'omissions':omit},indent=2))
if __name__=='__main__':write()
