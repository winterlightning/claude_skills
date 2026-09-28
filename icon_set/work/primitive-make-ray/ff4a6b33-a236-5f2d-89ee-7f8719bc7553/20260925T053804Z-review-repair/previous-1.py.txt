"""Person with Hair Swept Behind Ears.
Plan: Centered circular face (24,18), radius 10; face bottom 28; shoulder top 32; zero visible contact. Hair and rounded shoulders fit (8,4)-(40,44).
References: human_ref/user.svg circular jaw and smooth shoulders; Lucide user open rounded bust.
Reduction: Ear bowls join the circular jaw as one open facial outline; redundant side walls and neck seams omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'ff4a6b33-a236-5f2d-89ee-7f8719bc7553'
SOURCE_PATH = 'pictographic-primitives/avatars/woman_ff4a6b33-a236-5f2d-89ee-7f8719bc7553.svg'
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

class PersonWithHairSweptBehindEars(Solo48):
    icon_id = 'person-with-hair-swept-behind-ears'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('person', 'with', 'hair', 'swept', 'behind', 'ears')
    def build(self):

        self.add_arc('crown',(14,18),(34,18),radius_x=10,radius_y=14)
        path(self,'ear-right',(34,18),('B',(40,18),(34,13),(40,13)),('B',(32,24),(40,24),(36,24)))
        self.add_arc('face',(32,24),(16,24),radius_x=10)
        path(self,'ear-left',(16,24),('B',(8,18),(12,24),(8,24)),('B',(14,18),(8,13),(14,13)))
        self.relate('connect','crown','ear-right')
        self.relate('connect','face','ear-right')
        self.relate('connect','face','ear-left')
        self.relate('connect','crown','ear-left')
        path(self,'fringe',(14,18),('B',(24,12),(19,18),(22,15)),('B',(34,18),(26,15),(29,18)))
        self.relate('connect','fringe','crown')
        self.relate('connect','fringe','ear-left')
        self.relate('connect','fringe','ear-right')

        body_top=28+HEAD_BODY_CENTERLINE_GAP
        path(self,'body',(8,44),('L',(8,body_top+8)),('A',(16,body_top),8,8,True))
        self.add_line('body-top',(16,body_top),(24,body_top))
        self.add_line('body-top-right',(24,body_top),(32,body_top))
        path(self,'body-right',(32,body_top),('A',(40,body_top+8),8,8,True),('L',(40,44)))
        self.relate('connect','body','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')

