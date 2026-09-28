"""Magnifying Glass.

Plan: Centerline extremes (6,6)-(42,42); SQUARE keyshape supports the complete standalone source silhouette.
Construction: Lucide search: circular lens with attached diagonal handle.
Reduction: No decorative content added. Integer geometry with profile stroke and round caps.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd025ed05-d171-467f-99ec-c07ccf1aaf1f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/magnifying glass 2_d025ed05-d171-467f-99ec-c07ccf1aaf1f.svg'
AUTHOR = "gpt-6"

class Batch04Icon0(Solo48):
    icon_id = 'magnifying-glass-d025ed05'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('magnifying-glass',)
    keywords = ('magnifying', 'glass')

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
        path("lens",(21,6),[("A",(36,21),15,15,True),("A",(30,33),15,15,True),("A",(21,36),15,15,True),("A",(6,21),15,15,True),("A",(21,6),15,15,True)],True)
        self.add_line("handle",(30,33),(42,42));self.relate("connect","lens","handle")
