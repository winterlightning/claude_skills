"""Construction Worker with Bob and Overalls.
Plan: Centered circular face radius 8, cy=18, bottom=26; body top=30 gives zero ink gap. Mirrored broad shoulders retain a distinct clothing cue. Bounds (8,4)-(40,44).
References: human_ref/user.svg circular face and curved shoulders; Lucide hard-hat for crown/brim construction.
Reduction: Hair and fine hat details reduced; overall straps and bib retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '9b4d94cd-89d5-4be3-9389-31e23612ec7c'
SOURCE_PATH = 'pictographic-primitives/avatars/woman construction_9b4d94cd-89d5-4be3-9389-31e23612ec7c.svg'
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


class ConstructionWorkerWithBobAndOveralls(Solo48):
    icon_id = 'construction-worker-with-bob-and-overalls'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    categories = ('primitives', 'avatars')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('construction', 'worker', 'with', 'bob', 'and', 'overalls')

    def build(self):
        path(self,'helmet',(8,18),('A',(24,4),16,14,True),('A',(40,18),16,14,True))
        self.add_polyline('brim',(8,18),(16,18),(32,18),(40,18))
        self.add_line('ridge',(24,4),(24,10))
        self.add_arc('face',(16,18),(32,18),radius_x=8,sweep=False)
        self.relate('connect','helmet','ridge')
        self.relate('connect','helmet','brim')
        self.relate('connect','brim','face')
        for side in (-1,1):
         x=24+side*16
         self.add_line('hair-'+str(side),(x,18),(x,24))
         self.relate('connect','hair-'+str(side),'brim')

        axis=24
        body_top=18+8+HEAD_BODY_CENTERLINE_GAP
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
        self.relate('connect','face','body')
        self.add_polyline('body-overalls',(16,body_top),(20,42),(28,42),(32,body_top))
        self.relate('connect','body','body-overalls')
