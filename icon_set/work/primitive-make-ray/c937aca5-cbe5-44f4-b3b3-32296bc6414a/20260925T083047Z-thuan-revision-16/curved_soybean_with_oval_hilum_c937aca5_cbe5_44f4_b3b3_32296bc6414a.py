"""A curved soybean with a diagonally oriented oval hilum. Restore the softly rounded lower-left contour and slanted open interior oval.
Construction: Source-specific kidney silhouette; no useful exact Lucide match.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c937aca5-cbe5-44f4-b3b3-32296bc6414a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-soybean-with-oval-hilum/20260925T083047Z-thuan-mac/reference/soybean_c937aca5-cbe5-44f4-b3b3-32296bc6414a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-soybean-with-oval-hilum'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('curved', 'soybean', 'with', 'oval', 'hilum')

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

        path('bean',(14,42),[('C',(6,32),(8,42),(6,36)),('C',(15,18),(6,26),(11,23)),('C',(23,7),(18,14),(17,10)),('C',(30,6),(25,6),(28,6)),('C',(42,20),(38,6),(42,13)),('C',(14,42),(42,32),(29,42))],True)
        path('hilum',(20,27),[('C',(27,20),(20,24),(24,20)),('C',(30,26),(30,20),(32,23)),('C',(21,30),(28,30),(23,33)),('C',(20,27),(20,29),(20,28))],True)

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
