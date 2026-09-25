"""Plain V-Neck Vest.
Plan: Mirror-owned V-neck waistcoat with curved armholes, round outer hem corners and central opening. Bounds (8,4)-(40,44).
References: Lucide shirt: sparse coherent outline; source for waistcoat opening.
Reduction: No buttons or secondary stitching.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'e2d88122-906a-5dc0-865e-6b8edd2474ba'
SOURCE_PATH = 'pictographic-primitives/clothes/vest male_e2d88122-906a-5dc0-865e-6b8edd2474ba.svg'
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


class PlainVNeckVest(Solo48):
    icon_id = 'plain-v-neck-vest'
    keyshape = Keyshape.VRECT_L
    category = 'clothes'
    categories = ('primitives', 'clothes')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('plain', 'v-neck', 'vest')

    def build(self):
        axis=24
        symmetric(self,'outline',(axis,20),[('B',(18,4),(20,17),(19,12)),('L',(8,4)),('B',(12,20),(8,12),(12,14)),('B',(8,26),(12,24),(8,24)),('L',(8,40)),('A',(12,44),4,4,False),('L',(axis,36))])
        self.add_line('opening',(axis,20),(axis,36))
        self.relate('connect','outline','opening')
