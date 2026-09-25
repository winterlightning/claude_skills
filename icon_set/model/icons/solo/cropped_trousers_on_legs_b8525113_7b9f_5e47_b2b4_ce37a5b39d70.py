"""Cropped Trousers on Legs.

Plan: Cropped trouser silhouette with paired open legs and outward feet; all paired coordinates derive from the vertical axis. Bounds (8,4)-(40,44).
Construction references: human_ref/full_body_ref.png simple limbs; Lucide shirt coherent garment outline.
Simplification: Anatomical calves become single clean lower-leg strokes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8525113-7b9f-5e47-b2b4-ce37a5b39d70'
SOURCE_PATH = 'pictographic-primitives/clothes/trousers calves_b8525113-7b9f-5e47-b2b4-ce37a5b39d70.svg'
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


class CroppedTrousersOnLegs(Solo48):
    icon_id = 'cropped-trousers-on-legs'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('cropped', 'trousers', 'on', 'legs')

    def build(self):
        self.add_polyline('trousers',(12,4),(36,4),(40,32),(32,32),(28,32),(24,18),(20,32),(16,32),(8,32),closed=True)
        for side in (-1,1):
            x=lambda off:24+side*off
            name='left' if side<0 else 'right'
            path(self,'leg-'+name,(x(8),32),('L',(x(8),40)),('A',(x(12),44),4,4,side<0),('L',(x(16),44)))
            self.relate('connect','trousers','leg-'+name)
