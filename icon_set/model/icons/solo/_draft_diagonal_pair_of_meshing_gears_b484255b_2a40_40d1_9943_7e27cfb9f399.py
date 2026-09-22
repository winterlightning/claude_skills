"""Two equal toothed wheels in a diagonal natural machine pair.
HRECT_L extremes (4,8)-(44,40). Shared tooth definition at centers (14,30)/(34,18),
radius 10 with radius-2 axle holes. Reference supplies the diagonal arrangement;
Lucide cog informs radial repeats. Draft: clearance between gears unresolved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b484255b-2a40-40d1-9943-7e27cfb9f399'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_12/cog double_b484255b-2a40-40d1-9943-7e27cfb9f399.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'diagonal-pair-of-meshing-gears'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'Uncategorized'
    aliases = ('Double Interlocking Gears',)
    keywords = ('gears','wheels','teeth','interlocking','mechanical','pair','machine')
    def build(self):
        corners=[(-4,-10),(4,-10),(4,-6),(10,-6),(10,6),(4,6),(4,10),(-4,10),(-4,6),(-10,6),(-10,-6),(-4,-6)]
        for i,(x,y) in enumerate(((14,30),(34,18))):
            self.add_polyline(f'gear-{i}',*[(x+dx,y+dy) for dx,dy in corners],closed=True)
            self.add_arc(f'axle-{i}-a',(x-2,y),(x+2,y),radius_x=2)
            self.add_arc(f'axle-{i}-b',(x+2,y),(x-2,y),radius_x=2)
            self.add_contour(f'axle-{i}',f'axle-{i}-a',f'axle-{i}-b',closed=True)
