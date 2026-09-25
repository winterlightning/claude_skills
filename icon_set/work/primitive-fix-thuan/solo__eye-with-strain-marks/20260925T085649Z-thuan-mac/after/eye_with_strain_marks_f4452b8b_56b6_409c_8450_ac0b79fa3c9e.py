'Restored readable wavy strain lines and an outlined pupil; kept mirrored almond eye geometry.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide eye, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='f4452b8b-56b6-409c-8450-ac0b79fa3c9e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__eye-with-strain-marks/20260925T085649Z-thuan-mac/reference/eyestrain_f4452b8b-56b6-409c-8450-ac0b79fa3c9e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='eye-with-strain-marks'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Preserve the outlined circular pupil and wavy irritation marks. A compact pupil-to-lid clearance remains visibly open at 48px.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'fc090816cee66845bd5a07ff052f33332ec66f569bde8077617ad388c869fc4b'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='primitives-generate'
    aliases=()
    keywords=('eye', 'with', 'strain', 'marks')

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
        self.path('eye',(6,31),('C',(12,25),(18,21),(24,21)),('C',(30,21),(36,25),(42,31)),('C',(36,37),(30,42),(24,42)),('C',(18,42),(12,37),(6,31)),closed=True)
        self.oval('pupil',24,31,3)
        for i,x in enumerate((17,31)):
         self.path(f'strain-{i}',(x,6),('C',(x-5,10),(x+5,10),(x,13)))
