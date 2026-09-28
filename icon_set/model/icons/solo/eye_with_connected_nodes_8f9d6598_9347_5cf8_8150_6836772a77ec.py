"""Eye with Connected Nodes.

Plan: Mirrored almond lids and four diagonal rays; upper/lower circle nodes connect at real cardinal endpoints. Extremes (6,6)-(42,42).
Reduction: Iris simplified to a pupil; the two linked nodes and four rays remain.
Construction reference: Lucide eye.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8f9d6598-9347-5cf8-8150-6836772a77ec'
SOURCE_PATH = 'pictographic-primitives/business/source tracking_8f9d6598-9347-5cf8-8150-6836772a77ec.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('8f9d6598-9347-5cf8-8150-6836772a77ec', 'pictographic-primitives/business/source tracking_8f9d6598-9347-5cf8-8150-6836772a77ec.svg'),)

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


class EyeWithConnectedNodes(Solo48):
    icon_id = 'eye-with-connected-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('eye', 'with', 'connected', 'nodes')

    def build(self):
        for name,a,b in [('upper-left',(9,24),(24,15)),('upper-right',(24,15),(39,24)),('lower-right',(39,24),(24,33)),('lower-left',(24,33),(9,24))]:
            self.add_arc(name,a,b,radius_x=17)
        self.add_contour('eye','upper-left','upper-right','lower-right','lower-left',closed=True)
        self.add_dot('pupil',(24,24))
        for name,cy,node_y,eye_y in [('top',8,10,15),('bottom',40,38,33)]:
            pts=[(22,cy),(24,cy-2),(26,cy),(24,cy+2)]
            for i,a in enumerate(pts):self.add_arc(f'{name}-{i}',a,pts[(i+1)%4],radius_x=2)
            self.add_contour(name,*[f'{name}-{i}' for i in range(4)],closed=True)
            self.add_line(name+'-link',(24,node_y),(24,eye_y))
            self.relate('connect',name,name+'-link')
            self.relate('connect',name+'-link','eye')
        for sx in (-1,1):
            for sy in (-1,1):self.add_line(f'ray-{sx}-{sy}',(24+sx*18,24+sy*16),(24+sx*14,24+sy*14))
