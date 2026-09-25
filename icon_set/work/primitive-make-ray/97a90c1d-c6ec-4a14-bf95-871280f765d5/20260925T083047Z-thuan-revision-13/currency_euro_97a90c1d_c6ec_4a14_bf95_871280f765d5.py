"""Euro currency sign with two unequal-length crossbars and smooth open terminals. Restore the short flat ends and the shorter lower crossbar.
Construction: Lucide euro original and atomic-debug: coherent curved bowl with unequal parallel bars.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '97a90c1d-c6ec-4a14-bf95-871280f765d5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__currency-euro/20260925T083047Z-thuan-mac/reference/currency euro_97a90c1d-c6ec-4a14-bf95-871280f765d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'currency-euro'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('currency', 'euro')

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

        path('curve',(40,4),[('L',(34,4)),('C',(18,20),(24,4),(18,12)),('C',(18,28),(18,23),(18,25)),('C',(34,44),(18,36),(24,44)),('L',(40,44))])
        poly('upper-bar',(8,20),(18,20),(31,20));poly('lower-bar',(8,28),(18,28),(28,28));join('curve','upper-bar');join('curve','lower-bar')

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
