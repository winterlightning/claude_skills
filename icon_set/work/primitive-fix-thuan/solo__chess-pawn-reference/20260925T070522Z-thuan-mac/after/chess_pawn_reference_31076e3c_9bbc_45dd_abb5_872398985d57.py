"""A chess pawn with a round head, curved taper and broad base. Replace angular waist with concave curves and restore the collar.
Construction: Source-specific pawn; no useful exact local Lucide match.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '31076e3c-9bbc-45dd-abb5-872398985d57'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chess-pawn-reference/20260925T070522Z-thuan-mac/reference/chess pawn 1_31076e3c-9bbc-45dd-abb5-872398985d57.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chess-pawn-reference'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('chess', 'pawn', 'reference')

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
        # Head's cardinal apex is exactly y=4. Shared neck and base nodes.
        path('pawn',(18,20),[('C',(15,13),(16,18),(15,16)),('A',(24,4),9,9,True),('A',(33,13),9,9,True),('C',(30,20),(33,16),(32,18)),('L',(29,23)),('C',(34,36),(28,28),(30,32)),('L',(36,36)),('A',(40,40),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,40)),('A',(12,36),4,4,True),('L',(14,36)),('C',(19,23),(18,32),(20,28)),('L',(18,20))],True)
        line('collar',(19,23),(29,23));join('collar','pawn')
        line('base-seam',(14,36),(34,36));join('base-seam','pawn')

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
