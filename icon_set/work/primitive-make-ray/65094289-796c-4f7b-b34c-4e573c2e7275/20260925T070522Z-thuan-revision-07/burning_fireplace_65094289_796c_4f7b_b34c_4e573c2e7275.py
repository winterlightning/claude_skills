"""Fire burning inside a fireplace with projecting mantel and hearth. Restore the architectural surround and an open teardrop flame.
Construction: Source-specific fireplace; no useful exact local Lucide match.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '65094289-796c-4f7b-b34c-4e573c2e7275'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__burning-fireplace/20260925T070522Z-thuan-mac/reference/inglenook_65094289-796c-4f7b-b34c-4e573c2e7275.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'burning-fireplace'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('burning', 'fireplace')

    exception = {'reason': 'Retain projecting mantel and hearth bands. Their two-unit interior slots are clean at native size and distinguish the fireplace from a plain rectangular frame.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '26d187ba2770f8d5d33ab08cc473bfa6e81a89e944a75e8d2f98e61ff2953b16'}

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

        poly('mantel',(6,6),(42,6),(42,12),(38,12),(10,12),(6,12),closed=True)
        poly('hearth',(6,36),(10,36),(38,36),(42,36),(42,42),(6,42),closed=True)
        for x in (10,38):
            line(f'post-{x}',(x,12),(x,36));join(f'post-{x}','mantel');join(f'post-{x}','hearth')
        path('flame',(24,18),[('C',(32,30),(28,22),(32,25)),('C',(24,36),(32,34),(28,36)),('C',(18,30),(20,36),(16,34)),('C',(24,18),(20,27),(23,23))],True);join('flame','hearth')

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
