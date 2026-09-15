"""Swing on a splayed frame with two ropes and curved seat. No useful Lucide swing match; mirrored support geometry and a semicircular seat keep the structure coherent.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='915b55b6-88bb-4695-9e96-85f5616755a8'
SOURCE_PATH='pictographic-primitives/symbol/swing_915b55b6-88bb-4695-9e96-85f5616755a8.svg'
AUTHOR='gpt-6'

class SwingSet(Solo48):
    icon_id='swing-set'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('swing', 'playground', 'park', 'kids', 'play', 'recreation', 'garden', 'children')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def raw(self,n,points):
        for j,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(n+'-'+str(j),a,b)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        self.path('beam',[(10,6),(18,6),(30,6),(38,6)])
        self.add_line('left-leg',(10,6),(6,42));self.add_line('right-leg',(38,6),(42,42))
        for name in ('left-leg','right-leg'):self.relate('connect',name,'beam')
        for name,x in [('left',18),('right',30)]:
            self.add_line(name+'-rope',(x,6),(x,32))
            self.relate('connect',name+'-rope','beam')
        self.add_arc('seat',(18,32),(30,32),radius_x=6,sweep=False)
        self.relate('connect','seat','left-rope');self.relate('connect','seat','right-rope')
