"""Open Padlock with Keyhole.

Plan: Rounded body and U shackle on a shared x=24 axis; the open version releases the right end. Centerline extremes (8,4)-(40,44).
Reduction: The small round-headed keyhole is reduced to a round-ended slit. The open shackle has a full 9-unit gap above the body.
Construction reference: Lucide lock-keyhole-open.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03e70f4d-188c-5a94-b816-b2183050a118'
SOURCE_PATH = 'pictographic-primitives/apps/security unlock_03e70f4d-188c-5a94-b816-b2183050a118.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('03e70f4d-188c-5a94-b816-b2183050a118', 'pictographic-primitives/apps/security unlock_03e70f4d-188c-5a94-b816-b2183050a118.svg'),)

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


class OpenPadlockWithKeyhole(Solo48):
    icon_id = 'open-padlock-with-keyhole'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('open', 'padlock', 'with', 'keyhole')

    def build(self):
        _box(self,'body',8,20,40,44,4,attachments=((14,20),(34,20)))
        self.add_line('shackle-left',(14,20),(14,11))
        self.add_arc('shackle-top',(14,11),(34,11),radius_x=10,radius_y=7)
        self.add_contour('shackle','shackle-left','shackle-top')
        self.relate('connect','shackle','body')
        self.add_line('keyhole',(24,29),(24,35))
