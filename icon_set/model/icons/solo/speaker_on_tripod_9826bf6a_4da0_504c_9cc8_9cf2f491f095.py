"""Speaker on Tripod.

Plan: Wide rounded cabinet on a central post and three repeated feet. Extremes (6,6)-(42,42).
Reduction: Concentric driver ring reduced to one clear circle; all three tripod feet remain.
Construction reference: Lucide speaker.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9826bf6a-4da0-504c-9cc8-9cf2f491f095'
SOURCE_PATH = 'pictographic-primitives/audio/speaker stand_9826bf6a-4da0-504c-9cc8-9cf2f491f095.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('9826bf6a-4da0-504c-9cc8-9cf2f491f095', 'pictographic-primitives/audio/speaker stand_9826bf6a-4da0-504c-9cc8-9cf2f491f095.svg'),)

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


class SpeakerOnTripod(Solo48):
    icon_id = 'speaker-on-tripod'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('speaker', 'on', 'tripod')

    def build(self):
        _box(self,'cabinet',6,6,42,30,4)
        _circle(self,'driver',24,18,3)
        self.add_polyline('stem',(24,30),(24,38),(24,42))
        self.add_polyline('feet',(10,42),(24,38),(38,42))
        self.relate('connect','stem','cabinet')
        self.relate('connect','stem','feet')
