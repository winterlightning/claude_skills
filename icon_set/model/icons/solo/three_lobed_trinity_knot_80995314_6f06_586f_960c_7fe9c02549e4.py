from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80995314-6f06-586f-960c-7fe9c02549e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/triangle_80995314-6f06-586f-960c-7fe9c02549e4.svg'
AUTHOR = "gpt-6"


class Drawing(Solo48):
    icon_id = 'three-lobed-trinity-knot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('trinity', 'knot', 'triquetra', 'celtic', 'loops', 'symbol', 'interlace', 'three')

    def build(self):
        # Plan: one continuous three-lobed crossing curve; mirrored side lobes and pointed outer tips.
        # Centerline extremes: (6,6)-(42,42). Construction: No useful local triquetra match; supplied reference establishes three crossing lobes.
        def path(name,*points,closed=False):
            self.add_polyline(name,*points,closed=closed)
        def circle(name,x,y,r):
            self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        def join(a,b):
            self.relate('connect',a,b)

        axis = 24
        tip, left, right = (axis,6), (axis-18,42), (axis+18,42)
        # The side-loop controls mirror about the same axis.
        self.add_bezier('right-loop',tip,((axis+26,30),(axis,42),left))
        self.add_bezier('lower-loop',left,((axis-18,14),(axis+18,14),right))
        self.add_bezier('left-loop',right,((axis,42),(axis-26,30),tip))
        self.add_contour('knot','right-loop','lower-loop','left-loop',closed=True)
