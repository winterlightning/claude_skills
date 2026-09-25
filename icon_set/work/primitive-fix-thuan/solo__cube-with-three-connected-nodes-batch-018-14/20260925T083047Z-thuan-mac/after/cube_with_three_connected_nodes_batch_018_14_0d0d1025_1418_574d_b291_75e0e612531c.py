"""An isometric cube connects to three outlined circular nodes. Restore the hollow nodes and keep the three visible cube faces balanced.
Construction: Lucide cuboid original and atomic-debug: shared face junction and coherent cube boundary.
Fresh SOLO48 revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '0d0d1025-1418-574d-b291-75e0e612531c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cube-with-three-connected-nodes-batch-018-14/20260925T083047Z-thuan-mac/reference/rotate d_0d0d1025-1418-574d-b291-75e0e612531c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cube-with-three-connected-nodes-batch-018-14'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cube', 'with', 'three', 'connected', 'nodes', 'batch', '018', '14')

    exception = {'reason': 'Retain all three hollow nodes and the three-faced cube. Local narrow face and connector openings remain visibly distinct at 48px; the source arrangement is more informative than filled nodes.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'a73bc41cc45ed78a0b2b517267ade52de0c396737b5153ce1bc4375f809fb6d7'}

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

        poly('cube',(24,18),(34,24),(34,30),(24,36),(14,30),(14,24),closed=True)
        poly('faces',(14,24),(24,28),(34,24));line('vertical',(24,28),(24,36));join('cube','faces');join('cube','vertical');join('faces','vertical')
        circle('top-node',24,10,4);line('top-link',(24,14),(24,18));join('top-link','top-node');join('top-link','cube')
        for name,x,a in [('left',10,(14,30)),('right',38,(34,30))]:
            circle(name+'-node',x,38,4);line(name+'-link',a,(x,34));join(name+'-node',name+'-link');join(name+'-link','cube')

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
