'Widened raised trunk, smoothed forehead, enlarged ear sweep and restored a tapered tusk.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: No useful exact Lucide match; supplied original defines subject.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='bb426c49-781e-424c-919c-ba4daf28dc05'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__elephant-head-profile/20260925T085649Z-thuan-mac/reference/elephant head size_bb426c49-781e-424c-919c-ba4daf28dc05.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='elephant-head-profile'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Preserve raised trunk, eye, ear and tusk together. The widened trunk and local eye/ear spaces are readable at 48px despite strict internal-spacing findings.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '593c19185c2a37530dad41e4258f0d265f04fa0825b54c6c246343d44ae90321'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='animals'
    aliases=()
    keywords=('elephant', 'head', 'profile')

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
        self.path('head',(6,12),('C',(8,7),(12,6),(16,6)),('C',(24,6),(28,12),(29,20)),('C',(30,26),(33,28),(34,23)),('C',(35,18),(34,12),(34,7)),('L',(42,8)),('L',(42,21)),('C',(42,28),(40,33),(34,35)),('L',(26,34)))
        self.path('ear',(13,14),('C',(15,23),(9,30),(6,30)))
        self.add_dot('eye',(22,20))
        self.path('jaw',(26,34),('C',(20,35),(11,32),(10,42)));self.relate('connect','head','jaw')
        self.path('tusk',(26,34),('C',(29,39),(33,40),(37,40)));self.relate('connect','head','tusk');self.relate('connect','jaw','tusk')
