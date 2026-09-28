"""Security Shield with Four Network Nodes.

Plan: Central shield with intrinsic vertical division, four mirrored circular nodes and diagonal links. Centerline extremes (6,6)-(42,42).
Reduction: Small hexagonal nodes become circles; four real network connections and the divided shield remain.
Construction reference: Lucide shield.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19688650-b71a-496a-9e4f-98211e2e851e'
SOURCE_PATH = 'pictographic-primitives/apps/security hub shield_19688650-b71a-496a-9e4f-98211e2e851e.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('19688650-b71a-496a-9e4f-98211e2e851e', 'pictographic-primitives/apps/security hub shield_19688650-b71a-496a-9e4f-98211e2e851e.svg'),)

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


class SecurityShieldWithFourNetworkNodes(Solo48):
    icon_id = 'security-shield-with-four-network-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'apps'
    categories = ('apps', 'primitives')
    aliases = ()
    keywords = ('security', 'shield', 'with', 'four', 'network', 'nodes')

    def build(self):
        axis=24
        self.add_polyline('shield',(16,16),(axis,14),(32,16),(32,26),(axis,34),(16,26),closed=True)
        self.add_line('division',(axis,14),(axis,34))
        self.relate('connect','division','shield')
        for side,x,shield_x in [('left',8,16),('right',40,32)]:
            for level,cy,start_y,join_y in [('top',8,10,16),('bottom',40,38,26)]:
                name=f'{side}-{level}'
                _circle(self,name+'-node',x,cy,2)
                self.add_line(name+'-link',(x,start_y),(shield_x,join_y))
                self.relate('connect',name+'-link',name+'-node')
                self.relate('connect',name+'-link','shield')
