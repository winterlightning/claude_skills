"""Person with Round Hat and Bob.
Plan: Centered circular face radius 7, cy=20, bottom=27; body top=31 gives zero ink gap. Mirrored broad shoulders retain a distinct clothing cue. Bounds (8,4)-(40,44).
References: human_ref/user.svg circular face and curved shoulders; Lucide hat-glasses for crown/brim construction.
Reduction: Hair and fine hat details reduced; overall straps and bib retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '1ac68a90-7c63-4cad-abe7-a2d3bfc53212'
SOURCE_PATH = 'pictographic-primitives/avatars/wide hat girl_1ac68a90-7c63-4cad-abe7-a2d3bfc53212.svg'
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


class PersonWithRoundHatAndBob(Solo48):
    icon_id = 'person-with-round-hat-and-bob'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    categories = ('primitives', 'avatars')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'with', 'round', 'hat', 'and', 'bob')

    def build(self):
        path(self,'hat',(8,24),('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,24)))
        self.add_arc('head-top',(17,20),(31,20),radius_x=7)
        self.add_arc('face',(31,20),(17,20),radius_x=7)
        self.add_contour('head','head-top','face',closed=True)

        axis=24
        body_top=20+7+HEAD_BODY_CENTERLINE_GAP
        left=8
        right=48-left
        rx=16-left
        ry=8
        self.add_line('body-left-side',(left,44),(left,body_top+ry))
        self.add_arc('body-left-shoulder',(left,body_top+ry),(16,body_top),radius_x=rx,radius_y=ry)
        self.add_line('body-top',(16,body_top),(24,body_top))
        self.add_line('body-top-right',(24,body_top),(32,body_top))
        self.add_arc('body-right-shoulder',(32,body_top),(right,body_top+ry),radius_x=rx,radius_y=ry)
        self.add_line('body-right-side',(right,body_top+ry),(right,44))
        self.add_contour('body','body-left-side','body-left-shoulder','body-top','body-top-right','body-right-shoulder','body-right-side')
        self.relate('connect','head','body')
        self.add_polyline('body-overalls',(16,body_top),(20,42),(28,42),(32,body_top))
        self.relate('connect','body','body-overalls')
