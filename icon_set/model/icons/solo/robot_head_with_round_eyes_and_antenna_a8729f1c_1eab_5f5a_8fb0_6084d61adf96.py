"""Robot Head with Round Eyes and Antenna.

Plan: Head rounded rectangle owns paired eyes and ear rods about x=24; antenna joins its top midpoint. Centerline extremes (4,8)-(44,40).
Reduction: Circular eyes and antenna tip become round marks; ears become short rods to avoid tiny rectangular holes.
Construction reference: Lucide bot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8729f1c-1eab-5f5a-8fb0-6084d61adf96'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot head_a8729f1c-1eab-5f5a-8fb0-6084d61adf96.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('a8729f1c-1eab-5f5a-8fb0-6084d61adf96', 'pictographic-primitives/artificial-intelligence/robot head_a8729f1c-1eab-5f5a-8fb0-6084d61adf96.svg'), ('bb6d85a5-1bcc-5cd4-aa3f-4c9d4c04486f', 'pictographic-primitives/artificial-intelligence/robot head_bb6d85a5-1bcc-5cd4-aa3f-4c9d4c04486f.svg'), ('ccc22d8d-7a89-51c3-b2fa-9a24f23030e0', 'pictographic-primitives/artificial-intelligence/robot head_ccc22d8d-7a89-51c3-b2fa-9a24f23030e0.svg'))

def _circle(icon, name, cx, cy, radius):
    left, right = (cx-radius, cy), (cx+radius, cy)
    icon.add_arc(name+'-upper', left, right, radius_x=radius)
    icon.add_arc(name+'-lower', right, left, radius_x=radius)
    icon.add_contour(name, name+'-upper', name+'-lower', closed=True)


def _box(icon, name, left, top, right, bottom, radius, attachments=()):
    # One rounded rectangle owns all corners and cardinal attachment nodes.
    cx, cy = (left+right)//2, (top+bottom)//2
    points = [(cx,top),(right-radius,top),(right,top+radius),
              (right,cy),(right,bottom-radius),(right-radius,bottom),
              (cx,bottom),(left+radius,bottom),(left,bottom-radius),
              (left,cy),(left,top+radius),(left+radius,top),(cx,top)]
    members = []
    for index, (start,end) in enumerate(zip(points,points[1:])):
        if start == end:
            continue
        member = f'{name}-{index}'
        if index in (1,4,7,10):
            icon.add_arc(member, start, end, radius_x=radius)
        else:
            dx,dy=end[0]-start[0],end[1]-start[1]
            inside=[p for p in attachments if (p[0]-start[0])*dy == (p[1]-start[1])*dx
                    and 0 < (p[0]-start[0])*dx+(p[1]-start[1])*dy < dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-start[0])*dx+(p[1]-start[1])*dy)
            nodes=[start]+inside+[end]
            for j,(a,b) in enumerate(zip(nodes,nodes[1:])):
                part=member+f'-split-{j}'
                icon.add_line(part,a,b)
                members.append(part)
            continue
        members.append(member)
    icon.add_contour(name, *members, closed=True)


class RobotHeadWithRoundEyesAndAntenna(Solo48):
    icon_id = 'robot-head-with-round-eyes-and-antenna'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('robot', 'head', 'with', 'round', 'eyes', 'and', 'antenna')

    def build(self):
        _box(self, 'head', 10, 18, 38, 40, 4)
        for side, x, end in [('left', 10, 4), ('right', 38, 44)]:
            self.add_line('ear-'+side, (x,29), (end,29))
            self.relate('connect', 'head', 'ear-'+side)
        for index, x in enumerate((19,29)):
            self.add_dot(f'eye-{index}', (x,29))
        self.add_line('antenna', (24,8), (24,18))
        self.relate('connect', 'antenna', 'head')
