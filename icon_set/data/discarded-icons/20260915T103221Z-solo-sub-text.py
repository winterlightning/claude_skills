"""SUB in a single row: narrow S, round-bottomed U, and two-bowl B. Lucide strikethrough and type inform coherent letter strokes; no letters omitted.

SOLO48 HRECT_L; live visible envelope (2, 6, 46, 42).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID='295f78a7-9bc7-4067-98f6-00bc14bc4585'
SOURCE_PATH='pictographic-primitives/symbol/sub (text)_295f78a7-9bc7-4067-98f6-00bc14bc4585.svg'
AUTHOR='gpt-6'

class SubText(Solo48):
    icon_id='sub-text'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/symbols"
    aliases=()
    keywords=('sub', 'subscribe', 'subtitle', 'substitute', 'label', 'text', 'letters')

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

        self.add_arc('s-crown',(10,16),(4,16),radius_x=3,radius_y=8,sweep=False)
        self.add_arc('s-upper',(4,16),(7,24),radius_x=3,radius_y=8,sweep=False)
        self.add_arc('s-lower',(7,24),(10,32),radius_x=3,radius_y=8)
        self.add_arc('s-base',(10,32),(4,32),radius_x=3,radius_y=8)
        self.add_contour('s','s-crown','s-upper','s-lower','s-base')
        self.add_line('u-left',(19,8),(19,36))
        self.add_arc('u-base',(19,36),(27,36),radius_x=4,sweep=False)
        self.add_line('u-right',(27,36),(27,8))
        self.add_contour('u','u-left','u-base','u-right')
        self.add_arc('b-top',(36,8),(36,24),radius_x=8)
        self.add_arc('b-bottom',(36,24),(36,40),radius_x=8)
        self.raw('b-spine',[(36,40),(36,24),(36,8)])
        self.add_contour('b','b-top','b-bottom','b-spine-1','b-spine-2',closed=True)
