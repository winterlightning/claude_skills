"""Plain Boxer Shorts.
Plan: A broad waistband above mirrored sloping hems and a rounded crotch. Bounds (4,8)-(44,40).
References: Lucide shirt: one continuous outline with an attached garment seam.
Reduction: No identity-bearing detail omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '2c95789e-c630-58ae-9a1a-c5eabed6c498'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear shorts male_2c95789e-c630-58ae-9a1a-c5eabed6c498.svg'
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


class PlainBoxerShorts(Solo48):
    icon_id = 'plain-boxer-shorts'
    keyshape = Keyshape.HRECT_L
    category = 'clothes'
    categories = ('primitives', 'clothes')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('plain', 'boxer', 'shorts')

    def build(self):
        axis=24
        symmetric(self,'outline',(axis,8),[('L',(8,8)),('L',(7,16)),('L',(4,40)),('L',(18,38)),('L',(20,32)),('A',(axis,28),4,4,True)])
        self.add_line('waistband',(7,16),(41,16))
        self.relate('connect','outline','waistband')
