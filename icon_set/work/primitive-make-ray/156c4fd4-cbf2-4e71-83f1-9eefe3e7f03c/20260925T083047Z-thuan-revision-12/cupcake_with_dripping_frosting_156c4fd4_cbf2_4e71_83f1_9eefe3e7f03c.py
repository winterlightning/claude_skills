"""A cupcake with a domed top and uneven dripping icing above a tapered wrapper. Restore multiple rounded drips and retain intentional asymmetry.
Construction: Source-specific frosting; no useful exact local Lucide match.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '156c4fd4-cbf2-4e71-83f1-9eefe3e7f03c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cupcake-with-dripping-frosting/20260925T083047Z-thuan-mac/reference/icing_156c4fd4-cbf2-4e71-83f1-9eefe3e7f03c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cupcake-with-dripping-frosting'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cupcake', 'with', 'dripping', 'frosting')

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

        path('frosting',(10,30),[('C',(6,24),(6,30),(6,27)),('C',(14,14),(6,19),(9,15)),('C',(24,6),(16,8),(20,6)),('C',(34,14),(28,6),(32,8)),('C',(42,24),(39,15),(42,19)),('C',(38,32),(42,28),(40,32)),('C',(32,29),(34,34),(32,32)),('C',(26,29),(32,24),(26,24)),('L',(26,32)),('C',(20,32),(26,37),(20,37)),('L',(20,28)),('C',(14,28),(20,24),(14,24)),('C',(10,30),(14,30),(12,30))],True)
        path('wrapper',(10,30),[('L',(13,39)),('C',(17,42),(13,41),(15,42)),('L',(31,42)),('C',(35,39),(33,42),(35,41)),('L',(38,32))]);join('wrapper','frosting')

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
