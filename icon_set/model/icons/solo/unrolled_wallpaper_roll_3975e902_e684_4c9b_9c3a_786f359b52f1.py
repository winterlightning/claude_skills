"""Unrolled Wallpaper Roll.
Plan: A vertical cylindrical roll with a rounded top, circular lower end and a flat sheet attached at shared knots. Bounds (6,6)-(42,42).
References: Lucide scroll: curled ends attached to a flat sheet.
Reduction: Fine roll thickness omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '3975e902-e684-4c9b-9c3a-786f359b52f1'
SOURCE_PATH = 'pictographic-primitives/construction/wallpaper_3975e902-e684-4c9b-9c3a-786f359b52f1.svg'
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


class UnrolledWallpaperRoll(Solo48):
    icon_id = 'unrolled-wallpaper-roll'
    keyshape = Keyshape.SQUARE
    category = 'construction'
    categories = ('construction', 'primitives')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('unrolled', 'wallpaper', 'roll')

    def build(self):
        path(self,'roll',(6,14),('A',(22,14),8,8,True),('L',(22,34)),('A',(14,42),8,8,True),('A',(6,34),8,8,True),('L',(6,14)),closed=True)
        self.add_arc('curl',(6,34),(22,34),radius_x=8)
        self.add_polyline('sheet',(22,14),(42,14),(42,42),(14,42))
        self.relate('connect','roll','curl')
        self.relate('connect','roll','sheet')
