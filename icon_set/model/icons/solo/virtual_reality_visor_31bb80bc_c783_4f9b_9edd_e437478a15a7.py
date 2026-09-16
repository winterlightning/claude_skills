"""Virtual Reality Visor.
Plan: One mirror-owned, smoothly bulging visor outline with a rounded central nose notch. Bounds (4,8)-(44,40).
References: Lucide glasses for paired eye-area balance; source for blank visor and nose notch.
Reduction: No detail omitted from the blank face.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '31bb80bc-c783-4f9b-9edd-e437478a15a7'
SOURCE_PATH = 'pictographic-primitives/combination/vr headset 1_31bb80bc-c783-4f9b-9edd-e437478a15a7.svg'
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


class VirtualRealityVisor(Solo48):
    icon_id = 'virtual-reality-visor'
    keyshape = Keyshape.HRECT_L
    category = 'combination'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('virtual', 'reality', 'visor')

    def build(self):
        symmetric(self,'visor',(24,8),[('B',(4,24),(6,8),(4,12)),('B',(14,40),(4,34),(8,40)),('B',(24,30),(19,40),(19,30))])
