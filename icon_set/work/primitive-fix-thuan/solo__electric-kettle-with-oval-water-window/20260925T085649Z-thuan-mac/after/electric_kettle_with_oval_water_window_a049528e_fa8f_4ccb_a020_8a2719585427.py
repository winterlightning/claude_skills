'Restored a taller kettle, lid knob and a larger elongated water window; retained broad open handle and spout.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: Lucide coffee, original and atomic geometry inspected.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a049528e-fa8f-4ccb-a020-8a2719585427'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__electric-kettle-with-oval-water-window/20260925T085649Z-thuan-mac/reference/tea kettle_a049528e-fa8f-4ccb-a020-8a2719585427.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='electric-kettle-with-oval-water-window'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Keep a useful elongated water-level window. Its closest clear gap to the body is about 2.38px, with a visibly open oval and distinct outline at 48px.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'cb838389445383380c318c491fb6a176f4d0d472385390f7ba599dc37c180ea0'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='drinks'
    aliases=()
    keywords=('electric', 'kettle', 'with', 'oval', 'water', 'window')

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
        self.path('body',(6,16),('L',(13,16)),('C',(15,9),(29,9),(31,16)),('L',(34,37)),('A',(29,42),5,5,True),('L',(14,42)),('A',(9,37),5,5,True),('L',(11,24)),('L',(6,16)),closed=True)
        self.add_line('knob',(22,6),(22,11));self.relate('connect','knob','body')
        self.path('handle',(31,16),('C',(38,14),(42,18),(42,23)),('C',(42,29),(38,33),(34,35)));self.relate('connect','handle','body')
        self.oval('window',22,27,4,7)
