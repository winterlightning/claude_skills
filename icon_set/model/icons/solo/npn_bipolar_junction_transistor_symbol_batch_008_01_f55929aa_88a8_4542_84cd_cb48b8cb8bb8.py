"""NPN Bipolar Junction Transistor Symbol.
Plan: NPN base, collector and outward emitter arrow retained; optional enclosing circle omitted for clear circuit topology.
Construction reference: Lucide cpu; independently solved SOLO48 geometry.
Source copy inspected: work/brief-exports/20260917-all-todo-batches-15/batches/batch-008/references/npn bipolar transistor_f55929aa-88a8-4542-84cd-cb48b8cb8bb8.svg
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f55929aa-88a8-4542-84cd-cb48b8cb8bb8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/electronics/npn bipolar transistor_f55929aa-88a8-4542-84cd-cb48b8cb8bb8.svg'
AUTHOR = 'gpt-6'


class GeneratedSolo(Solo48):
    icon_id = 'npn-bipolar-junction-transistor-symbol-batch-008-01'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-008"
    aliases = ()
    keywords = ('npn', 'bipolar', 'junction', 'transistor', 'symbol')

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

        line('base-lead',(6,24),(18,24))
        line('base',(18,14),(18,34))
        path('collector',(18,18),(42,6))
        path('emitter',(18,30),(42,42))
        path('arrow',(26,38),(34,38),(30,30))

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
