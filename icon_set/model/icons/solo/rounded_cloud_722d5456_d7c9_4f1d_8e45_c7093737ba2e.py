"""Cloud.

Plan: Mirrored central radius12 dome and radius8 lateral lobes; shared tangent nodes. Centerline bounds (4,10)-(44,38).
Construction: Lucide cloud: continuous lobes and flat base; preserve the supplied large central lobe and paired side lobes.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '722d5456-d7c9-4f1d-8e45-c7093737ba2e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/cloud 1_722d5456-d7c9-4f1d-8e45-c7093737ba2e.svg'
AUTHOR = "gpt-6"

class Batch02Icon3(Solo48):
    icon_id = 'rounded-cloud-722d5456'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/cloud"
    aliases = ('rounded-cloud',)
    keywords = ('rounded', 'cloud')

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
        axis=24
        path("outline",(12,22),[("A",(axis,10),12,12,True),("A",(36,22),12,12,True),("A",(44,30),8,8,True),("A",(36,38),8,8,True),("L",(12,38)),("A",(4,30),8,8,True),("A",(12,22),8,8,True)],True)
