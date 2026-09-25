"""An empty upright application panel with one shallow header band.
VRECT_XL gives exact centerline extremes (6,2)-(58,62).
Owner: mirrored rounded enclosure, radius 6, with a horizontal header at y=18.
The side rails split at the two true divider attachments. No source details omitted.
Lucide panels-top-left original and atoms inform quarter-circle corners and divider.
Preserves the source's recorded user choice of container family.
"""
from ._base import Container64
from ...keyshapes import Keyshape

SOURCE_ICON_ID = "f2a30549-19ad-459a-ac75-4bcb81aafc02"
SOURCE_PATH = "pictographic-primitives/_uncategorized_32/remnant_f2a30549-19ad-459a-ac75-4bcb81aafc02.svg"
AUTHOR = "gpt-6"

class Drawing(Container64):
    icon_id = "blank-panel-with-header-band"
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("Application Window with Top Header",)
    keywords = ("panel", "header", "card", "frame", "blank", "layout")

    def build(self):
        axis, left, top, bottom, radius, header = 32, 6, 2, 62, 6, 18
        right = 2*axis-left
        points = [(left+radius,top),(right-radius,top),(right,top+radius),
                  (right,header),(right,bottom-radius),(right-radius,bottom),
                  (left+radius,bottom),(left,bottom-radius),(left,header),(left,top+radius)]
        arcs = {1,4,6,9}
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%len(points)]; name=f"frame-{i}"; members.append(name)
            if i in arcs: self.add_arc(name,a,b,radius_x=radius)
            else: self.add_line(name,a,b)
        self.add_contour("frame",*members,closed=True)
        self.add_line("header",(left,header),(right,header))
        self.relate("connect","header","frame")
