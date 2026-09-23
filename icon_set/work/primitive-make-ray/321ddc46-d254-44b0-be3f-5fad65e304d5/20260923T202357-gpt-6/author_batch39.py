from pathlib import Path
import json,textwrap
AUTHOR='gpt-6'
ROWS=json.loads(Path('/tmp/batch39.json').read_text())
SOURCE_ICON_ID=[r['source_uuid'] for r in ROWS]
SOURCE_PATH=[r['reference_path'] for r in ROWS]
helpers='''
    def circle(self, name, x, y, r):
        self.add_arc(name+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)

    def box(self, name, l, t, r, b, radius=3):
        q=radius
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{name}-{k}'; ids.append(ident)
            a,z=pts[k],pts[(k+1)%8]
            if k%2: self.add_arc(ident,a,z,radius_x=q)
            else: self.add_line(ident,a,z)
        self.add_contour(name,*ids,closed=True)

    def heart(self, name, cx, top, half, bottom):
        # Mirrored lobes and tangent downward shoulders share one outline.
        l=cx-half; r=cx+half; y=top+half//2
        self.add_bezier(name,(cx,top+3),
            ((cx-half//2,top-3),(l,top),(l,y)),
            ((l,y+4),(cx-half//2,bottom-4),(cx,bottom)),
            ((cx+half//2,bottom-4),(r,y+4),(r,y)),
            ((r,top),(cx+half//2,top-3),(cx,top+3)))
'''
D=[]
def add(key,plan,refs,omissions,body): D.append((key,plan,refs,omissions,textwrap.dedent(body).strip()))
add('HRECT_M','Two row boundaries and a detached deletion cross; direction intentionally left weighted.',['table'],'No defining parts omitted.', '''
for y in (10,38): self.add_line('row-'+str(y),(20,y),(44,y))
self.add_line('cross-a',(4,20),(12,28))
self.add_line('cross-b',(4,28),(12,20))
self.relate('connect','cross-a','cross-b')
''')
add('SQUARE','Two repeated rounded blocks at left and a downward arrow at right.',['table','arrow-right'],'No defining parts omitted.', '''
for i,y in enumerate((6,28)): self.box('block-'+str(i),6,y,24,y+14)
self.add_line('shaft',(38,6),(38,42))
self.add_polyline('head',(30,34),(38,42),(42,38))
self.relate('connect','shaft','head')
''')
add('SQUARE','Spreadsheet with a header and a two-by-two cell array; dimension arrows below and right.',['table','arrow-right'],'Reduced cell count to preserve open cells.', '''
self.box('sheet',6,6,30,30,2)
for name,a,b in [('header',(6,14),(30,14)),('row',(6,22),(30,22)),('column',(18,14),(18,30))]:
    self.add_line(name,a,b);self.relate('connect',name,'sheet')
self.relate('connect','header','column');self.relate('connect','row','column')
self.add_line('vertical',(42,6),(42,30))
for name,pts in [('up',((38,10),(42,6),(46,10))),('down',((38,26),(42,30),(46,26))),('left',((10,38),(6,42),(10,46))),('right',((26,38),(30,42),(26,46)))]:
    self.add_polyline(name,*pts)
self.add_line('horizontal',(6,42),(30,42))
for h in ('up','down'): self.relate('connect',h,'vertical')
for h in ('left','right'): self.relate('connect',h,'horizontal')
''')
add('VRECT_L','Portable restroom with arched roof, inset door and triangular door emblem.',['table'],'Omitted tiny door handle; retained triangular emblem.', '''
self.add_arc('roof',(8,12),(40,12),radius_x=16,radius_y=8)
self.add_polyline('walls',(40,12),(40,44),(8,44),(8,12))
self.add_line('roof-seam',(8,12),(40,12))
self.relate('connect','roof','walls');self.relate('connect','roof-seam','walls');self.relate('connect','roof','roof-seam')
self.add_polyline('door',(16,44),(16,21),(32,21),(32,44))
self.relate('connect','door','walls')
self.add_polyline('emblem',(24,28),(20,35),(28,35),closed=True)
''')
add('SQUARE','Landscape frame, sun and two mountain peaks with retouch rays outside upper right corner.',['wand-sparkles','table'],'Reduced retouch rays to three and omitted redundant mountain baseline.', '''
self.add_polyline('frame',(27,12),(6,12),(6,42),(42,42),(42,25))
self.circle('sun',16,22,3)
self.add_polyline('mountains',(13,34),(20,27),(26,34),(33,23),(38,34))
self.add_line('wand',(34,14),(42,22))
for n,a,b in [('ray-top',(34,6),(34,8)),('ray-right',(42,10),(40,12)),('ray-left',(26,6),(28,8))]: self.add_line(n,a,b)
''')
add('CIRCLE','Circular enclosure with diagonal wand and three plus-shaped glints.',['wand-sparkles'],'No defining parts omitted; simplified wand tip.', '''
self.circle('enclosure',24,24,20)
self.add_polyline('wand',(12,36),(26,22),(30,26),(16,40),closed=True)
self.relate('connect','wand','enclosure')
for n,x,y in [('spark-left',15,16),('spark-top',29,12),('spark-right',36,23)]:
    self.add_line(n+'-h',(x-2,y),(x+2,y)); self.add_line(n+'-v',(x,y-2),(x,y+2)); self.relate('connect',n+'-h',n+'-v')
''')
add('VRECT_L','Round award with two angular notched ribbon tails mirrored about x=24.',['award'],'No defining parts omitted.', '''
self.circle('medal',24,20,16)
for name,pts in [('left',((12,31),(8,40),(16,40),(18,44),(24,36))),('right',((36,31),(40,40),(32,40),(30,44),(24,36)))]:
    self.add_polyline(name,*pts); self.relate('connect',name,'medal')
self.relate('connect','left','right')
''')
add('VRECT_L','Round award with curved flaring ribbon tails, retaining the reference variant.',['award'],'No defining parts omitted.', '''
self.circle('medal',24,20,16)
for name,sgn in [('left',-1),('right',1)]:
    def p(x,y): return (24+sgn*x,y)
    self.add_bezier(name,p(10,33),(p(13,35),p(15,38),p(16,40)),(p(12,38),p(10,39),p(9,44)),(p(6,42),p(3,39),p(0,36)))
    self.relate('connect',name,'medal')
self.relate('connect','left','right')
''')
add('SQUARE','Closed rounded square surrounding a right arrow, as in the supplied image.',['table','arrow-right'],'No defining parts omitted.', '''
self.box('frame',6,6,42,42,4)
self.add_line('shaft',(15,24),(33,24))
self.add_polyline('arrow',(25,16),(33,24),(25,32))
self.relate('connect','shaft','arrow')
''')
add('HRECT_M','Long right arrow; source has no terminal bar, so none is introduced.',['arrow-right'],'No defining parts omitted.', '''
self.add_line('shaft',(4,24),(44,24))
self.add_polyline('arrow',(30,10),(44,24),(30,38))
self.relate('connect','shaft','arrow')
''')
add('HRECT_M','Opposed open brackets surrounding a rightward arrow.',['arrow-right','table'],'No defining parts omitted.', '''
self.add_polyline('left-bracket',(10,10),(4,10),(4,38),(10,38))
self.add_polyline('right-bracket',(38,10),(44,10),(44,38),(38,38))
self.add_line('shaft',(14,24),(34,24))
self.add_polyline('arrow',(26,16),(34,24),(26,32))
self.relate('connect','shaft','arrow')
''')
add('SQUARE','Rounded square enclosing a rising arrow.',['arrow-right','table'],'No defining parts omitted.', '''
self.box('frame',6,6,42,42,4)
self.add_line('shaft',(24,33),(24,15))
self.add_polyline('arrow',(16,23),(24,15),(32,23))
self.relate('connect','shaft','arrow')
''')
add('VRECT_L','Padlock whose body contains a receding road and dashed centerline.',['table'],'Reduced the road centerline to one dash.', '''
self.box('body',8,23,40,44,4)
self.add_line('shackle-left',(14,23),(14,14))
self.add_arc('shackle-top',(14,14),(34,14),radius_x=10)
self.add_line('shackle-right',(34,14),(34,23))
self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
self.relate('connect','shackle','body')
self.add_polyline('road',(15,44),(20,31),(28,31),(33,44))
self.relate('connect','road','body')
self.add_line('center-dash',(24,37),(24,39))
''')
add('SQUARE','Hand-authored 4M height text between upper and lower chevrons.',['arrow-right'],'No defining parts omitted.', '''
self.add_polyline('up',(20,10),(24,6),(28,10))
self.add_polyline('down',(20,38),(24,42),(28,38))
self.add_polyline('four',(15,16),(6,29),(19,29))
self.add_line('four-stem',(15,16),(15,33)); self.relate('connect','four','four-stem')
self.add_polyline('m',(26,33),(26,17),(34,28),(42,17),(42,33))
''')
add('SQUARE','Robber facing victim, with forward gun and money mark; heads share size and body gap.',['human_ref/full_body_ref.png'],'Omitted tiny angry eyebrows and hand-outline folds; retained two people, weapon and money sign.', '''
for name,x in [('robber',12),('victim',36)]:
    self.circle(name+'-head',x,12,6)
    self.add_line(name+'-torso',(x,26),(x,42))
    self.mark_human_figure(name,head=name+'-head',torso=name+'-torso',torso_junction='start')
self.add_polyline('arm',(12,28),(6,28),(6,34),(20,34))
self.relate('connect','arm','robber-torso')
self.add_polyline('gun',(20,34),(20,28),(28,28),(28,34))
self.relate('connect','gun','arm')
self.add_bezier('money',(42,28),((34,24),(32,33),(38,34)),((44,35),(44,42),(36,40)))
self.add_line('money-stem',(39,25),(39,42));self.relate('connect','money','money-stem')
''')
add('SQUARE','Articulated robot arm with circular joints, open gripper and wireless arcs.',['bot','rainbow'],'Reduced wireless bands to two plus a dot; no 5G text exists in supplied reference.', '''
self.circle('base-joint',14,30,6)
self.circle('wrist',34,16,4)
self.add_line('arm-top',(17,25),(30,14)); self.add_line('arm-bottom',(20,30),(35,20))
for n in ('arm-top','arm-bottom'):
    self.relate('connect',n,'base-joint');self.relate('connect',n,'wrist')
self.add_polyline('support',(12,36),(15,42),(23,42),(20,33));self.relate('connect','support','base-joint')
self.add_polyline('gripper',(38,16),(42,21),(42,27));self.relate('connect','gripper','wrist')
self.add_bezier('wifi-outer',(6,10),((11,5),(19,5),(24,10)))
self.add_bezier('wifi-inner',(11,16),((14,13),(17,13),(20,16)))
self.add_dot('wifi-point',(16,21))
''')
add('SQUARE','Diagonal dagger with poison droplet and an open-neck vial at lower right.',['wand-sparkles'],'Omitted blade bevel; preserved blade, guard, grip, droplet and vial.', '''
self.add_polyline('blade',(14,28),(36,6),(33,19),(22,34))
self.add_line('guard',(10,24),(26,40))
self.add_polyline('grip',(14,28),(6,36),(6,42),(12,42),(20,34))
self.relate('connect','blade','guard');self.relate('connect','grip','guard');self.relate('connect','blade','grip')
self.add_bezier('drop',(40,17),((36,22),(36,26),(40,26)),((44,26),(44,22),(40,17)))
self.add_bezier('vial',(32,42),((32,39),(28,38),(28,34)),((28,27),(42,27),(42,34)),((42,38),(38,39),(38,42)))
''')
add('SQUARE','Combined male and female sign surrounding a heart.',['heart','arrow-right'],'No defining parts omitted.', '''
self.circle('ring',21,24,15)
self.heart('heart',21,17,7,30)
self.add_line('male-stem',(32,13),(42,6));self.relate('connect','male-stem','ring')
self.add_polyline('male-head',(34,6),(42,6),(42,14));self.relate('connect','male-head','male-stem')
self.add_line('female-stem',(21,39),(21,42));self.relate('connect','female-stem','ring')
self.add_line('female-cross',(15,42),(27,42));self.relate('connect','female-cross','female-stem')
''')
add('SQUARE','Rainbow above a heart, preserving the stacked arrangement.',['rainbow','heart'],'Reduced rainbow from four arcs to three for clearer band spacing.', '''
for i,r in enumerate((18,10,2)):
    self.add_arc('rainbow-'+str(i),(24-r,24),(24+r,24),radius_x=r)
self.heart('heart',24,32,10,42)
''')
add('HRECT_L','Roof chevron above a horizontal double open-ended wrench.',['wrench'],'No defining parts omitted.', '''
self.add_polyline('roof',(4,24),(24,8),(44,24))
self.add_bezier('jaw-left',(6,30),((16,25),(19,40),(6,40)))
self.add_bezier('jaw-right',(42,30),((32,25),(29,40),(42,40)))
self.add_line('handle',(15,35),(33,35))
self.relate('connect','handle','jaw-left');self.relate('connect','handle','jaw-right')
''')
for row,(key,plan,refs,omissions,body) in zip(ROWS,D):
 out=Path(row['out']); row.update(keyshape=key,plan=plan,construction_references=refs,omissions=omissions)
 module=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}
# Construction plan: {plan}
# Reference reduction: {omissions}
# Construction references: {refs!r}

class AuthoredIcon(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}

    def build(self):
'''+textwrap.indent(body,'        ')+'\n'+helpers
 filename=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
 (out/filename).write_text(module);row['module']=filename
Path('/tmp/batch39.json').write_text(json.dumps(ROWS,indent=2))
# Keep the batch authoring source with its source identities in the result folder.
(Path(ROWS[0]['out'])/'author_batch39.py').write_text(Path(__file__).read_text())
print('Authored',len(D),'standalone modules')
