"""Curved Arrow from Circular Node.
Plan: Circular start attaches to an arch via its top cardinal point; right descent ends in an open head. Ink (2,6)-(46,42).
Reference construction: undo-2; network.
Reduction: Keep the defining source features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0cd85c1d-4c92-4870-bc35-f5c420829cf0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/relation organize_0cd85c1d-4c92-4870-bc35-f5c420829cf0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'curved-arrow-from-circular-node'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('curved', 'arrow', 'from', 'circular', 'node')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])): self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        circle('start',10,34,6)
        self.add_bezier('arch',(10,28),((10,17),(14,8),(24,8)),((34,8),(38,17),(38,28)))
        self.add_line('descent',(38,28),(38,34))
        self.add_contour('route','arch','descent')
        self.relate('connect','route','start')
        self.add_polyline('head',(32,28),(38,34),(44,28));self.relate('connect','head','route')
