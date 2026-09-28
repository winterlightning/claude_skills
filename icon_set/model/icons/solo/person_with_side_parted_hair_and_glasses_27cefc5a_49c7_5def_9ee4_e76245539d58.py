"""Person with Side-Parted Hair and Glasses.
Plan: Circular face centered (24,18), radius 14; face bottom 32, shoulder top 36, zero painted gap. Hair structure and body cue plain derive from source; mirrored except side part. Bounds (8,4)-(40,44).
References: human_ref/user.svg circular jaw and smooth shoulders; Lucide glasses paired circular lenses.
Reduction: Outer hair layers simplified; round lenses and a short diagonal part retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '27cefc5a-49c7-5def-9ee4-e76245539d58'
SOURCE_PATH = 'pictographic-primitives/avatars/woman glasses_27cefc5a-49c7-5def-9ee4-e76245539d58.svg'
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

class PersonWithSidePartedHairAndGlasses(Solo48):
    icon_id = 'person-with-side-parted-hair-and-glasses'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    categories = ('primitives', 'avatars')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'with', 'side-parted', 'hair', 'and', 'glasses')
    def build(self):
        path(self,'crown',(10,18),('A',(24,4),14,14,True),('A',(38,18),14,14,True))
        self.add_arc('face',(38,18),(10,18),radius_x=14)
        self.relate('connect','crown','face')
        for side in (-1,1):
         cx=24+side*10
         circle(self,'lens-'+str(side),cx,18,4)
         self.relate('connect','lens-'+str(side),'face')
         self.relate('connect','lens-'+str(side),'crown')
        self.add_line('bridge',(18,18),(30,18))
        self.relate('connect','bridge','lens--1')
        self.relate('connect','bridge','lens-1')
        self.add_line('part',(24,4),(28,8))
        self.relate('connect','part','crown')
        body_top=32+HEAD_BODY_CENTERLINE_GAP
        path(self,'body',(8,44),('L',(8,body_top+8)),('A',(16,body_top),8,8,True))
        self.add_line('body-top',(16,body_top),(24,body_top))
        self.add_line('body-top-right',(24,body_top),(32,body_top))
        path(self,'body-right',(32,body_top),('A',(40,body_top+8),8,8,True),('L',(40,44)))
        self.relate('connect','body','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
