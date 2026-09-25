"""Robot Head with Pointed Chin.

Plan: Symmetric dome flows into vertical cheeks, deliberate jaw corners and a tangent-continuous circular chin. Centerline extremes (8,4)-(40,44).
Reduction: Capsule eyes become round-ended bars and small ear boxes are omitted.
Construction reference: Lucide bot.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd5af8b0d-da9b-5cd5-a276-0347c1c82f1e'
SOURCE_PATH = 'pictographic-primitives/artificial-intelligence/robot head_d5af8b0d-da9b-5cd5-a276-0347c1c82f1e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('d5af8b0d-da9b-5cd5-a276-0347c1c82f1e', 'pictographic-primitives/artificial-intelligence/robot head_d5af8b0d-da9b-5cd5-a276-0347c1c82f1e.svg'),)

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


class RobotHeadWithPointedChin(Solo48):
    icon_id = 'robot-head-with-pointed-chin'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'artificial-intelligence'
    categories = ('artificial-intelligence', 'primitives')
    aliases = ()
    keywords = ('robot', 'head', 'with', 'pointed', 'chin')

    def build(self):
        self.add_arc('crown-left',(8,20),(24,4),radius_x=16)
        self.add_arc('crown-right',(24,4),(40,20),radius_x=16)
        self.add_line('cheek-right',(40,20),(40,26))
        self.add_line('jaw-right',(40,26),(28,42))
        self.add_arc('chin',(28,42),(20,42),radius_x=5)
        self.add_line('jaw-left',(20,42),(8,26))
        self.add_line('cheek-left',(8,26),(8,20))
        self.add_contour('head','crown-left','crown-right','cheek-right','jaw-right','chin','jaw-left','cheek-left',closed=True)
        for i,x in enumerate((18,30)):
            self.add_line(f'eye-{i}',(x,20),(x,25))
