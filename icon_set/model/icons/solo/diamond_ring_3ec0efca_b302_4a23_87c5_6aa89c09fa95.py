"""Diamond ring with a smooth oval band and a symmetric faceted setting."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ec0efca-b302-4a23-87c5-6aa89c09fa95'
SOURCE_PATH = 'pictographic-primitives/symbol/ring 1_3ec0efca-b302-4a23-87c5-6aa89c09fa95.svg'
AUTHOR = 'gpt-6'

class DiamondRing(Solo48):
    icon_id = 'diamond-ring'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'symbol'
    aliases = ()
    keywords = ('ring', 'diamond', 'engagement', 'wedding', 'jewelry', 'proposal', 'gem', 'marriage')

    def build(self) -> None:
        # Plan: smooth, mirrored oval band with a faceted gem behind its crown.
        # VRECT_L centerline extremes (8,4)-(40,44) preserve the upright ring.
        # Lucide gem: deliberate facet corners; omit tiny internal facet lines.
        axis = 24
        left, right = (16,18), (32,18)
        self.add_bezier('band-crown',left,((21,15),(27,15),right))
        right_segments = [((37,21),(40,24),(40,30)),
                          ((40,38),(33,44),(axis,44))]
        self.add_bezier('band-right',right,*right_segments)
        mirror = lambda p: (2*axis-p[0],p[1])
        starts = [right,right_segments[0][2]]
        left_segments = [(mirror(b),mirror(a),mirror(start))
                         for start,(a,b,end) in reversed(list(zip(starts,right_segments)))]
        self.add_bezier('band-left',(axis,44),*left_segments)
        self.add_contour('band','band-crown','band-right','band-left',closed=True)
        gem_half = [left,(12,10),(17,4)]
        gem = gem_half + [(2*axis-x,y) for x,y in reversed(gem_half)]
        self.add_polyline('gem',*gem)
        self.relate('connect','band','gem')
