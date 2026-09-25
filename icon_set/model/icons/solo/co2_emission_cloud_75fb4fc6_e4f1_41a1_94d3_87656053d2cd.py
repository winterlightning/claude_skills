from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '75fb4fc6-e4f1-41a1-94d3-87656053d2cd'
SOURCE_PATH = 'pictographic-primitives/other/cloud with co2_75fb4fc6-e4f1-41a1-94d3-87656053d2cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'co2-emission-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('CO2', 'emissions', 'cloud', 'carbon')

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
        # Plan: open three-lobed cloud above custom C, oval O, lowered 2. Baseline y42.
        # SQUARE centerline extremes (6,6)-(42,42). Shared cloud shoulders at y14.
        self.add_arc('cloud-left',(6,22),(14,14),radius_x=8)
        self.add_arc('cloud-crown',(14,14),(34,14),radius_x=10,radius_y=8)
        self.add_arc('cloud-right',(34,14),(42,22),radius_x=8)
        self.add_contour('cloud','cloud-left','cloud-crown','cloud-right')
        self.add_arc('letter-c',(12,30),(12,42),radius_x=6,sweep=False)
        self.add_arc('letter-o-top',(20,36),(28,36),radius_x=4,radius_y=6)
        self.add_arc('letter-o-bottom',(28,36),(20,36),radius_x=4,radius_y=6)
        self.add_contour('letter-o','letter-o-top','letter-o-bottom',closed=True)
        self.add_arc('two-cap',(36,35),(42,35),radius_x=3)
        self.add_line('two-diagonal',(42,35),(36,42))
        self.add_line('two-base',(36,42),(42,42))
        self.add_contour('two','two-cap','two-diagonal','two-base')
