"""Factory with Twin Chimneys.

Plan: Two identical chimney rectangles share roof attachment nodes; centered peak. Centerline bounds (6,6)-(42,42).
Construction: Lucide factory: structural roof and chimney silhouette; preserve the supplied central pitched roof and two equal stacks, without adding windows.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fa0c17b5-c48d-4eaa-b6c7-45512d2a0593'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/factory 1_fa0c17b5-c48d-4eaa-b6c7-45512d2a0593.svg'
AUTHOR = "gpt-6"

class Batch02Icon12(Solo48):
    icon_id = 'factory-with-twin-chimneys-fa0c17b5'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    aliases = ('factory-with-twin-chimneys',)
    keywords = ('factory', 'with', 'twin', 'chimneys')

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
        self.add_polyline("building",(6,26),(16,26),(axis,20),(32,26),(42,26),(42,42),(6,42),closed=True)
        for side in (-1,1):
            p=lambda x,y:(axis+side*x,y)
            name=f"chimney-{side}"
            self.add_polyline(name,p(18,26),p(18,6),p(10,6),p(8,26))
            self.relate("connect","building",name)
