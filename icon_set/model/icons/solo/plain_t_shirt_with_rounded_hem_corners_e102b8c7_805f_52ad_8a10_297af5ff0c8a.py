"""Plain T-Shirt with Rounded Hem Corners.

Plan: Shared x=24 axis, shallow crew neck, mirrored angled sleeves and rounded hem. Extremes (6,6)-(42,42).
Reduction: Retains the shallow crew neck, angled sleeves and rounded hem; no extra seams.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e102b8c7-805f-52ad-8a10-297af5ff0c8a'
SOURCE_PATH = 'pictographic-primitives/clothes/shirt plain_e102b8c7-805f-52ad-8a10-297af5ff0c8a.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e102b8c7-805f-52ad-8a10-297af5ff0c8a', 'pictographic-primitives/clothes/shirt plain_e102b8c7-805f-52ad-8a10-297af5ff0c8a.svg'),)

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


class PlainTShirtWithRoundedHemCorners(Solo48):
    icon_id = 'plain-t-shirt-with-rounded-hem-corners'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('plain', 't-shirt', 'with', 'rounded', 'hem', 'corners')

    def build(self):
        self.add_arc('neck',(16,6),(32,6),radius_x=8,radius_y=6,sweep=False)
        pts=[(32,6),(38,10),(42,20),(34,24),(34,38)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_line(f'right-{i}',a,b)
        self.add_arc('hem-right',(34,38),(30,42),radius_x=4)
        self.add_line('hem',(30,42),(18,42))
        self.add_arc('hem-left',(18,42),(14,38),radius_x=4)
        pts=[(14,38),(14,24),(6,20),(10,10),(16,6)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_line(f'left-{i}',a,b)
        self.add_contour('shirt','neck',*[f'right-{i}' for i in range(4)],'hem-right','hem','hem-left',*[f'left-{i}' for i in range(4)],closed=True)
