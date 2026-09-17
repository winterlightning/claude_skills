"""Concentric Crosshair.
Plan: Two concentric circles with nine-unit radial separation and four cardinal spurs; radial envelope22.
Reference construction: crosshair.
Reduction: Stop crosshair strokes at the outer circle to preserve the two clean circular openings.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '77bc6d32-25e9-5f18-9d71-564dacddc13d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor target_77bc6d32-25e9-5f18-9d71-564dacddc13d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'concentric-crosshair-reference'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/interface-essential'
    aliases = ()
    keywords = ('concentric', 'crosshair')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        circle('outer',24,24,15);circle('inner',24,24,6)
        for j,(a,b) in enumerate([((4,24),(9,24)),((39,24),(44,24)),((24,4),(24,9)),((24,39),(24,44))]):
         self.add_line(f'spur-{j}',a,b);self.relate('connect',f'spur-{j}','outer')
