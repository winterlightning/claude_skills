"""Laced Corset with Cups.
Plan: Mirrored sweetheart neckline, fitted waist and pointed hem; two straps and one centered lacing cross. Centerline bounds (8,4)-(40,44).
References: Lucide shirt for coherent garment contour; supplied corset for neckline and lacing.
Reduction: Underwire seams omitted; repeated lacing reduced to one open X.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'eaa011df-947f-57a7-ae02-68cc522f0dce'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear corset_eaa011df-947f-57a7-ae02-68cc522f0dce.svg'
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


class LacedCorsetWithCups(Solo48):
    icon_id = 'laced-corset-with-cups'
    keyshape = Keyshape.VRECT_L
    category = 'clothes'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('laced', 'corset', 'with', 'cups')

    def build(self):
        axis=24
        symmetric(self,'corset',(axis,18),[
         ('B',(8,12),(18,8),(8,8)),
         ('B',(10,30),(8,20),(10,24)),
         ('B',(8,40),(10,34),(9,37)),('L',(axis,44))])
        for side in (-1,1):
         x=axis+side*16
         self.add_line('strap-'+str(side),(x,4),(x,12))
         self.relate('connect','corset','strap-'+str(side))
        self.add_polyline('lace-a',(20,26),(24,30),(28,34))
        self.add_polyline('lace-b',(28,26),(24,30),(20,34))
        self.relate('connect','lace-a','lace-b')
