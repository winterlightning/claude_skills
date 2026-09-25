'Replaced narrow detached oval ears with broad natural ears, integrated a curled trunk into the face and restored two eyes.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: No useful exact Lucide match; supplied original defines subject.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='448ae7e7-230e-5858-9857-5a4d7a93f188'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__elephant-head/20260925T085649Z-thuan-mac/reference/elephant head_448ae7e7-230e-5858-9857-5a4d7a93f188.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='elephant-head'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Preserve the eyes and integrated curled trunk within broad ears. Compact eye-to-face and trunk-return clearances remain visibly separated at 48px and preserve recognition.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '2398442e2c4cbd5c9d7f527204f508328107c44c275b86393c43f0a9a28122a6'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='animals'
    aliases=()
    keywords=('elephant', 'head')

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
        self.path('face',(14,12),('C',(14,4),(34,4),(34,12)),('C',(36,19),(30,25),(28,28)),('L',(28,34)),('C',(28,39),(36,38),(36,33)),('C',(36,40),(32,42),(27,42)),('C',(21,42),(20,38),(20,33)),('L',(20,27)),('C',(14,23),(12,17),(14,12)),closed=True)
        for side in (-1,1):
         x=lambda a:24+side*a
         self.path(f'ear-{side}',(x(10),12),('C',(x(15),4),(x(18),10),(x(18),17)),('C',(x(18),24),(x(15),33),(x(10),26)),('L',(x(9),23)))
         self.relate('connect','face',f'ear-{side}')
         self.add_dot(f'eye-{side}',(x(4),18))
