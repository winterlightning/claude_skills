"""Chef toque above a mirrored curled moustache. Restore the outlined moustache lobes rather than a shallow wavy stroke.
Construction: Lucide chef-hat original and atomic-debug: three lobes over a cuff. human_ref/user.svg inspected; no head or torso in this symbol.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '61b954c0-9ee8-4b2b-b3e2-f4636524a669'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chef-hat-with-mustache/20260925T070522Z-thuan-mac/reference/chef gear hat moustache_61b954c0-9ee8-4b2b-b3e2-f4636524a669.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chef-hat-with-mustache'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('chef', 'hat', 'with', 'mustache')

    exception = {'reason': 'Retain the toque cuff with its clean two-unit slot and the open curled moustache. Pleats were removed to keep the hat and hair legible at native size.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '3bdd107e829427ec6a8661d941a5c24d9d35ffd0fc5377ef1a8474a09a4321b7'}

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

        path('hat',(10,19),[('C',(6,13),(7,18),(6,16)),('C',(16,9),(6,7),(12,6)),('C',(24,6),(18,6),(20,6)),('C',(32,9),(28,6),(30,6)),('C',(42,13),(36,6),(42,7)),('C',(38,19),(42,16),(41,18)),('L',(38,25)),('L',(10,25)),('L',(10,19))],True)
        line('cuff',(10,19),(38,19));join('cuff','hat')
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            path(f'moustache-{side}',p(0,36),[('C',p(10,36),p(3,33),p(7,33)),('C',p(18,34),p(14,39),p(16,36)),('C',p(8,42),p(18,40),p(13,42)),('C',p(0,36),p(4,42),p(1,39))],True)
        join('moustache--1','moustache-1')

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
