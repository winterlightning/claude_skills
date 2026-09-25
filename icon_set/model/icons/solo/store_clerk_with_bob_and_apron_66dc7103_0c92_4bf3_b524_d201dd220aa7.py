"""Store Clerk with Bob and Apron.
Plan: Centered circular face (24,18), radius 10; face bottom 28; shoulder top 32; zero visible contact. Hair and rounded shoulders fit (8,4)-(40,44).
References: human_ref/user.svg circular jaw and smooth shoulders; Lucide user open rounded bust.
Reduction: Facial microdetails and neck seams omitted; source hairstyle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = '66dc7103-0c92-4bf3-b524-d201dd220aa7'
SOURCE_PATH = 'pictographic-primitives/avatars/woman store clerk_66dc7103-0c92-4bf3-b524-d201dd220aa7.svg'
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

class StoreClerkWithBobAndApron(Solo48):
    icon_id = 'store-clerk-with-bob-and-apron'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    categories = ('primitives', 'avatars')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('store', 'clerk', 'with', 'bob', 'and', 'apron')
    def build(self):
        self.add_arc('crown',(14,18),(34,18),radius_x=10,radius_y=14)
        self.add_arc('face',(34,18),(14,18),radius_x=10)
        self.relate('connect','crown','face')
        for side in (-1,1):
         x=24+side*10
         path(self,'hair-'+str(side),(x,18),('B',(24+side*16,24),(x+side*4,19),(24+side*16,21)))
         self.relate('connect','hair-'+str(side),'face')
         self.relate('connect','hair-'+str(side),'crown')
        path(self,'fringe',(14,18),('B',(24, 12),(19,18),(22,15)),('B',(34,18),(26,15),(29,18)))
        self.relate('connect','fringe','crown')
        self.relate('connect','fringe','face')

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
        self.add_polyline('body-apron',(16,body_top),(16,40),(32,40),(32,body_top))
        self.relate('connect','body-top','body-apron')
        self.relate('connect','body-top-right','body-apron')

