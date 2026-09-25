"""A rounded coconut drink with a wavy cut band and bent straw. Restore the round shell and repeated small waves instead of one broad S-curve.
Construction: Source-specific coconut; Lucide drum supports coherent curved shell construction.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e56410b3-feae-47c6-986d-ad4b7fd0714d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cut-coconut-bowl-with-wavy-band-and-straw/20260925T083047Z-thuan-mac/reference/coconut_e56410b3-feae-47c6-986d-ad4b7fd0714d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cut-coconut-bowl-with-wavy-band-and-straw'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cut', 'coconut', 'bowl', 'with', 'wavy', 'band', 'and', 'straw')

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

        path('shell',(9,19),[('L',(30,19)),('L',(39,19)),('C',(42,28),(41,22),(42,25)),('C',(24,42),(42,36),(34,42)),('C',(6,28),(14,42),(6,36)),('C',(9,19),(6,25),(7,22))],True)
        path('wave',(6,28),[('C',(13,27),(9,28),(10,27)),('C',(20,31),(16,27),(16,31)),('C',(28,27),(24,31),(24,27)),('C',(36,31),(32,27),(32,31)),('C',(42,28),(39,31),(39,28))]);join('wave','shell')
        path('straw',(30,19),[('L',(33,10)),('C',(40,6),(34,7),(37,6)),('L',(42,6))]);join('straw','shell')

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
