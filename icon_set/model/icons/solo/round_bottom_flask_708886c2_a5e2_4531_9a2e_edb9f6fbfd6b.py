"""Round Bottom Flask.

Plan: Centerline extremes (8,4)-(40,44); VRECT_L keyshape supports the complete standalone source silhouette.
Construction: Lucide flask-round: round lower bulb, narrow neck and projecting lip. Empty source interior is preserved.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '708886c2-a5e2-4531-9a2e-edb9f6fbfd6b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/bowl_708886c2-a5e2-4531-9a2e-edb9f6fbfd6b.svg'
AUTHOR = "gpt-6"

class Batch04Icon12(Solo48):
    icon_id = 'round-bottom-flask-708886c2'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/flask"
    aliases = ('round-bottom-flask',)
    keywords = ('round', 'bottom', 'flask')

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
        self.add_polyline("lip",(14,4),(18,4),(30,4),(34,4))
        path("body",(18,4),[("L",(18,14)),("C",(8,28),(18,20),(8,18)),("A",(40,28),16,16,False),("C",(30,14),(40,18),(30,20)),("L",(30,4))])
        self.relate("connect","lip","body")
