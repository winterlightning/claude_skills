"""Clicking Mouse Pointer.
Plan: Compact pointer and tail share a notch; detached click marks occupy the upper and left quadrants. Ink (4,4)-(44,44).
Reference construction: mouse-pointer-click.
Reduction: Use a thin round-ended tail; omit the right click stroke where the pointer occupies the available width.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '51abfbed-d6ec-5db0-9428-35d4ae0a14e1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cursor highlight click_51abfbed-d6ec-5db0-9428-35d4ae0a14e1.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'clicking-mouse-pointer'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('clicking', 'mouse', 'pointer')
    def build(self):

        def circle(name,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):
                self.add_arc(f'{name}-{j}',a,b,radius_x=r)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)

        self.add_polyline('pointer',(18,18),(42,26),(31,31),(26,42),closed=True)
        self.add_line('tail',(31,31),(40,40))
        self.relate('connect','tail','pointer')
        self.add_line('click-top',(20,6),(20,10))
        self.add_line('click-left',(6,20),(10,20))
        self.add_line('click-diagonal',(7,7),(10,10))
        self.add_line('click-upper-right',(33,7),(30,10))
        self.add_line('click-lower-left',(7,33),(10,30))
