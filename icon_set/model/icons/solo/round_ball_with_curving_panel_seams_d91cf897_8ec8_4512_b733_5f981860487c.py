"""Basketball Sports Ball.

Plan: Basketball sphere with a horizontal seam and two curved panel seams; remove one crowded seam.
Construction reference: No useful exact Lucide match; geometric arc construction.
Keyshape CIRCLE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd91cf897-8ec8-4512-b733-5f981860487c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/softball_d91cf897-8ec8-4512-b733-5f981860487c.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'round-ball-with-curving-panel-seams'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('basketball', 'sports', 'ball')

    def build(self):

        self.arc('outline-top',(4,24),(44,24),20)
        self.arc('outline-bottom',(44,24),(4,24),20)
        self.add_contour('ball','outline-top','outline-bottom',closed=True)
        self.add_line('equator',(4,24),(44,24));self.relate('connect','ball','equator')
        self.arc('seam-left',(12,8),(12,40),26,sweep=True)
        self.arc('seam-right',(36,8),(36,40),26,sweep=False)
        for p in ['seam-left','seam-right']:
            self.relate('connect','ball',p);self.relate('connect','equator',p)

    def circle(self, name, x, y, r, ry=None):
        ry = r if ry is None else ry
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r, radius_y=ry)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def path(self, name, points, closed=False):
        self.add_polyline(name, *points, closed=closed)

    def arc(self, name, a, b, r, ry=None, sweep=True):
        self.add_arc(name, a, b, radius_x=r, radius_y=r if ry is None else ry, sweep=sweep)

    def rect(self, name, x, y, w, h, r=4):
        points=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f'{name}-{i}'; ids.append(part)
            if i%2: self.arc(part,a,b,r)
            elif a != b: self.add_line(part,a,b)
            else: ids.pop()
        self.add_contour(name,*ids,closed=True)
