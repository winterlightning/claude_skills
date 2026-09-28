"""Seated figure with forward arm, bent leg and open wheelchair wheel. Lucide accessibility informs the articulated figure; source wheel remains open.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='da29f68e-5632-431d-92e7-4ee9f999acb8'
SOURCE_PATH='pictographic-primitives/symbol/wheelchair_da29f68e-5632-431d-92e7-4ee9f999acb8.svg'
AUTHOR='gpt-6'

class WheelchairAccessible(Solo48):
    icon_id='wheelchair-accessible'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    categories = ("symbol", "state")
    aliases=()
    keywords=('wheelchair', 'accessibility', 'disabled', 'handicap', 'access', 'mobility', 'parking', 'inclusive')

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

        self.oval('head',24,10,4)
        self.path('body',[(24,14),(24,20),(24,28),(34,28),(40,40),(42,40)])
        self.relate('connect','head','body')
        self.add_line('arm',(24,20),(34,20));self.relate('connect','arm','body')
        self.add_arc('wheel',(10,24),(24,38),radius_x=10,large_arc=True,sweep=False)
