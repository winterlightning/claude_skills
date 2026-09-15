"""Diagonal double open-end wrench. Lucide wrench informs open rounded jaws; the outlined handle is reduced to one straight joining stroke, retaining both opposing mouths.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='9f43f349-dca9-5cdc-ac05-5e18a00b8508'
SOURCE_PATH='pictographic-primitives/symbol/wrench right_9f43f349-dca9-5cdc-ac05-5e18a00b8508.svg'
AUTHOR='gpt-6'

class WrenchDoubleOpenEnd(Solo48):
    icon_id='wrench-double-open-end'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('wrench', 'spanner', 'tool', 'repair', 'fix', 'settings', 'mechanic', 'maintenance')

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

        self.add_line('upper-top',(42,6),(37,6));self.add_arc('upper-outer-a',(37,6),(33,14),radius_x=5,sweep=False)
        self.add_arc('upper-outer-b',(33,14),(37,16),radius_x=5,sweep=False);self.add_line('upper-bottom',(37,16),(42,16))
        self.add_contour('upper-jaw','upper-top','upper-outer-a','upper-outer-b','upper-bottom')
        self.add_line('lower-bottom',(6,42),(11,42));self.add_arc('lower-outer-a',(11,42),(15,34),radius_x=5,sweep=False)
        self.add_arc('lower-outer-b',(15,34),(11,32),radius_x=5,sweep=False);self.add_line('lower-top',(11,32),(6,32))
        self.add_contour('lower-jaw','lower-bottom','lower-outer-a','lower-outer-b','lower-top')
        self.add_line('handle',(15,34),(33,14));self.relate('connect','handle','upper-jaw');self.relate('connect','handle','lower-jaw')
