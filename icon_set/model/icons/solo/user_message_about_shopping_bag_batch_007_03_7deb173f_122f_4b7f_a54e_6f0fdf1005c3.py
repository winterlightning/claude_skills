"""User Message About Shopping Bag.
Plan: Shopping bag with broad arched handle inside open speech outline; separate continuous face profile. No detached head/body pair.
Construction reference: Lucide panels-top-left; independently solved SOLO48 geometry.
Source copy inspected: work/brief-exports/20260917-all-todo-batches-15/batches/batch-007/references/shopping bag user message_7deb173f-122f-4b7f-a54e-6f0fdf1005c3.svg
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7deb173f-122f-4b7f-a54e-6f0fdf1005c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/ecommerce/shopping bag user message_7deb173f-122f-4b7f-a54e-6f0fdf1005c3.svg'
AUTHOR = 'gpt-6'


class GeneratedSolo(Solo48):
    icon_id = 'user-message-about-shopping-bag-batch-007-03'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecommerce"
    aliases = ()
    keywords = ('user', 'message', 'about', 'shopping', 'bag')

    def build(self):

        def line(name, start, end):
            self.add_line(name, start, end)
        def arc(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx, radius_y=ry, sweep=sweep)
        def curve(name, start, *segments):
            self.add_bezier(name, start, *segments)
        def path(name, *points, closed=False):
            self.add_polyline(name, *points, closed=closed)
        def circle(name, x, y, r, ry=None):
            ry = r if ry is None else ry
            points = [(x-r,y),(x,y-ry),(x+r,y),(x,y+ry)]
            for j in range(4): arc(f'{name}-{j}',points[j],points[(j+1)%4],r,ry)
            self.add_contour(name,*(f'{name}-{j}' for j in range(4)),closed=True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                path(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
                return
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),
                 (x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(f'{name}-{j}',pts[j],pts[(j+1)%8],r)
                else: line(f'{name}-{j}',pts[j],pts[(j+1)%8])
            self.add_contour(name,*(f'{name}-{j}' for j in range(8)),closed=True)

        path('bubble',(27,6),(6,6),(6,38),(10,42),(18,42))
        rect('bag',15,22,12,11)
        arc('handle',(15,22),(27,22),6,7)
        curve('profile',(42,18),((40,18),(40,24),(40,27)))
        path('nose-chin',(40,27),(36,32),(40,32),(40,38))
        arc('chin',(40,38),(42,40),2)
        line('jaw',(42,40),(42,42))

        # Connect only actual shared endpoints, including contour junctions.
        # Split receiving straight runs at attachment nodes to preserve topology.
        from ...primitives import Line, Point
        endpoints = {p.start for p in self.primitives} | {p.end for p in self.primitives}
        replacements = {}
        rebuilt = []
        for primitive in self.primitives:
            if isinstance(primitive, Line) and primitive.start != primitive.end:
                a, b = primitive.start, primitive.end
                dx, dy = b.x-a.x, b.y-a.y
                cuts = [q for q in endpoints if q not in (a,b)
                        and (q.x-a.x)*dy == (q.y-a.y)*dx
                        and 0 < (q.x-a.x)*dx+(q.y-a.y)*dy < dx*dx+dy*dy]
                if cuts:
                    nodes = [a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]
                    ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        ident=f'{primitive.element_id}-join-{j}'
                        rebuilt.append(Line(ident,u,v)); ids.append(ident)
                    replacements[primitive.element_id]=ids
                    continue
            rebuilt.append(primitive)
        if replacements:
            from dataclasses import replace
            self.primitives[:] = rebuilt
            self.contours[:] = [replace(c, members=tuple(k for m in c.members for k in replacements.get(m,[m]))) for c in self.contours]
        for i, a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end} & {b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)
