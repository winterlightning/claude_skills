"""Celsius unit with a degree ring at upper left and a large open C. Lucide type informs the open letter contour; both intrinsic unit components retained.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='58335f1d-dfae-41ef-bec6-fad278930777'
SOURCE_PATH='pictographic-primitives/symbol/temperature_58335f1d-dfae-41ef-bec6-fad278930777.svg'
AUTHOR='gpt-6'

class DegreesCelsius(Solo48):
    icon_id='degrees-celsius'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('celsius', 'temperature', 'degrees', 'weather', 'climate', 'heat', 'thermometer', 'unit')

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

        self.oval('degree',10,10,4)
        self.add_arc('c-tip-top',(42,18),(30,14),radius_x=12,radius_y=4,sweep=False)
        self.add_arc('c-upper',(30,14),(16,28),radius_x=14,sweep=False)
        self.add_arc('c-lower',(16,28),(30,42),radius_x=14,sweep=False)
        self.add_arc('c-tip-bottom',(30,42),(42,38),radius_x=12,radius_y=4,sweep=False)
        self.add_contour('c','c-tip-top','c-upper','c-lower','c-tip-bottom')
