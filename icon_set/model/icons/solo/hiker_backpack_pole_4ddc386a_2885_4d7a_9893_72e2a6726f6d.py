"""Right-facing hiker with backpack, striding legs and held pole. Lucide person-standing and backpack inform a sparse articulated figure; double body outlines simplified to coherent strokes.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='4ddc386a-2885-4d7a-9893-72e2a6726f6d'
SOURCE_PATH='pictographic-primitives/symbol/trekking_4ddc386a-2885-4d7a-9893-72e2a6726f6d.svg'
AUTHOR='gpt-6'

class HikerBackpackPole(Solo48):
    icon_id='hiker-backpack-pole'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('hiking', 'trekking', 'hiker', 'backpack', 'walking', 'outdoors', 'mountain', 'adventure')

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

        self.oval('head',27,10,4)
        self.path('body',[(24,23),(20,32),(6,42)])
        self.path('front-leg',[(20,32),(30,34),(34,42)]);self.relate('connect','body','front-leg')
        self.path('pack',[(14,18),(24,23),(20,32),(10,27)],True);self.relate('connect','pack','body')
        self.path('arm',[(24,23),(32,28),(42,28)]);self.relate('connect','arm','body');self.relate('connect','arm','pack')
        self.path('pole',[(42,16),(42,28),(42,42)]);self.relate('connect','pole','arm')
