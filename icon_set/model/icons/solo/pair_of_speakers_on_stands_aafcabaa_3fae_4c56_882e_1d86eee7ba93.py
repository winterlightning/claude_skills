"""Pair of Speakers on Stands.

Plan: Two cabinets share dimensions, driver offsets, posts and feet. Extremes (4,8)-(44,40).
Reduction: Driver rings become round marks so both two-driver cabinets and full stands remain legible.
Construction reference: Lucide speaker.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aafcabaa-3fae-4c56-882e-1d86eee7ba93'
SOURCE_PATH = 'pictographic-primitives/audio/speakers stand_aafcabaa-3fae-4c56-882e-1d86eee7ba93.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('aafcabaa-3fae-4c56-882e-1d86eee7ba93', 'pictographic-primitives/audio/speakers stand_aafcabaa-3fae-4c56-882e-1d86eee7ba93.svg'),)

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


class PairOfSpeakersOnStands(Solo48):
    icon_id = 'pair-of-speakers-on-stands'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('pair', 'of', 'speakers', 'on', 'stands')

    def build(self):
        for n,cx in enumerate((12,36)):
            name=f'speaker-{n}'
            self.add_polyline(name,(cx-8,8),(cx+8,8),(cx+8,32),(cx,32),(cx-8,32),closed=True)
            for i,y in enumerate((16,24)):self.add_dot(f'{name}-driver-{i}',(cx,y))
            self.add_line(name+'-post',(cx,32),(cx,40))
            self.add_polyline(name+'-foot',(cx-8,40),(cx,40),(cx+8,40))
            self.relate('connect',name,name+'-post')
            self.relate('connect',name+'-post',name+'-foot')
