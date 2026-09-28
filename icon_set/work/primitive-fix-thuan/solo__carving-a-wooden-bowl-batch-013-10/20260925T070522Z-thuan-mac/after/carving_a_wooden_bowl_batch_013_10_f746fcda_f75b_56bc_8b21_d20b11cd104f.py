"""A handled carving gouge cuts a bowl beside a curled wood shaving. Restore the visible handle and shaving spiral; omit the tiny bowl foot for a clean bowl silhouette.
Construction: Source-specific craft tool; no useful exact local Lucide match.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'f746fcda-f75b-56bc-8b21-d20b11cd104f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__carving-a-wooden-bowl-batch-013-10/20260925T070522Z-thuan-mac/reference/wood carving bowl_f746fcda-f75b-56bc-8b21-d20b11cd104f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'carving-a-wooden-bowl-batch-013-10'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('carving', 'a', 'wooden', 'bowl', 'batch', '013', '10')

    exception = {'reason': 'Retain the characteristic curling wood shaving and outlined gouge handle. The curl has a readable two-unit local gap; omit the tiny foot to preserve a clean bowl.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'be4fd0d864c256ba677e76cffee35bc3409842c1fc6680255688374714af2b9e'}

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

        path('handle',(6,10),[('A',(10,6),4,4,True),('L',(12,6)),('L',(22,16)),('L',(16,22)),('L',(6,12)),('L',(6,10))],True)
        poly('blade',(19,19),(28,28));join('handle','blade')
        path('bowl',(6,28),[('L',(42,28)),('A',(24,42),18,14,True),('A',(6,28),18,14,True)],True);join('blade','bowl')
        path('shaving',(34,28),[('C',(42,18),(39,26),(42,22)),('C',(36,12),(42,14),(40,12)),('C',(32,18),(32,12),(30,16)),('C',(36,20),(32,20),(35,21))]);join('shaving','bowl')

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
