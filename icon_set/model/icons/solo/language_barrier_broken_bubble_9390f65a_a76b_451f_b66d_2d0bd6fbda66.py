"""Speech bubble with a lightning crack and lower-left tail. Restore a tall bubble and a sharper coherent crack; rounded outer corners.
Construction: Lucide mail informs rounded enclosure construction; source defines crack and tail.
Fresh standalone revision; original preserved.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9390f65a-a76b-451f-b66d-2d0bd6fbda66'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broken-speech-bubble-batch-003/20260925T070522Z-thuan-mac/reference/language barrier broken bubble_9390f65a-a76b-451f-b66d-2d0bd6fbda66.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broken-speech-bubble-solo-b003-03-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "chat"
    categories = ("primitives", "chat")
    aliases = ()
    keywords = ('broken', 'speech', 'bubble', 'batch', '003')

    exception = {'reason': 'Retain the defining lightning-shaped crack. Its 2.3-unit local opening remains visible in both themes; no profile or stroke change.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '6944bddd736abdfb3be026b1307312ad979148fff24c072630f83faf4ac6e8da'}

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

        path('bubble',(10,6),[('L',(21,6)),('L',(25,13)),('L',(21,17)),('L',(31,28)),('L',(28,17)),('L',(32,14)),('L',(29,6)),('L',(38,6)),('A',(42,10),4,4,True),('L',(42,32)),('A',(38,36),4,4,True),('L',(24,36)),('L',(14,42)),('L',(14,36)),('L',(10,36)),('A',(6,32),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)

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
