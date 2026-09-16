"""Doctor with Bob and Stethoscope.
Plan: Centered circular face (24,14), radius 8; face bottom 22; shoulder top 26; zero visible contact. Hair and rounded shoulders fit (8,4)-(40,44).
References: human_ref/user.svg circular jaw and smooth shoulders; Lucide stethoscope curved tubing and chestpiece.
Reduction: Facial microdetails and neck seams omitted; source hairstyle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'de0e311a-2d02-455e-a168-7b93d8b8cdcb'
SOURCE_PATH = 'pictographic-primitives/avatars/woman doctor_de0e311a-2d02-455e-a168-7b93d8b8cdcb.svg'
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

class DoctorWithBobAndStethoscope(Solo48):
    icon_id = 'doctor-with-bob-and-stethoscope'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('doctor', 'with', 'bob', 'and', 'stethoscope')
    def build(self):
        self.add_arc('crown',(16,14),(32,14),radius_x=8,radius_y=10)
        self.add_arc('face',(32,14),(16,14),radius_x=8)
        self.relate('connect','crown','face')
        for side in (-1,1):
         x=24+side*8
         path(self,'hair-'+str(side),(x,14),('B',(24+side*16,20),(x+side*4,15),(24+side*16,17)))
         self.relate('connect','hair-'+str(side),'face')
         self.relate('connect','hair-'+str(side),'crown')
        path(self,'fringe',(16,14),('B',(24, 11),(21,14),(22,13)),('B',(32,14),(26,13),(27,14)))
        self.relate('connect','fringe','crown')
        self.relate('connect','fringe','face')

        body_top=22+HEAD_BODY_CENTERLINE_GAP
        path(self,'body',(8,44),('L',(8,body_top+8)),('A',(16,body_top),8,8,True))
        self.add_line('body-top',(16,body_top),(24,body_top))
        self.add_line('body-top-right',(24,body_top),(32,body_top))
        path(self,'body-right',(32,body_top),('A',(40,body_top+8),8,8,True),('L',(40,44)))
        self.relate('connect','body','body-top')
        self.relate('connect','body-top','body-top-right')
        self.relate('connect','body-top-right','body-right')
        self.relate('connect','face','body-top')
        self.relate('connect','face','body-top-right')
        path(self,'body-stethoscope',(16,26),('L',(16,30)),('A',(24,38),8,8,False),('A',(32,30),8,8,False),('L',(32,26)))
        self.relate('connect','body-stethoscope','body-top')
        self.relate('connect','body-stethoscope','body-top-right')
        self.add_line('body-tail',(24,38),(24,40))
        circle(self,'body-chestpiece',24,42,2)
        self.relate('connect','body-tail','body-stethoscope')
        self.relate('connect','body-tail','body-chestpiece')

