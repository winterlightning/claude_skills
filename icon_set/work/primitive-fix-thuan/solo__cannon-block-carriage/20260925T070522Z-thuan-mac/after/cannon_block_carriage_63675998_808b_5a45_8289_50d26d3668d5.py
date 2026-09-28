"""A cannon barrel rises above a round carriage wheel and a low support. Restore the long rounded barrel and axle ring.
Construction: Source-specific cannon silhouette; no useful exact Lucide match.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '63675998-808b-5a45-8289-50d26d3668d5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cannon-block-carriage/20260925T070522Z-thuan-mac/reference/modern weapon cannon_63675998-808b-5a45-8289-50d26d3668d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cannon-block-carriage'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cannon', 'block', 'carriage')

    exception = {'reason': 'Retain the round axle ring, barrel-over-wheel arrangement and low carriage. The axle ring has a visible two-unit hole; three-unit radial clearance and localized barrel/carriage spacing remain readable at 48px.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'c03271b17cb3deb3ed5b669aba633b073364d163338d66be928f4b9fa04e195b'}

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
        # End the barrel exactly on the wheel, exposing its front rim.
        path('barrel',(12,30),[('C',(10,21),(8,29),(8,24)),('C',(16,16),(11,18),(13,17)),('L',(44,8)),('L',(44,18)),('L',(30,24))])
        path('wheel',(12,30),[('A',(22,20),10,10,True),('A',(30,24),10,10,True),('A',(32,30),10,10,True),('A',(22,40),10,10,True),('A',(12,30),10,10,True)],True);join('wheel','barrel')
        circle('axle',22,30,3)
        poly('carriage',(12,30),(4,35),(4,40),(22,40));join('wheel','carriage');join('barrel','carriage')

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
