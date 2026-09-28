"""Person Using Self-Service Kiosk.

Plan: A circular-headed stick figure reaches to the kiosk on the left. Head(34,10), radius4; actual torso junction(34,22) gives exactly4 ink clearance on the vertical torso axis. Human reference: human_ref/full_body_ref.png. Centerline extremes (6,6)-(42,42).
Reduction: The illustrated body becomes a clear stick figure; screen thickness and small shelf detail are simplified.
Construction reference: Lucide user and hand.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '34fe284a-983c-5003-a20d-a0575899d98f'
SOURCE_PATH = 'pictographic-primitives/business/self service_34fe284a-983c-5003-a20d-a0575899d98f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('34fe284a-983c-5003-a20d-a0575899d98f', 'pictographic-primitives/business/self service_34fe284a-983c-5003-a20d-a0575899d98f.svg'),)

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


class PersonUsingSelfServiceKiosk(Solo48):
    icon_id = 'person-using-self-service-kiosk'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('person', 'using', 'self-service', 'kiosk')

    def build(self):
        _circle(self,'head',34,10,4)
        self.add_line('torso',(34,22),(34,32))
        self.add_polyline('legs',(28,42),(34,32),(42,42))
        self.relate('connect','torso','legs')
        self.add_polyline('arm',(34,22),(28,30),(18,30))
        self.relate('connect','arm','torso')
        self.add_polyline('kiosk',(6,16),(14,16),(18,30),(22,30),(18,42),(6,42),closed=True)
        self.relate('connect','arm','kiosk')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
