"""Thermometer with a mercury line and bulb dot. Lucide thermometer informs continuous tube and bulb; widened bore preserves internal clearance.

SOLO48 VRECT_L; live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='b9550739-2fcc-4d3f-b1da-62a62d9213f5'
SOURCE_PATH='pictographic-primitives/symbol/thermometer_b9550739-2fcc-4d3f-b1da-62a62d9213f5.svg'
AUTHOR='gpt-6'

class ThermometerMercury(Solo48):
    icon_id='thermometer-mercury'
    keyshape=Keyshape.VRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('thermometer', 'temperature', 'weather', 'heat', 'fever', 'measure', 'climate', 'hot')

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

        self.add_arc('cap',(15,13),(33,13),radius_x=9)
        self.add_line('right-tube',(33,13),(33,22))
        self.add_arc('right-shoulder',(33,22),(40,28),radius_x=7,radius_y=6)
        self.add_arc('bulb',(40,28),(8,28),radius_x=16)
        self.add_arc('left-shoulder',(8,28),(15,22),radius_x=7,radius_y=6)
        self.add_line('left-tube',(15,22),(15,13))
        self.add_contour('outline','cap','right-tube','right-shoulder','bulb','left-shoulder','left-tube',closed=True)
        self.add_line('mercury',(24,15),(24,24));self.add_dot('bulb-dot',(24,34))
