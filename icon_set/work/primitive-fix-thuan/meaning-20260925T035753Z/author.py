from pathlib import Path
import json,textwrap
ROOT=Path(__file__).parent
ROWS=json.loads((ROOT/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[r['source_uuid'] for r in ROWS]
SOURCE_PATH=[r['reference_path'] for r in ROWS]
HELPERS='''
def line(n,a,b): self.add_line(n,a,b)
def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
def contour(n,*p,closed=False): self.add_contour(n,*p,closed=closed)
def join(a,b): self.relate('connect',a,b)
def circle(n,x,y,r):
    arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
    contour(n,n+'a',n+'b',closed=True)
def box(n,l,t,r,b,k=4):
    line(n+'t',(l+k,t),(r-k,t));arc(n+'tr',(r-k,t),(r,t+k),k)
    line(n+'r',(r,t+k),(r,b-k));arc(n+'br',(r,b-k),(r-k,b),k)
    line(n+'b',(r-k,b),(l+k,b));arc(n+'bl',(l+k,b),(l,b-k),k)
    line(n+'l',(l,b-k),(l,t+k));arc(n+'tl',(l,t+k),(l+k,t),k)
    contour(n,*[n+x for x in ['t','tr','r','br','b','bl','l','tl']],closed=True)
'''
DESIGNS={
'browser-dollar-sign-right':('HRECT_M','Square browser window at left and a curved dollar on the right; its two S bowls share radius 5. Move the dollar beside the browser to preserve its conventional shape.', '''
box('browser',4,13,26,35)
line('toolbar',(4,21),(26,21));join('browser','toolbar')
line('s-top',(44,14),(39,14))
arc('s-upper',(39,14),(39,24),5,s=False)
arc('s-lower',(39,24),(39,34),5)
line('s-bottom',(39,34),(34,34))
contour('dollar-s','s-top','s-upper','s-lower','s-bottom')
line('stem-top',(39,10),(39,14));line('stem-bottom',(39,34),(39,38))
join('dollar-s','stem-top');join('dollar-s','stem-bottom')
'''),
'cartoon-cat-face':('HRECT_L','Cat face with mirrored pointed ears, a round jaw and whiskers on each cheek. Shared axis 24 controls ears, eyes, nose and whiskers.', '''
poly('ears',(10,26),(10,8),(20,16),(28,16),(38,8),(38,26))
arc('jaw',(38,26),(10,26),14);join('ears','jaw')
for i,side in enumerate([-1,1]):
    cheek=(24+side*14,26)
    for j,y in enumerate([22,30]):
        n=f'whisker-{i}-{j}'
        line(n,cheek,(24+side*20,y));join('ears',n);join('jaw',n)
    join(f'whisker-{i}-0',f'whisker-{i}-1')
    self.add_dot('eye-'+str(i),(24+side*6,24))
line('nose',(23,31),(25,31))
'''),
'capped-carpenter-beside-a-hand-saw':('HRECT_L','Capped carpenter head beside an upright hand saw with three coarse teeth and a large rectangular handle opening; preserve the reference layout.', '''
poly('saw',(4,40),(4,8),(16,8),(12,14),(16,18),(12,22),(16,28),(16,40),closed=True)
line('handle-top',(4,28),(16,28));join('saw','handle-top')
arc('cap',(28,16),(44,16),8)
line('brim',(24,16),(44,16));join('cap','brim')
line('face-r',(44,16),(44,24));arc('jaw',(44,24),(28,24),8);line('face-l',(28,24),(28,16))
contour('face','face-r','jaw','face-l')
join('cap','face');join('brim','face')
''')
}
for row in ROWS:
    key,plan,body=DESIGNS[row['icon_id']]
    out=Path(row['run']);name=row['icon_id']
    src=f'''from icon_set.model.keyshapes import Keyshape
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
    (out/(name.replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py')).write_text(src)
    (out/'design.json').write_text(json.dumps(dict(plan=plan,keyshape=key,feedback=row['feedback']),indent=2)+'\n')
print('Authored',len(ROWS),'standalone modules')
