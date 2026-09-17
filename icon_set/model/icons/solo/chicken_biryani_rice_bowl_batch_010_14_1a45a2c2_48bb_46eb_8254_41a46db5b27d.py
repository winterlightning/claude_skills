"""Chicken Biryani Rice Bowl.
Plan: Chicken portion, exposed bone and bowl; small overlapping rear portion omitted.
Construction reference: Lucide drumstick; independently solved SOLO48 geometry.
Source copy inspected: work/brief-exports/20260917-all-todo-batches-15/batches/batch-010/references/chicken biryani muslim yellow rice with chicken_1a45a2c2-48bb-46eb-8254-41a46db5b27d.svg
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1a45a2c2-48bb-46eb-8254-41a46db5b27d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/food/chicken biryani muslim yellow rice with chicken_1a45a2c2-48bb-46eb-8254-41a46db5b27d.svg'
AUTHOR = 'gpt-6'


class GeneratedSolo(Solo48):
    icon_id = 'chicken-biryani-rice-bowl-batch-010-14'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/batch-010"
    aliases = ()
    keywords = ('chicken', 'biryani', 'rice', 'bowl')

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

        line('rim',(4,28),(44,28))
        arc('bowl',(44,28),(4,28),20,12)
        curve('chicken',(16,28),((14,23),(17,19),(22,18)),((31,14),(40,20),(40,28)))
        path('bone',(22,18),(12,8),(6,8),(6,14),(16,28))


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
