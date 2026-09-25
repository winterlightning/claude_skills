"""Two equal toothed wheels in a diagonal natural machine pair.
SQUARE extremes 6..42. Shared tooth definition at centers (16,32)/(32,16),
radius 10 with radius-2 axle holes. Reference supplies the diagonal arrangement;
Lucide cog informs radial repeats. Draft: clearance between gears unresolved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82c1163c-aaf6-4c80-9120-18bf38090361'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_12/cog double 1_82c1163c-aaf6-4c80-9120-18bf38090361.svg'
AUTHOR = 'gpt-6-astra'
class Drawing(Solo48):
    icon_id = 'two-interlocking-toothed-wheels'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('Two Interlocking Gears',)
    keywords = ('gears','wheels','teeth','interlocking','mechanical','pair','machine')
    def build(self):
        corners=[(-4,-10),(4,-10),(4,-6),(10,-6),(10,6),(4,6),(4,10),(-4,10),(-4,6),(-10,6),(-10,-6),(-4,-6)]
        for i,(x,y) in enumerate(((16,32),(32,16))):
            self.add_polyline(f'gear-{i}',*[(x+dx,y+dy) for dx,dy in corners],closed=True)
            self.add_arc(f'axle-{i}-a',(x-2,y),(x+2,y),radius_x=2)
            self.add_arc(f'axle-{i}-b',(x+2,y),(x-2,y),radius_x=2)
            self.add_contour(f'axle-{i}',f'axle-{i}-a',f'axle-{i}-b',closed=True)
