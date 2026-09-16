"""Speaker with Woofer Center Cap.

Plan: Single large woofer circle with centered cap in a rounded square cabinet. Extremes (6,6)-(42,42).
Reduction: Upper tweeter is omitted to preserve the defining large woofer and its concentric center cap with open spacing.
Construction reference: Lucide speaker.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ee689c08-d961-4da4-bb3e-4299a3fb2c5f'
SOURCE_PATH = 'pictographic-primitives/audio/speakers_ee689c08-d961-4da4-bb3e-4299a3fb2c5f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ee689c08-d961-4da4-bb3e-4299a3fb2c5f', 'pictographic-primitives/audio/speakers_ee689c08-d961-4da4-bb3e-4299a3fb2c5f.svg'),)

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


class SpeakerWithWooferCenterCap(Solo48):
    icon_id = 'speaker-with-woofer-center-cap'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('speaker', 'with', 'woofer', 'center', 'cap')

    def build(self):
        _box(self,'cabinet',6,6,42,42,4)
        _circle(self,'woofer',24,24,9)
        self.add_dot('center-cap',(24,24))
