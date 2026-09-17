"""Partly Open Booklet.

Plan: Centerline extremes (8,4)-(40,44); VRECT_L keyshape supports the complete standalone source silhouette.
Construction: Lucide book-open: joined page contours. Original source owns the upright rectangular front and sloping rear page.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '660afc5b-ad9a-4a84-bc13-05a7149e7cc9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/booklet_660afc5b-ad9a-4a84-bc13-05a7149e7cc9.svg'
AUTHOR = "gpt-6"

class Batch04Icon3(Solo48):
    icon_id = 'partly-open-booklet-660afc5b'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/book"
    aliases = ('partly-open-booklet',)
    keywords = ('partly', 'open', 'booklet')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for i, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{i}"
                if kind == "L": self.add_line(member, here, end)
                elif kind == "A": self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == "C": self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, radius):
            path(name,(cx,cy-radius),[("A",(cx+radius,cy),radius,radius,True),("A",(cx,cy+radius),radius,radius,True),("A",(cx-radius,cy),radius,radius,True),("A",(cx,cy-radius),radius,radius,True)],True)
        self.add_polyline("front",(8,16),(36,16),(40,16),(40,44),(8,44),closed=True)
        self.add_polyline("rear",(8,16),(36,4),(36,16));self.relate("connect","front","rear")
