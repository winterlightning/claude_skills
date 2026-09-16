"""Medical Worker with Cap and Mask.
Plan: Circular face centered (24,20), radius 8; face bottom 28, shoulder top 32, zero painted gap. Hair structure and body cue plain derive from source; mirrored except side part. Bounds (8,4)-(40,44).
References: human_ref/user.svg circular jaw and smooth shoulders; Lucide user open rounded bust.
Reduction: Cap badge reduced to a short mark; mask uses the lower circular face and cap-edge boundary; fine hair and seams omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'd5311768-f441-4f6d-b961-865f42bc5a69'
SOURCE_PATH = 'pictographic-primitives/avatars/woman doctor_d5311768-f441-4f6d-b961-865f42bc5a69.svg'
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

class MedicalWorkerWithCapAndMask(Solo48):
    icon_id = 'medical-worker-with-cap-and-mask'
    keyshape = Keyshape.VRECT_L
    category = 'avatars'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    aliases = ()
    keywords = ('medical', 'worker', 'with', 'cap', 'and', 'mask')
    def build(self):
        path(self,'cap',(8,20),('L',(8,10)),('A',(14,4),6,6,True),('L',(34,4)),('A',(40,10),6,6,True),('L',(40,20)),('L',(32,20)),('L',(16,20)),('L',(8,20)),closed=True)
        self.add_arc('face',(32,20),(16,20),radius_x=8)
        self.relate('connect','cap','face')
        self.add_line('cap-mark',(24,4),(24,8))

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
        self.relate('connect','cap-mark','cap')
