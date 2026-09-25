"""A crowned chess piece with circular finial, collar, tapered stem and rounded base. Restore the missing stem so the crown reads as a chess piece.
Construction: Source-specific chess piece; no useful exact Lucide match.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1ec83c77-fb81-4fbb-9d48-20b45ebca8b3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crowned-chess-queen/20260925T083047Z-thuan-mac/reference/chess king_1ec83c77-fb81-4fbb-9d48-20b45ebca8b3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crowned-chess-queen'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('crowned', 'chess', 'queen')

    def build(self):

        def path(name, start, commands, closed=False):
            here, members = start, []
            for j, (kind, end, *a) in enumerate(commands):
                ident = f'{name}-{j}'
                if kind == 'L': self.add_line(ident, here, end)
                elif kind == 'A': self.add_arc(ident, here, end, radius_x=a[0], radius_y=a[1], sweep=a[2], large_arc=a[3] if len(a)>3 else False)
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

        circle('finial',24,7,3)
        path('crown',(16,24),[('L',(10,14)),('C',(14,13),(9,10),(12,11)),('L',(18,16)),('L',(24,10)),('L',(30,16)),('L',(34,13)),('C',(38,14),(36,11),(39,10)),('L',(32,24))]);join('finial','crown')
        rect('collar',14,24,34,30,2);join('crown','collar')
        path('stem-left',(18,30),[('C',(14,38),(18,33),(16,36))]);path('stem-right',(30,30),[('C',(34,38),(30,33),(32,36))]);join('stem-left','collar');join('stem-right','collar')
        path('base',(12,38),[('L',(14,38)),('L',(34,38)),('L',(36,38)),('A',(40,42),4,4,True),('L',(40,44)),('L',(8,44)),('L',(8,42)),('A',(12,38),4,4,True)],True);join('base','stem-left');join('base','stem-right')

        from icon_set.model.primitives import Line
        from dataclasses import replace
        endpoints={p.start for p in self.primitives}|{p.end for p in self.primitives}
        replacements,rebuilt={},[]
        for primitive in self.primitives:
            if isinstance(primitive,Line) and primitive.start!=primitive.end:
                a,b=primitive.start,primitive.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in endpoints if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b];names=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        name=f'{primitive.element_id}-node-{j}';rebuilt.append(Line(name,u,v));names.append(name)
                    replacements[primitive.element_id]=names
                    if not any(primitive.element_id in c.members for c in self.contours):self.add_contour(primitive.element_id,*names)
                    continue
            rebuilt.append(primitive)
        if replacements:
            self.primitives[:]=rebuilt
            self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in replacements.get(m,[m]))) for c in self.contours]
