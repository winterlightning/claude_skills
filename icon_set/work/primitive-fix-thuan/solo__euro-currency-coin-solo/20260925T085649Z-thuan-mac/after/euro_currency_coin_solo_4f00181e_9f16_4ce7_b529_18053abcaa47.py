'Restored the euro’s characteristic two horizontal bars with an open curved bowl inside the coin.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide euro, original and atomic geometry inspected.\nKeyshape CIRCLE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4f00181e-9f16-4ce7-b529-18053abcaa47'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__euro-currency-coin-solo/20260925T085649Z-thuan-mac/reference/circle euro_4f00181e-9f16-4ce7-b529-18053abcaa47.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='euro-currency-coin-solo'
    keyshape=Keyshape.CIRCLE
    exception={'reason': 'Keep two euro crossbars attached to the curved bowl. Their mutual gap meets 4px; the remaining advisories concern the intentional curved bar junctions.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'c5f13015f670484d385d6aa2c0ebaee490bcc10cd64ac272eb48ccc29d283703'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='other'
    aliases=()
    keywords=('euro', 'currency', 'coin', 'solo')

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
        self.oval('coin',24,24,20)
        self.path('euro',(31,15),('C',(21,11),(17,17),(17,24)),('C',(17,31),(21,37),(31,33)))
        for i,y in enumerate((20,28)):
         self.add_line(f'bar-{i}',(14,y),(27,y));self.relate('connect','euro',f'bar-{i}')
