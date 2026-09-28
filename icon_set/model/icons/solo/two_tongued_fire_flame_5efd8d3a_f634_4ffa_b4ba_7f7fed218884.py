"""Fire Flame.

Plan: Intentionally uneven tongues flow to broad radius16 lower body. Centerline bounds (8,4)-(40,44). No internal flame glyph.
Construction: Lucide flame: coherent curves around a rounded lower bowl; supplied reference owns the smaller left tongue and taller right tongue.
Reduction: Preserve the complete single subject; no unrelated detail added.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5efd8d3a-f634-4ffa-b4ba-7f7fed218884'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/container/fire 1_5efd8d3a-f634-4ffa-b4ba-7f7fed218884.svg'
AUTHOR = "gpt-6"

class Batch02Icon14(Solo48):
    icon_id = 'two-tongued-fire-flame-5efd8d3a'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "container"
    categories = ("container",)
    aliases = ('two-tongued-fire-flame',)
    keywords = ('two', 'tongued', 'fire', 'flame')

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
        path("outline",(24,4),[("C",(40,28),(32,10),(40,19)),("A",(8,28),16,16,True),("C",(12,20),(8,24),(11,22)),("C",(12,10),(13,16),(12,12)),("C",(22,20),(16,12),(20,16)),("C",(24,4),(25,14),(25,8))],True)
