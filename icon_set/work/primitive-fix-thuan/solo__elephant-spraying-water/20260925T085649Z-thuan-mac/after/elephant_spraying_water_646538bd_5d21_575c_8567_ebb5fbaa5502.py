'Opened the curled raised trunk, smoothed the ear and back, and restored two pointed water droplets.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: No useful exact Lucide match; supplied original defines subject.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='646538bd-5d21-575c-8567-ebb5fbaa5502'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__elephant-spraying-water/20260925T085649Z-thuan-mac/reference/elephant water_646538bd-5d21-575c-8567-ebb5fbaa5502.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='elephant-spraying-water'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Keep the raised trunk taper, whose local internal gap is about 2.35px. The water strokes and ear remain distinct; no tiny closed water holes remain.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '0e4c3e00074ada6c924675cbcc55201595b506db611b3efe3c5ccefa292fc714'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='animals'
    aliases=()
    keywords=('elephant', 'spraying', 'water')

    def path(self,n,p,*steps,closed=False):
        ids=[]
        for i,s in enumerate(steps):
            k=f'{n}-{i}'
            if s[0]=='L': q=s[1]; self.add_line(k,p,q)
            elif s[0]=='A': q=s[1]; self.add_arc(k,p,q,radius_x=s[2],radius_y=s[3],sweep=s[4])
            else: q=s[3]; self.add_bezier(k,p,(s[1],s[2],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def oval(self,n,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(n,(x,y-ry),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),('A',(x,y-ry),rx,ry,True),closed=True)
    def box(self,n,l,t,r,b,q=3):
        self.path(n,(l+q,t),('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True),closed=True)

    def build(self):
        self.path('animal',(18,42),('C',(18,38),(6,38),(6,28)),('C',(6,20),(8,15),(17,11)),('L',(20,16)),('C',(16,20),(13,23),(15,28)),('C',(17,30),(18,23),(22,25)),('C',(28,21),(36,26),(36,32)),('C',(36,38),(29,40),(25,38)))
        self.path('back',(36,32),('C',(42,32),(42,36),(42,42)));self.relate('connect','animal','back')
        self.add_line('water-a',(25,6),(30,6))
        self.add_line('water-b',(35,13),(40,16))
