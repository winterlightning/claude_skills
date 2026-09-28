"""Roman Shade with Horizontal Folds.

Plan: Rectangular fabric with a regular 10-unit horizontal fold series and shared wall nodes. Centerline extremes (8,4)-(40,44).
Reduction: Top rail reduced to the first band; three full-width interior folds retained.
Construction reference: Lucide blinds.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '38f248b8-c145-582a-9715-7307921c0cec'
SOURCE_PATH = 'pictographic-primitives/building/roman shade open_38f248b8-c145-582a-9715-7307921c0cec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('38f248b8-c145-582a-9715-7307921c0cec', 'pictographic-primitives/building/roman shade open_38f248b8-c145-582a-9715-7307921c0cec.svg'),)

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


class RomanShadeWithHorizontalFolds(Solo48):
    icon_id = 'roman-shade-with-horizontal-folds'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('roman', 'shade', 'with', 'horizontal', 'folds')

    def build(self):
        levels = tuple(4+i*10 for i in range(5))
        for i,y in enumerate(levels):
            self.add_line(f'fold-{i}',(8,y),(40,y))
        for side,x in [('left',8),('right',40)]:
            for i,(a,b) in enumerate(zip(levels,levels[1:])):
                name=f'wall-{side}-{i}'
                self.add_line(name,(x,a),(x,b))
                self.relate('connect',name,f'fold-{i}')
                self.relate('connect',name,f'fold-{i+1}')
                if i: self.relate('connect',name,f'wall-{side}-{i-1}')
