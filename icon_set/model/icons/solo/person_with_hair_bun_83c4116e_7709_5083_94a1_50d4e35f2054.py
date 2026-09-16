"""Person with Hair Bun.
Plan: Circular face center (24,22), radius10; bottom32, shoulders36, zero ink gap. Bun attaches to exact circular crown points (18,14),(30,14). Bounds (8,4)-(40,44).
References: human_ref/user.svg circular jaw and smooth shoulders; Lucide user open rounded bust.
Reduction: Facial microdetails and neck seams omitted; source hairstyle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '83c4116e-7709-5083-94a1-50d4e35f2054'
SOURCE_PATH = 'pictographic-primitives/avatars/woman_83c4116e-7709-5083-94a1-50d4e35f2054.svg'
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

class PersonWithHairBun(Solo48):
    icon_id = 'person-with-hair-bun'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'with', 'hair', 'bun')
    def build(self):

        path(self,'crown',(14,22),('A',(18,14),10,10,True),('A',(24,12),10,10,True),('A',(30,14),10,10,True),('A',(34,22),10,10,True))
        self.add_arc('face',(34,22),(14,22),radius_x=10)
        self.relate('connect','face','crown')
        path(self,'bun',(18,14),('B',(20,4),(16,8),(16,4)),('L',(28,4)),('B',(30,14),(32,4),(32,8)))
        self.relate('connect','bun','crown')
        path(self,'fringe',(14,22),('B',(24,17),(19,22),(22,20)),('B',(34,22),(26,20),(29,22)))
        self.relate('connect','fringe','face')
        self.relate('connect','fringe','crown')

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

