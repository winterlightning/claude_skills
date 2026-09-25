"""Bed and Window.

Plan: Bed beneath four-pane window; reduce pillow to an open rounded rise.
Construction reference: Lucide bed: side-view frame and curved pillow; window is a physical scene detail.
Keyshape SQUARE: whole subject uses the exact SOLO48 inset envelope.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7e80f189-9b58-4f06-b817-6b38b5348139'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/bed window_7e80f189-9b58-4f06-b817-6b38b5348139.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'bed-beneath-a-four-pane-window'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('bed', 'and', 'window')

    def build(self):
        self.add_line('headboard',(6,24),(6,42))
        self.path('seat',[(6,34),(42,34),(42,42)])
        self.relate('connect','headboard','seat')
        self.rect('window',26,6,16,16,2)
        self.add_line('mullion-v',(34,6),(34,22));self.add_line('mullion-h',(26,14),(42,14))
        for part in ['mullion-v','mullion-h']:self.relate('connect','window',part)
        self.relate('connect','mullion-v','mullion-h')

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
