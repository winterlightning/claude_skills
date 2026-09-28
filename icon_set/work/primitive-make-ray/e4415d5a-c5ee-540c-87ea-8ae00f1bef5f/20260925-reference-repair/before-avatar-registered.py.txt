"""Person with Bob and V-Neck Shirt.
Plan: Circular face centered (24,22), radius7; bottom29, shoulder top33, zero ink gap. Hair outline follows the source length and part. Whole bounds (8,4)-(40,44).
References: human_ref/user.svg circular jaw and smooth shoulders; Lucide user open rounded bust.
Reduction: Facial microdetails and neck seams omitted; source hairstyle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'e4415d5a-c5ee-540c-87ea-8ae00f1bef5f'
SOURCE_PATH = 'pictographic-primitives/avatars/woman_e4415d5a-c5ee-540c-87ea-8ae00f1bef5f.svg'
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

class PersonWithBobAndVNeckShirt(Solo48):
    icon_id = 'person-with-bob-and-v-neck-shirt'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'with', 'bob', 'and', 'v-neck', 'shirt')
    def build(self):
        path(self,'hair',(8,24),('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,24)))
        path(self,'fringe',(17,22),('B',(24, 15),(20,21),(22,18)),('B',(31,22),(26,18),(28,21)))
        self.add_arc('face',(31,22),(17,22),radius_x=7)
        self.relate('connect','fringe','face')

        body_top=29+HEAD_BODY_CENTERLINE_GAP
        path(self,'body',(8,44),('L',(8,body_top+8)),('A',(12,body_top),4,8,True))
        self.add_line('body-top',(12,body_top),(24,body_top))
        self.add_line('body-top-right',(24,body_top),(36,body_top))
        path(self,'body-right',(36,body_top),('A',(40,body_top+8),4,8,True),('L',(40,44)))
        self.relate('connect','body','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
        self.add_polyline('body-neckline',(12,body_top),(24,44),(36,body_top))
        self.relate('connect','body-top','body-neckline')
        self.relate('connect','body-top-right','body-neckline')

