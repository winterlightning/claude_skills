"""Magic cauldron with outlined bubble, sparkle, rounded rim and two small feet. Restore a hollow bubble and a visible rim band.
Construction: Source-specific vessel; no useful exact Lucide match.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '72f64d5e-456e-45c1-80a8-12d9cbe19516'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bubbling-magic-cauldron/20260925T070522Z-thuan-mac/reference/witch cauldron_72f64d5e-456e-45c1-80a8-12d9cbe19516.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bubbling-magic-cauldron'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bubbling', 'magic', 'cauldron')

    exception = {'reason': 'Retain the hollow bubble, sparkle and outlined rolled rim. The rim has a readable two-unit slot and emissions have three-unit visible gaps at 48px.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '9e0313b3b0a45196d4228f06783a453b04198f020abd77ff8aba37f58c45698f'}

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

        rect('rim',6,19,42,25,3)
        path('pot',(10,25),[('L',(10,28)),('C',(16,37),(10,32),(12,35)),('C',(24,39),(19,39),(21,39)),('C',(32,37),(27,39),(29,39)),('C',(38,28),(36,35),(38,32)),('L',(38,25))]);join('pot','rim')
        for s in (-1,1):
            line(f'foot-{s}',(24+s*8,37),(24+s*13,42));join(f'foot-{s}','pot')
        circle('bubble',13,9,3)
        poly('spark-v',(34,6),(34,9),(34,12));poly('spark-h',(31,9),(34,9),(37,9));join('spark-v','spark-h')

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
