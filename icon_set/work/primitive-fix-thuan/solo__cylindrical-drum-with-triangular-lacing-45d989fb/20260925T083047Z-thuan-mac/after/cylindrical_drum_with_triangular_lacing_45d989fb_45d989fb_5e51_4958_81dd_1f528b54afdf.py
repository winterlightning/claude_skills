"""A cylindrical drum with an elliptical head and downward-pointing triangular lacing. Correct the reversed triangle and restore the curved lower body.
Construction: Lucide drum original and atomic-debug: elliptical head, vertical walls and curved bottom.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '45d989fb-5e51-4958-81dd-1f528b54afdf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cylindrical-drum-with-triangular-lacing-45d989fb/20260925T083047Z-thuan-mac/reference/drum_45d989fb-5e51-4958-81dd-1f528b54afdf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cylindrical-drum-with-triangular-lacing-45d989fb'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cylindrical', 'drum', 'with', 'triangular', 'lacing', '45d989fb')

    exception = {'reason': 'Retain the drum’s elliptical head, upper rim band and downward lacing triangle. Local roughly two-unit rim openings remain clear in both themes; the narrow lower rim was omitted for clarity.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '8150edafe761a5da1f1c70f5a432bd2d19317ec49a087cfd829b7580332c318a'}

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

        path('head',(6,12),[('A',(42,12),18,6,True),('A',(6,12),18,6,True)],True)
        path('body',(6,12),[('L',(6,20)),('L',(6,36)),('A',(42,36),18,6,False),('L',(42,20)),('L',(42,12))]);join('head','body')
        path('band',(6,20),[('C',(14,23),(8,22),(11,23)),('C',(24,24),(18,24),(21,24)),('C',(34,23),(27,24),(30,24)),('C',(42,20),(37,23),(40,22))]);join('band','body')
        poly('lacing',(14,23),(24,36),(34,23));join('lacing','band')

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
