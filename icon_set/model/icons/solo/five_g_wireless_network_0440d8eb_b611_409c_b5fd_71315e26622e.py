from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0440d8eb-b611-409c-b5fd-71315e26622e'
SOURCE_PATH = 'pictographic-primitives/other/5g (text)_0440d8eb-b611-409c-b5fd-71315e26622e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'five-g-wireless-network'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('5G', 'wireless', 'network')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def rounded_rect(self, name, x0, y0, x1, y1, r):
        pts=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
        ids=[]
        for i in range(8):
            eid=f'{name}-{i}'
            a,b=pts[i],pts[(i+1)%8]
            if i%2: self.add_arc(eid,a,b,radius_x=r)
            else: self.add_line(eid,a,b)
            ids.append(eid)
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # Plan: squared upper 5 and one elliptical lower bowl; companion open G.
        # HRECT_M centerlines (4,10)-(44,38); shared cap height and baseline.
        self.add_line('five-cap',(16,10),(4,10))
        self.add_line('five-stem',(4,10),(4,22))
        self.add_arc('five-bowl',(4,22),(4,38),radius_x=12,radius_y=8)
        self.add_contour('five','five-cap','five-stem','five-bowl')
        self.add_arc('g-upper-right',(44,18),(36,10),radius_x=8,sweep=False)
        self.add_arc('g-upper-left',(36,10),(28,18),radius_x=8,sweep=False)
        self.add_line('g-left',(28,18),(28,30))
        self.add_arc('g-lower-left',(28,30),(36,38),radius_x=8,sweep=False)
        self.add_arc('g-lower-right',(36,38),(44,30),radius_x=8,sweep=False)
        self.add_polyline('g-spur',(44,30),(44,24),(36,24))
        self.add_contour('g-body','g-upper-right','g-upper-left','g-left','g-lower-left','g-lower-right')
        self.relate('connect','g-body','g-spur')
