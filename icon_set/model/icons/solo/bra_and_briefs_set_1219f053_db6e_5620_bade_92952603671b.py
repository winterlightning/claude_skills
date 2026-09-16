"""Bra and Briefs Set.
Plan: Mirrored paired bra cups and curved briefs, with shared cup attachment points and two vertical straps. Bounds (6,6)-(42,42).
References: Lucide shirt: minimal garment silhouettes; supplied set for paired arrangement.
Reduction: Tiny central clasp and stitching removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1219f053-db6e-5620-bade-92952603671b'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear female set_1219f053-db6e-5620-bade-92952603671b.svg'
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


class BraAndBriefsSet(Solo48):
    icon_id = 'bra-and-briefs-set'
    keyshape = Keyshape.SQUARE
    category = 'clothes'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('bra', 'and', 'briefs', 'set')

    def build(self):
        axis=24
        symmetric(self,'bra',(axis,14),[('B',(6,14),(18,10),(6,10)),('B',(axis,18),(6,26),(18,26))])
        for side in (-1,1):
         x=axis+side*18
         self.add_line('strap-'+str(side),(x,6),(x,14))
         self.relate('connect','bra','strap-'+str(side))
        symmetric(self,'briefs',(axis,32),[('L',(6,32)),('B',(18,42),(14,32),(14,38)),('L',(axis,42))])
