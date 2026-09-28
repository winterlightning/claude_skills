from pathlib import Path
import json, textwrap

ROOT = Path(__file__).parent
ROWS = json.loads((ROOT/'batch.json').read_text())
AUTHOR = 'gpt-6'
SOURCE_ICON_ID = [r['source_uuid'] for r in ROWS]
SOURCE_PATH = [r['reference_path'] for r in ROWS]

HELPERS = '''
def line(n,a,b): self.add_line(n,a,b)
def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
def contour(n,*p,closed=False): self.add_contour(n,*p,closed=closed)
def join(a,b): self.relate('connect',a,b)
def circle(n,x,y,r):
    arc(n+'a',(x-r,y),(x+r,y),r)
    arc(n+'b',(x+r,y),(x-r,y),r)
    contour(n,n+'a',n+'b',closed=True)
def box(n,l,t,r,b,k=4):
    line(n+'t',(l+k,t),(r-k,t));arc(n+'tr',(r-k,t),(r,t+k),k)
    line(n+'r',(r,t+k),(r,b-k));arc(n+'br',(r,b-k),(r-k,b),k)
    line(n+'b',(r-k,b),(l+k,b));arc(n+'bl',(l+k,b),(l,b-k),k)
    line(n+'l',(l,b-k),(l,t+k));arc(n+'tl',(l,t+k),(l+k,t),k)
    contour(n,*[n+x for x in ['t','tr','r','br','b','bl','l','tl']],closed=True)
'''

DESIGNS = {
'female-user-profile': ('VRECT_L', 'Long hair framing a circular face above broad shoulders; detached face-to-shoulder gap 4 ink units.', '''
circle('head',24,14,10)
for side in [-1,1]:
    x=24+side*10
    line('hair'+str(side),(x,14),(24+side*16,28))
    join('head','hair'+str(side))
arc('shoulders',(8,44),(40,44),16,12)
'''),
'four-piece-jigsaw-puzzle': ('SQUARE','Four pieces with two broad interlocking seams; shared center and square envelope.', '''
poly('frame',(6,6),(24,6),(42,6),(42,24),(42,42),(24,42),(6,42),(6,24),closed=True)
line('v1',(24,6),(24,10));arc('tab1',(24,10),(24,20),5,s=False);line('v2',(24,20),(24,24))
line('v3',(24,24),(24,28));arc('tab2',(24,28),(24,38),5);line('v4',(24,38),(24,42))
contour('vertical','v1','tab1','v2','v3','tab2','v4')
line('h1',(6,24),(24,24));line('h2',(24,24),(42,24));contour('horizontal','h1','h2')
join('frame','vertical');join('frame','horizontal');join('vertical','horizontal')
'''),
'gaming-console-and-controller': ('SQUARE','Upright console behind a gamepad with a directional cross and action button.', '''
poly('console',(6,18),(6,6),(24,6),(24,18))
arc('pad-tl',(6,26),(14,18),8);line('pad-top',(14,18),(34,18));arc('pad-tr',(34,18),(42,26),8)
poly('grips',(42,26),(42,42),(32,36),(16,36),(6,42),(6,26))
join('pad-tl','pad-top');join('pad-top','pad-tr');join('pad-tr','grips');join('grips','pad-tl');join('console','pad-top')
line('dpad-v',(17,26),(17,28));line('dpad-h',(15,27),(19,27));join('dpad-v','dpad-h')
self.add_dot('button',(32,27))
'''),
'grim-reaper-with-scythe': ('VRECT_L','Pointed hood and robe with a face opening beside an unmistakable long curved scythe.', '''
poly('robe',(8,44),(8,24),(20,14),(32,24),(32,44),closed=True)
circle('face',20,30,4)
line('shaft',(40,4),(40,44))
arc('blade-edge',(8,4),(40,14),32,10,s=True)
join('shaft','blade-edge')
'''),
'grinning-face-with-heart-eyes': ('HRECT_L','Two large outlined heart eyes and a grin; omit the enclosing face circle to preserve legal readable heart openings.', '''
for i,x in enumerate([12,36]):
    n='heart'+str(i)
    arc(n+'a',(x,12),(x-8,12),4,s=False)
    poly(n+'b',(x-8,12),(x,23),(x+8,12))
    arc(n+'c',(x+8,12),(x,12),4,s=False)
    join(n+'a',n+'b');join(n+'b',n+'c');join(n+'a',n+'c')
line('mouth-top',(12,32),(36,32));arc('mouth-bottom',(36,32),(12,32),12,8)
contour('mouth','mouth-top','mouth-bottom',closed=True)
'''),
'gudi-padwa-festival-flag': ('VRECT_L','Inverted ceremonial pot on a tall pole with a draped festival cloth.', '''
poly('pot',(8,16),(10,4),(24,4),(26,16),closed=True)
line('pole',(17,16),(17,44));join('pot','pole')
poly('cloth',(17,24),(40,24),(40,40),(29,36),(17,40))
join('pole','cloth')
'''),
'horned-demon-face': ('SQUARE','A round devil face with two pointed horns, slanted eyes and a smirk.', '''
poly('crown',(6,24),(6,6),(16,16),(32,16),(42,6),(42,24))
arc('jaw',(42,24),(6,24),18)
join('crown','jaw')
line('eye-left',(15,24),(18,25));line('eye-right',(33,24),(30,25))
line('smirk',(20,33),(28,33))
'''),
'howling-wolf-with-sound': ('SQUARE','A long raised muzzle, pointed ear and curved neck, with a separate howl wave.', '''
poly('profile',(6,42),(10,28),(6,23),(17,22),(27,8),(31,20),(27,30))
arc('neck',(27,30),(32,42),18,s=False)
join('profile','neck')
arc('howl',(36,6),(42,24),6,18)
'''),
'hutt-creature': ('HRECT_L','Broad slug-like alien with a heavy face, arms and a curling tail.', '''
arc('head',(14,24),(44,24),15,16)
line('side',(44,24),(44,31));arc('lower',(44,31),(35,40),9)
line('base',(35,40),(13,40));arc('tail',(13,40),(4,31),9)
poly('tail-tip',(4,31),(4,24),(10,30),(14,30),(14,24))
for a,b in [('head','side'),('side','lower'),('lower','base'),('base','tail'),('tail','tail-tip'),('tail-tip','head')]:join(a,b)
self.add_dot('eye-l',(24,20));self.add_dot('eye-r',(34,20))
line('mouth',(24,30),(35,30))
'''),
'kermit-face': ('SQUARE','Frog face with two bulging eyes, wide mouth and a pointed collar.', '''
circle('eye-l',14,12,6);circle('eye-r',34,12,6)
poly('left',(8,12),(6,28),(14,34));poly('right',(40,12),(42,28),(34,34))
join('eye-l','left');join('eye-r','right')
poly('collar',(14,34),(10,42),(21,38),(24,42),(27,38),(38,42),(34,34))
join('left','collar');join('right','collar')
arc('mouth',(17,26),(31,26),10,4,s=False)
'''),
'lidded-pot-with-rising-steam': ('SQUARE','Rounded cooking pot with a domed lid, handle and two steam wisps.', '''
poly('pot',(10,24),(10,36),(16,42),(32,42),(38,36),(38,24))
line('rim',(6,24),(42,24));join('pot','rim')
line('knob',(24,24),(24,18));join('knob','rim')
for i,x in enumerate([14,34]):line('steam'+str(i),(x,6),(x,14))
'''),
'linked-circular-handcuffs': ('HRECT_L','Two wrist cuffs with a short joining chain rather than three rings in a triangle.', '''
circle('left',13,17,9);circle('right',35,31,9)
line('chain',(22,17),(26,31));join('left','chain');join('right','chain')
'''),
'log-with-sprouting-branch': ('HRECT_L','Diagonal cylindrical tree log with a broad end-grain ring. Omit the small branch to emphasize the original tree-log concept.', '''
arc('cut-a',(12,15),(22,39),13);arc('cut-b',(22,39),(12,15),13)
contour('cut','cut-a','cut-b',closed=True)
line('top',(12,15),(31,8));arc('end',(31,8),(44,31),13,23);line('bottom',(44,31),(22,39))
join('cut','top');join('cut','bottom');join('top','end');join('end','bottom')
circle('grain',17,27,4)
'''),
}

for row in ROWS:
    name=row['icon_id']
    if name.startswith('square-'):
        body="box('frame',6,6,42,42)\n"
        if name=='square-caret-down': body+="poly('caret',(16,20),(24,28),(32,20))\n"
        elif name in ['square-caret-left','square-chevron-left']:body+="poly('chevron',(28,15),(19,24),(28,33))\n"
        elif name=='square-chevron-right':body+="poly('chevron',(20,15),(29,24),(20,33))\n"
        elif name=='square-down-left':body+="poly('head',(16,19),(16,32),(29,32))\nline('shaft',(16,32),(32,16))\njoin('head','shaft')\n"
        elif name=='square-down-right':body+="poly('head',(19,32),(32,32),(32,19))\nline('shaft',(16,16),(32,32))\njoin('head','shaft')\n"
        else:body+="poly('letter',(18,33),(18,15),(31,15))\nline('middle',(18,24),(28,24))\njoin('letter','middle')\n"
        DESIGNS[name]=('SQUARE','Square frame enclosing the conventional symbol named by the concept; misleading reference content replaced.',body)
    key,plan,body=DESIGNS[name]
    path=Path(row['run'])/(name.replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')
    source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = {name!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('meaning-revision',)
    def build(self):
        # {plan}
'''+textwrap.indent(textwrap.dedent(HELPERS+body).strip(),'        ')+'\n'
    path.write_text(source)
    (Path(row['run'])/'design.json').write_text(json.dumps(dict(plan=plan,keyshape=key,feedback=row['feedback']),indent=2)+'\n')
print('Authored',len(ROWS),'standalone modules')
