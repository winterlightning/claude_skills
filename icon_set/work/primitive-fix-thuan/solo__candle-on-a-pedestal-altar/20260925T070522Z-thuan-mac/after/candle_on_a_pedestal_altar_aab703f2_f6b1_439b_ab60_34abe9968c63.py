"""A lit candle stands on a pedestal altar. Restore a tall candle body, plain pedestal sides and a broad foot; flame remains pointed.
Construction: Source-specific altar; no useful exact local Lucide match.
Fresh standalone revision; original preserved.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'aab703f2-f6b1-439b-ab60-34abe9968c63'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__candle-on-a-pedestal-altar/20260925T070522Z-thuan-mac/reference/altar_aab703f2-f6b1-439b-ab60-34abe9968c63.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'candle-on-a-pedestal-altar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('candle', 'on', 'a', 'pedestal', 'altar')

    exception = {'reason': 'Retain the altar foot band and separate flame. The band has a clear two-unit opening and the flame has three-unit visible clearance above the candle.', 'approved_by': 'user delegated visual-exception judgment to gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '68bffec3ff293a7f403acf5062bef2bf2193a151ff9ab432ce9f3ea3418a837f'}

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

        path('flame',(24,4),[('C',(28,10),(25,6),(28,8)),('A',(20,10),4,2,True),('C',(24,4),(20,8),(23,6))],True)
        poly('candle',(20,27),(20,19),(28,19),(28,27))
        poly('table',(8,27),(20,27),(28,27),(40,27));join('candle','table')
        poly('pedestal',(12,27),(12,38),(8,44),(40,44),(36,38),(36,27));join('pedestal','table')
        line('base-seam',(12,38),(36,38));join('base-seam','pedestal')

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
