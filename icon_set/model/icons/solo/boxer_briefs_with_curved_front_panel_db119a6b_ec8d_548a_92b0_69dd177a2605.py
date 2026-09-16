"""Boxer Briefs with Curved Front Panel.
Plan: Mirrored boxer-brief silhouette; waistband and a curved front panel share real attachment nodes. Bounds (4,8)-(44,40).
References: Lucide shirt: joined garment seams; supplied brief for long front panel.
Reduction: Stitching omitted; crotch simplified into a rounded-stroke notch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = 'db119a6b-ec8d-548a-92b0-69dd177a2605'
SOURCE_PATH = 'pictographic-primitives/clothes/underwear shorts male_db119a6b-ec8d-548a-92b0-69dd177a2605.svg'
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


class BoxerBriefsWithCurvedFrontPanel(Solo48):
    icon_id = 'boxer-briefs-with-curved-front-panel'
    keyshape = Keyshape.HRECT_L
    category = 'clothes'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('boxer', 'briefs', 'with', 'curved', 'front', 'panel')

    def build(self):
        axis=24
        symmetric(self,'outline',(axis,8),[('L',(8,8)),('L',(7,16)),('L',(4,40)),('L',(18,40)),('L',(axis,30))])
        self.add_polyline('waistband',(7,16),(16,16),(32,16),(41,16))
        for side in (-1,1):
         x=axis+side*8
         path(self,'panel-'+str(side),(x,16),('L',(x,22)),('B',(axis,30),(x,28),(axis+side*4,30)))
         self.relate('connect','waistband','panel-'+str(side))
         self.relate('connect','outline','panel-'+str(side))
        self.relate('connect','panel--1','panel-1')
        self.relate('connect','outline','waistband')
