"""Branching Organization Diagram.

Plan: A wide rectangular parent owns a descending stem with two right branches and circular terminal nodes. Bounds (6,6)-(42,42).
Construction references: Lucide network: shared branching nodes and clean orthogonal connectors.
Simplification: No secondary text or node detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '14f1f8ba-2f05-5e7d-9a57-58aaaa13abf0'
SOURCE_PATH = 'pictographic-primitives/business/tree chart organize_14f1f8ba-2f05-5e7d-9a57-58aaaa13abf0.svg'
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


class BranchingOrganizationDiagram(Solo48):
    icon_id = 'branching-organization-diagram'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('branching', 'organization', 'diagram')

    def build(self):
        self.add_polyline('parent',(6,6),(30,6),(30,14),(18,14),(6,14),closed=True)
        path(self,'stem',(18,14),('L',(18,24)),('L',(18,34)),('A',(22,38),4,4,False),('L',(34,38)))
        self.add_line('branch',(18,24),(34,24))
        circle(self,'upper-node',38,24,4)
        circle(self,'lower-node',38,38,4)
        self.relate('connect','parent','stem')
        self.relate('connect','stem','branch')
        self.relate('connect','stem','lower-node')
        self.relate('connect','branch','upper-node')
