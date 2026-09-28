"""Decreasing Loading Circles.
Plan: Three circles share the horizontal centerline and decrease in radius from5 to3 to2. Radial envelope22.
Reference construction: loader.
Reduction: Compress the size progression; the smallest circle becomes a filled round dot at the required stroke weight.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7126606b-00db-56ef-be4a-3581fc00aabc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/loading line_7126606b-00db-56ef-be4a-3581fc00aabc.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'decreasing-loading-circles'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('decreasing', 'loading', 'circles')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        for j,(x,r) in enumerate([(9,5),(26,3),(42,2)]):circle(f'loading-{j}',x,24,r)
