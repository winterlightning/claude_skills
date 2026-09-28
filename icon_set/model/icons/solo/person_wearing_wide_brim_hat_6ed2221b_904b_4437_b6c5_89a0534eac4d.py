"""Person Wearing Wide-Brim Hat.
Plan: Centered circular face radius 8, cy=18, bottom=26; body top=30 gives zero ink gap. Mirrored broad shoulders retain a distinct clothing cue. Bounds (6,6)-(42,42).
References: human_ref/user.svg circular face and curved shoulders; Lucide hat-glasses for crown/brim construction.
Reduction: Hair and fine hat details reduced; V-neck retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '6ed2221b-904b-4437-b6c5-89a0534eac4d'
SOURCE_PATH = 'pictographic-primitives/avatars/wide hat girl_6ed2221b-904b-4437-b6c5-89a0534eac4d.svg'
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


class PersonWearingWideBrimHat(Solo48):
    icon_id = 'person-wearing-wide-brim-hat'
    keyshape = Keyshape.SQUARE
    category = 'avatars'
    categories = ('primitives', 'avatars')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'wearing', 'wide-brim', 'hat')

    def build(self):
        path(self,'crown',(14,18),('L',(14,16)),('A',(24,6),10,10,True),('A',(34,16),10,10,True),('L',(34,18)))
        self.add_polyline('brim',(6,18),(14,18),(16,18),(32,18),(34,18),(42,18))
        self.add_arc('face',(16,18),(32,18),radius_x=8,sweep=False)
        self.relate('connect','crown','brim')
        self.relate('connect','brim','face')

        axis=24
        body_top=18+8+HEAD_BODY_CENTERLINE_GAP
        left=6
        right=48-left
        rx=16-left
        ry=10
        self.add_line('body-left-side',(left,42),(left,body_top+ry))
        self.add_arc('body-left-shoulder',(left,body_top+ry),(16,body_top),radius_x=rx,radius_y=ry)
        self.add_line('body-top',(16,body_top),(24,body_top))
        self.add_line('body-top-right',(24,body_top),(32,body_top))
        self.add_arc('body-right-shoulder',(32,body_top),(right,body_top+ry),radius_x=rx,radius_y=ry)
        self.add_line('body-right-side',(right,body_top+ry),(right,42))
        self.add_contour('body','body-left-side','body-left-shoulder','body-top','body-top-right','body-right-shoulder','body-right-side')
        self.relate('connect','face','body')
        self.add_polyline('body-neckline',(16,body_top),(24,42),(32,body_top))
        self.relate('connect','body','body-neckline')
