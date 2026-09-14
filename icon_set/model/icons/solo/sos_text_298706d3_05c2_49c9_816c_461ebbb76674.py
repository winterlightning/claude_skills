"""SOS in one line with repeated S strokes and a capsule O. Lucide strikethrough informs the coherent letter curves; no letters dropped.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='298706d3-05c2-49c9-816c-461ebbb76674'
SOURCE_PATH='pictographic-primitives/symbol/sos (text)_298706d3-05c2-49c9-816c-461ebbb76674.svg'
AUTHOR='gpt-6'

class SosText(Solo48):
    icon_id='sos-text'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('sos', 'emergency', 'help', 'distress', 'rescue', 'signal', 'alert', 'text')

    def oval(self,n,cx,cy,rx,ry=None):
        ry=rx if ry is None else ry
        self.add_arc(n+'-top',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
        self.add_arc(n+'-bottom',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,points,closed=False):
        self.add_polyline(n,*points,closed=closed)

    def build(self):

        for label,x in [('left',4),('right',38)]:
            self.add_arc(label+'-crown',(x+6,16),(x,16),radius_x=3,radius_y=8,sweep=False)
            self.add_arc(label+'-upper',(x,16),(x+3,24),radius_x=3,radius_y=8,sweep=False)
            self.add_arc(label+'-lower',(x+3,24),(x+6,32),radius_x=3,radius_y=8)
            self.add_arc(label+'-base',(x+6,32),(x,32),radius_x=3,radius_y=8)
            self.add_contour(label,*[label+'-'+p for p in ['crown','upper','lower','base']])
        self.add_arc('o-top',(19,13),(29,13),radius_x=5)
        self.add_line('o-right',(29,13),(29,35))
        self.add_arc('o-bottom',(29,35),(19,35),radius_x=5)
        self.add_line('o-left',(19,35),(19,13))
        self.add_contour('o','o-top','o-right','o-bottom','o-left',closed=True)
