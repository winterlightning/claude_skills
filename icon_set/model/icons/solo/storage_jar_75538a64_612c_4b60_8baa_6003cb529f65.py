"""Storage Jar.
Plan: SQUARE, centerline bounds (6,6)-(42,42), complete standalone subject.
Construction: No useful local Lucide jar match; container is a different object. Source owns squat rounded body and broad flared lid. Paired shoulders and equal corner radii.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '75538a64-612c-4b60-8baa-6003cb529f65'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/jar 1_75538a64-612c-4b60-8baa-6003cb529f65.svg'
AUTHOR = "gpt-6"
class Batch05Icon5(Solo48):
    icon_id = 'storage-jar-75538a64'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('storage-jar',)
    keywords = ('storage', 'jar')
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
        axis=24
        path("body",(16,14),[("L",(32,14)),("A",(42,24),10,10,True),("L",(42,34)),("A",(34,42),8,8,True),("L",(14,42)),("A",(6,34),8,8,True),("L",(6,24)),("A",(16,14),10,10,True)],True)
        self.add_polyline("lid",(16,14),(10,6),(38,6),(32,14));self.relate("connect","lid","body")
