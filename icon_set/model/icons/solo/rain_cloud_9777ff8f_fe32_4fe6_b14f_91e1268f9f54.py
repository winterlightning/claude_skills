"""Rain Cloud.

Plan: Centerline extremes (6,6)-(42,42); SQUARE keyshape supports the complete standalone source silhouette.
Construction: Lucide cloud-rain: lobe silhouette with detached diagonal rain. Three equally spaced rain marks retain the source rhythm.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9777ff8f-fe32-4fe6-b14f-91e1268f9f54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/rain cloud_9777ff8f-fe32-4fe6-b14f-91e1268f9f54.svg'
AUTHOR = "gpt-6"

class Batch04Icon9(Solo48):
    icon_id = 'rain-cloud-9777ff8f'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/rain"
    aliases = ('rain-cloud',)
    keywords = ('rain', 'cloud')

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
        path("cloud",(14,14),[("A",(24,6),10,8,True),("A",(34,14),10,8,True),("A",(42,21),8,7,True),("L",(42,22)),("A",(36,28),6,6,True),("L",(12,28)),("A",(6,22),6,6,True),("A",(14,14),8,8,True)],True)
        for i,x in enumerate((14,26,38)):self.add_line(f"rain-{i}",(x,37),(x-5,42))
