"""Person with Center-Parted Hair.
Plan: Circular face centered (24,14), radius 10; face bottom 24, shoulder top 28, zero painted gap. Hair structure and body cue plain derive from source; mirrored except side part. Bounds (8,4)-(40,44).
References: human_ref/user.svg circular jaw and smooth shoulders; Lucide user open rounded bust.
Reduction: Facial microdetails and neck seams omitted; source hairstyle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '194e0c8a-520e-4ab3-9a3e-2d1ab17a737a'
SOURCE_PATH = 'pictographic-primitives/avatars/woman_194e0c8a-520e-4ab3-9a3e-2d1ab17a737a.svg'
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

class PersonWithCenterPartedHair(Solo48):
    icon_id = 'person-with-center-parted-hair'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'with', 'center-parted', 'hair')
    def build(self):
        self.add_arc('crown',(14,14),(34,14),radius_x=10)
        self.add_arc('face',(34,14),(14,14),radius_x=10)
        self.relate('connect','crown','face')
        for side in (-1,1):
         x=24+side*10
         self.add_line('hair-'+str(side),(x,14),(24+side*14,24))
         self.relate('connect','hair-'+str(side),'face')
         self.relate('connect','hair-'+str(side),'crown')
        path(self,'fringe',(14,14),('B',(24,9),(19,14),(22,12)),('B',(34,14),(26,12),(29,14)))
        self.relate('connect','fringe','crown')
        self.relate('connect','fringe','face')

        body_top=24+HEAD_BODY_CENTERLINE_GAP
        path(self,'body',(8,44),('L',(8,body_top+8)),('A',(16,body_top),8,8,True))
        self.add_line('body-top',(16,body_top),(24,body_top))
        self.add_line('body-top-right',(24,body_top),(32,body_top))
        path(self,'body-right',(32,body_top),('A',(40,body_top+8),8,8,True),('L',(40,44)))
        self.relate('connect','body','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
