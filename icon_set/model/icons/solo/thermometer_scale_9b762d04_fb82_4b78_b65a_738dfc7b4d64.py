"""Thermometer with two right-side scale ticks, mercury line and bulb dot. Lucide thermometer informs its connected outer contour; all source feature types retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='9b762d04-fb82-4b78-b65a-738dfc7b4d64'
SOURCE_PATH='pictographic-primitives/symbol/thermometer_9b762d04-fb82-4b78-b65a-738dfc7b4d64.svg'
AUTHOR='gpt-6'

class ThermometerScale(Solo48):
    icon_id='thermometer-scale'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('thermometer', 'temperature', 'weather', 'heat', 'fever', 'measure', 'climate', 'scale')

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

        self.add_arc('cap',(9,15),(27,15),radius_x=9)
        self.add_line('right-tube',(27,15),(27,24))
        self.add_arc('right-shoulder',(27,24),(30,30),radius_x=3,radius_y=6)
        self.add_arc('bulb',(30,30),(6,30),radius_x=12)
        self.add_arc('left-shoulder',(6,30),(9,24),radius_x=3,radius_y=6)
        self.add_line('left-tube',(9,24),(9,15))
        self.add_contour('outline','cap','right-tube','right-shoulder','bulb','left-shoulder','left-tube',closed=True)
        self.add_line('mercury',(18,17),(18,24));self.add_dot('bulb-dot',(18,33))
        for j,y in enumerate((10,20)):self.add_line('scale-'+str(j),(39,y),(42,y))
