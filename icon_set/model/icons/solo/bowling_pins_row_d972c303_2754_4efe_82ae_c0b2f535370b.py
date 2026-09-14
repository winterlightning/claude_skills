"""Three bowling pins in an equal row. No useful local Lucide bowling match; shared heads and smoothly bulging bellies preserve all three pins. Source overlaps separated for clearance.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='d972c303-2754-4efe-82ae-c0b2f535370b'
SOURCE_PATH='pictographic-primitives/symbol/three bowlings_d972c303-2754-4efe-82ae-c0b2f535370b.svg'
AUTHOR='gpt-6'

class BowlingPinsRow(Solo48):
    icon_id='bowling-pins-row'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('bowling', 'pins', 'skittles', 'sport', 'game', 'alley', 'strike', 'leisure')

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
        front=False

        for j,cx in enumerate((7,24,41)):
            n='pin-'+str(j);lower=front and j==1
            y=12 if lower else 8
            belly=4 if lower else 3
            base=36 if front and not lower else 40
            rx=belly-2
            self.add_arc(n+'-head',(cx-3,y+3),(cx+3,y+3),radius_x=3)
            self.add_line(n+'-neck-r',(cx+3,y+3),(cx+2,18))
            self.add_arc(n+'-upper-r',(cx+2,18),(cx+belly,29),radius_x=rx,radius_y=11)
            self.add_arc(n+'-lower-r',(cx+belly,29),(cx+2,base),radius_x=rx,radius_y=base-29)
            self.add_line(n+'-base',(cx+2,base),(cx-2,base))
            self.add_arc(n+'-lower-l',(cx-2,base),(cx-belly,29),radius_x=rx,radius_y=base-29)
            self.add_arc(n+'-upper-l',(cx-belly,29),(cx-2,18),radius_x=rx,radius_y=11)
            self.add_line(n+'-neck-l',(cx-2,18),(cx-3,y+3))
            self.add_contour(n,*[n+'-'+part for part in ('head','neck-r','upper-r','lower-r','base','lower-l','upper-l','neck-l')],closed=True)
