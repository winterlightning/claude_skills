"""Dripping Faucet.
Plan: A gooseneck faucet uses concentric outer and inner bends, a mounted base and one separate drop. Bounds (8,4)-(40,44).
References: Lucide droplet for coherent pointed top and round lower lobe; no direct faucet match.
Reduction: Mounting base narrowed to keep the falling drop visibly clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '379758cd-6fd1-5d45-8ea1-09170fdc5f99'
SOURCE_PATH = 'pictographic-primitives/construction/water fountain sink_379758cd-6fd1-5d45-8ea1-09170fdc5f99.svg'
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


class DrippingFaucet(Solo48):
    icon_id = 'dripping-faucet'
    keyshape = Keyshape.VRECT_L
    category = 'construction'
    categories = ('construction', 'primitives')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('dripping', 'faucet')

    def build(self):
        path(self,'faucet',(34,36),('L',(34,16)),('A',(22,4),12,12,False),('A',(10,16),12,12,False),('L',(19,16)),('A',(25,16),3,3,True),('L',(25,36)))
        self.add_polyline('base',(25,36),(34,36),(40,36),(40,44),(25,44),closed=True)
        self.relate('connect','faucet','base')
        path(self,'drop',(12,25),('B',(16,30),(13,27),(16,28)),('A',(8,30),4,4,True),('B',(12,25),(8,28),(11,27)),closed=True)
