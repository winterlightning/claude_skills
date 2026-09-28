"""Launching Rocket.

Plan: Symmetric pointed hull, window and swept fins above a pointed exhaust. Extremes (8,4)-(40,44).
Reduction: Two launch trails are omitted; circular window, swept fins and the attached pointed exhaust preserve the launch subject.
Construction reference: Lucide rocket.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e0a806b8-a1ad-489e-a872-c6a7caf3c71f'
SOURCE_PATH = 'pictographic-primitives/business/startup launch_e0a806b8-a1ad-489e-a872-c6a7caf3c71f.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('e0a806b8-a1ad-489e-a872-c6a7caf3c71f', 'pictographic-primitives/business/startup launch_e0a806b8-a1ad-489e-a872-c6a7caf3c71f.svg'),)

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


class LaunchingRocket(Solo48):
    icon_id = 'launching-rocket'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('launching', 'rocket')

    def build(self):
        self.add_arc('nose-right',(24,4),(36,28),radius_x=30)
        pts=[(36,28),(36,30),(40,36),(31,36),(17,36),(8,36),(12,30),(12,28)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_line(f'body-{i}',a,b)
        self.add_arc('nose-left',(12,28),(24,4),radius_x=30)
        self.add_contour('hull','nose-right',*[f'body-{i}' for i in range(7)],'nose-left',closed=True)
        _circle(self,'window',24,23,3)
        self.add_polyline('flame',(17,36),(24,44),(31,36))
        self.relate('connect','flame','hull')
