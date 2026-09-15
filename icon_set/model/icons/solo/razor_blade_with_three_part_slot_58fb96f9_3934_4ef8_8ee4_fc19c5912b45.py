"""Razor Blade with Three-Part Slot.

Plan: A symmetric stepped blade envelope surrounds a regular row of three mounting marks. Centerline extremes (4,8)-(44,40).
Reduction: The narrow connected mounting slot becomes three separated round marks; stepped blade ends preserve recognition. No useful exact Lucide blade match was found.
Construction reference: Lucide scissors (simple cutting-tool vocabulary only).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58fb96f9-3934-4ef8-8ee4-fc19c5912b45'
SOURCE_PATH = 'pictographic-primitives/beauty/shave_58fb96f9-3934-4ef8-8ee4-fc19c5912b45.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('58fb96f9-3934-4ef8-8ee4-fc19c5912b45', 'pictographic-primitives/beauty/shave_58fb96f9-3934-4ef8-8ee4-fc19c5912b45.svg'),)

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


class RazorBladeWithThreePartSlot(Solo48):
    icon_id = 'razor-blade-with-three-part-slot'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    aliases = ()
    keywords = ('razor', 'blade', 'with', 'three-part', 'slot')

    def build(self):
        self.add_polyline('blade',(8,8),(40,8),(40,14),(44,14),(44,34),(40,34),(40,40),(8,40),(8,34),(4,34),(4,14),(8,14),closed=True)
        for index,x in enumerate(range(14,35,10)):
            self.add_dot(f'slot-part-{index}',(x,24))
