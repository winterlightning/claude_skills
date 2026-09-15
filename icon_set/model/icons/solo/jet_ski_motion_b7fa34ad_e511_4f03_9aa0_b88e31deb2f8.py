"""Angular jet ski with upright handle, two trailing marks and a water wave. No useful exact Lucide match; source motion layout retained with coherent separated strokes.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='b7fa34ad-e511-4f03-9aa0-b88e31deb2f8'
SOURCE_PATH='pictographic-primitives/symbol/water scooter_b7fa34ad-e511-4f03-9aa0-b88e31deb2f8.svg'
AUTHOR='gpt-6'

class JetSkiMotion(Solo48):
    icon_id='jet-ski-motion'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('jet-ski', 'water-scooter', 'watercraft', 'speed', 'waves', 'sea', 'sport', 'summer')

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

        self.path('hull',[(6,14),(22,28),(32,22),(24,18),(12,6)])
        self.add_line('handle',(24,18),(24,6));self.relate('connect','handle','hull')
        self.add_line('speed-upper',(6,30),(18,38));self.add_line('speed-lower',(6,40),(8,42))
        self.add_arc('wave-up',(28,38),(36,38),radius_x=4)
        self.add_arc('wave-down',(36,38),(42,38),radius_x=3,radius_y=4,sweep=False)
        self.add_contour('water','wave-up','wave-down')
