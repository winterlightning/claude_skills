'Restored rounded speech bubble and a legible dollar with separate top and bottom currency stems.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide dollar-sign, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a0e713ab-5594-48b4-9fb9-5bd0a13657f4'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dollar-sign-chat-bubble-solo/20260925T085649Z-thuan-mac/reference/messages bubble round dollar sign_a0e713ab-5594-48b4-9fb9-5bd0a13657f4.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='dollar-sign-chat-bubble-solo'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Keep recognizable dollar stems and a rounded speech bubble. The S uses 3px internal gaps and its short lower stem retains about 3px clear separation from the bubble; both themes are legible at 48px.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'fcff269632092870cfecb4e598aedfb8d11b65b2d8d4beaa3775e37664aa958b'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='other'
    aliases=()
    keywords=('dollar', 'sign', 'chat', 'bubble', 'solo')

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
        self.path('bubble',(11,32),('C',(7,29),(6,26),(6,22)),('C',(6,12),(13,6),(24,6)),('C',(35,6),(42,12),(42,22)),('C',(42,33),(35,39),(24,39)),('L',(19,39)),('L',(7,42)),('L',(11,32)),closed=True)
        self.path('s',(29,15),('L',(22,15)),('A',(22,22),4,4,False),('L',(26,22)),('A',(26,29),4,4,True),('L',(19,29)))
        self.add_line('currency-top',(24,12),(24,15));self.add_line('currency-bottom',(24,29),(24,32))
        self.relate('connect','s','currency-top');self.relate('connect','s','currency-bottom')
