"""A three-dimensional cube selection marker made from disconnected corner strokes. Restore the three-way upper corners and bottom-center depth edge.
Construction: Lucide cuboid original and atomic-debug: shared three-way face junctions.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '62b1f42d-3c38-4348-8257-06a3dd82d9e9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cube-selection-with-disconnected-edge-corners/20260925T083047Z-thuan-mac/reference/select 3d_62b1f42d-3c38-4348-8257-06a3dd82d9e9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cube-selection-with-disconnected-edge-corners'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cube', 'selection', 'with', 'disconnected', 'edge', 'corners')

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

        poly('top',(19,8),(24,6),(29,8))
        for side in (-1,1):
            p=lambda x,y:(24+side*x,y)
            poly(f'upper-{side}',p(18,22),p(18,16),p(12,12))
            line(f'depth-{side}',p(18,16),p(14,18));join(f'upper-{side}',f'depth-{side}')
            poly(f'lower-{side}',p(18,30),p(18,36),p(13,39))
        poly('center',(18,20),(24,24),(30,20));line('center-v',(24,24),(24,29));join('center','center-v')
        poly('bottom',(19,39),(24,42),(29,39));line('bottom-v',(24,37),(24,42));join('bottom','bottom-v')

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
