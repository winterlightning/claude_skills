"""Cream Jar.

Plan: Rounded body with a wide cap integrated at shared neck nodes. Centerline bounds (4,8)-(44,40).
Construction: Lucide briefcase-business supplies rounded-rectangle corner construction; the supplied jar owns the broad neck and lid.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ed6bc0cd-a7f1-4e30-9ef5-92d6850bcdfe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/jar_ed6bc0cd-a7f1-4e30-9ef5-92d6850bcdfe.svg'
AUTHOR = "gpt-6"

class Batch02Icon5(Solo48):
    icon_id = 'cosmetic-cream-jar-ed6bc0cd'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/jar"
    aliases = ('cosmetic-cream-jar',)
    keywords = ('cosmetic', 'cream', 'jar')

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
        path("body",(10,18),[("L",(38,18)),("A",(44,24),6,6,True),("L",(44,34)),("A",(38,40),6,6,True),("L",(10,40)),("A",(4,34),6,6,True),("L",(4,24)),("A",(10,18),6,6,True)],True)
        path("lid",(10,18),[("L",(10,12)),("A",(14,8),4,4,True),("L",(34,8)),("A",(38,12),4,4,True),("L",(38,18))])
        self.relate("connect","body","lid")
