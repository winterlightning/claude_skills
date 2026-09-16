"""Steel I-Section.

Plan: An I-shaped profile has 8-unit flanges and web with four equal r4 concave fillets. Symmetry axes x=24,y=24. Extremes (6,6)-(42,42).
Reduction: Retains the full section and rounded inside corners; no decorative surface marks.
Construction reference: Lucide construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '113c95bf-86aa-5cf3-bbe6-56293543b99d'
SOURCE_PATH = 'pictographic-primitives/construction/steel_113c95bf-86aa-5cf3-bbe6-56293543b99d.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = (('113c95bf-86aa-5cf3-bbe6-56293543b99d', 'pictographic-primitives/construction/steel_113c95bf-86aa-5cf3-bbe6-56293543b99d.svg'),)

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


class SteelISection(Solo48):
    icon_id = 'steel-i-section'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'construction'
    aliases = ()
    keywords = ('steel', 'i-section')

    def build(self):
        axis=24
        radius=4
        quarter=[('line',(0,-18),(18,-18)),('line',(18,-18),(18,-10)),('line',(18,-10),(8,-10)),('arc',(8,-10),(4,-6)),('line',(4,-6),(4,0))]
        members=[]
        for n,(sx,sy,reverse) in enumerate(((1,1,False),(1,-1,True),(-1,-1,False),(-1,1,True))):
            def p(q):return (axis+sx*q[0],axis+sy*q[1])
            edges=list(reversed(quarter)) if reverse else quarter
            for i,(kind,a,b) in enumerate(edges):
                if reverse:a,b=b,a
                name=f'quarter-{n}-{i}'
                if kind=='arc':self.add_arc(name,p(a),p(b),radius_x=radius,sweep=False)
                else:self.add_line(name,p(a),p(b))
                members.append(name)
        self.add_contour('section',*members,closed=True)
