"""Water Repelling Surface Diagram.
Plan: Two repeated droplets above a flat material surface and a single bouncing trajectory. Bounds (4,8)-(44,40).
References: Lucide droplet for teardrop construction; source for reflected motion path.
Reduction: Two trajectories reduced to one bounce arrow; both droplets retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '966ee6d3-9c3d-400d-a6f8-8e39e0073ef3'
SOURCE_PATH = 'pictographic-primitives/construction/water repellent_966ee6d3-9c3d-400d-a6f8-8e39e0073ef3.svg'
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


def symmetric(icon, name, start, left_steps, axis=24):
    """One half owns the whole outline; reflect and reverse its traversal."""
    flip = lambda p: (2*axis-p[0], p[1])
    prior = start
    reverse = []
    for kind, end, *args in left_steps:
        if kind == 'B':
            reverse.append((kind, flip(prior), flip(args[1]), flip(args[0])))
        else:
            reverse.append((kind, flip(prior), *args))
        prior = end
    path(icon, name, start, *left_steps, *reversed(reverse), closed=True)


class WaterRepellingSurfaceDiagram(Solo48):
    icon_id = 'water-repelling-surface-diagram'
    keyshape = Keyshape.HRECT_L
    category = 'construction'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('water', 'repelling', 'surface', 'diagram')

    def build(self):
        for index,cx in enumerate((10,38)):
         path(self,f'drop-{index}',(cx,8),('B',(cx+4,14),(cx+1,10),(cx+4,12)),('A',(cx-4,14),4,4,True),('B',(cx,8),(cx-4,12),(cx-1,10)),closed=True)
        self.add_polyline('trajectory',(6,26),(14,32),(28,24))
        self.add_polyline('arrow',(20,24),(28,24),(28,32))
        self.add_line('surface',(4,40),(44,40))
        self.relate('connect','trajectory','arrow')
