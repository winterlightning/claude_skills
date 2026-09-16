"""Stadium Grandstand with Rising Roof.

Plan: Asymmetric rising canopy uses exact 3-4-5 circular tangent transitions over a repeated rail/post series and rounded platform. Extremes (4,8)-(44,40).
Reduction: Two decorative overhead rays are omitted. Both source IDs map to this shared rising-roof concept.
Construction reference: Lucide landmark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ae1df2fe-c322-457b-b0b0-783874deb9be'
SOURCE_PATH = 'pictographic-primitives/building/stadium 1_ae1df2fe-c322-457b-b0b0-783874deb9be.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('ae1df2fe-c322-457b-b0b0-783874deb9be', 'pictographic-primitives/building/stadium 1_ae1df2fe-c322-457b-b0b0-783874deb9be.svg'), ('0529d2e1-4d9c-4885-b3d2-08e55afe9213', 'pictographic-primitives/building/stadium 3_0529d2e1-4d9c-4885-b3d2-08e55afe9213.svg'))

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


class StadiumGrandstandWithRisingRoof(Solo48):
    icon_id = 'stadium-grandstand-with-rising-roof'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'building'
    aliases = ()
    keywords = ('stadium', 'grandstand', 'with', 'rising', 'roof')

    def build(self):
        _box(self,'platform',4,32,44,40,4,attachments=((16,32),(32,32)))
        self.add_polyline('left-wall',(8,32),(8,24),(8,20))
        self.add_arc('roof-left',(8,20),(12,16),radius_x=4)
        self.add_line('roof-flat',(12,16),(20,16))
        self.add_arc('roof-transition',(20,16),(28,12),radius_x=10,sweep=False)
        self.add_line('roof-rise',(28,12),(32,9))
        self.add_arc('roof-cap',(32,9),(40,13),radius_x=5)
        self.add_polyline('right-wall',(40,13),(40,24),(40,32))
        self.add_contour('roof','roof-left','roof-flat','roof-transition','roof-rise','roof-cap')
        for side in ('left-wall','right-wall'):
            self.relate('connect',side,'roof')
            self.relate('connect',side,'platform')
        self.add_polyline('rail',(4,24),(8,24),(16,24),(32,24),(40,24),(44,24))
        for side in ('left-wall','right-wall'):self.relate('connect','rail',side)
        for n,x in enumerate((16,32)):
            self.add_line(f'post-{n}',(x,24),(x,32))
            self.relate('connect',f'post-{n}','rail')
            self.relate('connect',f'post-{n}','platform')
