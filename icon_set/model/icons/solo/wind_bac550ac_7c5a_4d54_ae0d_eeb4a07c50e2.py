"""Two horizontal gusts with opposite curling ends. Lucide wind informs tangent line-to-hook joins and differing curl sizes; both source strokes retained.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='bac550ac-7c5a-4d54-ae0d-eeb4a07c50e2'
SOURCE_PATH='pictographic-primitives/symbol/wind_bac550ac-7c5a-4d54-ae0d-eeb4a07c50e2.svg'
AUTHOR='gpt-6'

class Wind(Solo48):
    icon_id='wind'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "symbol"
    aliases=()
    keywords=('wind', 'air', 'breeze', 'weather', 'blow', 'gust', 'climate', 'flow')

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

        self.add_line('upper-line',(4,20),(38,20));self.add_arc('upper-turn',(38,20),(38,8),radius_x=6,sweep=False)
        self.add_arc('upper-tip',(38,8),(32,14),radius_x=6,sweep=False)
        self.add_contour('upper','upper-line','upper-turn','upper-tip')
        self.add_line('lower-line',(4,30),(26,30));self.add_arc('lower-turn',(26,30),(26,40),radius_x=5)
        self.add_arc('lower-tip',(26,40),(21,35),radius_x=5)
        self.add_contour('lower','lower-line','lower-turn','lower-tip')
