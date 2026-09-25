"""Rounded cheese or nougat block with three differently sized holes and two open edge bites. Restore rounded corners and outlined interior holes.
Construction: Lucide mail original and atomic-debug informs rounded perimeter; source supplies holes and bites.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '55a2bdb7-4453-410a-a7dd-454e6337969d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cheese-block-open-holes/20260925T070522Z-thuan-mac/reference/nougat_55a2bdb7-4453-410a-a7dd-454e6337969d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cheese-block-open-holes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cheese', 'block', 'open', 'holes')

    exception = {'reason': 'Retain three hollow cheese holes and two edge bites. Local two-to-three-unit openings remain clear at 48px in both themes; increasing every gap would discard identifying holes.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '145a65ee86235919d5baf466f1e912c9bf7c3d5e331bd4b94f6229e3eb26c0d3'}

    def build(self):

        def path(name, start, commands, closed=False):
            here, members = start, []
            for j, (kind, end, *a) in enumerate(commands):
                ident = f'{name}-{j}'
                if kind == 'L': self.add_line(ident, here, end)
                elif kind == 'A': self.add_arc(ident, here, end, radius_x=a[0], radius_y=a[1], sweep=a[2])
                elif kind == 'C': self.add_bezier(ident, here, (a[0], a[1], end))
                here = end
                members.append(ident)
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line, poly = self.add_line, self.add_polyline
        def join(a,b): self.relate('connect',a,b)

        path('block',(10,8),[('L',(38,8)),('A',(44,14),6,6,True),('L',(38,14)),('A',(38,22),4,4,False),('L',(44,22)),('L',(44,30)),('A',(40,34),4,4,False),('A',(44,38),4,4,False),('L',(44,40)),('L',(10,40)),('A',(4,34),6,6,True),('L',(4,14)),('A',(10,8),6,6,True)],True)
        circle('hole-top',17,19,4);circle('hole-small',13,31,3);circle('hole-bottom',27,31,3)

        # Split receiving straight runs at actual attachment endpoints.
        # This preserves true T-junctions without adding any clearance waivers.
        from icon_set.model.primitives import Line
        from dataclasses import replace
        endpoints = {p.start for p in self.primitives} | {p.end for p in self.primitives}
        replacements, rebuilt = {}, []
        for primitive in self.primitives:
            if isinstance(primitive, Line) and primitive.start != primitive.end:
                a,b=primitive.start,primitive.end
                dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in endpoints if q not in (a,b) and
                      (q.x-a.x)*dy == (q.y-a.y)*dx and
                      0 < (q.x-a.x)*dx+(q.y-a.y)*dy < dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]
                    names=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        name=f'{primitive.element_id}-node-{j}'
                        rebuilt.append(Line(name,u,v));names.append(name)
                    replacements[primitive.element_id]=names
                    if not any(primitive.element_id in c.members for c in self.contours):
                        self.add_contour(primitive.element_id,*names)
                    continue
            rebuilt.append(primitive)
        if replacements:
            self.primitives[:]=rebuilt
            self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacements.get(m,[m]))) for c in self.contours]
