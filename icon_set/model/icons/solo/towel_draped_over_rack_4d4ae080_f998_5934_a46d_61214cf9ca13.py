"""Towel Draped over Rack.
Plan: Front towel panel owns rounded fold and hem; rail ends attach at fold sides. Ink (2,6)-(46,42).
Construction reference: layout-grid.
Reduction: Omit rear flap and second stripe to keep one clear fabric band.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4d4ae080-f998-5934-a46d-61214cf9ca13'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom hanger_4d4ae080-f998-5934-a46d-61214cf9ca13.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'towel-draped-over-rack'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hotels'
    aliases = ()
    keywords = ('towel', 'draped', 'over', 'rack')
    def build(self):

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def rect(name,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r),(x+r,y)]
            for i,(a,b) in enumerate(zip(pts,pts[1:])):
                if i%2: self.add_arc(f'{name}-{i}',a,b,radius_x=r)
                else: self.add_line(f'{name}-{i}',a,b)
            self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

        rect('towel',12,8,24,32,4)
        self.add_line('rail-left',(4,16),(12,16))
        self.add_line('rail-right',(36,16),(44,16))
        self.relate('connect','rail-left','towel')
        self.relate('connect','rail-right','towel')
        self.add_line('band',(12,30),(36,30))
        self.relate('connect','band','towel')
