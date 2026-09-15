"""Toolbox with Central Latch.

Plan: Rounded toolbox with open handle, split lid seam and one vertical latch. Shared nodes attach handle and latch. Bounds (4,8)-(44,40).
Construction references: Lucide briefcase-business: rounded body and raised carrying handle.
Simplification: Clipped latch corner reduced to a single stout latch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '21019f01-b694-5b5c-8638-506c55a1bbf3'
SOURCE_PATH = 'pictographic-primitives/business/tool box_21019f01-b694-5b5c-8638-506c55a1bbf3.svg'
AUTHOR = 'gpt-6'

def path(icon, name, start, *steps, closed=False):
    """Emit one coherent stroke; each knot belongs to its owning shape."""
    members = []
    point = start
    for index, step in enumerate(steps):
        member = f"{name}-{index + 1}"
        kind, end, *args = step
        if kind == "L":
            icon.add_line(member, point, end)
        elif kind == "A":
            rx, ry, sweep = args
            icon.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
        elif kind == "B":
            icon.add_bezier(member, point, (args[0], args[1], end))
        members.append(member)
        point = end
    icon.add_contour(name, *members, closed=closed)


def circle(icon, name, cx, cy, radius):
    path(icon, name, (cx-radius, cy),
         ("A", (cx, cy-radius), radius, radius, True),
         ("A", (cx+radius, cy), radius, radius, True),
         ("A", (cx, cy+radius), radius, radius, True),
         ("A", (cx-radius, cy), radius, radius, True), closed=True)


class ToolboxWithCentralLatch(Solo48):
    icon_id = 'toolbox-with-central-latch'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('toolbox', 'with', 'central', 'latch')

    def build(self):
        path(self,'body',(8,16),('L',(16,16)),('L',(32,16)),('L',(40,16)),('A',(44,20),4,4,True),('L',(44,26)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,26)),('L',(4,20)),('A',(8,16),4,4,True),closed=True)
        path(self,'handle',(16,16),('L',(16,12)),('A',(20,8),4,4,True),('L',(28,8)),('A',(32,12),4,4,True),('L',(32,16)))
        self.add_polyline('seam',(4,26),(24,26),(44,26))
        self.add_line('latch',(24,26),(24,31))
        self.relate('connect','body','handle')
        self.relate('connect','body','seam')
        self.relate('connect','seam','latch')
