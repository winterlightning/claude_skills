"""Two church towers flank a gabled nave. Restore roof seams, round window and arched entry; preserve left cross and source asymmetry.
Construction: Source architecture; no useful exact local Lucide match.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c126b7b6-6ab5-4ac1-9509-ac6389196ee7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__berlin-cathedral-reference/20260925T070522Z-thuan-mac/reference/landmark berlin cathedral_c126b7b6-6ab5-4ac1-9509-ac6389196ee7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'berlin-cathedral-reference'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('berlin', 'cathedral', 'reference')

    exception = {'reason': 'Preserve the source church towers, round window and arched doorway. Two-unit side clearances remain visibly open at 48px in light and dark; widening them would erase the architectural bays.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '62433374777b21ae8a93e7c89bf9ff0a9a1df33e034eb509577d1bf97a2d2c44'}

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
        # Shared tower widths leave a wider nave for the door and window.
        poly('outline',(6,42),(6,18),(10,13),(14,18),(14,24),(24,14),(34,24),(34,18),(38,13),(42,18),(42,42),(28,42),(20,42),(6,42))
        for x in (14,34):
            line(f'wall-{x}',(x,24),(x,42));join('outline',f'wall-{x}')
        for l,r in ((6,14),(34,42)):
            line(f'roof-{l}',(l,22),(r,22));join('outline',f'roof-{l}')
        circle('window',24,25,3)
        path('entry',(20,42),[('L',(20,37)),('A',(28,37),4,4,True),('L',(28,42))]);join('entry','outline')
        poly('cross-stem',(10,6),(10,9),(10,13));line('cross-bar',(7,9),(13,9));join('cross-stem','cross-bar');join('cross-stem','outline')

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
