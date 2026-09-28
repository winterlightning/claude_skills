"""Single Bed with Pillow.
Plan: Bed uses one shared front plane, upright headboard and centered pillow. Ink (6,2)-(42,46).
Construction reference: bed-single.
Reduction: Flatten blanket edge; pillow shares its lower boundary with the blanket.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ec421b89-c7d9-573b-bec3-256a6da2bdb4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/hotel single bed_ec421b89-c7d9-573b-bec3-256a6da2bdb4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-bed-with-pillow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/hotels'
    aliases = ()
    keywords = ('single', 'bed', 'with', 'pillow')
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

        self.add_line('frame',(8,44),(8,8))
        self.add_arc('top-left',(8,8),(12,4),radius_x=4)
        self.add_line('top',(12,4),(36,4))
        self.add_arc('top-right',(36,4),(40,8),radius_x=4)
        self.add_line('right',(40,8),(40,44))
        self.add_contour('headboard','frame','top-left','top','top-right','right')
        self.add_polyline('pillow',(16,26),(16,14),(32,14),(32,26))
        self.add_line('blanket',(8,26),(16,26))
        self.add_line('blanket-mid',(16,26),(32,26))
        self.add_line('blanket-right',(32,26),(40,26))
        self.add_contour('blanket-edge','blanket','blanket-mid','blanket-right')
        self.add_line('mattress-base',(8,36),(40,36))
        self.relate('connect','headboard','blanket-edge')
        self.relate('connect','headboard','mattress-base')
        self.relate('connect','pillow','blanket-edge')
