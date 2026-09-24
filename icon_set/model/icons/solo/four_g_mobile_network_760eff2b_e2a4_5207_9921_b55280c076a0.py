from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '760eff2b-e2a4-5207-9921-b55280c076a0'
SOURCE_PATH = 'pictographic-primitives/mobile/4g_760eff2b-e2a4-5207-9921-b55280c076a0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'four-g-mobile-network'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'mobile'
    aliases = ()
    keywords = ('4G', 'mobile', 'network')

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
        # Plan: triangular 4 with shared crossbar node; G matches the companion 3G.
        # HRECT_M centerlines (4,10)-(44,38); intentional lettering asymmetry.
        self.add_polyline('four-triangle',(14,10),(4,30),(14,30),closed=True)
        self.add_line('four-foot',(14,30),(14,38))
        self.add_line('four-crossbar',(14,30),(18,30))
        for a,b in [('four-triangle','four-foot'),('four-triangle','four-crossbar'),('four-foot','four-crossbar')]:
            self.relate('connect',a,b)
        self.add_arc('g-upper-right',(44,18),(36,10),radius_x=8,sweep=False)
        self.add_arc('g-upper-left',(36,10),(28,18),radius_x=8,sweep=False)
        self.add_line('g-left',(28,18),(28,30))
        self.add_arc('g-lower-left',(28,30),(36,38),radius_x=8,sweep=False)
        self.add_arc('g-lower-right',(36,38),(44,30),radius_x=8,sweep=False)
        self.add_polyline('g-spur',(44,30),(44,24),(36,24))
        self.add_contour('g-body','g-upper-right','g-upper-left','g-left','g-lower-left','g-lower-right')
        self.relate('connect','g-body','g-spur')
