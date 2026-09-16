"""Fitted Wrap-Front Vest.
Plan: A fitted waistcoat with curved armholes, an intentionally offset wrap closure and twin pointed hems. Bounds (8,4)-(40,44).
References: Lucide shirt for garment construction; source for wrap direction.
Reduction: Secondary waist seams omitted; overlap expressed by the off-center neckline and return seam.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'b2442b9a-c348-437d-9568-4c64ffef9416'
SOURCE_PATH = 'pictographic-primitives/clothes/vest female_b2442b9a-c348-437d-9568-4c64ffef9416.svg'
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


class FittedWrapFrontVest(Solo48):
    icon_id = 'fitted-wrap-front-vest'
    keyshape = Keyshape.VRECT_L
    category = 'clothes'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('fitted', 'wrap-front', 'vest')

    def build(self):
        path(self,'outline',(18,4),('B',(27,20),(19,12),(23,17)),('B',(30,4),(28,16),(30,9)),('L',(40,4)),('B',(36,20),(40,12),(36,14)),('B',(38,32),(36,24),(38,28)),('L',(40,40)),('L',(32,44)),('L',(24,38)),('L',(16,44)),('L',(8,40)),('L',(10,32)),('B',(12,20),(10,28),(12,24)),('B',(8,4),(12,14),(8,12)),('L',(18,4)),closed=True)
        self.add_polyline('closure',(27,20),(24,28),(24,38))
        self.relate('connect','outline','closure')
