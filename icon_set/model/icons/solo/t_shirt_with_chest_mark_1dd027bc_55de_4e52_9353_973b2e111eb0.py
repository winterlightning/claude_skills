"""T-Shirt with Chest Mark.

Plan: Rounded shoulders and hem share r4/r8 vocabulary; chest mark is intentionally on the right. Extremes (4,8)-(44,40).
Reduction: Small chest mark kept as a short round-ended stroke; neckline and broad rounded shoulders retained.
Construction reference: Lucide shirt.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1dd027bc-55de-4e52-9353-973b2e111eb0'
SOURCE_PATH = 'pictographic-primitives/clothes/shirt_1dd027bc-55de-4e52-9353-973b2e111eb0.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('1dd027bc-55de-4e52-9353-973b2e111eb0', 'pictographic-primitives/clothes/shirt_1dd027bc-55de-4e52-9353-973b2e111eb0.svg'),)

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


class TShirtWithChestMark(Solo48):
    icon_id = 't-shirt-with-chest-mark'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'clothes'
    categories = ('primitives', 'clothes')
    aliases = ()
    keywords = ('t-shirt', 'with', 'chest', 'mark')

    def build(self):
        self.add_arc('neck',(16,8),(32,8),radius_x=8,sweep=False)
        self.add_line('shoulder-right',(32,8),(36,8))
        self.add_arc('round-right',(36,8),(44,16),radius_x=8)
        pts=[(44,16),(44,22),(36,22),(36,36)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_line(f'right-{i}',a,b)
        self.add_arc('hem-right',(36,36),(32,40),radius_x=4)
        self.add_line('hem',(32,40),(16,40))
        self.add_arc('hem-left',(16,40),(12,36),radius_x=4)
        pts=[(12,36),(12,22),(4,22),(4,16)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_line(f'left-{i}',a,b)
        self.add_arc('round-left',(4,16),(12,8),radius_x=8)
        self.add_line('shoulder-left',(12,8),(16,8))
        self.add_contour('shirt','neck','shoulder-right','round-right',*[f'right-{i}' for i in range(3)],'hem-right','hem','hem-left',*[f'left-{i}' for i in range(3)],'round-left','shoulder-left',closed=True)
        self.add_line('chest-mark',(25,28),(27,28))
