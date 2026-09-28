"""Video Camera.
Plan: HRECT_M, centerline bounds (4,10)-(44,38), complete standalone subject.
Construction: Lucide video informs rounded body with a joined flared right lens housing. Horizontal keyshape reserves room for the projection.
Reduction: Preserve identity and clear negative space on the SOLO48 integer grid.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fa55d7ca-210a-4841-8bd4-a580b7f5f257'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/video_fa55d7ca-210a-4841-8bd4-a580b7f5f257.svg'
AUTHOR = "gpt-6"
class Batch05Icon7(Solo48):
    icon_id = 'video-camera-fa55d7ca'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('video-camera',)
    keywords = ('video', 'camera')
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
        path("body",(8,10),[("L",(26,10)),("A",(30,14),4,4,True),("L",(30,18)),("L",(30,30)),("L",(30,34)),("A",(26,38),4,4,True),("L",(8,38)),("A",(4,34),4,4,True),("L",(4,14)),("A",(8,10),4,4,True)],True)
        self.add_polyline("lens",(30,18),(44,12),(44,36),(30,30));self.relate("connect","body","lens")
