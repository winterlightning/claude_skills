"""Wood Board with Knot.
Plan: One rounded plank rectangle and one central oval knot. Bounds (4,8)-(44,40).
References: Supplied board for knot and wavy grain; no useful Lucide plank match.
Reduction: Two fine grain waves omitted because the knot and board walls leave insufficient clear space.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'cedb9824-d21f-4060-9df0-b542ab84c45a'
SOURCE_PATH = 'pictographic-primitives/construction/wood material_cedb9824-d21f-4060-9df0-b542ab84c45a.svg'
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

class WoodBoardWithKnot(Solo48):
    icon_id = 'wood-board-with-knot'
    keyshape = Keyshape.HRECT_L
    category = 'construction'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('wood', 'board', 'with', 'knot')
    def build(self):
        path(self,'board',(8,8),('L',(40,8)),('A',(44,12),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,12)),('A',(8,8),4,4,True),closed=True)
        path(self,'knot',(18,24),('A',(30,24),6,4,True),('A',(18,24),6,4,True),closed=True)
